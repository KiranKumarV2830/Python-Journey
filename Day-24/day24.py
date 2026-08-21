# Module : A module is a Python file containing reusable code -functions,classes,variables . It helps organize code into separate files instead of one giant script .

# def add(a,b):
#     return a + b
# print(add(2,5))

# import : Brings an entire module into your file ,accessed via modulename.function() .

# import math 
# print(math.sqrt(16))
# print(math.pi)

# from .... import.... : Imports specific functions/variables directly , no modules prefix needed . 

# from math import sqrt,pi
# print(sqrt(25))
# print(pi)

# import... as... : Gives a module a shorter/custom name .

# import math as m
# print(m.factorial(5))

# from math import factorial as fact
# print(fact(6))

# from module import * : Imports everything at once . Avoided in real projects - causes naming conflicts and unclear code . 

# from math import *
# print(sqrt(9))

# Built-in Modules : Pre-built modules that ship with Python,no install needed -math,random,datetime,os,sys.

# import random,datetime
# print(random.randint(1,10))
# print(datetime.date.time())

# import random
# print(random.randint(1,10))
# print(random.choice(["a","b","c"]))
# print(random.random())

# import datetime
# today = datetime.date.today()
# now = datetime.datetime.now()
# print(today)
# print(now)
# print(now.strftime("%H:%M"))

# import os
# print(os.getcwd())
# print(os.listdir())


# Creating your own Module : Save any .py file and its importable - as long as the importing file is in the same folder(or you set up the path properly)

# __name__ = "__main__" : Every Python file has a hidden variable __name__ .
# If you run the file directly __name__ becomes "__main__"
# If the file is imported into another file __name__ becomes the module's actual name 

# dir() : Lists everything available inside a module - useful for exploring what tools it offers without checking documentation . 

# import math
# print(dir(math))

# import random
# useful_names = [name for name in dir(random) if not name.startswith("_")]
# print(useful_names)

# Practice Questions 

# 1 . Import math as m find square root and factorial of a number .

# import math as m 
# print(m.sqrt(25))
# print(m.factorial(5))

# 2 . Use datetime to print today's date and current time separately

# import datetime 
# print(datetime.date.today())
# print(datetime.datetime.now())

# 3 . Use os.getcwd() to print current working directory

# import os
# print(os.getcwd())

