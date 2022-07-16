from fpdf import FPDF
from PIL import Image, ImageOps
# -----------------------------------------------
# get Inputs
name = input("Name: ")
name = name + " took CS50"
# -----------------------------------------------
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

# Add header
pdf.set_font("helvetica", "B", 50)ct

pdf.cell(0, 60, 'CS50P Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

# Add shirt
pdf.image("shirtificate.png", w=pdf.epw)

# Add text onto shirt
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
pdf.text(x=70, y=140, txt=name)

#Output
pdf.output("shirtificate.pdf")

# important hints are on https://pyfpdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image