import math 

def add(a,b) :
    return a + b

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b

def divide(a,b):
        try :
            return a / b 
        except ZeroDivisionError :
            print("Invalid number")


if __name__ == "__main__" :
    print(add(2,3))