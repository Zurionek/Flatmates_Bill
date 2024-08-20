import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
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
        """
        :param bill:
        :param flatmate2:
        :return:
        """
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = round((bill.amount * weight), 2)
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

        # Adding title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)

        # Insert Period Label and value
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=100, h=40, txt="Period:", align="L", )
        pdf.set_font(family="Times", size=16)
        pdf.cell(w=80, h=40, txt=bill.period, ln=1)

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

user_name = input("Hello, what is your name? ")
user_bill = float(input("{}, please enter the bill amount: ".format(user_name)))
bill_period = input("For what period the bill is issued? - Please provide month and year: ")
user_days_in_house = int(input("How many days you spent in the house during the period: {} :".format(bill_period)))
flatmate_name = input("What is the name of your flatmate? ")
flatmate_days_in_house = int(input("How many days {} spent in the house during the period: {} :".
                                   format(flatmate_name, bill_period)))


the_bill = Bill(user_bill, bill_period)
user_1 = Flatmate(user_name, user_days_in_house)
user_flatmate = Flatmate(flatmate_name, flatmate_days_in_house)

print("{} pays: ".format(user_name), user_1.pays(the_bill, user_flatmate))
print("{} pays: ".format(flatmate_name), user_flatmate.pays(the_bill, user_1))

pdf_report = PdfReport(filename="Report_1.pdf")
pdf_report.generate(flatmate1=user_1, flatmate2=user_flatmate, bill=the_bill)
