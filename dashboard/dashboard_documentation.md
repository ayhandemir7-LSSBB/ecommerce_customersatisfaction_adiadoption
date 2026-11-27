# Dashboard documentation: R1-03

Title of the dashboard: Email customers are our least satisfied: AI drafts, human-approved, can close the gap

Subtitle: Spreekorb is an invented company. Tiles marked SYNTHETIC use made-up numbers. Every AI draft is approved by a person before it is sent.

Tableau Public link: https://public.tableau.com/app/profile/ayhan.demir/viz/SpreekorbemailCSAIdraftshuman-approved/Dashboard1#2

Workbook: Spreekorb email CS_ AI drafts, human-approved.twbx

Screenshots:
![Spreekorb email CS](screenshots/Spreekorb%20email%20CS.png)

Shopzilla and Tobi-Bueck are public datasets used as proxy data. The market figures in M3 are cited (eDesk, Netomi 2020), see Sources.

## Sources
- Shopzilla (Kaggle): https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction
- Tobi-Bueck (Hugging Face): https://huggingface.co/datasets/Tobi-Bueck/customer-support-tickets
- eDesk (German shopper expectation, 24 h): https://www.edesk.com/de/blog/5-wesentliche-strategien-fuer-eine-effizientere-bearbeitung-von-kundenanfragen-im-online-handel-deutscher-markt/
- Netomi 2020 (e-commerce market average, 17.3 h): https://ai.netomi.com/hubfs/Content%20Library/customerservice-benchmarkreport-ecommerce.pdf
- langsmith/trace_summary.csv (R1-05): source of M7
- research/sector_research.md (KPI baseline) and research/use_cases.md

## Metrics
Tags: A problem, B use case, C trust. The CSV files are in dashboard/data/ and are computed from data/processed (M7: langsmith/trace_summary.csv) when the notebook R1-03_dashboard_prep runs. dashboard/data/dashboard_all.csv stacks all 7 metrics in one table (columns: metric, dim, series, value, unit, n, count_text, label, shown, highlight, synthetic, sort_order, source).

### M1 (A) Email CSAT vs other channels
- Headline: Email customers are the least satisfied: 73.5% give 4-5 vs 82.7% on Inbound and 83.2% on Outcall
- Chart type: Bar chart, one bar per channel, Email highlighted, label the percent
- Source: Shopzilla (Kaggle https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction), computed from shopzilla_contacts_clean.csv
- Synthetic label: No (public proxy data, different company)
- CSV file: dashboard/data/m1_csat_by_channel.csv

### M2 (A) Email CSAT by category
- Headline: Cancellation emails have the lowest satisfaction: only 60.9% give 4-5 (n=64) vs 73.5% for all email
- Chart type: Horizontal bars sorted by volume, show n in the label, filter shown = True
- Source: Shopzilla (Kaggle https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction), computed from shopzilla_email_clean.csv
- Synthetic label: No (public proxy data)
- CSV file: dashboard/data/m2_email_csat_by_category.csv

### M3 (A) SLA gap: today vs target vs market
- Headline: SYNTHETIC: Spreekorb answers emails in a median of 31 h; customers expect 24 h
- Chart type: Bullet or bar chart in hours with a reference line at 24 h; colours for today, target, market; touch time (minutes) as a separate small tile
- Source: research/sector_research.md KPI baseline; eDesk https://www.edesk.com/de/blog/5-wesentliche-strategien-fuer-eine-effizientere-bearbeitung-von-kundenanfragen-im-online-handel-deutscher-markt/; Netomi 2020 https://ai.netomi.com/hubfs/Content%20Library/customerservice-benchmarkreport-ecommerce.pdf; touch time: cost_estimation/cost_analysis.md (R1-06 timing test)
- Synthetic label: Yes for the Spreekorb-today rows (synthetic); target is target (proposed); market rows are cited (eDesk, Netomi 2020)
- CSV file: dashboard/data/m3_sla_gap.csv

### M4 (B) UC1 triage opportunity: what AI triage would route
- Headline: 98.0% of sample tickets are Customer Service / Returns / Billing: routine mails AI can triage and draft for human approval
- Chart type: Stacked bar by queue, split by language (en, de)
- Source: Tobi-Bueck (Hugging Face https://huggingface.co/datasets/Tobi-Bueck/customer-support-tickets), computed from tobi_tuning_150.csv only
- Synthetic label: Yes (SYNTHETIC, confirmed synthetic by Ayhan, 2026-11-26)
- CSV file: dashboard/data/m4_triage_mix.csv

### M5 (B) UC3 team view: email CSAT per team
- Headline: Email satisfaction ranges from 42.4% to 88.5% across 36 teams: a coaching signal, not a scorecard
- Chart type: Dot plot of CSAT per team in alphabetical order, filter shown = True
- Source: Shopzilla (Kaggle https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction), computed from shopzilla_email_clean.csv; teams have at least 5 distinct agents per team-month (group_ok)
- Synthetic label: No (public proxy data); team labels are pseudonyms that change on every R1-02 run
- CSV file: dashboard/data/m5_team_email_view.csv

### M6 (C) AI adoption pulse (trust)
- Headline: 56% would use the AI draft assistant; 'need training' is the most common reason (24 answers, synthetic)
- Chart type: Two tiles: Yes/No donut plus a bar chart of reasons (why_category)
- Source: data/processed/synthetic_team_pulse.csv
- Synthetic label: Yes (SYNTHETIC, made up, not Spreekorb staff)
- CSV file: dashboard/data/m6_ai_pulse.csv

### M7 (C) LangSmith trace evidence (R1-05)
- Headline: 30 held-out and timing drafts traced: 2.21 s and about EUR 0.000346 per draft (gpt-4o-mini, EUR estimate)
- Chart type: Three big-number tiles: drafts traced, average seconds per draft, average cost per draft in EUR
- Source: langsmith/trace_summary.csv + langsmith/monitoring_note.md (R1-05)
- Synthetic label: No (measured latency and token cost of gpt-4o-mini calls on invented Spreekorb emails, R1-05 LangSmith held-out and timing runs; dev runs not counted; EUR cost is an estimate, USD x 0.9123, tradingview.com USDEUR, 27 Nov 2026)
- CSV file: dashboard/data/m7_human_in_loop.csv

## Notes on hidden values and labels
- M2: 4 categories hidden (n<30). Only the top 8 categories by volume (n of at least 30) are shown. Hidden rows stay in the CSV with n and a blank value (shown = False).
- M5: 3 teams hidden (n<30). Hidden rows stay in the CSV with n and a blank value (shown = False).
- M5: the minimum of 5 distinct agents per team-month was asserted in R1-02 before names were dropped (flag group_ok). This card relies on that flag. No names are shown.
- M5: a team view needs works council (Betriebsrat) agreement and a DPIA before real use (see data/README.md).
- M3: Touch time is minutes, customer wait is hours: emails wait in an unprioritised queue. Touch time per email: 15 min manual (estimate (Ayhan, R1-06)) and 5 min with the AI draft (measured (self-reported average, Ayhan, R1-06; done second, learning bias)), from cost_estimation/cost_analysis.md (R1-06 timing test).
- M6: counts under 5 are shown as <5.
- M7: computed from langsmith/trace_summary.csv: drafts traced = sum of n, seconds per draft = n-weighted mean of avg_latency_s, cost per draft = total cost in EUR / drafts. m7_human_in_loop.csv is a legacy file name; it now holds the LangSmith trace rows.

## Story order: Chleo understands in 2 minutes
1. M1 (A): the problem: email customers are the least satisfied.
2. M2 (A): where it hurts inside email.
3. M3 (A): the SLA gap, clearly labelled synthetic.
4. M4 (B): what AI triage would do; a human approves every draft.
5. M7 (C): trust evidence: the held-out and timing drafts are traced (count, seconds, cost) in R1-05; EUR cost is an estimate.
6. M6 (C): trust: how the team feels about AI (synthetic).
7. M5 (B): team view, last: a coaching signal, not a scorecard.

## Tableau build steps (beginner-friendly)
1. Open Tableau Public. Choose Connect > Text file and open one CSV from dashboard/data/.
2. Make one sheet per metric (M1 to M7). Drag the fields to Columns and Rows and pick the chart type above. For M2 and M5 filter shown = True.
3. Put the headline of each metric into the sheet title. Use the text exactly as written above.
4. Create a new Dashboard. Drag the sheets in story order. Use a wide layout (for example 1200 x 900).
5. Put a SYNTHETIC badge on M3, M4, M6 and a source footer on every tile (source text and CSV name).
6. Label the M3 target as target (proposed) and the market values with their source (eDesk, Netomi 2020).
7. Add the title and the subtitle above as text boxes at the top.
8. Save the packaged workbook as a .twbx in dashboard/ (File > Save As, packaged workbook).
9. Publish: File > Save to Tableau Public (done, link above).
10. Take screenshots into dashboard/screenshots/ (done, embedded above).

## 2-minute test (Ayhan ticks)
Ask Chleo (or a colleague playing Chleo) to look at the dashboard for 2 minutes without help.
- [ ] She can say what the problem is (email customers are the least satisfied, first response is slow).
- [ ] She can say why it is worth solving (the gap to the target and the market).
- [ ] She sees where each number comes from (source footer on every tile).
- [ ] She can tell which tiles are synthetic (M3, M4, M6).
- [ ] She sees that a person approves every AI draft (see the subtitle and M4).
- [ ] The team tile reads as a coaching signal, not a scorecard.

Result: Test run 27 Nov 2026: 1 non-technical tester, 5 of 6 passed; fixed: SYNTHETIC badge on M4 made larger
