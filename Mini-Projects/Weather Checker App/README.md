# 🌦️ Weather Checker App

A simple command-line app that fetches and displays the current weather for any city, using the `requests` library and a free weather API.

Built as part of my Python learning journey (Day 25 — Virtual Environments & pip).

---

## Features

- Enter any city name and get its current weather instantly
- Uses [wttr.in](https://wttr.in) — a free weather API, no API key required
- Lightweight — just one external dependency (`requests`)

---

## How to Run

1. Clone this repository or download `weather.py` and `requirements.txt`
2. Create a virtual environment:
```bash
python -m venv myenv
```
3. Activate it:
```bash
# Windows
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate
```
4. Install the required package:
```bash
pip install -r requirements.txt
```
5. Run the app:
```bash
python weather.py
```
6. Enter a city name when prompted

---

## Example

```
Enter a City name: Bangalore
Bangalore: ⛅️ +27°C
```

---

## Concepts Used

- Virtual environments (`venv`) for isolated dependencies
- `pip install` for third-party libraries
- `pip freeze` to generate `requirements.txt`
- The `requests` library to make an HTTP GET request
- f-strings for building the API URL

---

## What I Learned

This project was my first hands-on use of a **third-party library** (not built into Python) and my first time making a real API call. It also gave me practical experience with the actual venv + pip workflow — creating an isolated environment, installing a package into it, and generating a `requirements.txt` so anyone else can set up the exact same environment.

---

## Author

**Kiran Kumar V**
GitHub: [@KiranKumarV2830](https://github.com/KiranKumarV2830)