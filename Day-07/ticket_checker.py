# Ticket Checker

age = int(input("What is your age ? : "))
ticket = input("Do you have ticket? (Y/N) : ").strip().upper()

if age >= 18:
    if ticket == "Y":
        print("Entry Allowed")
    if ticket == "N":
        print("Entry Denied")
else:
    print("Entry Denied")