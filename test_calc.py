import unittest
import calc

class  Testcalc(unittest.TestCase):
    def test_add(self):
        result=calc.add(10,5)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-5, 5), 0)
        self.assertEqual(calc.add(1.2, 1.3), 2.50)
        self.assertEqual(calc.add(-3, -6), -9)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-5, 7), -12)
        self.assertEqual(calc.subtract(-4,-4), 0)
        self.assertEqual(calc.subtract(1.2,0.2), 1)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(1.2, 1.2), 1.44)
        self.assertEqual(calc.multiply(5, 0), 0)
        self.assertEqual(calc.multiply(55,2), 110)
        self.assertEqual(calc.multiply(-55,-2), 110)
        self.assertEqual(calc.multiply(-55,2), -110)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(-2, 1), -2)
        self.assertEqual(calc.divide(-5, -1), 5)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        
    def test_power(self):
        self.assertEqual(calc.power(10, 2), 100)
        self.assertEqual(calc.power(2, -1), 0.5)
        self.assertEqual(calc.power(2, 0), 1)
        with self.assertRaises(ValueError):
            calc.power(-2, 0)
        
        
if __name__=='__main__':
    unittest.main()

