from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill
    """
    def __init__(self,amount,period):
        self.period = period
        self.amount = amount

class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = round((bill.amount * weight),2)
        return to_pay
class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Adding title
        pdf.set_font(family="Times", size=20, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        #Insert Period Label and value
        pdf.cell(w=100, h=40, txt="Period:", border=1, align="L")
        pdf.cell(w=130, h=40, txt=bill.period, border=1)

        pdf.output(self.filename)


the_bill = Bill(120,"August_2024")
john = Flatmate("John", 20)
marry = Flatmate("Marry", 25)

print("John pays: ", john.pays(the_bill,marry))
print("Marry pays: ", marry.pays(the_bill,john))

pdf_report = PdfReport(filename="Report_1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)