# Variable Scope : The area of the program where a variable can be used .

# There are two types
#1 .Local variable
#2 .Global variable

# Local variable : It is created inside a function. It can be only used inside that function

# def greet():
#     name = "Kiran"
#     print(name)
# greet()

# Global variable : It is created outside every function . It can be used anywhere

# name = "Kiran"
# def greet():
#     print(name)
# greet()
# print(name)

# name = "Python"
# def test():
#     name="AI"
#     print(name)
# test()
# print(name)

# Global keyword

# count = 10
# def increase():
#     global count
#     count+=1
# increase()
# print(count)

# Coding Problem

# Problem 1
# school = "Noble"
# def marks():
#     print(school)
# marks()

# Problem 2
# def school():
#     marks = 100
#     print(marks)
# school()

# Problem 3
# count = 5
# def increase():
#     global count
#     count += 1
# increase()
# print(count)

# Problem 4
# def bill():
#     price = 100
#     print(price)
# bill()

# Problem 5
# city = "Bangalore"
# def state():
#     print(city)
# def capital():
#     print(city)
# state()
# capital()

# Problem 6
# def person():
#     age = int(input("Enter your age:"))
#     print(age)
# person()

# Problem 7
# score = 5
# def marks():
#     global score
#     score += 10
# marks()
# print(score)

# Problem 8
# name = "Kiran"
# def school():
#     name="Jeevan"
#     print(name)
# school()
# print(name)

# Problem 9
# def college():
#     course = input("Enter your course name: ")
#     print(course)
# college()

# Problem 10
# name = "KIRAN"
# def total():
#     print(name)
# print(name.count("KIRAN"))

