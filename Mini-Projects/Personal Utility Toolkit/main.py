import calculator

import text_tools

import date_tools

print("===== PERSONAL TOOLKIT =====")
print(" 1 . Calculator ")
print(" 2 . Text Tools ")
print(" 3 . Date Tools ")

choice = int(input("Enter your choice : "))

match choice :
    case 1 :
        print("===== CALCULATOR =====")
        print(" 1 . Addition ")
        print(" 2 . Subtraction ")
        print(" 3 . Multiplication ")
        print(" 4 . Division ")
        choice1 = int(input('Enter your choice : '))
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        match choice1 :
            case 1 : 
                print(calculator.add(a,b))
            case 2 :
                print(calculator.subtract(a,b))
            case 3 : 
                print(calculator.multiply(a,b))
            case 4 :
                print(calculator.divide(a,b))
            case _ :
                print("Enter valid number from the menu .")
    case 2 :
        print("===== TEXT TOOLS =====")
        print(" 1 . Count Word ")
        print(" 2 . Reverse Word")
        print(" 3 . Check whether palindrome or not ")
        text = input("Enter any text")
        choice2 = int(input("Enter your choice : "))
        match choice2 :
            case 1 :
                print(text_tools.count_word(text))
            case 2 :
                print(text_tools.reverse_text(text))
            case 3 :
                print(text_tools.is_palindrome(text))
            case _ :
                print("Enter valid number from the menu.")
    case 3 :
        print("===== DATE TOOLS =====")
        print(" 1 . Today's Date ")
        print(" 2 . Count Days ")
        choice3 = int(input("Enter your choice : "))
        match choice3 :
            case 1 :
                print(date_tools.get_today())
            case 2 :
                year = int(input("Enter the year : "))
                month = int(input("Enter the month : "))
                date = int(input("Enter the date : "))
                print(date_tools.days_until(year,month,date))
    case _ : 
        print("Enter valid number from the menu . ")