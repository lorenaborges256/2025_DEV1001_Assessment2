from datetime import datetime


class Header:
    def __init__(self):
        self.app_name = "Notify Me CLI Application"
        self.version = "1.0 June 2025"
        self.description = (
            "This app notifies you via email when a product is back in stock.\n"
            "and also it checks stock levels and informs registered users if a desired product is available.\n"
        )
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.welcome_message = (
            f"\n📦 Welcome to {self.app_name} (Version {self.version})!\n"
            f"\n"
            f"{self.description}\n"
            f"\n"
            f">> Current session started at: {self.timestamp}\n"
        )

    def display_welcome(self):
        print("-" * 50)
        print("v" * 50)
        print(self.welcome_message)
        print("^" * 50)
        print("-" * 50)
