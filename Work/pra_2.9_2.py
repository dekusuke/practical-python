import sys
import csv

def read_prices(filename):
    prices = {}
    f = open(filename)
    rows = csv.reader(f)
    try:
        for row in rows:
            prices[row[0]] = float(row[1])
    except IndexError:
        pass

    return prices
    f.close()
