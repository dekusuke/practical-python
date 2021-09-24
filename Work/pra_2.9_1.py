import csv
import sys

def read_portfolio(filename):
    
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    portfolio = []
    for name, shares, price in rows:
        holding = {'name': name, 'shares': int(shares), 'price': float(price)}
        portfolio.append(holding)

    return portfolio
    f.close()
