print("==========MENU==========")
print(" 1 . Pizza - ₹250")
print(" 2 . Burger - ₹150")
print(" 3 . Sandwich - ₹120")
print("========================")

choice = int(input("Enter your choice: "))
quantity = int(input("Enter how much do you want :"))

match choice :
    case 1 :
        print("You ordered Pizza!")
        print(f"Quantity : {quantity}")
        print(f"Total Price : {quantity * 250}")
        print("Thank You For Ordering Come Back Again")
    case 2 :
        print("You ordered Burger!")
        print(f"Quantity : {quantity}")
        print(f"Total Price : {quantity * 150}")
        print("Thank You For Ordering Come Back Again")
    case 3 :
        print("You ordered Sandwich!")
        print(f"Quantity : {quantity}")
        print(f"Total Price : {quantity * 120}")
        print("Thank You For Ordering Come Back Again")
    case _:
        print("Invalid Choice! Order from the (1 - 3)")