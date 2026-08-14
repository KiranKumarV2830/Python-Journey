marks = [85, 72, 90, 65, 95]

print("Student Marks")
print("-------------")
for mark in marks :
    print(mark)
print(f"Highest Mark : {max(marks)}")
print(f"Lowest Mark : {min(marks)}")
print(f"Total Marks : {sum(marks)}")
print(f"Average Mark : {sum(marks)/len(marks)}")