#!/usr/bin/env python3
"""
Simple Python Calculator
Supports basic arithmetic operations: addition, subtraction, multiplication, division
"""

import sys

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

def sqrt(x):
    """Calculate square root of a number"""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return x ** 0.5

def display_menu():
    """Display calculator menu"""
    print("\n=== Python Calculator ===")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")
    print("=========================")

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    """Main calculator function"""
    print("Welcome to Python Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter choice (1-7): ")
            
            if choice == '7':
                print("Thank you for using Python Calculator!")
                sys.exit(0)
            
            if choice in ['1', '2', '3', '4', '5']:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"\nResult: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\nResult: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\nResult: {num1} × {num2} = {result}")
                elif choice == '4':
                    try:
                        result = divide(num1, num2)
                        print(f"\nResult: {num1} ÷ {num2} = {result}")
                    except ValueError as e:
                        print(f"\nError: {e}")
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"\nResult: {num1} ^ {num2} = {result}")
            
            elif choice == '6':
                num = get_number("Enter number: ")
                try:
                    result = sqrt(num)
                    print(f"\nResult: √{num} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
            
            else:
                print("\nInvalid choice! Please select 1-7.")
                
        except KeyboardInterrupt:
            print("\n\nExiting calculator...")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
