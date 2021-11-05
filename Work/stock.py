from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)
    

    def __init__(self, name, shares, price):

        self.name = name
        self.shares = shares
        self.price = price
    '''
    @property
    def shares(self):
        return self._shares



    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
    '''

        

    @property
    def cost(self):
        return self.shares * self.price




    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'



    def sell(self, num):
        self.shares = self.shares - num
        return self.shares

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor
        
    def cost(self):
        actual_cost = super().cost()
        return 1.25 * actual_cost
