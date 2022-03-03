import os
import sys

# Set the path to the current directory
# to avoid the error of the relative path
cwd = os.getcwd()
sys.path.insert(0, cwd)

from apps.controllers import get_all_users_controller
from apps.controllers import create_user_controller


def create_user():
    print("You chose to create a new user")
    print("Enter the following information:")
    name = input("Name: ")
    email = input("Email: ")

    create_user_controller({
        "name": name,
        "email": email
    })

    print("User created successfully")
    input("Press enter to continue")


def see_all_users():
    print("")
    print("You chose to see all users")
    users = get_all_users_controller()

    for user in users:
        print(f"ID: {user.id}")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print("")
    input("Press enter to continue")


def main():
    while True:
        # Clear the screen
        print("\033c")

        print("Hello, please choice one of the following options:")
        print("1. Create a new user")
        print("2. See all users")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_user()

        elif choice == "2":
            see_all_users()

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
