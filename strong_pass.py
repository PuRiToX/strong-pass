from pathlib import Path
import os
import secrets
import string

#Import HIBP Module
from hibp_checker import HIBPChecker

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(characters) for _ in range(length))


def check_basic_rules(password):
    issues = []
    
    # Minimum lenght
    if len(password) < 8:
        issues.append("Must have at least 8 characters")
    
    # Uppercase and lowercase
    if not any(c.isupper() for c in password):
        issues.append("Must contain at least one capital letter")
    if not any(c.islower() for c in password):
        issues.append("Must contain at least one lowercase letter")
    
    # Numbers and special characters
    if not any(c.isdigit() for c in password):
        issues.append("Must include at least one number")
    if not any(not c.isalnum() for c in password):
        issues.append("Must include at least one special character (ej. !@#)")
    
    # Show results
    if not issues:
        print("✅ Complies with basic safety rules")
        return False
    else:
        print("🔴 Problems encountered:")
        for issue in issues:
            print(f"- {issue}")
        return True

def load_common_passwords(filepath="rockyou.txt"):
    try:
        with open(filepath, 'r', encoding='latin-1') as f:
            # Read all lines and remove the spaces
            return {line.strip() for line in f}
    except FileNotFoundError:
        print(f"[-] Error: File '{filepath}' not found.")
        return set()

def is_common_password(password, common_passwords):
    # Checks both the original and lowercase passwords
    return (password in common_passwords) or (password.lower() in common_passwords)

def main():
    print("🔒 Password Strenght Validator 🔒")
    password = input("Enter you password: ")
    common_passwords = load_common_passwords()

    #Check if it complies with the basic rules
    suggest_new_password = check_basic_rules(password)
    
    # Debug: Check dictionary loading
    print(f"\n🔍 - Loading the common dictionary 'Rockyou'")
    print(f"Loaded passwords: {len(common_passwords)}")
    print(f"Examples: {list(common_passwords)[:5]}")
    
    if not common_passwords:
        print("The dictionary could not be loaded. Ignoring local verification")
    elif is_common_password(password, common_passwords):
        print("🔴 ¡The password has been found in the dictionary!")
        suggest_new_password = True
    else:
        print("✅ The password isn't in the dictionary.")

    #Call to the hibp_checker module
    print("\n🔍 Checking with the I Been Pwned API")
    count, message = HIBPChecker.check_password(password)
    print(message)  # Show result
    if count > 0:
        suggest_new_password = True

    if suggest_new_password == True:
        if input("\n¿Generate secure password? (y/n): ").lower() == "y":
            new_pass = generate_password()
            print(f"\n🔑 Password generated: {new_pass}")
            print("¡Copy it and save it in a safe place!")
    else: 
        print(f"\n🏆 Security Level: Very Strong")

if __name__ == "__main__":
    main()