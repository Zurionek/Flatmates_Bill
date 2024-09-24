"""
Flatmate bill is a simple program that helps 2 flatmates split the bill payment
based on the amount of days they spent in the flat in specific period
"""

from flat import Bill, Flatmate
from report import PdfReport, FileSharer

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

pdf_report = PdfReport(filename="{}.pdf".format(the_bill.period))
pdf_report.generate(flatmate1=user_1, flatmate2=user_flatmate, bill=the_bill)

Commented part of code to be used in case of file sharing
At the moment no API available
file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
