expression = input("Expression: ")

# Check if the expression contains spaces and an operator
if ' ' in expression and any(op in expression for op in ['+', '-', '*', '/']):
    num1, operator, num2 = expression.split()
    num1, num2 = float(num1), float(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            exit()
    else:
        print("Error: Invalid operator.")
        exit()

    print("Result:", result)
else:
    print("Error: Invalid input. Please enter a valid expression.")
