# Problem 1

print("***********************************")
print("WELCOME TO PYTHON PROGRAMMING  ")
print("***********************************")

# Problem 2

name = "Kiran Kumar V"
age = 17
city = "Bangalore"
dream_company = "Google"

print(f"Name : {name}")
print(f"Age : {age}")
print(f"City : {city}")
print(f"Dream Company : {dream_company}")

# Problem 3

name = "Kiran"
age = 17
height = 5.6
is_student = True
print(name,type(name))
print(age,type(age))
print(height,type(height))
print(is_student,type(is_student))

# Problem 4

name = "Python"

print(name.upper())
print(name.lower())
print(len(name))

# Problem 5

text = "   Hello World   "

print(text)
print(text.strip().upper().lower().len(text))

# Problem 6

name = input("Enter your name : ")
age = int(input("Enter your age :"))
college = input("Enter your college name :")
subject = input("Enter your favourite subject :")

print("======= STUDENT CARD =======")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"College : {college}")
print(f"Subject : {subject}")
print("============================")

# Problem 7

company = input("Enter your dream company :")
salary = int(input("Enter your salary goal :"))
language = input("Enter your Favourite Programing Language : ")

print("====== DREAM CARD ======")
print(f"Dream Company : {company}")
print(f"Salary Goal : {salary}")
print(f"Favourite Programming Language : {language}")
print("========================")

# Problem 8

age = int(input("Enter your age :"))
print(f"You are {age} years old.")
age = age + 5
print(f"After 5 years you will be {age} years old.")

# # Problem 9

email = "   KIRAN@GMAIL.COM   "
print(email.strip().lower())

# Problem 10

sentence = "I want to learn Java"
print(sentence.replace("Java","Python"))

# Problem 11

name = input("Enter your name :")
age = int(input("Enter your age :"))
movie =input("Enter your Favourite Movie :")
ai = input("Enter your Favourite AI :")
dream = input("Enter your Dream :")

print("============ MY BIO ============")
print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"Your Favourite movie is {movie}")
print(f"Your Favourite AI is {ai}")
print(f"Your Dream is {dream}")
print("================================")

# Problem 12

item = input("Enter the item name :")
price = float(input("Enter the price of the item :"))
quantity = int(input("Enter the quantity of the item :"))

print("You bought :")
print(f"{quantity} x {item}")
print(f"Price : \u20B9 {price}")
print(f"Total : \u20B9{price * quantity}")

# Problem 13

length = int(input("Enter the length of the rectangle :"))
breadth = int(input("Enter the breadth of the rectangle :"))
area = length * breadth

print(f"Area = {area}")

# Problem 14

radius = int(input("Enter the radius :"))
print(f"Diameter : {2 * radius}")
print(f"Circumference : {2 * 3.14 * radius}")
print(f"Area : {3.14 * radius **2}")

# # Problem 15

name ="   kIrAn KuMaR"
print(name.strip().title())
#
# # Problem 16
name = "Python"

print(name[0])
#
# # Problem 17
name = "Python"

print(name[-1])
#
# Problem 18
text = "   AI"

print(text.strip().upper())
#
# # Problem 19
age = "18"

print(int(age) + 2)
#
# # Problem 20
language = "python"

print(language.capitalize().replace("Python", "Java"))

# Mini project

name = input("Enter your name : ")
age = int(input("Enter your age :"))
city = input("Enter your city :")
college =input("Enter your college name :")
company = input("Enter your Dream company :")
ai = input("Enter your favourite AI :")
lang = input("Enter your favourite programming language :")

print("===========================")
print("   PERSONAL INFORMATION    ")
print("===========================")
print(f"Name            : {name.upper()}")
print(f"Age             : {age}")
print(f"City            : {city.capitalize()}")
print(f"College         : {college.title()}")
print(f"Dream           :{company}")
print(f"Favourite AI    : {ai}")
print(f"Language        : {lang}")
print("===========================")
