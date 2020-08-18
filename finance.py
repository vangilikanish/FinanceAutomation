'''
import csv

row_5 = 0

with open('/Users/kanish/Desktop/Finance(Delete)/exampleData.csv') as csvf:
    csv_reader = csv.reader(csvf)
    for row in csvf:
        if row[3] == 'Debit':
            print('Hello')
'''
