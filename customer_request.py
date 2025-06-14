import json
from datetime import datetime

class CustomerRequest:
    def __init__(self, name, email, product):
        self.name = name
        self.email = email
        self.product = product
        self.timestamp = datetime.now().isoformat()  # Stores the timestamp

    # @staticmethod
    # def reset_notification_requests(filename="notifications.json"):
    #     """Clear notification requests only if outdated (instead of full reset)."""
    #     try:
    #         with open(filename, "r") as file:
    #             requests = json.load(file)
            
    #         # Filter out expired requests 
    #         valid_requests = [
    #             req for req in requests 
    #             if (datetime.fromisoformat(req["timestamp"]) - datetime.now()).days < 7
    #         ]

    #         with open(filename, "w") as file:
    #             json.dump(valid_requests, file, indent=4)

    #         print("🛠️ -- Message for testing purposes only — hidden from the user. -- notification.json file cleared!")
        
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         print("🛠️ -- Message for testing purposes only—hidden from the user. -- ❌ No valid requests to reset.")
    @staticmethod
    def reset_notification_requests(filename="notifications.json"):
        """Reset notifications.json by deleting all previous requests at the start of a session."""
        try:
            with open(filename, "w") as file:
                json.dump([], file, indent=4)  # Overwrite file with an empty list
            print("🗑️ Notifications.json has been reset! All previous requests have been cleared.")
        except Exception as e:
            print(f"❌ Error resetting notifications: {e}")

    def save_to_file(self, filename="notifications.json"):
        """Save user requests while preventing duplicates and keeping data structured."""
        try:
            with open(filename, "r") as file:
                requests = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            requests = []

        new_request = {
            "name": self.name,
            "email": self.email,
            "product": self.product,
            "timestamp": self.timestamp
        }

        # Check if a duplicate request already exists before adding
        if not any(req["email"] == self.email and req["product"] == self.product for req in requests):
            requests.append(new_request)

            with open(filename, "w") as file:
                json.dump(requests, file, indent=4)

            print(f"📩 Notification request saved for {self.product}!")
        else:
            print(f"🔔 You already requested a notification for {self.product}. No duplicate requests allowed.")