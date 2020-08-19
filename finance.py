import csv
import json

csvf = 'exampleData.csv'
total_spending = []

class expense():
    with open(csvf) as csv_file:  
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                total_spending.append(0.0)
            else:
                debit = row[5]
                if debit == '':
                    total_spending.append(0.0)
                else:
                    total_spending.append(float(debit))
            line_count += 1
    expenses = sum(total_spending)

'''
csv_reader = [row for row in csv.reader(csv_file)]
THIS IS THE READER YOU SHOULD USE IF YOU WANT TO TAKE A SINGLE VALUE FORM A CELL
FOR EX. 'PRINT(CSV_READER[1][0])'
'''

'''
total_spending = list(map(float, total_spending))
USE THIS TO CONVERT THE VALUES IN A LIST INTO A STRING, INT, ETC
'''
