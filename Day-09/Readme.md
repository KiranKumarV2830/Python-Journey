# 🐍 Day 09 - For Loops

## 📅 Date

Day 09

---

# 📖 Topics Covered

* Introduction to `for` loops
* The `range()` function
* `range(start, stop, step)`
* Printing repeated statements
* Forward iteration
* Reverse iteration
* Using variables inside loops
* Output prediction
* IPO (Input → Process → Output)
* Edge Cases

---

# 📚 What I Learned

## ✅ What is a For Loop?

A **for loop** is used to execute a block of code repeatedly for every value in a sequence.

It is commonly used when the number of iterations is known.

---

## ✅ Syntax

```python
for variable in sequence:
    # Code to execute
```

---

## ✅ The `range()` Function

The `range()` function generates a sequence of numbers.

### Syntax

```python
range(start, stop, step)
```

### Parameters

* **start** → Starting value (included)
* **stop** → Ending value (not included)
* **step** → Increment or decrement value

---

# 📌 Important Rules

* Start value is included.
* Stop value is NOT included.
* Default start is `0`.
* Default step is `1`.
* Negative step is used for reverse counting.

---

# 💻 Examples

## Example 1

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

## Example 2

```python
for i in range(1,6):
    print(i)
```

Output

```
1
2
3
4
5
```

---

## Example 3

```python
for i in range(2,11,2):
    print(i)
```

Output

```
2
4
6
8
10
```

---

## Example 4

```python
for i in range(10,0,-2):
    print(i)
```

Output

```
10
8
6
4
2
```

---

## Example 5

```python
for i in range(3):
    print("Python")
```

Output

```
Python
Python
Python
```

---

## Example 6

```python
for i in range(5):
    print("Hello", i)
```

Output

```
Hello 0
Hello 1
Hello 2
Hello 3
Hello 4
```

---

## Example 7

```python
total = 0

for i in range(1,5):
    total += i

print(total)
```

Output

```
10
```

---

# 🌍 Real-Life Uses

* Printing multiplication tables
* Countdown timer
* Attendance systems
* Processing student marks
* Sending notifications
* Displaying menus
* Repeating tasks automatically

---

# 🧠 IPO (Input → Process → Output)

## Example: Countdown Timer

### Input

* Starting number

### Process

* Repeat the loop.
* Decrease the number by 1 each iteration.

### Output

* Countdown numbers.
* "Blast Off! 🚀"

---

# ⚠ Edge Cases

* User enters `0`
* User enters a negative number
* User enters text instead of a number
* User enters a very large number
* User presses Enter without entering anything

---

# 🚀 Mini Project

## Countdown Timer

### Features

* Takes starting number from the user.
* Counts down to 1.
* Displays **"Blast Off! 🚀"** after completion.

---

# 💡 Key Takeaways

* Use `for` loops when the number of repetitions is known.
* `range()` controls how the loop runs.
* The stop value is never included.
* The step value controls the increment or decrement.
* Predicting loop output improves logical thinking.

---

# 📂 Files

* `day09.py`
* `countdown_timer.py`

---

# 🎯 Progress

✅ Learned For Loops

✅ Learned `range()`

✅ Learned Forward and Reverse Loops

✅ Practiced Output Prediction

✅ Built Countdown Timer

---

# 🌟 Quote

> **"Automation begins with repetition. Loops allow computers to perform repetitive tasks efficiently."**
