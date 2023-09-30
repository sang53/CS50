from fpdf import FPDF

outputfile = "shirtificate.pdf"

def main():
    # get user name
    name = input("Name: ")

    # set up FPDF
    pdf = FPDF()
    pdf.add_page()

    # add image
    pdf.image("shirtificate.png", x=20, y=60, w=pdf.epw * 0.9)

    # set font for title & print
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(60, 20, "CS50 Shirtificate", align="C", center=True, new_x="LMARGIN", new_y="NEXT")

    # empty cell to align name onto shirt
    pdf.cell(60, 80, "", new_x="LMARGIN", new_y="NEXT")

    # set font & colour for name
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "", 20)

    # print cell & output file
    pdf.cell(60, 20, name + " took CS50", center=True, align="C")
    pdf.output(outputfile)

if __name__ == "__main__":
    main()