# Experiment 3: Simple Calculator
# University of South Asia

# --- Modular Functions (The "Logic" Section) ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# --- Main Program (The "User Interface" Section) ---
def main():
    print("=== Simple Calculator ===")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nSelect Operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        
        choice = input("\nEnter choice (1/2/3/4): ")

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid input! Please choose a number between 1 and 4.")
            
    except ValueError:
        print("Error: Please enter valid numeric values.")

# This line ensures the code only runs if the file is executed directly
if __name__ == "__main__":
    main()