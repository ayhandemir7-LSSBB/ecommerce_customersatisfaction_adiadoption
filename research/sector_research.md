# Sector research: Spreekorb

## Sector and size
- Sector: e-commerce (online retail), Berlin. Spreekorb is an invented company used as a case study.
- Size: about 500 employees (given in the client brief). That makes Spreekorb a large company. In the EU, an SME has fewer than 250 employees. Source: European Commission Recommendation 2003/361/EC.
- Focus: email customer service, SLA (first response time) and CSAT (customer satisfaction).
- CEO Chleo fears AI is a black box, so trust and transparency come first in every proposal.

## Why size matters
- Email volume: many tickets, so a small time saving per email adds up.
- Many agents and teams: a team-level view is useful, but only with a minimum group of 5 people.
- Works council (Betriebsrat): it must be involved in tools that can monitor staff (BetrVG par. 87(1) no. 6).
- GDPR Art. 35 (DPIA): customer emails hold personal data, so a data protection impact assessment is needed before real use.
- EU AI Act (Regulation (EU) 2024/1689): the assessment for worker monitoring is still open (to confirm with a lawyer).
- A large company has the legal, data protection and IT capacity to handle this. A small one often does not.

## Problems (with numbers)
Shopzilla is a public dataset from another company. It is a proxy/benchmark for Spreekorb, not Spreekorb data.
- Email share: 3.5% of 85907 contacts are Email (computed from shopzilla_contacts_clean.csv).
- First response time: median per channel is Email 0.12 hours (n=2896), Inbound 0.10 hours (n=65758), Outcall 0.10 hours (n=14125) (computed from response_hours, valid rows only).
- CSAT: mean CSAT per channel is Email 3.90, Inbound 4.25, Outcall 4.27; Email has the lowest share of CSAT scores 4-5 at 73.5% (computed from CSAT Score in shopzilla_contacts_clean.csv).
- Free text: 34.1% of Email contacts have a customer remark (computed from shopzilla_email_clean.csv), so root cause work has limited text.
- Ticket mix: tickets per queue in the Tobi-Bueck tuning sample are Customer Service 52, Product Support 50, Billing and Payments 28, Returns and Exchanges 20 (computed from tobi_tuning_150.csv only, the test set is not used).
- Spreekorb own volume, SLA target and CSAT: not available, source to find (Ayhan).

## Email KPI baseline
| KPI | Market benchmark | Spreekorb target (proposed) | Spreekorb today | Basis |
|---|---|---|---|---|
| Email first response (SLA) | German shoppers expect an email reply within 24 h; e-commerce average response time 17.3 h (German market estimate) | ≤ 24 h for 90% of emails, stretch 1 h (target (proposed)) | median 31 h, 58% within 24 h (synthetic) | Shopzilla is chat/phone-paced (email median 7 min, 95.9% within 24 h, computed from Shopzilla), so it is not used as the email SLA baseline; Spreekorb today is synthetic: no triage, manual drafts. |
| Email CSAT (share of 4-5 scores) | e-commerce median 82%, top quartile 92%+ (German market estimate) | 85% (target (proposed)) | 73.5% (computed from Shopzilla email) | Lowest of the channels: Inbound 82.7%, Outcall 83.2% (computed from Shopzilla). |
| Email volume | 20-50 tickets per 100 orders; another source says 2-5 contacts per 100 orders (German market estimate, sources disagree) | n/a | ~3,017 emails per month (computed from Shopzilla, busiest month) | Sources disagree on contact rate, so volume is used directly, not derived from orders. |
| Unanswered emails | German mystery-mailing study: one in three emails goes unanswered (German market estimate) | 0% (target (proposed)) | 6% reopened or chased again (synthetic) | Pressure signal for UC2. |

German market estimates: source links to be added by Ayhan.

## Data
Shopzilla is a public Kaggle dataset used as a proxy/benchmark for Spreekorb (synthetic status to confirm); it holds contacts, CSAT scores and response times, so it fits the SLA and CSAT problem (https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction). Tobi-Bueck is on Hugging Face, licence CC BY-NC 4.0 (per Hugging Face licence tag); synthetic status to confirm, and its multilingual English and German ticket texts with answers fit email triage and reply drafts (https://huggingface.co/datasets/Tobi-Bueck/customer-support-tickets). The team pulse is synthetic (made up, not Spreekorb staff) and shows adoption and trust at team level, so it fits the team view without real personal data.
