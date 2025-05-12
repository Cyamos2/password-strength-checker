# 🔐 Password Strength Checker (Python)

This is a modular Python script that evaluates whether a password is strong based on commonly recommended cybersecurity rules.

## ✅ What It Checks

The script verifies if a password includes:

- ✅ Minimum of 12 characters  
- 🔢 At least one number (`0–9`)  
- 🔠 At least one uppercase letter (`A–Z`)  
- ❗ At least one special character (e.g., `!`, `@`, `#`, `%`)

## 🧠 How It Works

The script defines a function:

```python
check_password_strength(password)
```

You can call this function with any string to check its strength.

### 🧪 Example:
```python
check_password_strength("CyberSafe123!")
```

Each rule is checked using loops and string methods like:

- `len()` to measure password length  
- `.isdigit()` to find numeric characters  
- `.isupper()` to detect uppercase letters  
- `not .isalnum()` to find special characters

The script includes a standard Python entry point:

```python
if __name__ == "__main__":
    test_password = "CyberSafe123"
    check_password_strength(test_password)
```

## 🧰 File Structure

```
password_strength_checker.py
README.md
```

## 🔄 Future Improvements

- 🧑‍💻 Accept user input via `input()`  
- 📊 Add password scoring (weak/medium/strong)  
- 📝 Log results to a file or database  
- 🖥️ Integrate with a GUI or web form  
- 🔍 Add regex-based rules for more precision

## 🧪 Why This Project?

This project supports my **CompTIA Security+** exam prep by helping me:

- 💡 Strengthen Python scripting skills  
- 🔐 Practice secure coding logic  
- 🛠️ Build real-world cybersecurity tools

---

✅ Feel free to clone, fork, or contribute!
