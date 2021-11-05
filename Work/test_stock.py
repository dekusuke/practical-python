import unittest
import stock

class TestStock(unittest.TestCase):   
    def test_create(self):
        s = stock.Stock('Goog', 100, 490.1)
        self.assertEqual(s.name, 'Goog')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        self.assertEqual(s.cost, 49010.0)
        s.sell(50)
        self.assertTrue(s.shares < 100)
    
    def test_bad_shares(self):
        s = stock.Stock('Goog', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '100'

            
if __name__ == '__main__':
    unittest.main()
