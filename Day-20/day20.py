# Dictionary : A dictionary stores data in key-value pairs .
# The left side is the key and right side is the value .

# student = {
#     "name" : "Kiran",
#     "Age"  : 18,
#     "Branch": "Cse",
#     "Marks" : 85
# }
# print(student)
# print(type(student))

# Accessing Values

# student = {
#     "name" : "Kiran",
#     "age" : 18
# }
# print(student["name"])
# print(student["age"])

# In list we use indexing whereas in the dictionary we use key for getting particular value .

# Adding a New Item 

# student = {
#     "name":"Kiran",
#     "age":18
# }
# student["branch"] = "CSE"
# print(student)

# Updating a Value 

# student = {
#     "name" : "Kiran",
#     "age" : 18
# }
# student["age"]=19
# print(student)

# get() : We can use get() to safely retrieve a value . Iff the key doesn't exist then it returns none . We can also provide a default value .

# student = {
#     "name":"Kiran",
#     "age" :18
# }

# print(student.get("name"))
# print(student.get("branch","Not Available"))

# Difference Between [] and get() : if we use the key is present in the dictionary then it gives KeyError but if we use get() and if it is not present it doesn't give error instead it gives none 

# keys(): It returns the dictionary's keys 

# student = {
#     "name":"Kiran",
#     "age":18,
#     "branch":"cse"
# }
# print(student.keys())
#        or
# for key in student.keys():
#     print(key)

# values() : It returns all the values .

# student = {
#     "name":"kiran",
#     "age":17,
#     "branch":"cse"
# }
# print(student.values())
#          or
# for values in student.values():
#     print(values)

# items() : It returns both the key and value .

# student = {
#     "name":"kiran",
#     "age":18,
#     "branch":"cse"
# }
# print(student.items())
#       or
# for key,value in student.items():
#     print(key,value)

# pop() : It removes a specific key .

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# student.pop("age")
# print(student)

# popitem() : It removes the last inserted key-value pair .

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }

# student.popitem()
# print(student)

# clear() : It removes everything .

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# student.clear()
# print(student)

# Checking if a Key Exists 

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }

# print("name" in student)

# Looping Through a Dictionary 

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# For Keys

# for key in student:
#     print(key)

# For Values

# for values in student:
#     print(values)

# For both Keys and Values

# for keys,value in student.items():
#     print(f"{keys} : {value}")

# Dictionary can contain different data types . 

# Lists Inside Dictionaries 
# A dictionary value can itself be a list .

# student = {
#     "name":"kiran",
#     "subjects":["Python","C++","Java"]
# }
# print(student["subjects"])
# print(student["subjects"][0])

# Nested Dictionaries : A dictionary can contain another dictionary 

# students = {
#     "student1":{
#         "name":"kiran",
#         "age":17,
#         "branch":"cse"
#     },

#     "student2":{
#         "name":"rahul",
#         "age":17,
#         "branch":"mechanical"
#     }
# }
# print(students["student1"]["name"])

# Practice Questions 

# Question 1 

# student = {
#     "name" : "Kiran",
#     "age"  : 18,
#     "branch": "CSE"
# }
# print(student)

# Question 2 

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# print(student["name"])

# Question 3 

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# print(student["branch"])

# Question 4

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# student["college"] = "RNSIT"
# print(student)

# Question 5 

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# student["age"] = 19
# print(student)

# Question 6

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# print(student.get("Kiran","name"))

# Question 7

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# print(student.get("marks"))

# Question 8

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# print(student.keys())

# Question 9

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# print(student.values())

# Question 10

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# for keys,values in student.items():
#     print(f"{keys} : {values}")

# Question 11

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# student.pop("age")
# print(student)

# Question 12

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE"
# }
# print("name" in student)

# Question 13

# student = {
#     "name": "Kiran",
#     "age": 18,
#     "branch": "CSE",
#     "marks" : 85
# }
# print(len(student))