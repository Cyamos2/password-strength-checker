password = "CyberSafe123"
length = len(password)

if length >= 12:
    print("The password is long enough.")
else:
    print("The password is too short.")

# Rule #2: Check for at least one number
has_number = False

for char in password:
    if char.isdigit():
        has_number = True
        break

if has_number:
    print("The password contains a number.")
else:
    print("The password does NOT contain a number.")

# Rule #3: Check for at least one uppercase letter

has_upper = False

for char in password:
    if char.isupper():
        has_upper = True
        break

if has_upper:
    print("The password contains an uppercase letter.")
else:
    print("The password does NOT contain an uppercase letter.")

# Rule #4: Check for at least one special character

has_special = False

for car in password:
    if not char.isalnum():
        has_special = True
        break

if has_special:
    print("The password contains a special character.")
else:
    print("The password does NOT contain a special character.")  