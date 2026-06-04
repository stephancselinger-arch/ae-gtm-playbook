"""
job_change_monitor.py

Monitors a list of target enterprise contacts for job changes and surfaces
ranked alerts to Slack with pre-built context for outreach.

WHY THIS EXISTS:
Job changes are the highest-signal buying event in enterprise SaaS.
A VP of Data Engineering moving to a new company brings their vendor preferences,
frustrations, and relationships with them - and has a window of roughly 60-90 days
before they inherit the incumbent stack and lose political capital to change it.

This script systematizes that window across an entire territory so no signal slips
through because I was heads-down on a different deal.

SETUP:
1. Copy .env.example → .env and fill in API keys
2. pip install -r requirements.txt
3. Add contacts to workflows/sample_contacts.csv
4. Run directly or schedule via cron: `0 8 * * 1-5 python job_change_monitor.py`

DEPENDENCIES:
- Proxycurl (nubela.co/proxycurl): LinkedIn profile enrichment API. $0.01/credit.
  At 200 monitored contacts checked daily, that's ~$2/day. Budget it like a tool.
- Slack Incoming Webhooks: free, no bot token needed.
- SQLite: zero-infrastructure state store. No RDS needed for a list of 500 people.
"""

import os
import csv
import json
import time
import sqlite3
import logging
import requests
from datetime import datetime
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

PROXYCURL_API_KEY = os.environ["PROXYCURL_API_KEY"]
SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
CONTACTS_CSV = Path(__file__).parent / "sample_contacts.csv"
DB_PATH = Path(__file__).parent / "job_state.db"

# Proxycurl rate limit: 300 req/min on paid plans. 0.5s sleep is conservative
# but keeps us well clear of throttling without meaningfully slowing a 200-contact run.
RATE_LIMIT_SLEEP_SECONDS = 0.5

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

def init_db(conn: sqlite3.Connection) -> None:
    """
    Creates the state table if it doesn't exist.
    We store the last observed title and company so we can detect deltas
    across runs without hitting the API more than once per contact per day.
    """
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contact_state (
            linkedin_url    TEXT PRIMARY KEY,
            full_name       TEXT,
            account_name    TEXT,
            tier            INTEGER,
            last_title      TEXT,
            last_company    TEXT,
            last_checked_at TEXT,
            change_detected INTEGER DEFAULT 0
        )
    """)
    conn.commit()


def upsert_state(conn: sqlite3.Connection, row: dict) -> None:
    conn.execute("""
        INSERT INTO contact_state
            (linkedin_url, full_name, account_name, tier, last_title, last_company, last_checked_at, change_detected)
        VALUES
            (:linkedin_url, :full_name, :account_name, :tier, :title, :company, :checked_at, :changed)
        ON CONFLICT(linkedin_url) DO UPDATE SET
            last_title      = excluded.last_title,
            last_company    = excluded.last_company,
            last_checked_at = excluded.last_checked_at,
            change_detected = excluded.change_detected
    """, row)
    conn.commit()


def get_baseline(conn: sqlite3.Connection, linkedin_url: str) -> Optional[dict]:
    """
    Returns the stored title and company for a contact, or None on first run.
    First-run contacts are seeded from the CSV - no Slack alert is sent
    because we don't know if the CSV data is current. On the next run, we compare.
    """
    cur = conn.execute(
        "SELECT last_title, last_company FROM contact_state WHERE linkedin_url = ?",
        (linkedin_url,)
    )
    row = cur.fetchone()
    return {"title": row[0], "company": row[1]} if row else None


# ---------------------------------------------------------------------------
# LinkedIn enrichment
# ---------------------------------------------------------------------------

def fetch_linkedin_profile(linkedin_url: str) -> Optional[dict]:
    """
    Fetches current profile data via Proxycurl.

    We use `use_cache=if-recent` to avoid spending a credit on a profile
    that Proxycurl already crawled within the past 29 days. This is the
    right tradeoff for job-change detection: a 30-day-old cache is still
    fresh enough to catch moves before the 60-day opportunity window closes.
    """
    params = {
        "url": linkedin_url,
        "use_cache": "if-recent",          # use Proxycurl cache if < 29 days old
        "fallback_to_cache": "on-error",   # don't burn a credit if LinkedIn blocks the request
    }
    headers = {"Authorization": f"Bearer {PROXYCURL_API_KEY}"}

    try:
        resp = requests.get(
            "https://nubela.co/proxycurl/api/v2/linkedin",
            params=params,
            headers=headers,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as e:
        # 404 = profile deleted/private. Log and skip rather than raising -
        # one bad URL shouldn't abort a 200-contact run.
        if e.response.status_code == 404:
            log.warning("Profile not found: %s", linkedin_url)
        else:
            log.error("Proxycurl error %s for %s: %s", e.response.status_code, linkedin_url, e)
        return None
    except requests.exceptions.RequestException as e:
        log.error("Network error fetching %s: %s", linkedin_url, e)
        return None


def extract_current_position(profile: dict) -> tuple[Optional[str], Optional[str]]:
    """
    Pulls the most recent position from the Proxycurl response.
    Proxycurl returns experiences in reverse-chronological order; index 0 is current.
    We check ends_at=None as the signal for 'still in this role'.
    """
    experiences = profile.get("experiences", [])
    for exp in experiences:
        if exp.get("ends_at") is None:
            title = exp.get("title", "Unknown Title")
            company = (exp.get("company") or {}).get("name") or exp.get("company_linkedin_profile_url", "Unknown Company")
            return title, company
    # If everything has an end date, fall back to the first entry - profile cleanup lag
    if experiences:
        return experiences[0].get("title"), experiences[0].get("company", {}).get("name")
    return None, None


# ---------------------------------------------------------------------------
# Slack alerting
# ---------------------------------------------------------------------------

def build_slack_alert(contact: dict, old_title: str, old_company: str, new_title: str, new_company: str) -> dict:
    """
    Structures the Slack message to surface the three things I need to act:
    1. Who moved and where they came from (context for the email)
    2. What they moved into (determines which use case to lead with)
    3. A direct link to their profile (no hunting)

    Tier-1 contacts get @channel pings because the 60-day window doesn't wait
    for me to scroll my Slack feed.
    """
    name = contact["full_name"]
    tier = int(contact["tier"])
    profile_url = contact["linkedin_url"]
    account = contact["account_name"]

    # Same company, different title = promotion or reorg. Still worth a touch -
    # new scope often means new budget authority and unsettled vendor relationships.
    is_company_change = old_company.lower().strip() != new_company.lower().strip()
    change_type = "moved to a new company" if is_company_change else "changed roles internally"
    # Build the context hint before the f-string to avoid apostrophe-in-string-literal issues
    context_hint = (
        "Lead with their new company pain, not the old deal."
        if is_company_change
        else "Reorg = new budget authority - revisit scope."
    )

    urgency_prefix = "<!channel> :rotating_light: *Tier 1 job change*\n" if tier == 1 else ":wave: *Job change detected*\n"

    text = (
        f"{urgency_prefix}"
        f"*<{profile_url}|{name}>* ({account}) has {change_type}.\n"
        f">*Was:* {old_title} @ {old_company}\n"
        f">*Now:* {new_title} @ {new_company}\n\n"
        f"Window: ~60 days before new vendor relationships solidify. {context_hint}"
    )

    return {"text": text}


def send_slack_alert(payload: dict) -> bool:
    try:
        resp = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
        resp.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        log.error("Failed to send Slack alert: %s", e)
        return False


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def load_contacts(csv_path: Path) -> list[dict]:
    with open(csv_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def run():
    log.info("Starting job change monitor - %s", datetime.now().isoformat())
    contacts = load_contacts(CONTACTS_CSV)
    log.info("Loaded %d contacts", len(contacts))

    conn = sqlite3.connect(DB_PATH)
    init_db(conn)

    alerts_sent = 0
    errors = 0

    for contact in contacts:
        linkedin_url = contact["linkedin_url"].strip()
        log.info("Checking %s (%s)", contact["full_name"], linkedin_url)

        baseline = get_baseline(conn, linkedin_url)
        profile = fetch_linkedin_profile(linkedin_url)

        if profile is None:
            errors += 1
            time.sleep(RATE_LIMIT_SLEEP_SECONDS)
            continue

        current_title, current_company = extract_current_position(profile)

        if current_title is None:
            log.warning("Could not extract position for %s", contact["full_name"])
            errors += 1
            time.sleep(RATE_LIMIT_SLEEP_SECONDS)
            continue

        state_row = {
            "linkedin_url": linkedin_url,
            "full_name": contact["full_name"],
            "account_name": contact["account_name"],
            "tier": contact["tier"],
            "title": current_title,
            "company": current_company,
            "checked_at": datetime.now().isoformat(),
            "changed": 0,
        }

        if baseline is None:
            # First time seeing this contact - seed baseline, no alert.
            # We need at least one clean run before we can detect deltas.
            log.info("  Seeding baseline: %s @ %s", current_title, current_company)
            upsert_state(conn, state_row)
            time.sleep(RATE_LIMIT_SLEEP_SECONDS)
            continue

        old_title = baseline["title"]
        old_company = baseline["company"]

        # Normalize before comparing to avoid false positives from trailing spaces,
        # Unicode variations in company names, or capitalization drift.
        title_changed = current_title.lower().strip() != old_title.lower().strip()
        company_changed = current_company.lower().strip() != old_company.lower().strip()

        if title_changed or company_changed:
            log.info(
                "  CHANGE DETECTED: [%s @ %s] → [%s @ %s]",
                old_title, old_company, current_title, current_company
            )
            payload = build_slack_alert(contact, old_title, old_company, current_title, current_company)
            if send_slack_alert(payload):
                alerts_sent += 1
                state_row["changed"] = 1
            else:
                errors += 1
        else:
            log.info("  No change: %s @ %s", current_title, current_company)

        upsert_state(conn, state_row)
        time.sleep(RATE_LIMIT_SLEEP_SECONDS)

    conn.close()
    log.info(
        "Run complete. %d contacts checked, %d alerts sent, %d errors.",
        len(contacts), alerts_sent, errors
    )


if __name__ == "__main__":
    run()
