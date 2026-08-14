correct_pin = 1234
balance = 5000
attempt = 1

while attempt <= 3:

    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("Welcome!")

        amount = int(input("Enter the amount to withdraw: ₹"))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            print("Transaction Successful!")
            print(f"Please collect your cash: ₹{amount}")
            print(f"Remaining Balance: ₹{balance}")
            print("Thank you for using our ATM!")

        break

    else:
        print("Incorrect PIN!")

        if attempt == 3:
            print("Card Blocked!")
            print("Please visit your bank.")
        else:
            print(f"You have {3 - attempt} attempt(s) left.")

    attempt += 1