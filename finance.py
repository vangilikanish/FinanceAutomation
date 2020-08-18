import csv

csvf = 'exampleData.csv'
rows = []

with open(csvf) as csv_file:  
    csv_reader = [row for row in csv.reader(csv_file)]
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            rows.append(0)
        else:
            debit = row[5]
            rows.append(debit)
        line_count += 1

print(rows)  
