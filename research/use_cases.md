# Use cases

## UC1 Email triage and reply drafts (human approves)
- Problem it solves: slow first response because agents sort and write every email by hand.
- Data used: Tobi-Bueck tickets (English and German) for tuning and testing.
- KPI: first response time (SLA) and share of drafts approved without edits.
- Human in the loop: an agent reads, edits and approves every draft. Nothing is sent automatically.
- Why it fits a large company: high email volume makes small savings add up, and there is capacity for review and compliance.

## UC2 Root cause report to the business
- Problem it solves: management sees low CSAT or slow replies but not why.
- Data used: Shopzilla contacts, CSAT, response times and customer remarks (proxy for Spreekorb).
- KPI: CSAT trend and the top causes found, checked against source tickets.
- Human in the loop: an analyst checks every cause and its cited tickets before the report goes out.
- Why it fits a large company: enough volume for patterns to show, and several departments (product, logistics, support) can act on the findings.

## UC3 Team-level view
- Problem it solves: leaders cannot see SLA, CSAT and adoption by team.
- Data used: Shopzilla team column (40 pseudonymised teams, Team NN / Other, computed from shopzilla_contacts_clean.csv, minimum 5 distinct agents per team-month) and the synthetic team pulse.
- KPI: team SLA, team CSAT and the adoption and trust pulse.
- Human in the loop: team leads discuss the view with the works council. Teams under 5 people are never shown.
- Why it fits a large company: many teams make a team view useful, and a Betriebsrat and data protection staff exist to agree the rules.
