from datetime import datetime
from tabulate import tabulate

class Header:
    def __init__(self):
        self.app_name = "Notify Me CLI Application"
        self.version = "1.0 June 2025"
        self.description = (
            "This app notifies you via email when a product is back in stock.\n"
            "It also checks stock levels and informs registered users if a desired product is available."
        )
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_welcome(self):
        header_table = [
            ["Application", self.app_name],
            ["Version", self.version],
            ["Session Started", self.timestamp]
        ]

        print("=" * 60)
        print(tabulate(header_table, tablefmt="fancy_grid"))
        print("\n📦 Welcome to the Notification App!\n")
        print(self.description)
        print("=" * 60)
