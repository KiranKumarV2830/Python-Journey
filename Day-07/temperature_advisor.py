temp = float(input("Enter Temperature: "))

if temp < 15 :
    print("It is very cold.")
elif temp > 15 and (temp < 30) :
    print("It is very pleasant")
elif temp > 30 :
    print("It is very hot")
else:
    print("Enter a valid temperature")