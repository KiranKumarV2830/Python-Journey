# Section D = Coding Challenge

# Problem 1

# count = 1
# while count <= 20:
#     print(count)
#     count += 1

# Problem 2

# for i in range(2,20,2):
#     print(i)

# Problem 3

# password = input("Enter your password : ")
#
# while password != "python123":
#     print("Invalid Password.")
#     password = input("Enter your password again : ")
# print("Welcome!")

# Problem 4

# attempt = 0
#
# while attempt == 0 :
#     pin = int(input("Enter your PIN: "))
#     while pin != 1234 :
#         print("Invalid PIN.")
#         print("Try Again.")
#         pin = int(input("Enter your PIN again: "))
#         attempt += 1
#         if attempt == 2:
#             print("Card Blocked All attempts fail !")
#             break
#     if pin == 1234:
#         print("Welcome!")
#         break

# Problem 5

# item = int(input("Enter the item number : "))
# quantity = int(input("Enter the quantity : "))
# match item :
#     case 1 :
#         print("You have ordered Pizza !")
#         print("Pizza is ₹250 ")
#         print(f"You want {quantity} Pizza .")
#         print(f"Total Price : ₹{quantity * 250}")
#         print("Thank You VISIT AGAIN")
#     case 2 :
#         print("You have ordered Burger !")
#         print("Burger is ₹150 ")
#         print(f"You want {quantity} Burger .")
#         print(f"Total Price : ₹{quantity * 150}")
#         print("Thank You VISIT AGAIN")
#     case 3 :
#         print("You have ordered Sandwich !")
#         print("Sandwich is ₹100 ")
#         print(f"You want {quantity} Sandwich .")
#         print(f"Total Price : ₹{quantity * 100}")
#         print("Thank You VISIT AGAIN")
#     case _ :
#         print("Please enter the item number from (1 - 3) ")

# Problem 6

# for i in range(3):
#     print("*****")

# Problem 7

# count  = 10
#
# while count >= 1 :
#     print(count)
#     count -= 1

# Problem 8

# num = int(input("Enter a number : "))
#
# while num <= 0 or num == 0:
#     print("Please enter a positive number . ")
#     num = int(input("Enter a number again : "))
# print(f"{num} is positive number . ")

# Problem 9

# user = input("Enter Your Username: ")
# password = input("Enter your password : ")
#
# while password != "python123" and user != "admin":
#     print("Invalid password and username please try again.")
#     user = input("Enter Your Username: ")
#     password = input("Enter your password : ")
#     if user == "admin" and password == "python123":
#         print("Welcome !")

# Problem 10
#
# num = int(input("Enter a number : "))
# count = 1
# for i in range(1,11):
#     print(f"{num} X {count} = {num*count}")
#     count += 1
#

# Problem 1

# num = int(input("Enter a number from (1 - 10) : "))
#
# while num > 10:
#     print("Wrong Number Try Again")
#     num = int(input("Enter a number from (1 - 10) again : "))
# if num < 10 :
#     print("Great Number ")

# Problem 2

# user = input("Enter your username : ")
# password = input("Enter your password : ")
#
# while user != "admin" or password !="python123":
#     print("Invalid username or password.")
#     user = input("Enter your username : ")
#     password = input("Enter your password : ")
# print("Login Successful!")

# Problem 3

# num = int(input("Enter a number : "))
#
# while num >= 1:
#     print(num)
#     num -= 1
# print("Blast Off!")

# Problem 4
#
# num = int(input("Enter a number : "))
# tables = 1
# while tables  <= 10:
#     print(f"{num} X {tables} = {num * tables}")
#     tables += 1

# Problem 5
#
# name = input("Enter Your Name : ")
# marks = int(input("Enter Your Marks : "))
#
# if (marks > 90) and (marks < 100):
#     print("GRADE : A ")
# elif marks <90 and (marks >80 ):
#     print("GRADE : B ")
# elif marks < 80 and (marks >70):
#     print("GRADE : C ")
# elif marks < 70 and (marks >60):
#     print("GRADE : D ")
# elif marks < 60 and (marks >50):
#     print("GRADE : Fail ")
# else:
#     marks = int(input("Enter Your Marks Again : "))

# Problem 6

print("1 . Rice ₹60/kg")
print("2 . Sugar ₹45/kg")
print('3 . Oil ₹180/kg')
item = int(input("Enter the item : "))
quantity = int(input("Enter the quantity : "))

match item :
    case 1 :
        print("Item            : Rice ")
        print(f"Quantity       : {quantity}")
        print("Price Per Unit  :  ₹60/kg")
        print(f"Total Price    : ₹{60*quantity}")
    case 2 :
        print("Item            : Sugar ")
        print(f"Quantity       : {quantity}")
        print("Price Per Unit  : ₹45/kg")
        print(f"Total Price    : ₹{45*quantity}")
    case 3:
        print("Item            : Oil ")
        print(f"Quantity       : {quantity}")
        print("Price Per Unit  : ₹180/kg")
        print(f"Total Price    : ₹{180*quantity}")
    case _:
        print("INVALID OPTION ENTER AGAIN")