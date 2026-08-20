# Day 24 — Modules & Imports

## 📌 Topics Covered
- What is a module
- `import` statement
- `from ... import ...`
- `import ... as ...` (aliasing)
- `from module import *` and why it's avoided
- Built-in modules (`math`, `random`, `datetime`, `os`)
- Creating and using your own custom module
- `__name__ == "__main__"`
- `dir()` function

## 🛠️ What I Practiced
- Wrote custom modules (`calculator.py`, `greetings.py`, `converter.py`, `shapes.py`) and imported them into a main file
- Used `math` and `random` with both plain import and aliasing
- Built a dice roll simulator using the `random` module
- Used `datetime` to print current date and time
- Used `os.getcwd()` to check the working directory
- Used `dir()` to explore available functions inside a module
- Practiced the `__name__ == "__main__"` pattern to separate test code from importable code

## 💼 Interview Prep
Answered 15 interview questions covering the difference between modules and packages, import styles, module search behavior, `__name__`, namespaces, and organizing code into packages.

## 🔑 Key Takeaway
Modules let you split code into reusable files instead of one giant script. Understanding `import` styles and `__name__ == "__main__"` is foundational — this pattern shows up in almost every real Python project going forward.

---
⬅️ [Day 23 — File Handling](../Day-23) | ➡️ Day 25 — Virtual Environments & pip