# Board: Spreekorb capstone (Round 1, submit Mon 30 Nov 2026 before 18:00 as project-5)

Status: To do > In progress > Review > Approved > Done. Only Ayhan sets Approved and Done.

| ID | Card | Spec | Status | Evidence | Handoff note |
|---|---|---|---|---|---|
| R1-00 | Bootstrap harness | (this notebook) | In progress | notebooks/00_bootstrap_harness.ipynb | |
| R1-01 | Research pack | specs/R1-01_research.md | Approved | notebooks/R1-01_research_pack.ipynb | Builder done, 1 fix round after reviewer + data check; numbers computed at run time from data/processed; open: Spreekorb email volume/SLA target/CSAT "source to find", Shopzilla + Tobi synthetic status to confirm. Ayhan to run. Approved by Ayhan 27 Nov 2026. |
| R1-02 | Data prep | specs/R1-02_data.md | Approved | notebooks/R1-02_data_prep.ipynb | Builder done, 2 fix rounds; reviewer/data/compliance PASS (minor polish after); Tobi row check fixed to 61,765; spec deviation: all channels kept + email-only file (Ayhan's call); open: Shopzilla licence, Tobi synthetic status. Ayhan to run (Restart & Run All). Approved by Ayhan 27 Nov 2026. |
| R1-02a | Download data | specs/R1-02_data.md | Approved | notebooks/R1-02a_download_data.ipynb | Reviewer: changes needed (no backup/undo for requirements.txt, wrong filename in git cell, data/README.md links missing); raw data git-ignored OK. Approved by Ayhan 27 Nov 2026. |
| R1-03 | Tableau dashboard | specs/R1-03_dashboard.md | Approved | notebooks/R1-03_dashboard_prep.ipynb | Builder done, 1 fix round after reviewer + data check; notebook writes 7 metric CSVs (dashboard/data/, small spec extension) + dashboard_documentation.md; Tableau built: .twbx + screenshot in dashboard/, Public link in docs, 2-minute test 27 Nov 5 of 6 passed (M4 badge enlarged); M7 pending R1-05. Approved by Ayhan 27 Nov 2026. |
| R1-04 | n8n POC | specs/R1-04_n8n_poc.md | To do | | |
| R1-05 | LangSmith sample | specs/R1-05_langsmith.md | To do | | |
| R1-06 | Timing + cost + timeline | specs/R1-06_cost_timeline.md | To do | | |
| R1-07 | README + submit | specs/R1-07_submit.md | To do | | |
| R1-08 | Round 1 decision | specs/R1-08_decision.md | To do | | |
