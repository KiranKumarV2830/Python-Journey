# Traffic Light

light = input("Enter the Light name (RED/YELLOW/GREEN) : ").strip().upper()

if light == "RED":
    print(f"{light} means stop ")
elif light == "YELLOW":
    print(f"{light} means ready your vehicle")
elif light == "GREEN":
    print(f"{light} means go ")
else :
    print("Enter a valid light name")