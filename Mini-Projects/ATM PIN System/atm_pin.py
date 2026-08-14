card = input("Did you insert the card (Y/N) : ").strip().upper()

pin = int(input("Enter PIN number : "))

if card == "Y" and pin == "1234":
    print("Transition Started")
else:
    print("Access Denied")