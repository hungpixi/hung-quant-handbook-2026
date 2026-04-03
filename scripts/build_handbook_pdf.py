from __future__ import annotations

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer


ROOT = Path(r"D:\code\trade")
SRC = ROOT / "docs" / "HUNG_QUANT_HANDBOOK_2026.md"
OUT = ROOT / "docs" / "HUNG_QUANT_HANDBOOK_2026.pdf"


def register_fonts():
    pdfmetrics.registerFont(TTFont("ArialVN", r"C:\Windows\Fonts\arial.ttf"))
    pdfmetrics.registerFont(TTFont("ArialVN-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
    pdfmetrics.registerFont(TTFont("ArialVN-Italic", r"C:\Windows\Fonts\ariali.ttf"))
    pdfmetrics.registerFont(TTFont("ArialVN-BoldItalic", r"C:\Windows\Fonts\arialbi.ttf"))


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="BookTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontName="ArialVN-Bold",
        fontSize=22,
        leading=28,
        spaceAfter=14,
        textColor=colors.HexColor("#102A43"),
    ))
    styles.add(ParagraphStyle(
        name="BookSubtitle",
        parent=styles["Heading2"],
        alignment=TA_CENTER,
        fontName="ArialVN",
        fontSize=12,
        leading=16,
        spaceAfter=18,
        textColor=colors.HexColor("#334E68"),
    ))
    styles.add(ParagraphStyle(
        name="CoverMeta",
        parent=styles["BodyText"],
        alignment=TA_CENTER,
        fontName="ArialVN",
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#486581"),
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="H1",
        parent=styles["Heading1"],
        fontName="ArialVN-Bold",
        fontSize=16,
        leading=20,
        spaceBefore=14,
        spaceAfter=8,
        textColor=colors.HexColor("#102A43"),
    ))
    styles.add(ParagraphStyle(
        name="H2",
        parent=styles["Heading2"],
        fontName="ArialVN-Bold",
        fontSize=13,
        leading=17,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.HexColor("#243B53"),
    ))
    styles.add(ParagraphStyle(
        name="BodyBook",
        parent=styles["BodyText"],
        fontName="ArialVN",
        fontSize=10.5,
        leading=15,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="QuoteBook",
        parent=styles["BodyText"],
        fontName="ArialVN-Italic",
        fontSize=10,
        leading=14,
        leftIndent=10,
        textColor=colors.HexColor("#486581"),
        spaceAfter=8,
    ))
    styles["Code"].fontName = "ArialVN"
    styles["Code"].fontSize = 9
    styles["Code"].leading = 12
    return styles


def page_canvas(canvas, doc):
    canvas.saveState()
    canvas.setFont("ArialVN", 9)
    canvas.setFillColor(colors.HexColor("#486581"))
    canvas.drawString(doc.leftMargin, 12 * mm, "Hung Quant Handbook 2026")
    canvas.drawRightString(A4[0] - doc.rightMargin, 12 * mm, str(doc.page))
    canvas.restoreState()


def draw_cover(story, styles):
    story.append(Spacer(1, 35 * mm))
    story.append(Paragraph("HƯNG QUANT HANDBOOK 2026", styles["BookTitle"]))
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph(
        "Sổ tay 30 ngày xây nền quant forex, nghiên cứu MQL5, và dựng 4 cỗ máy kiếm tiền",
        styles["BookSubtitle"],
    ))
    story.append(Spacer(1, 10 * mm))
    story.append(Paragraph("Phiên bản biên tập để đọc, học, và chia sẻ", styles["CoverMeta"]))
    story.append(Paragraph("Tác giả: Hưng", styles["CoverMeta"]))
    story.append(Paragraph("Tinh thần: Kính nghiệp, tôn trọng thị trường, học để sống sót lâu dài", styles["CoverMeta"]))
    story.append(Spacer(1, 16 * mm))
    story.append(Paragraph(
        "Tài liệu này được thiết kế như một handbook + workbook: vừa để đọc, vừa để làm bài tập, vừa để vận hành workflow nghiên cứu thực tế.",
        styles["QuoteBook"],
    ))
    story.append(PageBreak())


def parse_markdown(text: str, styles):
    story = []
    draw_cover(story, styles)
    in_code = False
    code_lines: list[str] = []
    bullet_buffer: list[str] = []

    def flush_bullets():
        nonlocal bullet_buffer
        if not bullet_buffer:
            return
        items = []
        for bullet in bullet_buffer:
            items.append(ListItem(Paragraph(bullet, styles["BodyBook"])))
        story.append(ListFlowable(items, bulletType="bullet", start="circle", leftIndent=16))
        story.append(Spacer(1, 4))
        bullet_buffer = []

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.strip().startswith("```"):
            flush_bullets()
            if not in_code:
                in_code = True
                code_lines = []
            else:
                story.append(Preformatted("\n".join(code_lines), styles["Code"]))
                story.append(Spacer(1, 6))
                in_code = False
                code_lines = []
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            flush_bullets()
            story.append(Spacer(1, 4))
            continue

        if line.strip() == "[[PAGEBREAK]]":
            flush_bullets()
            story.append(PageBreak())
            continue

        if line.startswith("# "):
            flush_bullets()
            continue

        if line.startswith("## "):
            flush_bullets()
            if line[3:].strip().lower() not in {"trang bìa", "trang bia"}:
                story.append(PageBreak())
            story.append(Paragraph(line[3:].strip(), styles["H1"]))
            continue

        if line.startswith("### "):
            flush_bullets()
            story.append(Paragraph(line[4:].strip(), styles["H2"]))
            continue

        if line.startswith("> "):
            flush_bullets()
            story.append(Paragraph(line[2:].strip(), styles["QuoteBook"]))
            continue

        if line.startswith("- "):
            bullet_buffer.append(line[2:].strip())
            continue

        if line[:2].isdigit() and line[1] == ".":
            flush_bullets()
            story.append(Paragraph(line, styles["BodyBook"]))
            continue

        flush_bullets()
        story.append(Paragraph(line, styles["BodyBook"]))

    flush_bullets()
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
        title="Hung Quant Handbook 2026",
        author="Hung",
    )
    text = SRC.read_text(encoding="utf-8")
    story = parse_markdown(text, styles)
    doc.build(story, onFirstPage=page_canvas, onLaterPages=page_canvas)
    print(f"Built PDF: {OUT}")


if __name__ == "__main__":
    main()
