student = {
    "name" : "Kiran",
    "branch" : "CSE",
    "Python" : 85,
    "Math" : 90,
    "Physics" : 78
}

print(student["name"])

print(student["branch"])

print(student["Python"])

print(student["Math"])

print(student["Physics"])

python_marks = student["Python"]
math_marks = student["Math"]
physics_marks = student["Physics"]

total = python_marks+math_marks+physics_marks

print(f"Total Marks : {total}")

average = total / 3
print(f"Average : {average}")