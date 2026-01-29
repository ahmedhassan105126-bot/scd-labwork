"""
Experiment 4: Writing Clean Code
Objective: Refactor a calculator into professional, documented code.
"""

class Calculator:
    """A class to handle basic mathematical operations with error handling."""

    def add(self, x: float, y: float) -> float:
        """Returns the sum of two numbers."""
        return x + y

    def subtract(self, x: float, y: float) -> float:
        """Returns the difference of two numbers."""
        return x - y

    def multiply(self, x: float, y: float) -> float:
        """Returns the product of two numbers."""
        return x * y

    def divide(self, x: float, y: float) -> float:
        """Returns the quotient. Raises ValueError on division by zero."""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

def run_tests():
    """Simple testing logic to verify the Calculator class."""
    calc = Calculator()
    assert calc.add(10, 5) == 15
    assert calc.divide(10, 2) == 5
    print("All tests passed!")

def main():
    calc = Calculator()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print(f"Sum: {calc.add(num1, num2)}")
        print(f"Division: {calc.divide(num1, num2)}")
        
    except ValueError as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    run_tests()  # Run internal verification
    main()