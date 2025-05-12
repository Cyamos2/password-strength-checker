# password-strength-checker
Python script that evaluates password strength based on common cybersecurity rules.

# Password Strength Checker 🔐

This is a simple Python script that evaluates whether a password is strong based on common cybersecurity standards.

## ✅ Features

The script checks for the following rules:
- Minimum length of 12 characters
- At least one number (`0–9`)
- At least one uppercase letter (`A–Z`)
- At least one special character (like `!`, `@`, `#`, etc.)

## 💻 How It Works

The script uses loops and string methods to check each rule:
- `len()` to check length
- `.isdigit()` to find numbers
- `.isupper()` to find uppercase letters
- `.isalnum()` to detect special characters (by checking for non-alphanumeric)

## 📂 File

- `password_strength_checker.py` — the main script

## 🚀 Future Ideas

- Allow user input instead of hardcoding the password
- Check password strength on a scale (weak → strong)
- Add regex for more advanced pattern matching
- Build a GUI or web tool version

## 📚 Why This Project?

This project is part of my cybersecurity-focused Python practice while preparing for the **CompTIA Security+** exam. It helps me:
- Reinforce Python logic
- Apply scripting to real security problems
- Build hands-on coding confidence

---

Feel free to clone, modify, or suggest improvements!
