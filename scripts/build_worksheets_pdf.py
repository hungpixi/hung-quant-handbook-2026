from __future__ import annotations

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(r"D:\code\trade")
SRC = ROOT / "docs" / "HUNG_QUANT_WORKSHEETS_2026.md"
OUT = ROOT / "docs" / "HUNG_QUANT_WORKSHEETS_2026.pdf"


def register_fonts():
    pdfmetrics.registerFont(TTFont("ArialVN", r"C:\Windows\Fonts\arial.ttf"))
    pdfmetrics.registerFont(TTFont("ArialVN-Bold", r"C:\Windows\Fonts\arialbd.ttf"))


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="TitleVN",
        parent=styles["Title"],
        fontName="ArialVN-Bold",
        fontSize=22,
        leading=28,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#102A43"),
        spaceAfter=12,
    ))
    styles.add(ParagraphStyle(
        name="HeadingVN",
        parent=styles["Heading1"],
        fontName="ArialVN-Bold",
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#243B53"),
        spaceBefore=8,
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="BodyVN",
        parent=styles["BodyText"],
        fontName="ArialVN",
        fontSize=11,
        leading=16,
        spaceAfter=8,
    ))
    return styles


def page_canvas(canvas, doc):
    canvas.saveState()
    canvas.setFont("ArialVN", 9)
    canvas.setFillColor(colors.HexColor("#486581"))
    canvas.drawString(doc.leftMargin, 12 * mm, "Hưng Quant Worksheets 2026")
    canvas.drawRightString(A4[0] - doc.rightMargin, 12 * mm, str(doc.page))
    canvas.restoreState()


def parse(text: str, styles):
    story = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            story.append(Spacer(1, 4))
            continue
        if line.strip() == "[[PAGEBREAK]]":
            story.append(PageBreak())
            continue
        if line.startswith("# "):
            story.append(Paragraph(line[2:].strip(), styles["TitleVN"]))
            story.append(Spacer(1, 4))
            continue
        if line.startswith("## "):
            story.append(Paragraph(line[3:].strip(), styles["HeadingVN"]))
            continue
        if line.startswith("### "):
            story.append(Paragraph(line[4:].strip(), styles["BodyVN"]))
            continue
        story.append(Paragraph(line, styles["BodyVN"]))
    return story


def main():
    register_fonts()
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="Hưng Quant Worksheets 2026",
        author="Hưng",
    )
    text = SRC.read_text(encoding="utf-8")
    story = parse(text, styles)
    doc.build(story, onFirstPage=page_canvas, onLaterPages=page_canvas)
    print(f"Built PDF: {OUT}")


if __name__ == "__main__":
    main()

