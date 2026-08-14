# Typecasting = The process of converting a variable from one data type to another data type.
#                 str(),float(),int(),bool()

# name = "Kiran"
# age = 25
# gpa = 3.2
# is_student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

# Converting into integer

# gpa = int(gpa)
# print(f"The gpa is {gpa}")
# print(type(gpa))

# Converting into float number

# age = float(age)
# print(f"The age is {age}")
# print(type(age))

# Converting into string

# age = str(age)
# print(f"The age is {age}")
# print(type(age))

# Converting into boolean = If there is nothing in the string it gives false as output if there is some word/value it will return as true as output

# name = bool(name)
# print(name)
# print(type(name))

# input() = takes the input from the user as a string and also returns it as a string

# name = input("Enter your name:")
# print(f"Hello {name}!")
#
# age = int(input("Enter your age:"))
# print(f"You are {age} years old.")

# Exercise 1 : Rectangle Area - Calculator

# length = int(input("Enter the length of the rectangle :"))
# breadth = int(input("Enter the breadth of the rectangle : "))

# area = length * breadth

# print(f"The area of the rectangle is {area}cm²")

# Exercise 2 : Shopping Cart program

# item = input("Enter the name of the item :")
# price = float(input("Enter the price of the item :"))
# quantity =int(input("Enter the quantity of the item :"))
# total = price * quantity
#
# print(f"You have bought {quantity} x {item}")
# print(f"The total is {total}")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")

# print("========== PROFILE ==========")
# print(f"Name : {name}")
# print(f"Age  : {age}")
# print(f"City : {city}")
# print("=============================")

# num1 =int(input("Enter the first number:"))
# num2 =int(input("Enter the second number:"))

# print(f"Sum of numbers : {num1+num2}")

# Challenge 01

name = input("Enter your name :")
company = input("Enter your dream company :")
lang =input("Enter your Favourite language :")
ai =input("Enter your Favourite AI model :")

print("======== MY DREAM ========")
print(f"Name : {name}")
print(f"Company : {company}")
print(f"Language : {lang}")
print(f"Favourite AI : {ai}")
print("==========================")

# Challenge 02

age = int(input("Enter your Age :"))
print(f"You are {age} years old")
age=age+1
print(f"Next year you will be {age}")

# Bonus Challenge

name = input("Enter your name :")
height = float(input("Enter your height :"))
weight = float(input("Enter your weight :"))

print("======== BMI INFO ========")
print(f"Name : {name}")
print(f"Height : {height}m")
print(f"Weight : {weight}kg")
print("==========================")
