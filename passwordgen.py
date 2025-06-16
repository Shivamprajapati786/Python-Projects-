import random
import string

def generate_password(length, use_special, use_digits):
    characters = list(string.ascii_letters)  # A-Z, a-z

    if use_digits:
        characters += list(string.digits)  # 0-9

    if use_special:
        characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?/")

    if not characters:
        raise ValueError("No character types selected.")

    # Ensure password includes at least one of each required type
    password = []

    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?/"))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password[:length])

def save_password(password):
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")
    print("✅ Password saved to 'passwords.txt'")

def main():
    print("🔐 Password Generator Tool")
    
    try:
        length = int(input("Enter password length: "))
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'

        password = generate_password(length, use_special, use_digits)
        print(f"\nGenerated Password: {password}")
        save_password(password)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
