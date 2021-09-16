def portfolio_cost(filename):

    with open('Data/missing.csv', 'rt') as f:
        headers = next(f)
        total = 0
        try:
            for line in f:
                row = line.split(',')
                number = int(row[1])
                price = float(row[2])
                cost = number * price
                total = total + cost
            return total
        except ValueError:
            print('something is missing')


cost2 = portfolio_cost('Data/missing.csv')
print('Total cost:', cost2)
