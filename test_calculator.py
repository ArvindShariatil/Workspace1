"""
Unit tests for the calculator module.
"""

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    """Test cases for calculator operations."""
    
    def test_add(self):
        """Test addition operation."""
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-5, -3), -8)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertEqual(calculator.add(2.5, 3.5), 6.0)
    
    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(-5, -3), -2)
        self.assertEqual(calculator.subtract(0, 5), -5)
        self.assertEqual(calculator.subtract(10.5, 5.5), 5.0)
    
    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-2, 3), -6)
        self.assertEqual(calculator.multiply(-2, -3), 6)
        self.assertEqual(calculator.multiply(0, 5), 0)
        self.assertEqual(calculator.multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Test division operation."""
        self.assertEqual(calculator.divide(6, 2), 3)
        self.assertEqual(calculator.divide(5, 2), 2.5)
        self.assertEqual(calculator.divide(-6, 2), -3)
        self.assertEqual(calculator.divide(-6, -2), 3)
        self.assertEqual(calculator.divide(0, 5), 0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculator.divide(5, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 2), 25)
        self.assertEqual(calculator.power(10, 0), 1)
        self.assertEqual(calculator.power(2, -1), 0.5)
        self.assertEqual(calculator.power(4, 0.5), 2.0)
    
    def test_modulo(self):
        """Test modulo operation."""
        self.assertEqual(calculator.modulo(10, 3), 1)
        self.assertEqual(calculator.modulo(15, 5), 0)
        self.assertEqual(calculator.modulo(7, 2), 1)
        self.assertEqual(calculator.modulo(20, 6), 2)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculator.modulo(5, 0)
        self.assertIn("Cannot perform modulo with zero", str(context.exception))


if __name__ == '__main__':
    unittest.main()
