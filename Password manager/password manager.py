from cryptography.fernet import Fernet
import os
import json

# File definition
PASSWORD_FILE = "passwords.json"
KEY_FILE = "secret.key"

# Uploading the key
def load_key():
    if not os.path.exists(KEY_FILE):
        print('The key file was not found! Generating a new key...')
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file: # Creates a new key and saves it to secret.key
            key_file.write(key) 
        print("A new key has been created. Save this file securely!")
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read() # Reads the key from the file.

# Uploading passwords
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}  #!Important! If passwords.json is empty, the program will show that there are no passwords!

# Showing saved passwords
def show_passwords(fernet):
    passwords = load_passwords()

    if not passwords:
        print("\nNo saved passwords.")
        return

    print("\nList of saved passwords:")
    for service, data in passwords.items():
        decrypted_password = fernet.decrypt(data["password"].encode()).decode()
        print(f"\n{service.capitalize()}")
        print(f"   Login: {data['login']}")
        print(f"   Password: {decrypted_password}")

# Adding a new password
def add_password(fernet):
    service = input('Enter the name of the service (e.g., Gmail): ').lower()
    login = input('Enter login: ')
    password = input('Enter password: ')

    passwords = load_passwords()  
    encrypted_password = fernet.encrypt(password.encode()).decode() # Encrypting the password

    passwords[service] = {"login": login, "password": encrypted_password} # Adding a new password

    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4) # Saving the updated JSON

    print(f"\nPassword for {service.capitalize()} saved!")

# Main Menu
def main():
    key = load_key()
    fernet = Fernet(key)

    while True:
        print("\nSelect an action: ")
        print("1 Show all passwords")
        print("2 Add a new password")
        print("3 Exit")
        
        choice = input("Enter the number: ")
        
        if choice == "1":
            show_passwords(fernet)
        elif choice == "2":
            add_password(fernet)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Incorrect input, please try again.")

# Launching the program
if __name__ == "__main__":
    main()
