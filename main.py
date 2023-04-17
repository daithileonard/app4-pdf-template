from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
pdf.set_font(family="Times", size=12)
pdf.cell(w=0, h=12, txt="Hi PDF", align='L', ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hello", align='L', ln=1, border=1)
pdf.cell(w=0, h=12, txt="Its Me", align='L', ln=1, border=1)

pdf.output("output.pdf")