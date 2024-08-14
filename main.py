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
        pass

the_bill = Bill(120,"March_2021")
john = Flatmate("John", 20)
marry = Flatmate("Marry", 25)

print("John pays: ", john.pays(the_bill,marry))
print("Marry pays: ", marry.pays(the_bill,john))