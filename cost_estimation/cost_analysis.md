# Cost analysis (R1-06)

Spreekorb is an invented company. Every number is computed, cited, or labelled estimate / synthetic. The timing emails are the synthetic set spreekorb_emails_60.csv. Volume and the handling-time cross-check come from Shopzilla (https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction), a real-data proxy, not Spreekorb.

## Assumptions

| item | value | unit | label | source |
|---|---|---|---|---|
| usd_eur | 0.9123 | EUR per USD | estimate | tradingview.com USDEUR, 27 Nov 2026 (as in langsmith/monitoring_note.md) |
| rate_h | 95 | EUR/h | estimate | IT freelancer median, freelancermap Freelancer-Kompass 2026, https://www.freelancermap.de/blog/stundensatz-it-freelancer/ |
| hours_day | 8 | h/day | estimate | standard working day, own assumption (no source) |
| days_prototype | 10 | days | estimate | own estimate, no source (Round 1 prototype, done, sunk cost) |
| days_pilot | 15 | days | estimate | own estimate, no source (n8n + mailbox + review UI + DPA / works-council prep) |
| days_rollout | 10 | days | estimate | own estimate, no source |
| weeks_prototype | 2 | weeks | estimate | own estimate, no source (done in Round 1) |
| weeks_pilot | 6 | weeks | estimate | own estimate, no source |
| weeks_rollout | 8 | weeks | estimate | own estimate, no source |
| volume | 3017 | emails/month | computed (Shopzilla proxy, busiest month) | research/sector_research.md; Shopzilla data https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction (real-data proxy, not Spreekorb) |
| timing_set | 10 | emails | synthetic | data/processed/spreekorb_emails_60.csv, rows with timing_flag, split heldout (synthetic set) |
| manual_min | 15 | min/email | estimate | estimate (Ayhan), revised from 20 to 15 min on 27 Nov 2026 after the Shopzilla cross-check; no measured basis |
| ai_min | 5 | min/email | measured (self-reported average, Ayhan) | Ayhan, 27 Nov 2026; average, done second on the same emails (learning bias) |
| n8n_eur | 60 | EUR/month | estimate | https://n8n.io/pricing (Pro about 50 EUR billed annually, 60 monthly; third-party sites differ, check before buying) |
| n8n_limit | 10000 | executions/month | estimate | https://n8n.io/pricing (Pro plan) |
| n8n_exec_per_email | 1 | executions/email | estimate | own assumption: one email = one n8n execution |
| ls_usd | 39 | USD/seat/month | estimate | LangSmith Plus, https://www.langchain.com/pricing (10k base traces included) |
| ls_seats | 2 | seats | estimate | own estimate, no source |
| at_usd | 20 | USD/seat/month | estimate | Airtable Team, annual billing, https://support.airtable.com/docs/airtable-plans |
| at_seats | 3 | editors | estimate | own estimate, no source |
| tableau_eur | 0 | EUR/month | estimate | Tableau Public, public data only, https://public.tableau.com/app/about |
| salary | 2650 | EUR/month gross | estimate | mid of 2,400-2,900; https://www.profiling-institut.de/ausbildungsberufe/kaufmann-dialogmarketing/ (BA Entgeltatlas median 2,922), https://www.gehalt.de/beruf/kaufmann-frau-fuer-dialogmarketing (about 2,460) |
| overhead | 1.2 | factor | estimate | employer cost on top of gross, own estimate, no source |
| hours_month | 160 | h/month | estimate | paid hours per month, own estimate, no source |
| queue_match | 85 | % (n=20) | synthetic | langsmith/monitoring_note.md (held-out, synthetic emails) |
| re_route | 15 | % (n=20) | computed | 100 - queue_match (langsmith/monitoring_note.md, synthetic emails) |
| ai_cost_per_draft | 0.000347 | EUR/draft | measured (USD by LangSmith), EUR estimate | langsmith/trace_summary.csv timing_10 total_cost_eur / n |
| shopzilla_handling_p5 | 2.8 | min (unit assumed seconds) | computed | data/raw/shopzilla_cs_satisfaction.csv connected_handling_time, n=242 filled rows, unit assumed seconds, mostly calls; https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction |
| shopzilla_handling_median | 7.1 | min (unit assumed seconds) | computed | data/raw/shopzilla_cs_satisfaction.csv connected_handling_time, n=242 filled rows, unit assumed seconds, mostly calls; https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction |
| shopzilla_handling_p95 | 15.3 | min (unit assumed seconds) | computed | data/raw/shopzilla_cs_satisfaction.csv connected_handling_time, n=242 filled rows, unit assumed seconds, mostly calls; https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction |

## 1. Build (day rate x days)

Day rate = 95 EUR/h x 8 h = 760 EUR/day (estimate).

| phase | days (estimate) | cost EUR (estimate) | in payback |
|---|---|---|---|
| Prototype | 10 | 7,600.00 | no, sunk (done in Round 1) |
| Pilot | 15 | 11,400.00 | yes |
| Rollout | 10 | 7,600.00 | yes |
| Total | 35 | 26,600.00 | |
| Build for payback (pilot + rollout) | 25 | 19,000.00 | |

Prototype was done in Round 1 (n8n POC, LangSmith, Tableau) and is sunk. Payback uses pilot + rollout build cost only. Days are own estimates without source.

## 2. AI calls

AI cost per draft: 0.000347 EUR (timing_10: total_cost_eur 0.003469 / 10 drafts from langsmith/trace_summary.csv; USD measured by LangSmith, the EUR column is already converted at USDEUR 0.9123, an estimate, and is not converted again).

Monthly = 0.000347 x 3,017 emails = 1.05 EUR/month (computed).

## 3. Tools per month (pilot)

| tool | seats | EUR/month (estimate) |
|---|---|---|
| n8n Cloud Pro | 1 | 60.00 |
| LangSmith Plus | 2 | 71.16 |
| Airtable Team | 3 | 54.74 |
| Tableau Public | 0 | 0.00 |
| Total | | 185.90 |

- USD prices converted at 0.9123 (tradingview.com USDEUR, 27 Nov 2026). Seat counts are estimates.
- n8n: 3,017 executions/month (assumption: one email = one execution) vs 10,000 included: OK, below the limit. Price taken as 60 EUR monthly billing; about 50 EUR if billed annually. Check before buying. Self-hosted n8n is a rollout option (not costed).
- Airtable is used: the review queue is an Airtable base (n8n/airtable_setup.md), so it is costed here.
- Tableau Public is free but public data only. Real Spreekorb data cannot go on Tableau Public; a Tableau Cloud licence would be needed, price: source to add.

## 4. Value

### Timing evidence (10 held-out emails, data/timing_log.csv)

- Manual: 15 min per email on average. Label: estimate (Ayhan), revised from 20 to 15 min on 27 Nov 2026 after the Shopzilla cross-check; no measured basis.
- AI-assisted (draft + review + edit + send): 5 min per email on average, self-reported average by Ayhan.

### Timing test limits

- One person did the test, and that person also built the system.
- Only 10 synthetic held-out emails (spreekorb_emails_60.csv).
- No blinding.
- No counterbalancing: AI-assisted was done second on the same emails, so there is a learning bias (AI time probably understated, saving overstated).
- Averages only; per-email minutes were not recorded.
- Pilot fix: several agents, per-email timing, counterbalanced order.

### Cross-check of the manual time (Shopzilla handling time)

Shopzilla (https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction) column connected_handling_time is filled for only 242 rows; the unit is not documented, assumed seconds. Computed in minutes: 5th percentile 2.8, median 7.1, 95th percentile 15.3, max 33.1.
Rows are mostly Inbound / Outcall calls, all channels mixed. Email rows: n=4, anecdotal, no email rate is reported.
The median of 7.1 min (mostly calls) neither proves nor refutes the 15 min estimate (Ayhan). It is used as a conservative case.

### Formula (main case, manual = 15 min)

- Minutes saved per email = 15 - 5 = 10
- Hours saved per month = 3,017 x 10 / 60 = 502.8 h
- Agent cost per hour = 2,650 x 1.2 / 160 = 19.88 EUR/h (estimate)
- Value per month = 502.8 x 19.88 = 9,993.81 EUR (estimate)
- Net per month = value - AI calls - tools = 9,993.81 - 1.05 - 185.90 = 9,806.87 EUR
- Payback = build for payback (pilot + rollout) / net per month = 19,000.00 / 9,806.87 = 1.9 months (estimate)

Time saved is capacity (agents answer more emails, faster), not an automatic headcount cut.

### Main case vs conservative case

| metric | main (manual 15 min, estimate Ayhan) | conservative (manual 7.1 min, Shopzilla median, computed) |
|---|---|---|
| minutes saved per email | 10.0 | 2.1 |
| hours saved per month | 502.8 | 106.4 |
| value EUR/month | 9,993.81 | 2,115.36 |
| net EUR/month (after AI calls and tools) | 9,806.87 | 1,928.41 |
| payback months (pilot + rollout build) | 1.9 | 9.9 |

### Sensitivity (AI-assisted fixed at the self-reported average)

Levels 3, 10, 20, 26 min are illustrative, not measured.

| manual min | saved min | hours saved/month | value EUR/month | net EUR/month | payback months |
|---|---|---|---|---|---|
| 3 (illustrative) | -2.0 | -100.6 | -1,998.76 | -2,185.71 | n/a (no payback) |
| 7.1 (Shopzilla median, computed) | 2.1 | 106.4 | 2,115.36 | 1,928.41 | 9.9 |
| 10 (illustrative) | 5.0 | 251.4 | 4,996.91 | 4,809.96 | 4.0 |
| 15 (Ayhan) | 10.0 | 502.8 | 9,993.81 | 9,806.87 | 1.9 |
| 20 (illustrative) | 15.0 | 754.2 | 14,990.72 | 14,803.77 | 1.3 |
| 26 (illustrative) | 21.0 | 1,056.0 | 20,987.01 | 20,800.06 | 0.9 |

At 5 min AI-assisted and 3 min manual the saving is negative: AI would cost more time than it saves. The business case depends on the manual time, which is still an estimate.

### Second value: faster first response through triage (qualitative)

Auto triage routes each email to the right queue / department, so customers should get a first response sooner (SLA). No SLA improvement number is claimed.
- Held-out queue_match is 85% on 20 synthetic emails (langsmith/monitoring_note.md), so about 15% still need manual re-routing.
- A human approves every draft; nothing is sent automatically.
- Link to the proposed SLA target: first response within 24 h for 90% of emails (research/sector_research.md).

