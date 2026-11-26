# Opportunities and risks

| Opportunity | Risk | Mitigation |
|---|---|---|
| Faster first response with AI reply drafts | A wrong draft is sent to a customer | A human approves every reply before it is sent |
| Root cause insight for the business | The AI invents reasons (hallucination) | LangSmith evals on a held-out test set, cite the source tickets |
| Team-level view of SLA and CSAT | It turns into performance monitoring of people | Team level only, minimum group of 5, Betriebsrat agreement first |
| Use of customer ticket texts | Personal data goes to OpenAI | Data processing agreement (DPA), transfer check, PII masking, GDPR Art. 35 DPIA, EU AI Act (Regulation (EU) 2024/1689) check |
| Trust through transparency (answers CEO Chleo's black box fear) | Staff distrust the tool and do not use it | Show the steps and sources, involve the works council, track the trust pulse |

## One risk avoided on purpose
- No auto-send of replies: the AI only drafts, a human decides.
- No individual agent scoring: no agent names are stored, only team level views.
