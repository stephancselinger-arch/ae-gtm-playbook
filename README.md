# AE GTM Playbook

A working reference for AI-augmented enterprise sales execution. Not a philosophy deck - a set of tools, templates, and workflows I actually use.

## What's here

| File | Purpose |
|---|---|
| `workflows/job_change_monitor.py` | Python script that polls LinkedIn via Proxycurl, detects job changes in a target account list, and pushes ranked alerts to Slack |
| `research/prospect_research_template.md` | Repeatable framework for building an account thesis from 100% public data: SEC filings, job postings, G2 reviews, press releases |
| `competitive-intelligence/buyer_psychology_framework.md` | Competitor positioning by buyer psychology - not features, but the fear and inertia patterns each archetype owns and where those patterns break |
| `qualification/meddicc_framework.md` | MEDDICC as a working discipline, not a CRM field set - what each letter actually means, how AEs fake it, the discovery questions that surface truth, and a 0-21 scoring rubric for honest forecasting |

## Philosophy in practice

Enterprise buyers don't buy software. They buy a reduction in a specific risk they already believe they have. My job is to find the moment when that belief crystallizes - a new executive, a failed audit, a competitor shipping something they can't - and be positioned there already.

The tools I use: Clay for signal aggregation, Proxycurl for LinkedIn enrichment, Perplexity for rapid 10-K synthesis, n8n for gluing CRM events to outreach triggers, and Python for anything that needs to run on a schedule without a monthly SaaS bill attached.

None of this replaces knowing the product cold and having opinions about the customer's architecture. It just means I show up to those conversations with context.
