import csv
import sys

def portfolio_cost(filename):
    
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total = 0
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            cost = int(record['shares']) * float(record['price'])
            total = total + cost
        except ValueError:
            print(f"Row {rowno}: Couldn't convert: {row}")
    print('Total cost:', total)
    f.close()
    

        

    

