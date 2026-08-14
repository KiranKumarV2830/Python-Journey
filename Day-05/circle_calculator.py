import math

radius = float(input("Enter the radius of the circle :"))

diameter = radius * 2

area = math.pi * (radius ** 2)

circumference = 2 * math.pi * radius

print(f"Diameter of the circle      : {diameter}cm")
print(f"Area of the circle          : {round(area,2)}cm²")
print(f"Circumference of the circle : {round(circumference,2)}cm")