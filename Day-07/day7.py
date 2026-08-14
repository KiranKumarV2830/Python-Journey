 # Nested If condition : It is a condition where if statement is placed under another if statement to check another condition

age = int(input("Enter your age :"))

if age >= 18:
    print("You are old enough to drive .")
    quest = input("Do you have driver license ? (Y/N) : ").strip().upper()
    if quest == "Y":
        print("You can drive .")
    elif quest == "N":
        print("You cannot drive. Pay the fees and go .")
    else:
        print("Tell the correct answer")
else:
    print("You are not old enough to drive!")

# Practice Problem 1

age = int(input("Enter your age : "))

if age >= 18 :
    print("You are Eligible fro driving license ")
else :
    print("You are not old enough to drive")


# Practice Problem 2

