"""
University of South Asia
Experiment 5: Unit Testing Implementation
"""

import unittest  # <--- [Concept 1: unittest Module]

# The Unit to be tested
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        return a / b if b != 0 else None

# ==========================================
# TEST CLASS SECTION
# ==========================================

# [Concept 2: Test Class] Inherits from unittest.TestCase
class TestCalculator(unittest.TestCase):

    # [Concept 3: setUp Method]
    def setUp(self):
        """Prepares the environment before each test."""
        self.calc = Calculator()
        print("Test Setup: Instance created.")

    # [Concept 4: tearDown Method]
    def tearDown(self):
        """Cleans up resources after each test."""
        print("Test Teardown: Resources cleared.")

    # [Concept 5: Assertion Methods]
    def test_addition(self):
        # Using assertEqual to check if 10+5 is 15
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subtraction(self):
        # Using assertNotEqual to check logic
        self.assertNotEqual(self.calc.subtract(10, 5), 0)

    def test_is_greater(self):
        # Using assertTrue
        self.assertTrue(self.calc.add(5, 5) > 5)

    def test_division_by_zero(self):
        # Using assertIsNone for edge cases
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)

    def test_membership(self):
        # Using assertIn to check if a value exists in a results list
        results = [self.calc.add(1, 1), self.calc.add(2, 2)]
        self.assertIn(2, results)

# ==========================================
# EXECUTION ENGINE
# ==========================================
if __name__ == "__main__":
    # This triggers the unittest framework to find and run all "test_" methods
    unittest.main()