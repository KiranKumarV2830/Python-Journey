# if = Do some code only if condition is true else do something else .

age = int(input('Enter your age :'))

if age >= 100 :
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You have not born yet")
else:
    print("You are not signed up")


response = input("Would you like some food (Y/N):")

if response == "Y":
    print("Have some food")
else:
    print("No food for you")


name = input("Enter your name :")

if name == "":
    print("You did not enter your name")
else:
      print(f"Hello {name}")

# Boolean if statement

for_sale = True

if for_sale:
    print("Sale for sale")
else :
    print("it is no sale ")