import csv

def read_prices(filename):
    prices = {}
    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    try:
        for row in rows:
            prices[row[0]] = row[1]
    except IndexError:
        pass
    return prices
        
        


