# Airtable setup for R1-04 (Review queue)

Base: **Spreekorb Email Triage** · Table: **Review queue**
Create the fields with these exact names (lower case). 15 fields. The workflow maps to them by name.

| Field | Airtable type | Filled by | Purpose |
|---|---|---|---|
| email_id | Single line text (primary field) | Seed CSV | Tobi-Bueck row id, for tracing |
| subject | Single line text | Seed CSV | Email subject |
| body | Long text | Seed CSV | Email text |
| language | Single line text | Seed CSV | de or en |
| created | Created time | Airtable | The trigger watches this field |
| ai_queue | Single line text | n8n | AI queue suggestion |
| ai_priority | Single line text | n8n | AI priority suggestion |
| ai_reason | Long text | n8n | One-line reason (transparency) |
| draft_reply | Long text | n8n | AI draft, never sent automatically |
| policy_sections | Single line text | n8n | Policy sections the draft relies on, e.g. "Policy 4, Policy 5" (transparency) |
| status | Single select: New, Pending review, Approved, Edited, Rejected, Skipped: empty email | n8n, then the agent | Human-in-the-loop state |
| final_reply | Long text | Agent | What the agent would actually send |
| reviewer_note | Long text | Agent | Why edited or rejected |
| model | Single line text | n8n | Model and prompt version (gpt-4o-mini, prompt v4) |
| processed_at | Single line text | n8n | ISO time of the AI run |

## Steps
1. Create the base and table, then the fields above. Delete Airtable's default fields (Notes, Assignee...).
2. Copy the **base id** (`app...`) and **table id** (`tbl...`) from the Airtable URL.
3. Import `n8n/workflow.json` in n8n (Workflows > Import from file).
4. In the 4 Airtable nodes, paste the base id and table id where it says `PASTE_BASE_ID` / `PASTE_TABLE_ID` (or pick them from the list), and select your Airtable credential. Select your OpenAI credential in the model node.
5. Open both update nodes and check that the columns are mapped (n8n may ask to refresh the column list).
6. Activate the workflow. Then import `n8n/airtable_seed.csv` into the table (or paste the rows). Within about a minute each row gets an AI draft and status `Pending review`.
7. Review 3 rows yourself in Airtable: set status to Approved / Edited / Rejected and fill final_reply. Take the screenshots.
