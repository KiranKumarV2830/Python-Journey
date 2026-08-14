students = {
    "Kiran": [85, 90, 78],
    "Rahul": [75, 88, 92],
    "Arjun": [90, 95, 89]
}
for name in students.keys():
    print(name)

for marks in students.values():
    print(marks)

total = 0

for mark in students.values():
    for num in mark:
        total += num
print(total)

average = total / (len(students)*len(marks))
print(average)

highest = 0

for high in students.values():
    for num in high:
        if num > highest:
            highest = num

print(highest)

lowest = students["Kiran"][0]
for low in students.values():
    for num in low:
        if num < lowest:
            lowest = num 

print(lowest)