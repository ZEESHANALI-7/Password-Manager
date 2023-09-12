# import json
# import getpass
#
# def load_passwords():
#     try:
#         with open('passwords.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}
#
# def save_passwords(passwords):
#     with open('passwords.json', 'w') as file:
#         json.dump(passwords, file)

# def add_password(passwords):
#     service = input("Enter the service name: ")
#     username = input("Enter the username: ")
#     password = getpass.getpass("Enter the password: ")
#
#     passwords[service] = {
#         'username': username,
#         'password': password
#     }
#
#     save_passwords(passwords)
#     print("Password saved successfully.")
# def add_password(passwords):
#     service = input("Enter the service name: ")
#     username = input("Enter the username: ")
#     password = input("Enter the password: ")
#
#     passwords[service] = {
#         'username': username,
#         'password': password
#     }
#
#     save_passwords(passwords)
#     print("Password saved successfully.")
#
#
# def get_password(passwords):
#     service = input("Enter the service name: ")
#
#     if service in passwords:
#         username = passwords[service]['username']
#         password = passwords[service]['password']
#         print(f"Service: {service}\nUsername: {username}\nPassword: {password}")
#     else:
#         print("Password not found.")
#
# def main():
#     passwords = load_passwords()
#
#     while True:
#         print("\nMenu:")
#         print("1. Add a new password")
#         print("2. Get a password")
#         print("3. Exit")
#
#         choice = input("Enter your choice (1-3): ")
#
#         if choice == '1':
#             add_password(passwords)
#         elif choice == '2':
#             get_password(passwords)
#         elif choice == '3':
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
# if __name__ == '__main__':
#     main()















import json
import getpass

def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

def add_password(passwords):
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    if service in passwords:
        if isinstance(passwords[service], list):
            passwords[service].append({
                'username': username,
                'password': password
            })
        else:
            passwords[service] = [{
                'username': passwords[service]['username'],
                'password': passwords[service]['password']
            }, {
                'username': username,
                'password': password
            }]
    else:
        passwords[service] = [{
            'username': username,
            'password': password
        }]

    save_passwords(passwords)
    print("Password saved successfully.")



def get_password(passwords):
    service = input("Enter the service name: ")

    if service in passwords:
        entries = passwords[service]
        print(f"Service: {service}")

        for index, entry in enumerate(entries, start=1):
            username = entry['username']
            password = entry['password']
            print(f"\nEntry {index}:")
            print(f"Username: {username}")
            print(f"Password: {password}")
    else:
        print("Password not found.")

def main():
    passwords = load_passwords()

    while True:
        print("\nMenu:")
        print("1. Add a new password")
        print("2. Get a password")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_password(passwords)
        elif choice == '2':
            get_password(passwords)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
