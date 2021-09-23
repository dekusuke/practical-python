import csv
import sys

def portfolio_cost(filename):
    
    f = open('Data/portfolio.csv')
    rows = csv.reader(f)
    headers = next(rows)
    total = 0
    for row in rows:
        cost = int(row[1]) * float(row[2])
        total = total + cost
        
    return total
    f.close()
    
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

        

    

