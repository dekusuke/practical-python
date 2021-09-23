import csv
import sys

def read_portfolio(filename):
    
    f = open('Data/portfolio.csv')
    rows = csv.reader(f)
    headers = next(rows)
    portfolio = []
    for name, shares, price in rows:
        holding = {'name': name, 'shares': int(shares), 'price': float(price)}
        portfolio.append(holding)

    return portfolio
    f.close()

def read_prices(filename):
    prices = {}
    f = open('Data/prices.csv')
    rows = csv.reader(f)
    try:
        for row in rows:
            prices[row[0]] = float(row[1])
    except IndexError:
        pass

    return prices
    f.close()


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
total1 = 0
total2 = 0

for s in portfolio:
    total1 += s['shares'] * s['price']
    total2 += s['shares'] * prices[s['name']]


print('before', total1)
print('after', total2)
print('gain/loss', total1-total2)



