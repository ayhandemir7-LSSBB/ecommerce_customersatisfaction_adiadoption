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
| synthetic_team_pulse_summary.csv | 53 | Counts per team, answer and reason; counts under 5 shown as <5 (synthetic = True) |

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
- E-commerce keyword filter (applied after the queue filter and dedup): a ticket is kept only if its subject OR its body contains one of these words, case-insensitive: order, delivery, shipping, parcel, return, refund, exchange, invoice, payment, charge, damaged, cancel, Bestellung, Lieferung, Paket, Versand, Rücksendung, Rückgabe, Erstattung, Umtausch, Rechnung, Zahlung, beschädigt, stornieren. Why: the queues also hold off-topic tickets (for example software questions), and the tuning and test emails should look like Spreekorb shop email.
- Rule 1, start of word (prefix match): a keyword must match at the start of a word, so "orders" and "returned" match, but "border" does not. Caveat: "charge" also matches "charger" and "charging", so a few off-topic tickets can pass.
- Rule 2, idioms ignored: before matching, the idioms "in order to", "in charge", "in return" are removed (case-insensitive, whole words, any whitespace between the words) from the text used for matching only. The stored subject and body are not changed. Why: these idioms contain a keyword but are not about shop topics.
- Tickets left after the filter: 907.
- Stop rule: if fewer than 200 tickets remain after the filter, the notebook prints a WARNING and stops before sampling and writing. The sample would then be topped up with synthetic emails (not done in this notebook). It also stops if any queue has fewer than 10 tickets.
- Stratified sample (random_state 42): the test set (50) is 10 random tickets per queue (4 queues = 40) plus 10 random tickets from the remaining pool. The tuning set (150) is a random draw from what is left, so tuning and test never overlap. Added `ticket_id` (tuning T001 to T150, test T151 to T200), `split` (tuning or test) and `timing_test` (True for 10 test rows, random).
- Emails and phone numbers in subject, body and answer are replaced by [EMAIL] and [PHONE]. The phone pattern can also mask long number strings such as dates.

Held-out test set, tickets per queue and language (computed when the file was written):

| Queue | de | en |
|---|---|---|
| Customer Service | 6 | 4 |
| Returns and Exchanges | 1 | 9 |
| Billing and Payments | 9 | 11 |
| Product Support | 4 | 6 |

## What is synthetic
- `synthetic_team_pulse.csv` and its summary are fully made up (synthetic = True). The pulse is illustrative, not Spreekorb staff. Team labels (Pulse team A to H) are not linked to Shopzilla teams. The answer weights are placeholder assumptions, not data.
- The Tobi-Bueck tickets are synthetic (stated on the Hugging Face dataset card).
- Shopzilla is a public dataset for a different company; Spreekorb is invented. Treat results as illustration.

## Pseudonymisation, minimum group and the Other bucket
No agent, supervisor or manager names are stored. Teams are shown only as Team NN. Minimum group size is 5: a team-month needs at least 5 distinct agents, otherwise its rows are shown as Other. If Other has fewer than 5 distinct agents in a month, those rows are dropped. Rows dropped: 0 (all channels) and 17 (email). Other share of rows: 0.001 (all channels) and 0.002 (email). The pulse is team level only, with at least 5 answers per team and no respondent id.

Pseudonymised, not anonymous: timestamps and free text could still allow re-identification together with public data. Customer names in free text are not fully masked, so review before any OpenAI call.

## Test set rule
`tobi_test_50.csv` is read-only. Never use it for prompt tuning. Use it only for the final evaluation. timing_test rows measure latency only, never prompt tuning.

`langsmith/heldout_priority_labels.csv` (50 rows, made by notebook R1-02 from tobi_test_50.csv) is the labelling sheet. `priority_human`, `queue_human` and `note` start blank. The notebook keeps an existing sheet only if it has the same ticket ids and labels already filled; otherwise the old sheet is copied to the backup folder and a new blank one is written.

## Open items
- Shopzilla licence: to confirm.

## Compliance (before real use)
- Team SLA and CSAT views need works council (Betriebsrat) agreement (BetrVG par. 87(1) no. 6) and a data protection impact assessment (DPIA).
- The EU AI Act assessment for worker monitoring is open.
- Sending tickets to OpenAI needs a data processing agreement (DPA) and a transfer check.

<!-- R1-02b start -->
## R1-02b Synthetic Spreekorb email set

Why: the Tobi-Bueck tickets proved to be SaaS/IT topics even after the shop-keyword filter (0 of 50 held-out fully fit Spreekorb; this comes from Ayhan manual review, not a sourced figure). So the triage test, the timing test and the n8n demo use a synthetic Spreekorb set. Shopzilla stays for the dashboard.

- `data/processed/spreekorb_emails_60.csv`: 60 synthetic emails (S01-S60), 30 de / 30 en, 14 topics, written by gpt-4o-mini (temperature 0.9). Column synthetic = True.
- All emails are AI-generated synthetic test data (gpt-4o-mini), not real customers, and not for production or legal use.
- Split made in code from the grid before any AI output: 40 tuning, 20 heldout, 10 heldout rows have timing_flag = True.
- The grid was raised from 56 to 60 (+1 to Order status, Invoice resend, Double charge and How-to / product question; Ayhan approved, 27 Nov).
- Order number SPK- plus 6 digits is set in Python (seed 42). It is required in the body, except for How-to and Thanks emails (optional).
- queue_intended and priority_intended are the generator intentions, not ground truth. The queue_human and priority_human labels from Ayhan are the official truth.
- `langsmith/heldout_labels_v2.csv`: the 20 heldout emails with empty queue_human / priority_human for Ayhan to fill (the intended values are left out on purpose, to avoid anchoring).
- Triage output is a draft, and a human approves every reply (human oversight).
- The deletion-request and legal-threat emails are synthetic routing tests for escalation to a human or legal.
- Results are reported at whole-set or queue level only, since there are 1-2 heldout rows per topic.
- Notebook: `notebooks/R1-02b_synthetic_emails.ipynb`. Note: re-running R1-02 rewrites this README and drops this section; re-run R1-02b cell 3d to add it back.
<!-- R1-02b end -->
