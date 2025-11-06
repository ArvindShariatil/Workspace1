#!/usr/bin/env python3
"""
Interactive calculator application.
"""

import calculator


def main():
    """Run the interactive calculator."""
    print("=" * 40)
    print("    Welcome to the Calculator!")
    print("=" * 40)
    print("\nAvailable operations:")
    print("  1. Add (+)")
    print("  2. Subtract (-)")
    print("  3. Multiply (*)")
    print("  4. Divide (/)")
    print("  5. Power (^)")
    print("  6. Modulo (%)")
    print("  7. Exit")
    print("=" * 40)
    
    while True:
        print("\nSelect an operation (1-7): ", end="")
        choice = input().strip()
        
        if choice == '7':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please select a number between 1 and 7.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = calculator.add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = calculator.subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = calculator.multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = calculator.divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = calculator.power(num1, num2)
                operation = "^"
            elif choice == '6':
                result = calculator.modulo(num1, num2)
                operation = "%"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
