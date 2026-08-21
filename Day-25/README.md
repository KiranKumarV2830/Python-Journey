# Day 25 — Virtual Environments & pip

## 📌 Topics Covered
- What a virtual environment is and why it's needed
- Creating a virtual environment with `venv`
- Activating and deactivating a virtual environment
- What `pip` is and how it installs third-party packages
- Installing a specific package version (`==`)
- Uninstalling packages
- Listing installed packages with `pip list`
- Generating and using `requirements.txt` (`pip freeze`)

## 🛠️ What I Practiced
- Created and activated a virtual environment from the terminal
- Installed a real third-party package (`requests`) inside an isolated environment
- Ran into and fixed a real VS Code interpreter mismatch issue (Pylance not resolving `requests`)
- Ran into and resolved a real `pip install` build failure (missing `pkg_resources` when installing an older `pandas` version)
- Generated a `requirements.txt` using `pip freeze`

## 🎯 Mini Project — Weather Checker App
Built a CLI app that:
- Takes a city name from the user
- Uses the `requests` library to call the free [wttr.in](https://wttr.in) weather API
- Prints the current weather for that city
- Comes with its own `requirements.txt` so anyone can recreate the environment

📂 Project repo: [weather-checker-app](../Mini-Projects/Weather-Checker-App)

## 💼 Interview Prep
Covered questions on the difference between global and virtual Python environments, `pip list` vs `pip freeze`, why `venv` folders shouldn't be committed to GitHub, and how `requirements.txt` enables reproducible environments.

## 🔑 Key Takeaway
This was less about syntax and more about real developer workflow — every professional Python project uses a virtual environment to avoid dependency conflicts between projects. Also got real practice debugging actual tooling errors (interpreter mismatch, build failures), not just code bugs — a skill just as important as writing the code itself.

---
⬅️ [Day 24 — Modules & Imports](../Day-24) | ➡️ Day 26 — Python Libraries & Packages