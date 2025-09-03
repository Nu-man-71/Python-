def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    """Exponentiation function"""
    return x ** y

def modulo(x, y):
    """Modulo function"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x % y

def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("          SIMPLE CALCULATOR")
    print("=" * 40)
    
    operations = {
        '1': ('Addition (+)', add),
        '2': ('Subtraction (-)', subtract),
        '3': ('Multiplication (*)', multiply),
        '4': ('Division (/)', divide),
        '5': ('Power (^)', power),
        '6': ('Modulo (%)', modulo)
    }
    
    while True:
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == '7':
            print("Thank you for using the calculator!")
            break
        
        if choice not in operations:
            print("Invalid input! Please select a valid option.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            
            print(f"\nResult: {num1} {operation_name.split('(')[1][:-1]} {num2} = {result}")
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        
        continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if continue_calc not in ['y', 'yes']:
            print("Thank you for using the calculator!")
            break


def simple_calc():
    """Simplified calculator for single operations"""
    print("Simple Calculator - Enter 'quit' to exit")
    
    while True:
        try:
            expression = input("Enter calculation (e.g., 5 + 3): ").strip()
            
            if expression.lower() in ['quit', 'exit', 'q']:
                break
            
        
            allowed_chars = set('0123456789+-*/(). ')
            if not all(c in allowed_chars for c in expression):
                print("Invalid characters! Use only numbers and +, -, *, /, (, )")
                continue
            
            result = eval(expression)
            print(f"Result: {result}")
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except Exception as e:
            print(f"Invalid expression: {e}")

if __name__ == "__main__":
    print("Choose calculator mode:")
    print("1. Full Calculator (menu-based)")
    print("2. Simple Calculator (expression-based)")
    
    mode = input("Enter choice (1 or 2): ").strip()
    
    if mode == '1':
        calculator()
    elif mode == '2':
        simple_calc()
    else:
        print("Invalid choice. Running full calculator...")
        calculator()