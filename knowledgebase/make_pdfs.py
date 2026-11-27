# Renders knowledge_base/source/*.md into knowledge_base/*.pdf. Usage: python make_pdfs.py <source_folder> <output_folder>
import re, sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                ListFlowable, ListItem, PageBreak)

SRC = Path(sys.argv[1]); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
INK, GREY, CORAL = colors.HexColor("#2E3440"), colors.HexColor("#6B7280"), colors.HexColor("#C8553D")
FOOT = "Invented for an Ironhack case study. Spreekorb is not a real company. Not legal advice."

S = {
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=INK, spaceAfter=4),
    "h1b": ParagraphStyle("h1b", fontName="Helvetica", fontSize=12, leading=16, textColor=GREY, spaceAfter=6),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11.5, leading=15, textColor=CORAL, spaceBefore=8, spaceAfter=3),
    "p": ParagraphStyle("p", fontName="Helvetica", fontSize=10, leading=13.5, textColor=INK, spaceAfter=4),
    "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=8.5, leading=11, textColor=GREY, spaceAfter=6),
    "quote": ParagraphStyle("q", fontName="Helvetica", fontSize=9.5, leading=12.5, textColor=INK, leftIndent=10,
                            borderPadding=(4, 6, 4, 6), backColor=colors.HexColor("#F4F5F7")),
    "cell": ParagraphStyle("c", fontName="Helvetica", fontSize=9, leading=11.5, textColor=INK),
    "cellb": ParagraphStyle("cb", fontName="Helvetica-Bold", fontSize=9, leading=11.5, textColor=INK),
}

def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    return t

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
    canvas.drawString(18 * mm, 10 * mm, FOOT)
    canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()

def render(md_path):
    lines = md_path.read_text(encoding="utf-8").split("\n")
    story, i, h1_count = [], 0, 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln:
            i += 1; continue
        if ln.startswith("## Page 2"):
            story.append(PageBreak())
        if ln.startswith("# "):
            h1_count += 1
            story.append(Paragraph(inline(ln[2:]), S["h1"] if h1_count == 1 else S["h1b"])); i += 1; continue
        if ln.startswith("## "):
            story.append(Paragraph(inline(ln[3:]), S["h2"])); i += 1; continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
                i += 1
            data = [[Paragraph(inline(c), S["cellb"] if r == 0 else S["cell"]) for c in row] for r, row in enumerate(rows)]
            t = Table(data, colWidths=[(A4[0] - 36 * mm) / len(rows[0])] * len(rows[0]), repeatRows=1)
            t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EDEFF2")),
                                   ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#C9CED6")),
                                   ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
            story += [t, Spacer(1, 6)]; continue
        if ln.startswith(">"):
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(inline(lines[i].lstrip("> ").rstrip())); i += 1
            story += [Paragraph("<br/>".join(block), S["quote"]), Spacer(1, 6)]; continue
        if re.match(r"^(- |\d+\. )", ln):
            items, numbered = [], ln[0].isdigit()
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(ListItem(Paragraph(inline(re.sub(r"^(- |\d+\. )", "", lines[i])), S["p"]), leftIndent=12))
                i += 1
            story += [ListFlowable(items, bulletType="1" if numbered else "bullet", start=1 if numbered else None,
                                   leftIndent=12, bulletFontSize=8), Spacer(1, 3)]; continue
        style = S["meta"] if (ln.startswith("*") and ln.endswith("*")) or ln.startswith("Version") or ln.startswith("Between") else S["p"]
        story.append(Paragraph(inline(ln), style)); i += 1
    out = OUT / (md_path.stem + ".pdf")
    SimpleDocTemplate(str(out), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm,
                      bottomMargin=18 * mm, title=md_path.stem).build(story, onFirstPage=footer, onLaterPages=footer)
    return out

for md in sorted(SRC.glob("0*.md")):
    print(render(md))
