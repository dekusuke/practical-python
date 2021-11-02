import os
import time
def follow(filename):
    
    f = open(filename)
    f.seek(0, os.SEEK_END)
    output = []

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line
        '''
        if change < 0:
            output.append(name)
            output.append(price)
            output.append(change)                        
            print(output)
            output = []
        '''
        


if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')
    
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

