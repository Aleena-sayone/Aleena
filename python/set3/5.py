import unittest

class Arithmetic:    
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def divide(self, x, y):
        return x / y

    def multiply(self, x, y):
        return x * y

class TestArithmetic(unittest.TestCase): 
    def setUp(self):
        self.arithmetic = Arithmetic()

    def testAdd(self):
        self.assertEqual(4, self.arithmetic.add(2, 2))      
        self.assertEqual(10, self.arithmetic.add(3, 7))     
        self.assertEqual(90, self.arithmetic.add(-10, 100)) 

    def testSubtract(self):
        self.assertEqual(4, self.arithmetic.subtract(6, 2))      
        self.assertEqual(23, self.arithmetic.subtract(30, 7))    
        self.assertEqual(400, self.arithmetic.subtract(500, 100)) 

    def testDivide(self):
        self.assertEqual(4, self.arithmetic.divide(8, 2))     
        self.assertEqual(10, self.arithmetic.divide(100, 10)) 
        self.assertEqual(2, self.arithmetic.divide(4, 2)) 

    def testMultiply(self):
        self.assertEqual(4, self.arithmetic.multiply(2, 2))      
        self.assertEqual(21, self.arithmetic.multiply(3, 7))     
        self.assertEqual(1000, self.arithmetic.multiply(10, 100))


arithmetic = Arithmetic()

# add 4 and 2
print(arithmetic.add(4, 2))

# subtract 2 from 6
print(arithmetic.subtract(6, 2))

# divide 100 by 10
print(arithmetic.divide(100, 10))

# multiply 3 by 7
print(arithmetic.multiply(3, 7))
unittest.main()

