# Exception : Exception is a error that occurs during the execution of the program .

# In this example if the user enters hello instead of integer than it gives error 

# number = int(input("Enter a number : "))
# print(number)

# Syntax Error VS Exception 

# Syntax Error : The code itself is written incorrectly . Python cannot properly understand the code .

# Exception : The code is valid Python , but something goes wrong while running it . The syntax is valid but the conversion fails .

# Try and Except 

# Syntax :
# try :
#    # code that might cause an error
#except : 
#    # what to do if an error happens 

# try : 
#     number = int(input("Enter a number : "))
#     print(number)
# except : 
#     print("Invalid Input!")

# Specific Exceptions 

# ValueError : ValueError occurs when a function recieves a value of the correct type but the value itself is not valid for that operation .
# try : 
#     age = int(input("Enter your age : "))
# except ValueError:
#     print("Please enter a number .")

# ZeroDivisionError : ZeroDivisionError occurs when you try to divide a number by zero .
# try:
#     result = 10 / 0 
# except ZeroDivisionError:
#     print("Cannot Divide by zero .")

# TypeError : TypeError occurs when an operation or function is used with an inappropriate data type . 
# try:
#     result = "10" + 5 
# except TypeError:
#     print("Invalid Data types.")

# IndexError : IndexError occurs when you try to access an index that doesn't exist in a sequence such as list or tuple . 
# numbers = [10,20,30]
# try:
#     print(numbers[5])
# except IndexError:
#     print("Index does not exist.")

# KeyError : KeyError occurs when you try to access a dictionary using a key that doesn't exist .
# student = {
#     "name" : "Kiran"
# }
# try :
#     print(student["age"])
# except KeyError:
#     print("Key does not exist.")

# Multiple Exceptions : You can handle different errors separately .

# try :
#     number = int(input("Enter a number:"))
#     result = 100/number
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot Divide by zero")

# else : else runs only when no exception occurs .

# try :
#     number = int(input("Enter a number : "))
# except ValueError:
#     print("Invalid input")
# else:
#     print("You entered :",number)

# Finally : finally runs whether an exception happens or not . 

# try :
#     number = int(input("Enter a number:"))
# except ValueError:
#     print("Invalid input.")
# finally:
#     print("Program finished.")

# Practice Questions 

# Question 1

# try : 
#     age = int(input("Enter your age : "))
# except ValueError:
#     print("Please enter a valid age .")
# else:
#     print(f"Your age is {age}")

# Question 2

# try : 
#     num1 = int(input("Enter first number : "))
#     num2 = int(input("Enter second number : "))
#     result = num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("Cannot Divide by zero .")
# except ValueError:
#     print("please enter numbers only")

