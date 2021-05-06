import webbrowser


from flat import Bill, Flatmate
from report import PdfReport

amount = float(input('Enter the bill amount: '))
period = input('What is the bill period? E.g. Dececember 2020: ')

name1 = input('What is your name? ')
days_in_house1 = int(
    input(f'How many days did {name1} stay in the house during the bill period? '))

name2 = input('What is your flatmate name? ')
days_in_house2 = int(
    input(f'How many days did {name2} stay in the house during the bill period? '))

the_bill = Bill(amount, period)

flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{name2} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
