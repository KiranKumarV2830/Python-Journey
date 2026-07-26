# Student Result Calculator

def total_marks(m1,m2,m3):
    return m1+m2+m3

def percentage(total):
    return total

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    else:
        return "Fail"

def result(name,grade):
    return name+grade

print(total_marks(100,100,100))
print(percentage(300))
print(grade(30))
print(result("Kiran",100))