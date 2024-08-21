import webbrowser

from fpdf import FPDF

class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        """
        :param flatmate1:
        :param flatmate2:
        :param bill:
        """
        pdf = FPDF(orientation="P", unit="pt")
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)

        # Flatmate1 & Flatmate2 pays
        flatmate1_pays = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pays = str(flatmate2.pays(bill, flatmate1))
        bill_total = str(bill.amount)

        # Adding title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)

        # Insert Period Label and value
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=100, h=40, txt="Period:", align="L", )
        pdf.set_font(family="Times", size=16)
        pdf.cell(w=80, h=40, txt=bill.period, ln=1)

        #Insert bill total value
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=100, h=40, txt="Total:", align="L", )
        pdf.set_font(family="Times", size=16)
        pdf.cell(w=80, h=40, txt=bill_total, ln=1)

        # Insert Name and due amount of the first flatmate (str method to be used to change the float into str)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=100, h=40, txt=flatmate1.name + ":", align="L", )
        pdf.set_font(family="Times", size=16)
        pdf.cell(w=80, h=40, txt=flatmate1_pays, ln=1)

        # Insert Name and due amount of the second flatmate (str method to be used to change the float into str)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=100, h=40, txt=flatmate2.name + ":", align="L")
        pdf.set_font(family="Times", size=16)
        pdf.cell(w=80, h=40, txt=flatmate2_pays, ln=1)

        pdf.output(self.filename)

        # Automatically open PDF report in the default browser
        webbrowser.open(self.filename)
