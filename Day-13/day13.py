# Return : It sends a value back from a function to the place where the function was called

# def add(a,b):
#     return a+b
# result = add(3,4)
# print(result)
#
# def full_name(first,last):
#     return first+" "+last
# print(full_name("Kiran","Kumar V"))
#
# def is_adult(age):
#     return age >=18
# print(is_adult(20))

# Coding Problems

# Problem 1

def add(a,b):
    return a+b
print(add(1,2))

# Problem 2

def square(num):
    return num*num
result = square(5)
print(result)

# Problem 3

def cube(num):
    return num*num*num
print(cube(5))

# Problem 4

def full_name(first,last):
    return first+" "+last
print(full_name("Kiran","Kumar V"))

# Problem 5

def total(price,quantity):
    return price*quantity
print(total(20,2))

# Problem 6

def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
print(is_even(5))

# Problem 7

def largest(a,b):
    if a > b:
        return a
    else:
        return b
print(largest(2,5))

# Problem 8

def percentage(total,obtained):
    return total/obtained*100
print(percentage(10,20))

# Problem 9

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
print(grade(100))

# Problem 10

def discount(price):
    return price*0.1
print(discount(100))