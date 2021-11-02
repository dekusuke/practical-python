import csv
import sys
from report import read_portfolio
import stock
def portfolio_cost(filename):
    
    '''
    records = read_portfolio(filename)
    total = 0
    for rowno, row in enumerate(records, start=1):        
        try:
            cost = int(row.shares) * float(row.price)
            total = total + cost
        except ValueError:
            print(f"Row {rowno}: Couldn't convert: {row}")
    print('Total cost:', total)
    '''
    portfolio = read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    portfolio_cost(argv[1])


if __name__ == '__main__':
    import sys
    main(sys.argv)
    

        

    

