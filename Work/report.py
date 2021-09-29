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

def print_report(list_port, dic_pri):
    report = []
    for dic in list_port:
        add = (dic['name'], dic['shares'], dic_pri[dic['name']], dic_pri[dic['name']] - dic['price'])
        report.append(add)
    print(report)

    return report

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = print_report(portfolio, prices)
    headers = ('Name', 'Shares', 'Price', 'Change')

    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
        

    for name, shares, price, change in report:
        price = '$' + str(price)
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')



