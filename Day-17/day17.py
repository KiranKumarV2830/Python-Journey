# 2D List : It is a list containing other lists .

students =[
    ["Kiran",85,90],
    ["Rahul",80,70],
    ["Arun",75,80],
]

# Accessing a row

# print(students[0])  # Output: ['Kiran', 85, 90]

# Accessing an Indiviual Element

# list[row][column]

# print(students[0][0])  # Output: Kiran -> First Element of First Row

# Changing an Element

# You can modify an element just like a normal list

# students[1][1]=80
# print(students)

# using len() function to get the number of rows

# print(len(students))  # Output: 3

# Looping Through a 2D List : With a 2D List we can use nested loops to access each element of the list.


# students = [
#     ["Kiran", 85, 90],
#     ["Rahul", 80, 70],
#     ["Arun", 75, 80],
# ]

# print(students)
# for student in students:
#     print(student)  

# Nested for loop
#The outer loop gets each row while the inner loop gets each item inside that row . 
# for student in students:
#     for value in student:
#         print(value)

# Coding Problems

# Problem 1

# students = [
#     ["Kiran", 85],
#     ["Rahul", 90],
#     ["Arun", 78]
# ]

# for value in students:
#     print(value)

# Problem 2 

# students = [
#     ["Kiran", 85],
#     ["Rahul", 90],
#     ["Arun", 78]
# ]

# for value in students:
#     for item in value:
#         print(item)

# Problem 3

# students = [
#     ["Kiran", 85, 90],
#     ["Rahul", 78, 82],
#     ["Arun", 92, 88]
# ]

# for value in students:
#     for item in value:
#         print(item)

# Problem 4

# students = [
#     ["Kiran", 85, 90],
#     ["Rahul", 78, 82],
#     ["Arun", 92, 88]
# ]

# students[0][1] = 95

# print(students)

# Problem 5 

# seats = [
#     ["A1", "A2", "A3"],
#     ["B1", "B2", "B3"],
#     ["C1", "C2", "C3"]
# ]

# for row in seats:
#     for name in row:
#         print(name)

