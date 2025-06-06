import json
from datetime import datetime

class CustomerRequest:
    def __init__(self, name, email, product):
        self.name = name
        self.email = email
        self.product = product
        self.timestamp = datetime.now().isoformat()  # Stores the timestamp

    @staticmethod
    def reset_notification_requests(filename="notifications.json"):
        """Clear notification requests at the start of each session."""
        try:
            with open(filename, "w") as file:
                json.dump([], file)  # Reset to an empty list
            print("-- user is not seeing this message -- ✅ Notification requests successfully cleared!")
        except Exception as e:
            print(f"-- user is not seeing this message -- ❌ Error clearing notification requests: {e}")

    def save_to_file(self, filename="notifications.json"):
        """Save user requests in a structured JSON file while preventing duplicates."""
        try:
            with open(filename, "r") as file:
                requests = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            requests = []

            # Check for duplicate requests
        new_request = {
            "name": self.name,
            "email": self.email,
            "product": self.product,
            "timestamp": self.timestamp
        }

        if not any(req["email"] == self.email and req["product"] == self.product for req in requests):
            requests.append(new_request)

            with open(filename, "w") as file:
                json.dump(requests, file, indent=4)

            print(f"📩 Notification request saved for {self.product}! (Requested at {self.timestamp})")
        else:
            print(f"🔔 You already requested a notification for {self.product}. No duplicate requests allowed.")