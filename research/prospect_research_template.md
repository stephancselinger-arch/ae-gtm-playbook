# Enterprise Prospect Research Template

**Purpose:** Build a defensible account thesis from public data before any human conversation. The goal is not a slide deck - it is knowing the one thing the account cares about most right now, and why our product addresses it specifically.

**Time budget:** 2 hours max. If you spend more than that, you're building a report nobody will read.

---

## 1. Trigger & Hypothesis

*Why is this account worth researching today, and what's the initial bet?*

| Field | Notes |
|---|---|
| **Trigger event** | What surfaced this account: job change, funding round, press release, competitor win, inbound |
| **Initial hypothesis** | In one sentence: the problem you think they have and why we solve it |
| **Hypothesis confidence** | 1-5. Be honest. This forces discipline on how much time to spend. |
| **Decision deadline** | Is there a natural forcing function - renewal, fiscal year end, public commitment? |

---

## 2. Firmographic Baseline

*What kind of company is this, and what does their financial posture tell us about how they buy?*

**Source priority: 10-K / 10-Q (public) → S-1 (if recent) → Crunchbase → LinkedIn headcount**

| Field | Data | Source |
|---|---|---|
| Revenue (last FY) | | 10-K, Item 6 |
| YoY revenue growth | | 10-K |
| Gross margin | | 10-K - matters because high-margin companies buy on outcome, low-margin on cost |
| R&D spend as % of revenue | | 10-K - high R&D% = they build; we need a strong build-vs-buy argument |
| Headcount (engineering) | | LinkedIn, job postings |
| Recent M&A activity | | Press releases, 10-K Item 1 |
| Geographic footprint | | 10-K - multi-region = data residency requirements = longer security review |

**Fiscal year end:** ___________
*(Q4 of their fiscal year is when budgets are renewed and easiest to attach to. Q1 is when new initiatives get funded.)*

**What the financials suggest about buying behavior:**
> Write 2-3 sentences. E.g.: "Gross margin at 71% and R&D at 24% of revenue suggests they prioritize capability over cost. Last year's $400M acquisition of a data integration company means they have a newly inherited tech stack with integration debt - that's a wedge."

---

## 3. Tech Stack Archaeology

*What are they actually running, and what does that tell us about where we fit and who we're displacing?*

**Sources: G2 buyer intent, job postings (LinkedIn/Greenhouse/Lever), BuiltWith, press releases, GitHub org**

### From job postings
Job descriptions are accidental architecture diagrams. Engineering job posts reveal:
- Infrastructure: cloud provider, orchestration tools, data warehouse
- Languages and frameworks (signals build-vs-buy orientation)
- Roles they can't fill (organizational stress = buying pressure)

| Signal | What I found | Implication |
|---|---|---|
| Cloud provider(s) | | Single cloud = potential platform lock-in risk they may want to mitigate |
| Data warehouse | | Snowflake/BigQuery/Redshift each have different partner ecosystems |
| Orchestration | | Airflow self-hosted vs. managed = indication of infra team maturity |
| Active hiring in our space | | Hiring 3 engineers to build what we sell = champion-side risk, evaluate carefully |
| Roles open 90+ days unfilled | | Organizational gap = buying opportunity |

### From G2 reviews (their current tools in our category)
Search G2 for the competitor/incumbent they're likely using.
- Filter reviews by "current user" and company size matching the prospect
- Look for reviews mentioning: performance, support responsiveness, integration complexity, pricing surprises
- The most negative patterns reveal the pain we should lead with

| Current tool (suspected) | Most common G2 complaint | How we address it |
|---|---|---|
| | | |
| | | |

### From GitHub (if org is public)
- What open-source tools are they contributing to or forking?
- Do they have internal tooling in our space? (Signals whether engineering has already tried to solve this)

---

## 4. Organizational Map

*Who makes decisions, who implements them, and who can kill a deal?*

**Sources: LinkedIn, press releases (exec hires/departures), company blog, conference speaker listings**

### Economic buyer
The person whose budget this comes from. Title varies: CTO, VP Engineering, CDO, CISO.

| Field | Notes |
|---|---|
| Name & title | |
| Time in role | < 18 months = still proving themselves = more open to change |
| Prior company | Brings vendor preferences and past failures with them |
| Public content (posts, talks, articles) | What do they publicly care about? This is the frame for your outreach |
| Recent org change | Reorg or new reports = unsettled relationships = opportunity |

### Champion candidate
The person who will feel the pain daily and can navigate the internal process.

| Field | Notes |
|---|---|
| Name & title | |
| Evidence they feel the problem | Specific - a post they wrote, a job req they posted, a conference talk |
| Internal credibility signals | How long in role, cross-functional scope, team size |
| Risk: are they also the person who would build this themselves? | If yes, need a strong build-vs-buy ROI argument ready |

### Blockers / negative personas
Who loses if we win? Whose job changes if we're adopted?

| Name / Role | Their stake in the status quo | Mitigation approach |
|---|---|---|
| | | |

---

## 5. Buying Signal Inventory

*What has changed recently that creates urgency? No urgency = no deal, just a conversation.*

**Sources: press releases, LinkedIn posts from executives, SEC 8-K (material events), job postings, news search**

| Signal | Date | What it implies | Urgency level (1-3) |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Signal types and what they mean:**

- **New executive hire (our space):** Budget authority shift; 90-day window before they inherit incumbent
- **Funding round / IPO filing:** New financial scrutiny = ROI clarity matters more; also new budget to deploy
- **Announced digital transformation initiative:** Named initiative = there's a budget line we can attach to
- **Recent acquisition:** Integration complexity = immediate pain in our category
- **Competitor win at this account (rumored/confirmed):** Loss risk - or proof the category is now funded
- **Regulatory change in their industry:** Compliance requirements create non-negotiable deadlines
- **Mass layoff followed by hiring in specific area:** Strategic pivot; old vendor relationships getting re-evaluated

---

## 6. Discovery Hypothesis

*What are the 3 questions I'll use to either confirm or destroy my thesis in the first call?*

The goal of discovery is not to gather information. It is to test whether your hypothesis is correct fast enough to know whether to invest or walk away.

| Hypothesis to test | Question that surfaces the truth | If confirmed → | If denied → |
|---|---|---|---|
| They have integration debt from last year's acquisition | "How are your teams currently sharing data between [acquired company] and the core platform?" | Accelerate - this is the wedge | Re-anchor to a different pain |
| The incumbent is losing internal credibility | "When was the last time your team evaluated whether [category tool] was still the right fit?" | Advance to demo | Understand switching cost framing |
| The economic buyer is being held accountable for a specific outcome | "What's the metric your leadership team is watching most closely heading into next year?" | Build ROI model around that metric | Broader discovery needed |

---

## 7. Risk Inventory

*What could prevent this deal from closing, even if they want to buy?*

| Risk | Likelihood (H/M/L) | Mitigation |
|---|---|---|
| Incumbent is entrenched at the IT/procurement level | | Map to an executive sponsor above IT |
| No dedicated budget; would require a new budget request | | Start with a pilot scoped to existing budget |
| Engineering team wants to build it themselves | | Get a VP-level perspective on opportunity cost; quantify build timeline |
| Legal / security review cycle > 90 days | | Front-load security documentation; reference a comparable customer's review timeline |
| Fiscal year end mismatch | | Identify if they can close in current FY or build for Q1 next FY |
| Champion doesn't have internal credibility to drive consensus | | Add a second champion; work toward exec sponsor engagement |

---

## Research Log

| Date | Source | Finding | Action taken |
|---|---|---|---|
| | | | |
| | | | |

---

*Template version: 1.0 - built for 100% public data sources only. No data acquired through paid intent platforms is used in this template. All conclusions are inferences from public signals and should be validated in discovery.*
