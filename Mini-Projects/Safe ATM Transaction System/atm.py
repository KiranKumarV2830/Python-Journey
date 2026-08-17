correct_pin = 2830
balance = 6500

try:
    pin = int(input("Enter your pin : "))
    if correct_pin == pin:
        print("PIN verified successful")
    else:
        print("Invalid PIN")
except ValueError:
    print("Please enter numbers only .")

count = 1
while count <= 10:
    print("===== ATM MENU =====")
    print("1 . Check Balance")
    print("2 . Withdraw Money")
    print("3 . Deposit Money")
    print("4 . Exit ")
    try :
        choice = int(input("Enter your choice :"))
        match choice:
            case 1:
                print(f"Your balance is {balance}")
            case 2:
                try:
                    withdraw = int(input("Enter withdrawal amount : "))
                    if withdraw <= 0:
                        print("Enter an amount greater than zero .")
                    elif withdraw > balance:
                        print("Insufficient Balance.")
                    else:
                        print("Withdrawal Successful.")
                        balance -= withdraw
                        print(f"Remaining Balance : {balance}")
                except ValueError:
                    print("Please enter a valid amount.")
            case 3:
                try:
                    deposit = int(input("Enter deposit amount : "))
                    if deposit <= 0:
                        print("Enter an amount greater than zero .")
                    else :
                        balance += deposit
                        print(f"New Balance : {balance}")
                        print("Deposit successful.")
                except ValueError:
                    print("Please enter a valid amount . ")
            case 4:
                print("Thank you for using the ATM")
                break
            case _:
                print("Invalid Choice.")
    except ValueError:
        print("Enter the correct choice!")
    count += 1
