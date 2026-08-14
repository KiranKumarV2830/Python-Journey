price = float(input("Enter the price of the items you purchased : "))

if price >= 5000:
    print(f"Original Price: ₹{price}")
    discount = price * 0.20
    discount = price - discount
    print(f"Final Price : ₹{discount}")
elif price >= 2000:
    print(f"Original Price: ₹{price}")
    discount = price * 0.10
    discount = price - discount
    print(f"Final Price : ₹{discount}")
else :
    print("You do not get any discount.")
