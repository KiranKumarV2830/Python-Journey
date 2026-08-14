python_students = {
    "Kiran",
    "Rahul",
    "Arjun",
    "Ravi"
}

java_students = {
    "Rahul",
    "Arjun",
    "Vijay",
    "Manoj"
}

for student in python_students :
    print(student)

for students in java_students :
    print(students)

print(python_students.intersection(java_students))

print(python_students.difference(java_students))

print(java_students.difference(python_students))

print(python_students.union(java_students))

print(len(python_students.union(java_students)))