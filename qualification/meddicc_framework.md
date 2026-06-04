# MEDDICC: A Working Qualification Framework

**What this is not:** A CRM field set. Most teams have MEDDICC fields in Salesforce and every one of them is filled in with the AE's wishful thinking 48 hours before forecast call. Fields are not qualification. Filling them in is not qualification. Qualification is a discipline applied to the deal itself - the framework is just where you write down the answer.

**What this is:** The version I actually use. Each letter has (1) what it really means, (2) the way AEs fake it, (3) what "qualified" looks like in evidence, (4) discovery questions that surface the truth, and (5) the tells that say you don't have it yet, even if the field is green.

Built for enterprise B2B SaaS deals at $250K+ ACV with 3+ month cycles. Smaller deals don't need this; bigger deals need more.

---

## The framework, briefly

| Letter | What it answers |
|---|---|
| **M** - Metrics | What measurable outcome does the buyer believe this will produce, and do they own that number? |
| **E** - Economic Buyer | Who personally signs, and have I sat across from them? |
| **D** - Decision Criteria | What criteria will the decision actually be made on - and did I help write them? |
| **D** - Decision Process | What are the exact steps, in order, between today and signature? |
| **I** - Identify Pain | What is the cost of doing nothing, expressed in their language, with their numbers? |
| **C** - Champion | Who advocates for me when I'm not in the room, and have they done it yet? |
| **C** - Competition | What else is being evaluated, including "build" and "do nothing"? |

The original framework is MEDDIC; the second C - Competition - was added later. I treat it as non-optional. In enterprise SaaS, the competition is almost always either an entrenched incumbent platform, a best-of-breed point solution the team already loves, or "the engineering team will build it on top of our data warehouse." All three are real.

---

## M - Metrics

### What it actually means

A specific, quantified business outcome the buyer expects from your solution, expressed in the buyer's units, owned by a named human, tied to a date.

Not "improve operational efficiency." Not "drive better customer experience." Those are categories of outcome, not metrics.

**Qualified looks like:** *"By end of Q2, reduce gross revenue churn from 9.2% to under 7% on the SMB book of business, worth ~$4.1M in retained ARR. The VP of Customer Success is accountable for this number to the CRO, and it's a stated board KPI for FY26."*

### How AEs fake it

- "They said they want to improve NRR." That's a category, not a metric. What's the current NRR, what's the target, by when, who reports it up?
- "Industry benchmark suggests they'd save X." Industry benchmarks don't sign POs. Their internal model does.
- ROI calculator output the buyer never validated. If you built the numbers and they nodded politely, you don't have metrics. You have a slide.

### Discovery questions that surface real metrics

> "If this works exactly as we hope, what changes in your quarterly business review six months from now?"

> "What's the metric your team is being asked about most often by leadership right now - and where does it sit today versus where it needs to be?"

> "Who reports this number up, and who do they report it to?"

The last question is the tell. If the answer is vague, the metric isn't yet owned. If the answer names two specific people and a cadence, you have metrics.

### Red flags

- The number changes between calls. Means it's not yet owned internally.
- The buyer agrees with every number you propose. They're being polite; they have no internal benchmark.
- Metrics are framed as "save time" or "reduce manual work" without an hours-to-dollars conversion. Soft metrics don't unlock budget.

---

## E - Economic Buyer

### What it actually means

The single person who can authorize the spend without asking anyone else. Not the highest title on the org chart. Not the loudest person in the room. The person whose signature, alone, ends the procurement process.

In enterprise SaaS this varies by category: CFO for finance/spend management, CRO for revenue tooling, CIO/CTO for platform and data infrastructure, CISO for security, CHRO for HR tech, COO for operations platforms. Below $500K ACV it may be a VP with budget authority. Above $1M it may be a committee, and you need to know the committee chair.

**Qualified looks like:** You have met them. You know what outcome they are personally accountable for. You know what they say about this category in 1:1s with their boss. You have a path to them that doesn't depend on a single person.

### How AEs fake it

- "I'm working with the VP of RevOps, she's basically the EB." She's not. Find out who signs her budget.
- "The EB is the CRO but my champion will brief her." That's not access; that's a hope. If you haven't met the EB by mid-cycle on a $500K+ deal, the deal is at risk regardless of how good the champion is.
- Conflating organizational seniority with budget authority. A CTO may not have GTM tooling budget. A CRO may not have data infrastructure budget. Follow the dollars, not the title.

### Discovery questions

To the champion:
> "Walk me through how a purchase like this gets approved in your org. Who needs to sign off, and in what order?"

> "If your CRO asked you tomorrow why we're evaluating this, what would you tell her - and what would she ask in response?"

Then later:
> "What would have to be true for you to introduce me to [EB] before our next milestone?"

The answer to that last one tells you whether you have a champion. If they hedge, you have a contact, not a champion.

### Direct EB engagement

When you do get the meeting, the agenda is not a demo. It is:

1. Confirm the business outcome they are accountable for
2. Confirm the timeline pressure (often a board commitment or annual plan)
3. Confirm the budget envelope and decision process
4. Get explicit on what would cause them to override an internal "no"

You do not pitch the EB. You qualify them.

### Red flags

- You're told the EB "doesn't get into vendor meetings." Sometimes true. More often a champion who isn't yet willing to put their credibility behind the introduction.
- The EB delegates the whole thing back to your champion after one meeting. Could be normal; could mean they weren't sold and didn't want to say so.
- Org chart shows three potential EBs and nobody can tell you which. That's a deal where the buying coalition isn't formed yet; you're early.

---

## D - Decision Criteria

### What it actually means

The specific, written criteria the buyer will use to choose between vendors (including "do nothing"). Technical, business, and relational.

**Qualified looks like:** You have seen the scorecard, or you have helped build it, or you can recite it from memory and the champion would confirm the recitation.

### How AEs fake it

- "They care about scale, performance, and price." So does every buyer. Criteria are specific - "must support 25,000 active seats with SSO via Okta and SCIM provisioning, p99 API response < 200ms, 99.95% uptime SLA" is a criterion. "Scale" is a category.
- Treating the RFP as the criteria. The RFP is often written by an analyst who doesn't make the decision, copied from a prior RFP, and weighted by whichever vendor helped them draft it. Read it carefully and then ask what's missing.
- Assuming criteria don't change. They change every time a new stakeholder enters the room.

### The criteria that actually matter

For enterprise B2B SaaS deals, the real criteria almost always include some combination of:

| Category | What it looks like in practice |
|---|---|
| Technical fit | Native integrations with their core system of record (Salesforce, Workday, NetSuite, Snowflake), SSO/SCIM, API rate limits, data residency, uptime SLA |
| Time-to-value | Implementation timeline, who does the work, when the first measurable outcome lands - 30/60/90 day milestones |
| Total cost | Not just subscription fee - implementation, integration engineering, internal admin headcount, projected usage-based overages |
| Risk profile | Vendor financial health, security posture (SOC 2 Type II, ISO 27001, pen test cadence), DPA and sub-processor list, contractual protections |
| Strategic fit | Does this enable a future capability the company has publicly committed to (AI roadmap, platform consolidation, multi-product expansion)? |
| Relationship | Quality of CSM coverage, executive sponsorship model, reference customers at comparable scale and stage |

The last one is rarely written down and frequently decisive.

### Discovery questions

> "When you've made decisions like this before, what ended up mattering most that you didn't expect going in?"

> "Who else, beyond your team, will have a perspective on what 'good' looks like here?"

> "If two vendors come in within 10% on price and technical fit, what breaks the tie?"

That last question surfaces the unwritten criterion. It is almost always the one that determines the deal.

### Influencing criteria

You are not a passive participant. Before any RFP, before any scorecard, you should be helping shape what gets measured:

- Weight criteria where you are strongest. If your time-to-value is 60 days and the competition is 6 months, get "time to first value" on the scorecard with appropriate weight.
- Surface criteria the buyer hasn't considered that matter. "Has the team thought about how this will scale when you roll out to the EMEA business unit next year, given the data residency requirements?" - now residency and multi-region support are criteria, and you brought them.
- Get criteria documented and shared early. Once it's in a doc the procurement team is using, changing it costs political capital.

### Red flags

- Criteria emerge for the first time during the proposal stage. Means someone else (or "do nothing") helped write them.
- Champion can't tell you the criteria without checking a document. Means they didn't help build it either.
- Buyer says "we don't have formal criteria, we'll know it when we see it." That's a deal that loses to inertia.

---

## D - Decision Process

### What it actually means

The exact sequence of steps, with named owners and dates, between today and signed contract. Not the buyer's procurement template - the actual path your specific deal will take.

**Qualified looks like:** You can name, in order, every step. You know who participates at each step. You know how long each step has taken on comparable deals in this account. You have a mutual close plan signed off by your champion.

### The full process, broken out

For an enterprise SaaS deal, the steps usually look like:

1. Technical evaluation - solution architect on their side, your SE; sometimes a hands-on pilot or proof-of-value scoped to a single team or workflow
2. Reference calls - they speak to 2-3 of your customers at comparable scale, ideally in their industry
3. Commercial proposal - pricing, term, ramp structure, usage tiers, key contract redlines surfaced
4. Security review - SOC 2 Type II, pen test results, DPA, sub-processor list, sometimes a custom security questionnaire (CAIQ or similar)
5. Procurement engagement - master subscription agreement negotiation, often 4-8 weeks alone at enterprise scale
6. Legal review - DPA, IP indemnification, liability caps, AI/data use clauses (increasingly load-bearing in 2026)
7. Final approval - economic buyer signs; sometimes finance committee or board sign-off above a threshold
8. Signature - their legal sends, your legal countersigns; PO issued by procurement before kickoff

Anywhere from 6 weeks (fast, motivated, prior-customer relationship) to 9 months (cold, large enterprise, custom paper). The deal you don't qualify on process is the deal that slips two quarters.

### How AEs fake it

- "They said they want to move by end of quarter." Wanting to move and having a process that supports moving are different things.
- Skipping security review timing. Enterprise security reviews routinely take 6-10 weeks. If you're 8 weeks from quarter end and security hasn't started, your forecast is wrong.
- Trusting verbal commitments to dates without a written mutual close plan. Verbal commits drift; written ones create gravity.

### Discovery questions

> "Walk me through the last time your team brought on a new vendor of comparable scale - what was the full process, and how long did each part take?"

> "Who has to be involved at each stage, and who has historically slowed things down?"

> "What's our security review look like in practice - who owns it, what's the typical timeline, and is there anything in flight ahead of us in the queue?"

### The mutual close plan

A document, co-built with the champion, that lists every step, owner, and date. Signed off (literally - emailed agreement) by the champion. Reviewed weekly. Updated when reality changes.

It is the single most underused tool in enterprise sales. The reason: AEs are afraid the buyer will feel rushed. In practice, sophisticated buyers respect the discipline and use the plan to drive their own internal process. The buyers who object to the plan are the buyers who weren't going to close anyway.

### Red flags

- Buyer says "let's keep momentum going" but won't commit to dates. Momentum without dates is drift.
- Procurement hasn't been notified of the deal as you approach final stages. They will add weeks the moment they're surprised.
- The champion says "I'll drive the process internally, don't worry about it." Worry about it. You have no visibility into a process you're not driving.

---

## I - Identify Pain

### What it actually means

The specific, current cost the buyer is incurring by not solving this problem. Quantified. Felt by a named person who has the credibility to act.

Pain is not a category of problem. Pain is the dollar figure or career risk attached to that problem, today.

**Qualified looks like:** *"Their customer onboarding takes 47 days on average against an industry benchmark of 18, and gross revenue churn in the first 90 days is running at 14%. The CRO committed to the board to bring time-to-first-value under 21 days this fiscal year. Every quarter this isn't solved is roughly $2.8M in early-stage churn they've publicly committed to reduce."*

### How AEs fake it

- "They said it's a pain point." A pain point is a vendor word. Pain is a number with a name on it.
- Pain identified but not owned. If no specific person is accountable for fixing it, there's no buying pressure - just a vague problem that's been around for years.
- Substituting the AE's hypothesis for the buyer's lived experience. You may know the category pain better than the buyer; the deal still requires them to feel it, in their own words.

### The pain hierarchy

Pain has a hierarchy of intensity:

1. **Public commitment unmet.** Executive promised the board / investors / market a number. Missing it has career consequence. Highest urgency.
2. **Active outage or incident.** Something is currently broken and someone is being held responsible. High urgency, often short window.
3. **Compounding cost.** Every quarter the problem persists costs measurable dollars. Medium urgency, but quantifiable.
4. **Strategic gap.** Competitor has something we don't, or a capability the team needs for the next phase. Real but easily deferred.
5. **Operational annoyance.** The team complains about a tool but no executive is being held accountable for the consequence. No urgency. Not a deal.

Categories 4 and 5 are where AEs spend most of their pipeline. They feel like deals - there are meetings, there are demos - but they don't close, because nobody is being held accountable for fixing them this quarter.

### Discovery questions

> "What does the current state cost the team in a typical quarter - in dollars, in hours, or in opportunity?"

> "Has anyone been held accountable for this problem? What was the consequence?"

> "If nothing changes in the next 12 months, what's the outcome - and is anyone publicly committed to a different outcome?"

The last question separates urgent pain from chronic pain. Chronic pain doesn't close.

### Red flags

- The pain is described by the champion but no one above them can articulate it. Pain that doesn't travel up the org doesn't unlock budget.
- The buyer agrees the pain is real but says "we've lived with it for years." Translation: they will continue to live with it.
- Pain is theoretical ("if we don't solve this, eventually...") rather than current. Future pain rarely closes deals; current pain does.

---

## C - Champion

### What it actually means

A person inside the account who (1) has personal credibility to influence the decision, (2) has a personal stake in your solution being chosen, (3) has demonstrated willingness to advocate for you when you're not in the room.

The third condition is the one most often missing. A friendly contact is not a champion. A champion has put their reputation on the line for you, in writing or in a room, at least once.

**Qualified looks like:** They have introduced you to two other stakeholders. They have shared internal context you would not have learned otherwise. They have told you about a problem with your proposal before it became a deal-breaker. They have used the phrase "we" when describing the path forward.

### How AEs fake it

- Confusing access with advocacy. The person who returns your calls fastest is not necessarily the person fighting for the deal internally.
- Single-threaded champions. If your one champion is poached, promoted, or moves teams, the deal dies. By mid-cycle you need a second.
- Champions without credibility. A junior champion may genuinely advocate but lack the standing to drive consensus among senior stakeholders. That's an advocate, not a champion. Useful but not sufficient.

### Building a champion

You do not appoint a champion. You build one over time by:

1. Giving them content they can use internally - ROI analysis, architecture diagrams, references from their peers.
2. Making them look smart in front of their leadership. Help them anticipate what their EB will ask before they walk into the meeting.
3. Surfacing risk to them privately before it becomes a problem publicly. They will trust you because you protected them once.
4. Asking them, explicitly, to advocate. "Would you be willing to brief the CRO before our next meeting?" If they say yes, you have a champion. If they hedge, you have a contact.

### Discovery questions to test champion strength

> "What do you think the biggest objection internally will be, and who will raise it?"

A real champion has thought about this and has an answer. A contact says "I don't know, I haven't really thought about it."

> "If this gets stuck in procurement, who can you call?"

A real champion names someone specific and explains why they have leverage. A contact says "we'll figure it out."

> "What would have to happen for you to recommend against this deal?"

A real champion gives you a clear, honest answer. A contact gives you a reassurance.

### Red flags

- Champion goes quiet between meetings. Possibly internal politics, possibly they've cooled. Either way, lose visibility = lose deal.
- Champion can't get you time with the EB despite multiple attempts. They don't have the standing to make the introduction, or they're not willing to spend the political capital.
- Champion changes jobs mid-deal. This kills more deals than competition does. Always have a second champion - not because the first will leave, but because they might.

---

## C - Competition

### What it actually means

Every alternative the buyer is considering, in order of how seriously each is being considered. Named vendors plus the two competitors AEs forget: **build internally** and **do nothing**.

**Qualified looks like:** You can name every vendor in the evaluation, the order they're ranked in the buyer's mind, what each is strongest on, and what the buyer privately doesn't like about each. You know whether build is on the table and who would do it. You know what "do nothing" looks like and what would force it.

### How AEs fake it

- "We're the only ones they're talking to." False roughly 95% of the time at enterprise scale. They're talking to others; they're just not telling you.
- Treating the named competitor as the only threat. The bigger threat is usually "no decision" - organizational inertia, deprioritization, budget reallocation.
- Underweighting build. SaaS buyers with mature data and platform teams routinely consider building on top of their warehouse (Snowflake, Databricks, BigQuery) or extending an existing internal platform. The build option has a champion (engineering or platform leadership), a budget (existing headcount), and a roadmap (always 6-9 months, always late).

### Mapping the competitive field

For each competitor, including build and do-nothing:

| Field | Notes |
|---|---|
| Vendor / option | |
| Internal sponsor | Who in the buying org is championing this option? |
| Their strongest argument | In the buyer's own framing |
| Their weakest argument | Where the buyer is privately skeptical |
| How they're positioning against us | What they're saying you can't do |
| Our counter | Not an attack - a reframe of the criteria |

If you can't fill in the "internal sponsor" column, you don't yet understand the competitive dynamic. Every option has a human behind it.

### Discovery questions

> "Who else are you evaluating, and what do you like about each?"

The "what do you like" framing is critical. Asking "who else are you considering" often gets a deflection. Asking what they like gets honesty - buyers want to be seen as having done diligence.

> "If you couldn't buy any vendor, what would your team build, how long would it take, and who would lead it?"

This surfaces the build option, which is often the strongest hidden competitor in platform and data-adjacent SaaS deals.

> "If this evaluation got paused for a year, what would happen?"

This surfaces the strength of "do nothing." If the answer is "nothing much," do-nothing is winning.

### Positioning principles

Covered in depth in [`competitive-intelligence/buyer_psychology_framework.md`](../competitive-intelligence/buyer_psychology_framework.md). In brief:

- Never position by attacking. Reframe the criteria instead.
- Control the evaluation scorecard. Weighted criteria beat sharper features.
- Get to the economic buyer before the incumbent renewal cycle does.

### Red flags

- Buyer won't name competitors. Usually means there are several and you're not the leading one.
- Champion downplays competition ("don't worry about them"). Either they don't know, or they're protecting you from bad news.
- You haven't asked about build in a deal where the buyer has a 200+ engineer team and a centralized data platform. Build is on the table whether you've asked or not.

---

## Scoring the deal

For each dimension, score yourself 0-3:

| Score | Meaning |
|---|---|
| **0** | I cannot answer the qualifying question for this dimension at all |
| **1** | I have a hypothesis but no verified evidence from the buyer |
| **2** | I have buyer-confirmed evidence but it has not been tested or written down |
| **3** | I have buyer-confirmed evidence, documented, and validated by a second source |

Sum the seven scores. Out of 21:

- **0-7:** Early. Not a forecast deal. Continue discovery; do not commit dates.
- **8-13:** Mid-funnel. Forecast as upside or commit based on the missing dimensions and the time available.
- **14-18:** Late-stage qualified. Forecast as commit if there's a written mutual close plan and the dates work.
- **19-21:** Closed-won shouldn't be a surprise. If it is, your scoring is generous.

Score honestly, weekly, with the same lens. The number is only useful if it's consistent. The number is most useful as a tool to identify which dimension is dragging the deal - go work on that dimension this week.

---

## Cross-cutting principles

**1. Qualification is continuous, not a stage.** Every conversation either confirms or weakens your qualification. The deal you stopped qualifying in week 4 is the deal that surprises you in week 14.

**2. The dimension you don't want to ask about is the one most worth qualifying.** If you've been avoiding asking who else is being evaluated, that's the question to ask next. Avoidance is data.

**3. Disqualify deliberately.** The fastest path to a strong pipeline is killing the deals that won't close so you can spend that time on the ones that will. A deal that scores 5/21 in week 8 is not a deal - it's an exercise in optimism.

**4. Champion + Economic Buyer + Pain is the minimum viable triangle.** If you have all three with high confidence, the rest can be built. If any one is weak, the deal is at structural risk regardless of how strong the others are.

**5. Write it down, or it didn't happen.** Qualification you carry in your head is qualification that disappears at the next forecast call. Notes in the CRM. Mutual close plan in a shared doc. Champion confirmations in email. The discipline is the documentation.

**6. The framework is a lens, not a script.** Don't ask discovery questions in MEDDICC order. Don't introduce the framework to the buyer - they don't care what your sales methodology is. Use it after the conversation to audit what you learned, not during it to drive what you ask.

---

*Framework version: 1.0 - calibrated for enterprise B2B SaaS deals $250K+ ACV. Update the scoring rubric after each closed deal (won and lost) with the dimension that turned out to be the actual driver. Patterns will emerge after 6-8 deals; rewrite this doc when they do.*
