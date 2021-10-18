import csv
import sys
import stock
from fileparse import parse_csv
import tableformat

def read_portfolio(filename):
    with open(filename) as lines:
        portdicts = parse_csv(lines, select=['name', 'shares', 'price'], types=[str,int,float], has_headers=True)
        portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

def read_prices(filename):
    with open(filename) as lines:
        prices = parse_csv(lines)
    return prices

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = float(current_price) - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows

def portfolio_report(portfolio_filename, prices_filename):
    
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report_data(portfolio, prices)
    
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)


def print_report(reportdata, formatter):

    formatter.headings(['name', 'shares', 'price', 'change'])

    

    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
    '''

    for name, shares, price, change in reportdata:
        price = float(price)
        change = float(change)


    
        '''
        print(f'{name:>10s} {shares:>10d} {price:>10f} {change:>10.2f}')
        '''



        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
