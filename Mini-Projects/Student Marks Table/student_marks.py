students = [
    ["Kiran",85,90,88],
    ["Akash",85,79,98],
    ["Jeevan",92,88,95]
]

for student in students:
    print(student)



print(f"Name: {students[0][0]}, Marks: {sum(students[0][1:])}")
print(f"Name: {students[1][0]}, Marks: {sum(students[1][1:])}")
print(f"Name: {students[2][0]}, Marks: {sum(students[2][1:])}") 

