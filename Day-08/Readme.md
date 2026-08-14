# 🐍 Day 08 - Match-Case Statement

## 📅 Date 09/07/2026

Day 08 - Week 02

---

# 📖 Topics Covered

* Introduction to `match-case`
* `case` statements
* `case _` (Default Case)
* Difference between `if-elif-else` and `match-case`
* Menu-driven programming
* IPO (Input → Process → Output) problem-solving technique

---

# 📚 What I Learned

## ✅ Match-Case Statement

The `match-case` statement is a decision-making statement introduced in **Python 3.10**. It compares one variable against multiple fixed values and executes the matching case.

### Syntax

```python
match variable:
    case value1:
        # code

    case value2:
        # code

    case _:
        # default code
```

---

## ✅ case _

`case _` acts as the default case. It executes when none of the other cases match, similar to the `else` statement.

---

## ✅ When to Use Match-Case

Use `match-case` when:

* Comparing one variable with multiple fixed values.
* Creating menus.
* Handling user choices.
* Improving code readability.

---

# 🍔 Mini Project

## Restaurant Ordering System

### Features

* Displays a restaurant menu.
* Accepts the user's choice.
* Accepts the quantity.
* Calculates the total price.
* Displays the ordered item and total bill.
* Handles invalid menu selections using `case _`.

---

# 🧠 Problem-Solving (IPO)

## Input

* Customer's menu choice.
* Quantity of food.

## Process

* Check the selected menu item.
* Calculate:

```
Total Price = Quantity × Price
```

* Display the order details.

## Output

* Ordered item.
* Quantity.
* Total price.
* Thank-you message.

---

# 💡 Key Takeaways

* `match-case` makes menu-based programs cleaner than long `if-elif-else` statements.
* Always plan the solution using IPO before writing code.
* Use meaningful output messages to improve the user experience.

---

# 📂 Files

* `day08.py`
* `restaurant_menu.py`

---

# 🚀 Progress

✅ Learned Match-Case

✅ Built Restaurant Ordering System

✅ Practiced IPO Analysis

---

*"First think. Then plan. Then code."*
