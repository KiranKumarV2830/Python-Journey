# List Methods

# append() : adds one item to the end of a list .

# fruits = ["Apple","Banana"]
# fruits.append("Mango")
# print(fruits)

# insert() : adds an item at the specific index . 
#syntax : list.insert(index,value)

# fruits = ["Apple","Banana","Mango"]
# fruits.insert(1,"Orange")
# print(fruits)

# remove() : removes an item by its value .

# fruits = ["Apple","Banana","Mango"]
# fruits.remove("Banana")
# print(fruits)

# pop() : removes an item using its index and returns the removed item .

# fruits = ["Apple","Banana","Mango"]
# removed = fruits.pop(1)
# print(removed)
# print(fruits)

# clear() : removes everything from the list .

# fruits = ["Apple","Banana","Mango"]
# fruits.clear()
# print(fruits)

# sort() : arranges the items in ascending order .

# numbers = [50,10,40,20,30]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# reverse() : reverses the current order . 

# numbers = [10,20,30,40]
# numbers.reverse()
# print(numbers)

# count() : tells you how many times a value occurs in a list .

# numbers = [10,20,10,30,10]
# print(numbers.count(10))

# index() : tells you the index of the first occurrence of a value in a list .

# fruits = ["Apple","Banana","Mango"]
# print(fruits.index("Mango"))

# Coding Problems 

# Problem 1 

# cart =[]
# item1 = input("Enter the first item : ")
# item2 = input("Enter the second item : ")
# item3 = input("Enter the third item : ")
# cart.append(item1)
# cart.append(item2)
# cart.append(item3)

# print("Shopping Cart :")
# for items in cart:
#     print(items)

# Problem 2

# students = ["Kiran","Rahul","Arun"]
# name = input("Enter the name of the student : ")
# students.append(name)

# print(students)

# Problem 3

# movies = ["KGF","Avatar","Leo"]

# movies.insert(1,"RRR")
# print(movies)

# Problem 4

# shopping = ["Rice", "Milk", "Sugar", "Oil"]
# item = input("Enter the item to remove from the shopping list : ")
# shopping.remove(item)
# print(shopping)

# Problem 5 

# numbers = [5, 2, 8, 1, 9]
# numbers.pop()
# print(numbers)

# Problem 6

# marks = [85,62,95,70,88]
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)

# Problem 7

# numbers = [10, 20, 10, 30, 10, 40]
# print(numbers.count(10))

# Problem 8

# languages = ["Python", "Java", "C++", "JavaScript"]
# lang = input("Enter the programming language to find its index : ")
# lang_index = languages.index(lang)
# print(f"The index of {lang} is: {lang_index}")

# Problem 9

# shopping = ["Rice", "Milk", "Sugar", "Oil"]
# response = input("Do You want to clear your cart ? (yes/no) : ")
# if response == "yes":
#     shopping.clear()
#     print(shopping)
