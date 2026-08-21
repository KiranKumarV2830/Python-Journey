# Day 23 — File Handling

## 📌 Topics Covered
- Opening files with `open()` and file modes (`'r'`, `'w'`, `'a'`, `'r+'`)
- The `with` statement for safe, auto-closing file handling
- `.read()`, `.readline()`, `.readlines()`
- Looping through a file line by line
- `.write()` and `.writelines()`
- Handling missing files with `FileNotFoundError`
- Checking file existence with `os.path.exists()`

## 🛠️ What I Practiced
- Read and wrote text files using all major modes
- Counted lines, words, and characters in a file
- Copied file contents from one file to another
- Searched a file for lines containing a keyword
- Deleted a specific line from a file by rewriting it without that line
- Handled missing files gracefully instead of crashing

## 🎯 Mini Project — Personal Notes App (CLI)
Built a menu-driven command-line app with:
- `add_note()` — saves a note with a timestamp using append mode
- `view_notes()` — reads and displays all notes, numbered
- `delete_notes()` — removes a specific note by rewriting the file without it
- `search_notes()` — case-insensitive keyword search across all notes
- A `while True` menu loop using `match`/`case`

📂 Project repo: [notes-app-cli](../Mini-Projects/Notes-App-CLI)

## 💼 Interview Prep
Covered questions on file modes, `with` vs manual `close()`, text vs binary mode, handling large files efficiently, and common file-handling exceptions.

## 🔑 Key Takeaway
File handling is the foundation for almost every real project — reading configs, saving user data, logging, and more. Understanding `with`, the right file mode for the job, and safely handling missing files are skills that show up constantly going forward.

---
➡️ [Day 24 — Modules & Imports](../Day-24)