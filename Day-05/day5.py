# Arithmetic Operators

# Addition

friends = 0
friends = friends + 1
friends += 1 # Augmented operator
print(friends)

# Subtraction

friends = 0
friends = friends - 1
friends -= 1 # Augmented operator
print(friends)

# Multiplication

friends = 2
friends =friends *3
friends *= 3 # Augmented Operator
print(friends)

# Division

friends = 5
friends = friends /2
friends /= 2  #Augmented Operator
print(friends)

# Exponential

num = 5
num = num ** 2
num **= 2 # Augmented Operator
print(num)

# Modulus = Gives remainder as an output

num = 10
remainder = num % 2
print(remainder)

# Math Modules

x = 3.14
y = -4
z=5

# Rounding off

result1=round(x)
print(result1)

# Giving Absolute value

result2 = abs(y)
print(result2)

# Power function

result3 = pow(z,3)
print(result3)

# Maximum Value

result4 = max(x,y,z)
print(result4)

# Minimum Value

result5 = min(x,y,z)
print(result5)

# import math modules

import math

x = 9.1
print(math.pi)
print(math.e)
result = math.sqrt(81)
result2 = math.ceil(x)
result3 = math.floor(x)
print(math.factorial(5))
print(result3)

# Calculate Circumference of the circle

import math

radius = float(input("Enter the radius :"))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {round(circumference,2)}")

# Calculate Area of the circle

import math

radius = float(input("Enter radius :"))
area = math.pi * radius **2
print(f"The area of the circle is {round(area,2)}")

# To find Hypotenuse of the right triangle

import math

a = float(input("Enter side a :"))
b = float(input("Enter side b :"))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The Hypotenuse of the triangle is {c}")

# Practice 1

a = int(input("Enter a number :"))
b = int(input("Enter a number:"))
print(f"Sum = {a+b}")
print(f"Difference = {a-b}")
print(f"Product = {a*b}")
print(f"Quotient = {a/b}")
print(f"Floor Division = {a//b}")
print(f"Remainder = {a%b}")
print(f"Power = {a**b}")

# Practice 2

import math

radius = float(input("Enter radius :"))
area = math.pi * (radius ** 2)
circumference = 2 *math.pi *radius

print(f"The Area of the circle is  {round(area,2)}")
print(f"The circumference of the circle is {round(circumference,2)}")

# Mini Project 1

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

print(f"Sum           : {num1 + num2}")
print(f"Difference    : {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division      : {num1 / num2} ")

# Mini Project 2

name = input("Enter the name :")
height = float(input("Enter the height :"))
weight = float(input("Enter the weight :"))

bmi = weight / pow(height,2)
print("==========BMI RESULT==========")
print(f"Name     : {name}")
print(f"BMI      : {bmi}")
print("==============================")