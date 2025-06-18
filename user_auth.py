import json
import os
import re

USER_FILE = "users.json"


class UserAuth:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        """Load existing users from JSON"""
        if os.path.exists(USER_FILE):
            with open(USER_FILE, "r") as file:
                data = json.load(file)
            return data["users"]  # Load list of users
        return []

    def save_users(self):
        """Save user data to JSON"""
        with open(USER_FILE, "w") as file:
            json.dump({"users": self.users}, file, indent=4)

    def is_valid_email(self, email):
        """Validate email format using regex"""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)

    def find_user_by_email(self, email):
        """Search for a user by email"""
        for user in self.users:
            if (
                isinstance(user, dict) and user.get("Email") == email
            ):  # Ensuring `user` is a dictionary
                return user
        return None

    def login_or_register(self):
        """Handles user login or account creation with email validation"""

        while True:
            choice = input("What would like to do? (Login/Create): ").strip().lower()

            if choice == "login":
                email = input("Enter your email: ").strip()
                user = self.find_user_by_email(email)

                if user:
                    print(f"\n✅ Welcome back, {user['Name']}!")
                    return user["Name"], user["Email"]
                else:
                    print("❌ No account found. Please create an account.")

            elif choice == "create":
                name = input("Enter your name: ").strip()

                while True:
                    email = input("Enter your email: ").strip()
                    if self.is_valid_email(email):
                        break
                    print(
                        "❌ Invalid email format. Please enter a valid email address."
                    )

                if self.find_user_by_email(email):
                    print("❌ Email already registered. Try logging in instead.")
                else:
                    new_user = {"Name": name, "Email": email}
                    self.users.append(new_user)
                    self.save_users()
                    print(f"\n✅ Account created! Welcome, {name}!")
                    return name, email

            else:
                print("❌ Invalid choice. Please type 'Login' or 'Create'.")
