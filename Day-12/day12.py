# default Arguments = A default value for certain parameters
#                     Default is used when that argument is omitted
#                     make your functions more flexible , reduces # of arguments
#                    1 . positional  2. default 3. keyboard  4.arbitary
#
# def net_price(list_price,discount=0,tax=0.05):
#     return list_price * (1-discount)*(1+tax)

# print(net_price(500))
# print(net_price(500,0.1))
# print(net_price(500,0.1,0))

# Parameter : It is a variable which is defining a function it also acts as placeholder for a value .

# Argument : It is an actual value which is used for calling the function .

# def greet(name):
#     print(f"Hello {name}")
# greet("Kiran")
#
# def square(num):
#     print(num*num)
# square(6)
#
# def welcome(student):
#     print(f"Welcome {student}")
# welcome("Kiran")
#
# def add(a,b):
#     print(a+b)
# add(5,3)
#
# def city(place):
#     print(place)
#
# city("Bengaluru")

# Coding Problem 1

def greet(name):
    print(f"Hello {name}")
greet("Kiran")

# Coding Problem 2

def student(name,age):
    print(f"Name : {name}")
    print(f"Age : {age}")
student("Kiran",17)

# Coding Problem 3

def restaurant(food):
    print(f"You ordered {food}")
restaurant("Pizza")

# Coding Problem 4

def multiply(a,b):
    print(a*b)
multiply(2,4)

# Coding Problem 5

def movie(name,rating):
    print(f"Movie : {name}")
    print(f"Rating : {rating}")
movie("Avengers",5)

# Coding Problem 6

def square(num):
    print(num*num)
square(5)

# Coding Problem 7

def rectangle(length,width):
    print(length*width)
rectangle(10,20)

# Coding Problem 8

def calculator(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
calculator(10,5)

# Coding Problem 9

def marks(student,marks):
    print(f"Student : {student}")
    print(f"Marks : {marks}")
marks("Kiran",25)

# Coding Problem 10

def shopping(item,quantity):
    print(f"Item : {item}")
    print(f"Quantity : {quantity}")
shopping("Kiwi",2)

#Think Like a Programmer

def login(username,password):
    print(f"Username : {username}")
    print(f"Password : {password}")
    print("You have logged in")
def search_food(food_name):
        print(f"Food Name : {food_name}")
def select_restaurant(name):
        print(f"Restaurant Name : {name}")
def add_to_cart(item,quantity):
        print(f"Item : {item}")
        print(f"Quantity : {quantity}")
def apply_coupon(code):
        print(f"Code : {code}")
def calculate_bill(amount,discount):
        print(f"Amount : {amount}")
        print(f"Discount : {discount}")
def payment(method,amount):
        print(f"Method : {method}")
        print(f"Amount : {amount}")
def track_order(order_id):
        print(f"Order id : {order_id}")
def cancel_order(order_id):
        print(f"Order id : {order_id}")
def rate_restaurant(rating):
        print(f"Rating : {rating}")

# Mini Project

def show_movies():
    print(f"Movie is starting at 10.30")
def book_ticket(movie_name,tickets):
    print(f"Movie ticket : {movie_name}")
    print(f"Tickets : {tickets}")
def calculate_bill(ticket_price,quantity):
    print(f"Bill : {ticket_price}")
    print(f"Quantity : {quantity}")
def payment(method,amount):
    print(f"Method : {method}")
    print(f"Amount : {amount}")
def thank_you(name):
    print(name)