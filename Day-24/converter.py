unit = input("Select the unit you want to convert to (C/F) : ").strip().upper()

temp = int(input("Enter the temperature : "))

if unit == "c":
    cel = (temp * 9 ) / 5 + 32
    print(f"The temperature is {cel}C")
elif unit == "f":
    fah = (temp * 1.8) + 32
    print(f"The temperature is {fah}")
else:
    print("Invalid unit")