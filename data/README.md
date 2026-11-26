# Data

## Sources
- Shopzilla customer service contacts (Kaggle, eCommerce Customer Service Satisfaction): https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction . Licence: to confirm (Kaggle page did not render).
- Tobi-Bueck customer support tickets (Hugging Face): https://huggingface.co/datasets/Tobi-Bueck/customer-support-tickets . Licence: CC BY-NC 4.0 (per Hugging Face licence tag, checked 2026-11-26).

## Raw files are not committed
`data/raw/` is git-ignored. Download it with notebook R1-02a. Raw files: `shopzilla_cs_satisfaction.csv`, `tobi_bueck_tickets.csv`.

## Processed files (`data/processed/`, made by notebook R1-02)
| File | Rows | What it is |
|---|---|---|
| shopzilla_contacts_clean.csv | 85907 | All channels (Inbound, Outcall, Email), pseudonymised |
| shopzilla_email_clean.csv | 3006 | Email channel only, pseudonymised |
| tobi_tuning_150.csv | 150 | Tickets for tuning and demo (split = tuning) |
| tobi_test_50.csv | 50 | Held-out test tickets (split = test); 10 have timing_test = True |
| synthetic_team_pulse.csv | 80 | Synthetic agent pulse, team level (synthetic = True) |
| synthetic_team_pulse_summary.csv | see file | Counts per team, answer and reason; counts under 5 shown as <5 (synthetic = True) |

## Column changes (Shopzilla)
- Added `response_hours` = issue_responded minus Issue_reported at, in hours. Negative values are set to empty. `response_valid` is True when response_hours is usable. Use valid rows only for medians.
- Added `team` = Team NN from the Supervisor, pseudonymised. The numbering is random on every run of the notebook, so labels differ between runs and the mapping is not saved.
- Added `group_ok` = True when the team-month has at least 5 distinct agents (checked before agent names were dropped).
- Dropped `Agent_name`, `Supervisor`, `Manager`, `connected_handling_time`, `Order_id`, `Unique id`, `Customer_City`, `Agent Shift`, `Tenure Bucket`. The last four are a row-level re-identification risk. They can be added later only as aggregates with at least 5 per group.
- Customer Remarks is kept for the root cause report (UC2). Emails, phone numbers and urls are replaced by [EMAIL], [PHONE], [URL]. Agent, supervisor and manager name parts are replaced by [NAME]. Other personal details in free text are possible (to confirm).
- Timestamps parsed day-first (dd/mm/yyyy hh:mm); Survey_response_Date parsed as dd-Mon-yy.

## Column changes (Tobi-Bueck)
- Kept only the latest version (400; blank versions excluded), duplicates on subject and body removed before sampling.
- Kept queues: Customer Service, Returns and Exchanges, Billing and Payments, Product Support. Languages: en, de.
- Random sample of 200 (random_state 42). Added `ticket_id`, `split` (tuning or test) and `timing_test` (True for 10 test rows).
- Emails and phone numbers in subject, body and answer are replaced by [EMAIL] and [PHONE]. The phone pattern can also mask long number strings such as dates.

## What is synthetic
- `synthetic_team_pulse.csv` and its summary are fully made up (synthetic = True). The pulse is illustrative, not Spreekorb staff. Team labels (Pulse team A to H) are not linked to Shopzilla teams. The answer weights are placeholder assumptions, not data.
- Whether the Tobi-Bueck tickets are synthetic: to confirm.
- Shopzilla is a public dataset for a different company; Spreekorb is invented. Treat results as illustration.

## Pseudonymisation, minimum group and the Other bucket
No agent, supervisor or manager names are stored. Teams are shown only as Team NN. Minimum group size is 5: a team-month needs at least 5 distinct agents, otherwise its rows are shown as Other. If Other has fewer than 5 distinct agents in a month, those rows are dropped. Rows dropped: 0 (all channels) and 17 (email). Other share of rows: 0.001 (all channels) and 0.002 (email). The pulse is team level only, with at least 5 answers per team and no respondent id.

Pseudonymised, not anonymous: timestamps and free text could still allow re-identification together with public data. Customer names in free text are not fully masked, so review before any OpenAI call.

## Test set rule
`tobi_test_50.csv` is read-only. Never use it for prompt tuning. Use it only for the final evaluation. timing_test rows measure latency only, never prompt tuning.

## Open items
- Shopzilla licence: to confirm.
- Whether the Tobi-Bueck tickets are synthetic: to confirm.

## Compliance (before real use)
- Team SLA and CSAT views need works council (Betriebsrat) agreement (BetrVG par. 87(1) no. 6) and a data protection impact assessment (DPIA).
- The EU AI Act assessment for worker monitoring is open.
- Sending tickets to OpenAI needs a data processing agreement (DPA) and a transfer check.
