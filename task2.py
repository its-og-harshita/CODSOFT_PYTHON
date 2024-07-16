def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."

def exponentiate(num1, num2):
    return num1 ** num2

def modulo(num1, num2):
    return num1 % num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /, **, %): ")

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
elif operation == "**":
    result = exponentiate(num1, num2)
elif operation == "%":
    result = modulo(num1, num2)
else:
    result = "Error: Invalid operation."

print("Result:", result)