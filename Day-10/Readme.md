# 🐍 Day 10 - While Loops

## 📅 Date

Day 10

---

# 📖 Topics Covered

* While Loops
* Loop Conditions
* Boolean Expressions
* Infinite Loops
* Increment & Decrement
* `break` Statement
* Input Validation
* User Authentication
* ATM PIN Verification System
* IPO (Input → Process → Output)
* Edge Cases

---

# 📚 What I Learned

## ✅ What is a While Loop?

A **while loop** repeatedly executes a block of code **as long as the specified condition is `True`**.

Unlike a `for` loop, a `while` loop is generally used when the number of iterations is unknown.

---

## ✅ Syntax

```python
while condition:
    # Code to execute
```

---

# 💻 Examples

## Example 1 - Print Numbers 1 to 5

```python
count = 1

while count <= 5:
    print(count)
    count += 1
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

## Example 2 - Print "Hello" Five Times

```python
count = 1

while count <= 5:
    print("Hello")
    count += 1
```

---

## Example 3 - Countdown Timer

```python
count = 5

while count >= 1:
    print(count)
    count -= 1

print("Blast Off! 🚀")
```

---

## Example 4 - Password Verification

```python
password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted!")
```

---

## Example 5 - Positive Number Validation

```python
number = int(input("Enter a positive number: "))

while number <= 0:
    print("Invalid Number")
    number = int(input("Enter Again: "))

print("Thank You!")
```

---

# 🌍 Real-Life Applications

* ATM PIN Verification
* Login Systems
* Mobile Phone Lock Screen
* Guess the Number Game
* Menu-Driven Programs
* Input Validation
* Retry Until Success
* Banking Applications

---

# ⚠️ Infinite Loop

An **infinite loop** occurs when the loop condition never becomes `False`.

Example:

```python
while True:
    print("Hello")
```

To stop an infinite loop, use:

```python
break
```

---

# 🧠 IPO (Input → Process → Output)

## ATM PIN Verification

### Input

* ATM PIN
* Withdrawal Amount

### Process

* Verify the PIN.
* Allow a maximum of 3 attempts.
* If the PIN is correct, ask for the withdrawal amount.
* Check whether the account has enough balance.
* Complete the transaction.

### Output

* Welcome Message
* Incorrect PIN
* Transaction Successful
* Remaining Balance
* Card Blocked

---

# ⚠️ Edge Cases

* Wrong PIN
* More than 3 incorrect attempts
* Negative withdrawal amount
* Zero withdrawal amount
* Withdrawal exceeds account balance
* Empty input
* Non-numeric input

---

# 🚀 Mini Project

## ATM PIN Verification System

### Features

* 3 PIN attempts
* Balance checking
* Withdrawal validation
* Remaining balance display
* Card blocking after failed attempts
* Professional user messages

---

# 💡 Key Takeaways

* Use `while` loops when the number of repetitions is unknown.
* Always update the loop variable.
* Validate user input before processing it.
* Use `break` to exit a loop early.
* Think about edge cases before writing code.

---

# 📂 Files

* `day10.py`
* `atm_pin_verification.py`

---

# 🎯 Progress

✅ Learned While Loops

✅ Learned Infinite Loops

✅ Learned `break`

✅ Learned Input Validation

✅ Built ATM PIN Verification System

---

# 🌟 Quote

> **"A loop continues until the goal is achieved. Persistence in programming mirrors persistence in learning."**
