bank_name = input("Enter your bank name : ")
bank_balance = float(input("Enter your balance : "))

def show_balance():
    print(f"Your current balance is {bank_balance}")

def deposit(amount):
    global bank_balance
    bank_balance += amount

def withdraw(amount):
    global bank_balance
    bank_balance -= amount

def bank_details():
    print(f"Your Bank Name : {bank_name}")

show_balance()
deposit(2000)
withdraw(1000)
bank_details()
print(bank_balance)
print(f"Your current balance is {bank_balance}")