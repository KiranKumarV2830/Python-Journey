# 📝 Notes App (CLI)

A simple command-line notes application built in Python. Add, view, search, and delete notes — all saved to a text file so they persist between runs.

Built as part of my Python learning journey (Day 23 — File Handling).

---

## Features

- **Add a note** — saves your note with a timestamp
- **View all notes** — displays every saved note, numbered
- **Search notes** — find notes containing a keyword (case-insensitive)
- **Delete a note** — remove a specific note by its number
- **Persistent storage** — notes are saved to `notes.txt`, so nothing is lost when you close the program

---

## How to Run

1. Clone this repository or download the `notes_app.py` file
2. Make sure you have Python 3 installed
3. Open a terminal in the project folder
4. Run:
```bash
python notes_app.py
```
5. Follow the on-screen menu to add, view, search, or delete notes

---

## Example

```
===== NOTES APP =====
1. Add a note
2. View all notes
3. Delete a note
4. Search notes
5. Exit
Enter choice: 1
Enter your notes: Buy groceries

===== NOTES APP =====
Enter choice: 2
1. Buy groceries
```

---

## Concepts Used

- File handling (`open()`, `'r'`, `'w'`, `'a'` modes)
- `with` statement for safe file handling
- `.readlines()` and `.write()`
- `try` / `except` for handling missing files (`FileNotFoundError`)
- String methods (`.strip()`, `.lower()`)
- `match` / `case` for menu control flow
- Functions and modular code structure

---

## What I Learned

This was my first end-to-end Python project combining file handling with a real, usable command-line interface. Building each function separately (add → view → delete → search → menu) and testing them one at a time helped me understand how small pieces come together into a working application.

---

## Author

**Kiran Kumar V**
GitHub: [@KiranKumarV2830](https://github.com/KiranKumarV2830)