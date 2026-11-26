# AGENTS.md: Spreekorb capstone

## Project
Ironhack AI Consulting capstone. Client: Spreekorb, invented Berlin e-commerce company, about 500 employees, no AI yet.
CEO Chleo fears AI is a black box. Focus: email customer service, SLA (first response time) and CSAT.
Use cases: UC1 email triage + reply drafts (human approves), UC2 root cause report to the business, UC3 team-level view.

## Stack
Python 3.12, Jupyter in VS Code, pandas, OpenAI gpt-4o-mini, LangSmith, n8n, Tableau (.twbx + Tableau Public).

## Repo map
data/raw (downloads, not committed) | data/processed | research | dashboard | n8n | langsmith | cost_estimation | feedback | notebooks | specs | decisions | logs

## Card flow
board.md is the communication board. Status: To do > In progress > Review > Approved > Done.
1. Ayhan names the card. Read its spec in specs/ first.
2. builder writes ONE task notebook: notebooks/<card-id>_<short-name>.ipynb.
3. reviewer checks the notebook against the spec. compliance-checker and data-checker when the spec says so.
4. Ayhan runs the notebook, then moves the card to Approved. Only Ayhan sets Approved or Done.
5. Write a one-line handoff note on the card in board.md.

## Task notebook pattern (every card)
Cells, short and beginner-friendly, # comments:
1. Check: right folder, input files exist. Print PASS/FAIL.
2. Backup: copy every file you will change to _backup/<timestamp>/.
3. Create: do the card's steps (write files with %%writefile or Python).
4. Verify: each acceptance item from the spec prints PASS/FAIL.
5. Unchanged: prove existing files you did not own are unchanged.
6. Undo: restore the backup (runs only if RUN_UNDO = True).
7. Git: print git commands, never run them.

## Definition of Done
All spec checks PASS, reviewer OK, Ayhan approved, board.md updated.

## Never
- Never commit, push or reset git. Ayhan commits.
- Never read or write .env or real keys. Use .env.example names only.
- Never use real personal data. Never record agent names or IDs; team level only, minimum group of 5.
- Never invent numbers or sources. Cite, or label "estimate" or "synthetic".
- Never touch files outside the card's spec. Smallest change that meets the spec.
