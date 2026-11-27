# LangSmith monitoring note: R1-05

Prompt v5 (n8n/triage_prompt.md), model gpt-4o-mini, temperature 0.2. Written by notebooks/R1-05_langsmith.ipynb.

## What was monitored
- Every AI triage + draft call is traced in LangSmith as spreekorb_triage: the email in, the JSON out (language, queue, priority, reason, draft reply, policy sections), time, tokens and cost.
- Dev set: spreekorb-dev-v4 (14 tuning emails, one per topic, seed 44), experiment dev-v5-617203f1. Truth = intended labels.
- Official held-out set: spreekorb-heldout-20 (20 emails, never used for tuning), experiment heldout-v5-489260bd. Run once per prompt version. Truth = human labels (queue_human, priority_human) by Ayhan; intended labels are secondary columns.
- Code checks only, no AI grading. A person scores the 10 timing_flag drafts 1 to 5 (human_review.csv).
- Old LangSmith experiments (Tobi datasets, policy-8) stay as history and are not used.

## Why the set is synthetic
- The public Tobi-Bueck tickets turned out to be SaaS and IT topics: 0 of 50 fit Spreekorb, by manual review (Ayhan).
- So the test emails are 60 invented Spreekorb emails (spreekorb_emails_60.csv, synthetic, generated): 14 topics, German and English, tuning and held-out split.

## Prompt history v1 to v5
- v1 and v2: earlier versions. The version notes in n8n/triage_prompt.md do not record what changed, so nothing is claimed here.
- v3: added queue definitions, a priority rubric (aligned with Policy 8) and a length rule.
- v4 (27 Nov 2026): after dev run 2, added the reply language rule: an English email gets an English reply, a German email a German reply with du.
- v5 (27 Nov 2026): after dev-v4, language field first in the output, length 40 to 120 words, no unknown facts (no dispatch status or check results), each policy section cited once. Brand Voice Guide v1.1.
- Rule: the prompt is never tuned on the held-out emails. A change gets a new version and a new experiment.

## Held-out results per evaluator (share of drafts passing)

| Evaluator | What it checks | Dev (14) | Held-out (20) |
|---|---|---|---|
| queue_match | queue equals the truth (held-out: human label) | 93% | 85% |
| priority_match | priority equals the truth (held-out: human label) | 71% | 70% |
| priority_within_one | priority at most one step off | 100% | 95% |
| no_banned_phrase | no banned phrase (EN/DE guardrails) and no em dash | 100% | 100% |
| cited_sections_valid | cited sections are Policy 1 to 10 | 100% | 100% |
| policy_fact_cited | a draft with days, hours or EUR cites a policy section | 100% | 95% |
| citations_used | draft cites at least one policy section (how-to and thanks topics pass) | 100% | 95% |
| escalation_flagged | deletion request and legal threat start with Escalate to; other topics do not | 100% | 100% |
| language_match | draft in the email language (stopword guess on the draft) | 100% | 100% |
| word_count | 40 to 120 words (40 to 80 for escalation holding replies) | 100% | 100% |
| signoff_ok | draft ends with the sign-off of the email language | 100% | 100% |
| no_unknown_status | no claim of dispatch status or check results | 100% | 100% |
| citations_unique | no policy section listed twice | 93% | 100% |
| queue_intended_match | secondary: queue equals the intended queue | n/a | 90% |
| priority_intended_match | secondary: priority equals the intended priority | n/a | 70% |

By queue (human label), held-out. Queues with n < 5 are anecdotal, not rates:
- Billing and Payments (n=5): queue_match 1.0, priority_match 0.8
- Customer Service (n=7): queue_match 1.0, priority_match 0.71
- Product Support (n=5): queue_match 0.4, priority_match 0.4
- Returns and Exchanges (n=3): queue_match 1.0, priority_match 1.0

Time and cost (heldout_20): 20 drafts traced, average 2.21 s, 3099.2 tokens in / 129.8 out, total 0.007591 USD, 0.006925 EUR. USD is the cost LangSmith calculates from token counts (not an OpenAI invoice); EUR is an estimate: USD x 0.9123, tradingview.com (USDEUR), 27 Nov 2026). Source: LangSmith run cost (measured, USD).
Time and cost (timing_10): 10 drafts traced, average 2.22 s, 3107.2 tokens in / 128.9 out, total 0.003802 USD, 0.003469 EUR. USD is the cost LangSmith calculates from token counts (not an OpenAI invoice); EUR is an estimate: USD x 0.9123, tradingview.com (USDEUR), 27 Nov 2026). Source: LangSmith run cost (measured, USD).
Label context (computed from heldout_labels_v2.csv and spreekorb_emails_60.csv, not by an AI): human and intended labels agree on 19/20 queues and 14/20 priorities. Priority is partly a judgement call, so a low priority_match is partly label disagreement, not only AI error. The human label stays the official truth.
Full table: langsmith/trace_summary.csv. Human scores: langsmith/human_review.csv.

## Transparency message for Chleo
- The AI never sends an email. It prepares a draft plus a suggested queue and priority. A person reads, edits and decides.
- Every draft can be opened and inspected: the email, the prompt version, the policy sections it relied on, what it wrote, how long it took and what it cost.
- Rules such as banned phrases, length, language and valid policy citations are checked by code, the same way every time.
- We tested on invented emails only, and only 20 in the final test. This shows the method works and is visible. It does not prove quality yet.
- Scores rate the AI drafts, never agents. No agent names or IDs are recorded.

## Limits
- Synthetic data: invented emails, not real Spreekorb customers.
- Only 20 held-out emails, 1 to 2 per topic: report results for the whole set or at queue level, never per topic.
- The held-out run happens once per prompt version. Any prompt change after a held-out run is a new version; the old held-out result stays as it is. Deleting a held-out experiment to rerun it is a human decision.
- Code checks test form, not truth: a draft can pass all of them and still be wrong. That is why a person reviews every draft.
- The banned phrase check finds exact phrases only; language is guessed from common words; time includes the network from the laptop that ran the notebook.
- Cost comes from LangSmith in USD; the EUR figure is an estimate with the dated rate above.
- Only synthetic emails were sent. OpenAI and LangSmith are US processors: real customer emails need a data processing agreement, a transfer basis and an EU region where offered, first. The works agreement is a draft, so this setup is prepared for compliance, not proof of it.

## Evidence
- LangSmith share link: PENDING: paste the public share link of the held-out experiment
- PENDING screenshot: experiment table with the evaluator columns (langsmith/screenshots/)
- PENDING screenshot: one trace showing input, output, latency, tokens and cost (langsmith/screenshots/)
