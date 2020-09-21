import csv

class Calc:
    def __init__(self, file):
        self.file = file

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
    
    def bal(self):
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            lBal = list(csv_reader)
            print('This is your starting balance: '+ (lBal[-1][8]) + '\nThis is your closing balance: ' + (lBal[1][8]))

    def date(self):
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            lDate = list(csv_reader)
            print('This is you finanacial overview starting from ' + (lDate[-1][0]) + ' up to ' + (lDate[1][0]) + '.')

uname = input('Name: ')
n = int(input('Amount of Files: '))
print('Hello, ' + uname)
#files = []
while (n > 0):
    ufile = input('File ' + str(n) + ' : ')
    #files += [ufile]
    c1 = Calc(ufile)
    c1.date()
    c1.bal()
    c1.exp()
    c1.inc()
    n -= 1
