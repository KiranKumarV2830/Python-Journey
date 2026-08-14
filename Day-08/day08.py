# match_case = it is statement which helps in decision-making that compares one variable against multiple fixed values and executes the code of matching case
#case_ acts as else part

day = int(input("Enter the day :"))

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid")

choice = int(input("Enter your choice :"))

match choice :
    case 1:
        print("Pizza")
    case 2 :
        print("Burger")
    case 3 :
        print("Sandwich")
    case _ :
        print("Invalid choice")