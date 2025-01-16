import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test addition method
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
    
    # Test subtraction method
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
    
    # Test multiplication method
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
    
    # Test division method
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(10, 0), None)  # Division by zero
    
    # Test edge case for division by zero
    def test_division_by_zero(self):
        """Test division by zero."""
        self.assertIsNone(self.calc.divide(10, 0))  # Expected None for division by zero

    # Test non-numeric inputs (you can add such tests depending on how you want to handle errors)
    # For this, the divide function is expected to return None when the inputs aren't numbers
    def test_invalid_inputs(self):
        """Test division with invalid inputs (non-numeric)."""
        with self.assertRaises(ValueError):
            self.calc.divide("a", 2)
        with self.assertRaises(ValueError):
            self.calc.divide(2, "b")
        with self.assertRaises(ValueError):
            self.calc.divide("a", "b")

if __name__ == "__main__":
    unittest.main()
