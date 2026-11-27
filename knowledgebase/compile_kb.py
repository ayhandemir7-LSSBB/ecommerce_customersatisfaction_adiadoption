# Ingest: extract text from knowledge base PDFs 01-03 into one compiled file (doc 04 is design evidence, not prompt)
import sys, re, hashlib
from pathlib import Path
from pypdf import PdfReader

KB = Path(sys.argv[1]); OUT = Path(sys.argv[2])
FOOT = "Invented for an Ironhack case study. Spreekorb is not a real company. Not legal advice."
DOCS = ["01_customer_service_policy.pdf", "02_brand_voice_guide.pdf", "03_reply_guardrails.pdf"]

parts = []
for name in DOCS:
    text = "\n".join(page.extract_text() for page in PdfReader(KB / name).pages)
    lines = [l.strip() for l in text.split("\n")]
    lines = [l for l in lines if l and FOOT not in l and not re.fullmatch(r"Page \d+", l)]
    # a lone bullet glyph becomes "- " in front of the next line
    clean, bullet = [], False
    for l in lines:
        if len(l) == 1 and not l.isalnum():
            bullet = True; continue
        clean.append(("- " if bullet else "") + l); bullet = False
    lines = clean
    parts.append(f"=== {name.replace('.pdf', '')} ===\n" + "\n".join(lines))
compiled = "\n\n".join(parts) + "\n"
OUT.write_text(compiled, encoding="utf-8")
print(OUT, len(compiled.split()), "words, sha256", hashlib.sha256(compiled.encode()).hexdigest()[:12])
