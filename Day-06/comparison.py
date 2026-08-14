# Comparison Operator

age =int(input("Enter your age: "))

if age > 18:
    print("You are ready to vote .")
elif age == 18:
    var = input("Do you have voter id ? (Y/N) :")
    if var == "Y":
        print("You can vote")
    else:
        print("Go and fill the form")
else:
    print("You are not ready to vote .")

age = int(input("Enter your age: "))

if age >= 20 :
    print("You can drink ")
elif age >=18 :
    print("Do you have permission from your parents ")
elif age <18 :
    print("You cannot drink.")

name = input("Enter your name: ")

if name != "":
    print(f"Hello {name}")
else:
    print("Enter some name")