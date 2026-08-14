# Set : Set is a collection of values .
# Sets are created using {}

# numbers = {10,30,20}
# print(numbers)
# print(type(numbers))

# Sets are not allowed for duplicate values . If there are an duplicate values it will remove automatically .

# For creating empty set we should use numbers = set() .
# If we use numbers ={} it creates a empty dictionaries .

# Sets do not use indexing as it is unordered collections .

# Adding Elements 

# numbers = {10,20,30}
# numbers.add(400)
# print(numbers)

# We can also add strings

# languages = {"Python", "Java"}
# languages.add("C++")
# print(languages)

# Adding Multiple Elements : We should use update() for adding multiple elements .

# numbers = {10,20,30}
# numbers.update([40,50,60])
# print(numbers)

# numbers = {10,20,30}
# numbers.update({40,60})
# print(numbers)

# remove() removes an item from the set if the set is not present then it raises an error KeyError .

# numbers = {10, 20, 30}
# numbers.remove(70)
# print(numbers)

# discard() it also removes an element if the value doesnt exist it doesnt give any error

# numbers = {10, 20, 30}
# numbers.remove(20)
# print(numbers)

# clear() : It removes everything from the set

# numbers = {10, 20, 30}
# numbers.clear()
# print(numbers)

# Membership Testing : You can in keyword to check whether the value exist or not .

# languages = {"Python","C++","Java"}
# print("Python" in languages)

# Set Union : Union combines the elements from the two sets

# a = {1,2,3}
# b = {4,5,6}
# print(a|b)
#     or
# print(a.union(b))

# Set Intersection : Intersection gives value which is present in the both the sets .

# a = {1,2,3}
# b = {3,4,5}
# print(a&b)
#     or
# print(a.intersection(b))

# Set Difference : Difference gives the values that are present in the first set but not in the second set

# a = {1,2,3}
# b = {3,4,5}
# print(a-b)
#    or
# print(a.difference(b))
# print(b-a)

# Symmetric Difference : It gives the value that are in either sets but not in both

# a = {1,2,3}
# b = {3,4,5}
# print(a^b)
#    or
# print(a.symmetric_difference(b))

# Looping Through a Set : We can use for loop but we should not depend on the order 

# a = {1,2,3}
# for i in a:
#     print(i)

# Practice Question 

# Question 1 

# numbers = {10,20,30,40,50}
# for i in numbers :
#     print(i)

# Question 2 

# Output will be 10, 20, 30, 40 because the set doesn't allow duplicate values instead it removes automatically if it finds it .

# Question 3 

# numbers = set()
# print(numbers)

# Question 4 

# numbers = {10,20,30}
# numbers.add(40)
# print(numbers)

# Question 5

# numbers = {10,20,30}
# numbers.remove(20)
# print(numbers)

# Question 6

# It will not remove anything and also it doesn't give error.

# numbers = {10,20,30}
# numbers.discard(100)
# print(numbers)

# Question 7

# languages = {"Python","C++","Java"}
# print("Python" in languages)

# Question 8

# {1,2,3,4,5} is the output
# a = {1,2,3}
# b = {3,4,5}
# print(a|b)

# Question 9

# {3} is the output 
# a = {1,2,3}
# b = {3,4,5}
# print(a&b) 

# Question 10

# {1,2} is for a - b and {4,5} is for b - a

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a-b)
# print(b-a)

