def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("SIMPLE CALCULATOR")

    try:
        # Prompt the user to input two numbers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        # Prompt the user to choose an operation
        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please enter a number between 1 and 4.")
            return

        if choice == '1':
            result = add(num1, num2)
            operator = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operator = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operator = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operator = "/"

        print(f"\nResult: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
