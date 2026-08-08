cart = []

while True:

    print("===== SHOPPING CART =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Sort Cart")
    print("5. Clear Cart")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item to add: ")
        cart.append(item)

    elif choice == 2:
        item = input("Enter the item to remove: ")

        if item in cart:
            cart.remove(item)
        else:
            print("Item not found.")

    elif choice == 3:
        for item in cart:
            print(item)

    elif choice == 4:
        cart.sort()

    elif choice == 5:
        cart.clear()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")