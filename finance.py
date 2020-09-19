import csv

class Calc:
    def __init__(self, file):
        self.file = file

    def cDate(self):
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            x = 0
            line_count = 0
            for row in csv_reader:
                x += 1
                if line_count == x:
                    print(row[0])
            line_count += 1

    def date(self):
        with open('exampledata.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            date = list(csv_reader)
            fDate = date[1][0]
            print('Starting from ' + ' to ' + fDate)

    def exp(self):
        total_expense = []
        with open(self.file) as csv_file:  
            csv_reader = csv.reader(csv_file, delimiter = ',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    total_expense.append(0.0)
                else:
                    debit = row[5]
                    if debit == '':
                        total_expense.append(0.0)
                    else:
                        total_expense.append(float(debit))
                line_count += 1
        print('Total Expenses: ' + str(sum(total_expense)))

    def inc(self):
        total_income = []
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    total_income.append(0.0)
                else:
                    credit = row[6]
                    if credit == '':
                        total_income.append(0.0)
                    else:
                        total_income.append(float(credit))
                line_count += 1
        print('Total Income: ' + str(sum(total_income)))

uname = input('Name: ')
ufile = input('File: ')
c1 = Calc(ufile)
print('Hello, ' + uname)
c1.cDate()
c1.date()
c1.exp()
c1.inc()
