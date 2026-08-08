
---

# 3️⃣ `Student-Marks-Analyzer/README.md`

```markdown
# 📊 Student Marks Analyzer

A beginner-friendly Python mini project created during **Day 15 of my Python Journey**.

The project uses a Python list to store student marks and performs basic calculations on the data.

---

# 🎯 Project Goal

The goal of this project is to practice Python lists and basic built-in functions.

The program analyzes:

- Highest mark
- Lowest mark
- Total marks
- Average marks

---

# 📚 Concepts Used

- Python Lists
- `for` Loop
- `max()`
- `min()`
- `sum()`
- `len()`
- Arithmetic Operations
- F-Strings

---

# 💻 Code

```python
marks = [85, 72, 90, 65, 95]

print("Student Marks")
print("-------------")

for mark in marks:
    print(mark)

print(f"Highest Mark : {max(marks)}")
print(f"Lowest Mark : {min(marks)}")
print(f"Total Marks : {sum(marks)}")
print(f"Average Mark : {sum(marks) / len(marks)}")