# 📅 Day 14 - Variable Scope

## 📖 Topic

Today I learned about **Variable Scope** in Python.

Variable scope determines where a variable can be accessed within a program. Python mainly has **Local Variables** and **Global Variables**.

---

# 📚 Concepts Learned

- Variable Scope
- Local Variables
- Global Variables
- Local vs Global Variables
- The `global` Keyword
- Variable Shadowing
- Scope Rules
- Best Practices for Variables

---

# 🧠 Definitions

### Local Variable
A local variable is created inside a function and can only be accessed within that function.

Example:

```python
def greet():
    name = "Kiran"
    print(name)
```

---

### Global Variable

A global variable is created outside all functions and can be accessed anywhere in the program.

Example:

```python
name = "Kiran"

def greet():
    print(name)
```

---

### Global Keyword

The `global` keyword allows a function to modify a global variable.

Example:

```python
count = 0

def increase():
    global count
    count += 1
```

---

# 💻 Programs

- Local Variable Example
- Global Variable Example
- Global Keyword Example
- Variable Shadowing
- Bank Balance Program
- Counter Program
- School Information
- Student Details
- Shopping Cart
- Score Counter

---

# 🚀 Mini Project

## 🏦 Bank Account System

### Features

- Display Bank Name
- Display Current Balance
- Deposit Money
- Withdraw Money
- Update Balance
- Show Final Balance

---

# 🛠 Skills Practiced

- Creating Local Variables
- Creating Global Variables
- Using the `global` Keyword
- Understanding Variable Scope
- Updating Global Variables
- Writing Cleaner Functions

---

# 📂 Real-Life Examples

- ATM Balance
- Instagram Logged-in User
- YouTube Views Counter
- Bank Account
- School Information
- Shopping Cart

---

# 📖 Learning Outcome

After completing Day 14, I can:

- Explain Variable Scope.
- Differentiate between Local and Global Variables.
- Use the `global` keyword correctly.
- Understand Variable Shadowing.
- Decide when to use Local or Global Variables.

---

# 📚 Topics Covered

- Local Variables
- Global Variables
- Variable Scope
- `global` Keyword
- Variable Shadowing
- Scope Rules

---

# 🎯 Key Takeaways

- Local variables exist only inside functions.
- Global variables can be accessed throughout the program.
- Local variables are generally safer because they prevent accidental changes.
- Use the `global` keyword only when modifying a global variable.
- Understanding scope helps write cleaner and more organized code.

---

# 🛠 Language

Python 3

---

# 👨‍💻 Author

**Kiran Kumar V**

Learning Python one day at a time. 🚀