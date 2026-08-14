# Looping Through a List : We already know for loops now combine them with a list .

# numbers = [10,20,30,40,50]
# for num in numbers :
#     print(num)

# Looping Through a List of Names 

# students = ["Kiran","Jeevan","Akash","Ritesh","Suhas"]
# for student in students :
#     print(student)

# Calculating a Total Using a Loop

# marks = [80,90,75,85]
# total = 0

# for mark in marks :
#     total = total + mark
#           or
#     total += mark
# print(total)

# Searching Inside a List

# students = ["Kiran","Ritesh","Akash","Jeevan"]
# for student in students :
#     if student == "Kiran":
#         print("Student Found")

# Filtering Values 

# marks = [45,78,90,32,85,60]
# for mark in marks:
#     if mark >= 60 :
#         print(mark)

# Looping Through a Tuple

# subjects = ("Python","Java","C++")
# for subject in subjects :
#     print(subject)

# Looping Through a Set

# languages = {"Python","Java","C++"}
# for language in languages:
#     print(language)

# Looping Through a Dictionary 

# student = {
#     "name" : "Kiran",
#     "age" : 18,
#     "branch" : "CSE"
# }

# for key in student:
#     print(key)

# Looping Through A Dictionary Keys

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }

# for keys in student.keys():
#     print(keys)

# Looping Through a Dictionary Values 

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# for values in student.values():
#     print(values)

# Looping Through Keys and Values

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# for key,value in student.items():
#     print(f"{key}   : {value}")

# Dictionary of Marks 

# marks = {
#     "Python" : 85,
#     "Math" : 90,
#     "Physics" : 78
# }
# for subject,mark in marks.items():
#     print(f"{subject} : {mark}")

# Calculate Dictionary Total 

# marks = {
#     "Python" : 85,
#     "Maths" : 90,
#     "Physics" : 78
# }
# total = 0
# for mark in marks.values():
#     total += mark

# print(total)

# Find the Highest Mark 

# marks = [85,90,78,95,88]
# highest = marks[0]
# for mark in marks:
#     if mark > highest:
#         highest = mark
# print(highest)

# Find the Lowest Mark 

# marks = [85,90,78,95,88]
# lowest = marks[0]
# for mark in marks :
#     if mark < lowest:
#         mark = lowest
# print(lowest)

# Counting Values

# marks = [45,78,90,32,85,60]
# count = 0
# for mark in marks:
#     if mark >= 40:
#         count +=1
# print(count)

# Nested Collections 

# students = [
#     ["Kiran",85],
#     ["Rahul",90],
#     ["Arjun",78]
# ]
# for student in students:
#     print(student)

# Nested Loop

# students = [
#     ["Kiran", 85],
#     ["Rahul", 90],
#     ["Arjun", 78]
# ]
# for student in students:
#     for value in student:
#         print(value)

# Dictionary Containing Dictionary 

# students = {
#     "student1" : {
#         "name":"kiran",
#         "marks":85
#     },

#     "student2" : {
#         "name":"rahul",
#         "marks":90
#     }
# }

# for student_id,student_data in students.items():
#     print(student_id)
#     print(student_data)
# for student_id,student_data in students.items():
#     print(student_data["name"])
#     print(student_data["marks"])

# Practice Questions 

# Question 1

# numbers = [10,20,30,40,50]
# for number in numbers :
#     print(number)

# Question 2

# students = ["Kiran","Rahul","Arjun","Ravi"]
# for student in students:
#     print(student)

# Question 3

# numbers = [10,20,30,40,50]
# total = 0
# for number in numbers :
#     total += number
# print(total)

# Question 4 

# marks = [80,90,70,60]
# total = 0
# for mark in marks :
#     total += mark
# average = total / len(marks)
# print(average)

# Question 5

# numbers = [20,65,40,80,30,90]
# for number in numbers:
#     if number > 50:
#         print(number)

# Question 6

# numbers = [20,65,40,80,30,90]
# count = 0
# for number in numbers:
#     if number > 50:
#         count += 1
# print(count)

# Question 7

# subjects = ("Python","Math","Physics")
# for subject in subjects:
#     print(subject)

# Question 8

# languages = {"Python","Java","C++"}
# for lang in languages:
#     print(lang)

# Question 9

# student = {
#     "name" : "Kiran",
#     "age" : 18,
#     "branch" : "CSE"
# }
# for keys,values in student.items():
#     print(f"{keys} : {values}")

# Question 10

# marks = {
#     "Python" : 85,
#     "Math" : 90,
#     "Physics" : 78
# }
# total = 0
# for mark in marks.values():
#     total += mark
# print(total)

# Question 11

# numbers = [25,80,45,90,60]
# highest = numbers[0]
# for num in numbers :
#     if num > highest :
#         highest = num
# print(highest)

# Question 12

# numbers = [25,80,45,90,60]
# lowest = numbers[0]
# for num in numbers :
#     if num < lowest:
#         num = lowest
# print(lowest)

