# Tuple : It is collection of values which are ordered indexed and immutable . 

# Tuple are usually written in parenthesis() .

# student = ("Kiran",18,"CSE")
# print(student)
# print(type(student))

# Like lists tuple indexing also starts from 0 .

# students = ("Kiran",92.86,"PCMC")
# print(students[0])
# print(students[1])
# print(students[2])

# Tuple also supports negative indexing .

# students = ("Kiran",92.86,"PCMC")
# print(students[-1])
# print(students[-2])
# print(students[-3])

# Like lists tuple also support slicing it takes index value .

# marks = (85, 90, 88, 92, 95)

# print(marks[1:4])
# print(marks[1:])
# print(marks[:3])

# Tuple are immutable , it means when we create a tuple the elements inside the tuple cannot be changed . When we want to change it gives TypeError because the tuple cannot be changed after creation .

# numbers = (10,30,100)
# numbers[0]=100
# print(numbers)

# Tuple methods : Tuple only have few methods than list as list is mutable and tuple is immutable .

# There is only two important methods 
# 1 . index()
# 2 . count()

# count() tells how many times a value appears .

# numbers = (10, 20, 10, 30, 10)
# print(numbers.count(10))

# index() tells us the position of the first occurrence of the value .

# numbers = (10, 20, 30, 40)
# print(numbers.index(30))

# Tuple Unpacking : Tuple unpacking means assigning tuple values to separates variables .

# student = ("Kiran",17,"CSE")
# name,age,branch = student
# print(name)
# print(age)
# print(branch)

# Looping Through a Tuple

# We can use a for loop to access every value .

# marks = (80,90,57,98)
# for mark in marks :
#     print(mark)

# Tuples can be useful for storing information that should not be changed

# student = ("Kiran",17,"CSE",85)
# name,age,branch,marks = student
# print(f"Name   : {name}")
# print(f"Age    : {age}")
# print(f"Branch : {branch}")
# print(f"Marks  : {marks}")

# List of Tuple : We can also store multiple tuples inside a list .

# students = [
#     ("Kiran",85),
#     ("Rahul",78),
#     ("Arjun",92)
# ]

# for student in students :
#     print(student)

# Use a tuple when the data should remain unchanged . 

# Practice Questions 

# Question 1 

# languages = ("Python","Java","C++","Javascript")
# print(languages)

# Question 2

# numbers = (10, 20, 30, 40, 50)
# print(numbers[2])

# Question 3

# numbers = (10, 20, 30, 40, 50)
# print(numbers[1:4])

# Question 4

# numbers = (10, 20, 10, 30, 10, 40)
# print(numbers.count(10))

# Question 5 

# numbers = (10, 20, 30, 40, 50)
# print(numbers.index(40))

# Question 6

# student = ("Kiran",18,"CSE")
# name,age,branch = student
# print(name)
# print(age)
# print(branch)

# Question 7

# The output is 20

# numbers = (10,20,30)
# print(numbers[1])

# Question 8

# The output is 20, 30

# numbers = (10,20,30,40)
# print(numbers[1:3])

# Question 9

# It shows error TypeError

# numbers = (10,20,30)
# numbers[0]=100
# print(numbers)

# Question 10

# Square bracket means it is list but  parenthesis is tuple where list is mutable and tuple is immutable .

