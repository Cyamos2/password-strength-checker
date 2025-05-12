def check_password_strength(password):
    length = len(password)
    
    if length >= 12:
        print("The password is long enough.")
    else:
        print("The password is too short.")

    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    if has_number:
        print("The password contains a number.")
    else:
        print("The password does NOT contain a number.")

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        print("The password contains an uppercase letter.")
    else:
        print("The password does NOT contain an uppercase letter.")

    has_special = False
    for char in password:
        if not char.isalnum():
            has_special = True
            break
    if has_special:
        print("The password contains a special character.")
    else:
        print("The password does NOT contain a special character.")

if __name__ == "__main__":
    test_password = "CyberSafe123"
    check_password_strength(test_password)
