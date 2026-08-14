# Python calculator

operator = input("Select the operator (+ - * / // % **):")
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

if operator == "+":
    result = num1 + num2
    print(f"Sum is {round(result)}")
elif operator == "-":
    result = num1 - num2
    print(f"Subtraction is {round(result)}")
elif operator == "*":
    result = num1 * num2
    print(f"Multiplication is {round(result)}")
elif operator == "/":
    result = num1 / num2
    print(f"Division is {round(result)}")
elif operator == "//":
    result = num1 // num2
    print(f"Floor Division is {round(result)}")
elif operator == "%":
    result = num1 % num2
    print(f"Modulus is {round(result)}")
elif operator == "**":
    result = num1 ** num2
    print(f"Exponent is {round(result)}")
else:
    print(f"{operator} is not a valid operator")