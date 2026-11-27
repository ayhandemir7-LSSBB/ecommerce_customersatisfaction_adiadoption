# Spreekorb: AI for email customer service (Ironhack capstone, Round 1)

Independent case study. Spreekorb is an invented Berlin e-commerce company (about 500 employees, no AI yet). All data is public or synthetic and is labelled as such.

## Overview

- Client: Spreekorb. CEO Chleo fears that AI is a black box. This project answers with transparency: every number has a source or a label (estimate, measured, synthetic), every AI draft shows a short reason and the policy sections it used, and a person approves every draft. Nothing is sent automatically.
- Focus: email customer service, SLA (first response time) and CSAT (customer satisfaction).
- UC1: email triage plus reply drafts, a human approves (built as the Round 1 POC in n8n).
- UC2: root cause report to the business (described in research/use_cases.md).
- UC3: team-level view, a coaching signal and not a scorecard (team tile M5 in the dashboard).
- Round 1 deliverables: research pack, data prep, Tableau dashboard, n8n POC, LangSmith monitoring sample, cost and timeline, this README.

## Data and privacy

- Data is synthetic or public: Shopzilla (Kaggle) and Tobi-Bueck (Hugging Face, synthetic) are proxy datasets, the Spreekorb emails and the policy documents are invented. Sources are listed in `data/README.md` and `dashboard/dashboard_documentation.md`.
- Team level only, minimum group of 5. No agent names or IDs are recorded.
- Before real use: data processing agreement (DPA), works council (Betriebsrat) agreement and a data protection impact assessment (DPIA), see `n8n/workflow_documentation.md`.
- No keys in the repo. Keys live in a local `.env` file that is git-ignored; `.env.example` lists the names only.

## What is where

| Path | Content |
|---|---|
| `research/` | Sector research (`research/sector_research.md`), opportunities and risks (`research/opportunities_risks.md`), use cases (`research/use_cases.md`) |
| `data/` | Data README (`data/README.md`), processed data in `data/processed/`, timing log (`data/timing_log.csv`); raw downloads are not committed |
| `dashboard/` | Tableau workbook: [Spreekorb email CS_ AI drafts, human-approved.twbx](dashboard/Spreekorb%20email%20CS_%20AI%20drafts%2C%20human-approved.twbx), documentation with the Tableau Public link (`dashboard/dashboard_documentation.md`), metric CSVs in `dashboard/data/` |
| `n8n/` | POC workflow (`n8n/workflow.json`, credentials removed), documentation (`n8n/workflow_documentation.md`), Airtable setup (`n8n/airtable_setup.md`), seed emails (`n8n/airtable_seed.csv`), prompt (`n8n/triage_prompt.md`), screenshots in `n8n/screenshots/` |
| `langsmith/` | Monitoring sample: note (`langsmith/monitoring_note.md`), trace summary (`langsmith/trace_summary.csv`), human review (`langsmith/human_review.csv`), screenshots in `langsmith/screenshots/` |
| `cost_estimation/` | Cost analysis (`cost_estimation/cost_analysis.md`) and timeline (`cost_estimation/timeline_estimate.md`) |
| `knowledgebase/` | Invented Spreekorb policy documents (PDF) used by the draft prompt |
| `decisions/` | Decision log (`decisions/decision_log.md`) |
| feedback | Round 1 decision (added by card R1-08) |
| `notebooks/` | One task notebook per card (build evidence, run top to bottom) |
| `specs/`, `board.md`, `logs/` | How the project was built: specs, board, agent log |

## How to view the dashboard

1. Open the Tableau Public link: https://public.tableau.com/app/profile/ayhan.demir/viz/SpreekorbemailCSAIdraftshuman-approved/Dashboard1#2

Workbook:
2. Or open the packaged workbook [Spreekorb email CS_ AI drafts, human-approved.twbx](dashboard/Spreekorb%20email%20CS_%20AI%20drafts%2C%20human-approved.twbx) in Tableau Desktop or Tableau Public.
3. Each tile has a headline, a source footer and a SYNTHETIC badge where the numbers are made up. The metric definitions are in `dashboard/dashboard_documentation.md`.
4. No Tableau? See the screenshot: ![Dashboard](dashboard/screenshots/Spreekorb%20email%20CS.png)

## How to run the POC

Needs: Python 3.12, an OpenAI key, a LangSmith key, an n8n account and an Airtable account.

1. Install and set keys: `pip install -r requirements.txt`, copy `.env.example` to `.env` and fill in the values. Variable names: AIRTABLE_ID, LANGSMITH_API_KEY, LANGSMITH_PROJECT, LANGSMITH_TRACING, OPENAI_API_KEY. Never commit `.env`.
2. Airtable: create the base and the Review queue table as described in `n8n/airtable_setup.md`.
3. n8n: import `n8n/workflow.json` (Workflows > Import from file), paste the Airtable base id and table id, select your Airtable and OpenAI credentials, activate the workflow.
4. Import `n8n/airtable_seed.csv` into the table. Each row gets an AI draft and the status Pending review. A person then sets Approved, Edited or Rejected. Nothing is sent. Details: `n8n/workflow_documentation.md`.
5. LangSmith: run `notebooks/R1-05_langsmith.ipynb` top to bottom (uses OPENAI_API_KEY and LANGSMITH_API_KEY). It writes `langsmith/trace_summary.csv` and `langsmith/monitoring_note.md`.
6. Optional: re-run the other notebooks in `notebooks/` in card order (R1-02a downloads the raw data first).

## About the numbers

This README quotes no figures. Every figure (CSAT, SLA, timing, cost, payback) lives in its source file with its label (estimate, measured or synthetic): `dashboard/dashboard_documentation.md`, `langsmith/monitoring_note.md`, `cost_estimation/cost_analysis.md`.
