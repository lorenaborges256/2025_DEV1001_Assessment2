# Detect Stock Changes and trigger notifications
import json
import time
from stock_checker import StockChecker
from notifier import send_email_notification

class StockMonitor:
    def __init__(self, stock_file="stock.txt", notifications_file="notifications.json"):
        self.stock_checker = StockChecker(stock_file)
        self.notifications_file = notifications_file
        self.previous_stock = self.stock_checker.stock_data  # Store initial stock levels

    def check_stock_updates(self):
        """Checks if previously out-of-stock products are now available."""
        current_stock = self.stock_checker.check_stock()

        try:
            with open(self.notifications_file, "r") as file:
                pending_notifications = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pending_notifications = []

        updated_products = []

        for request in pending_notifications:
            product = request["product"]
            email = request["email"]

            if product in current_stock and current_stock[product] > 0:
                updated_products.append((product, email))

        # Send email notifications for restocked items
        for product, email in updated_products:
            send_email_notification(email, product)
            print(f"📩 Sent notification for {product} to {email}")

        # Remove notified requests from `notifications.json`
        pending_notifications = [req for req in pending_notifications if req["product"] not in current_stock or current_stock[req["product"]] == 0]

        with open(self.notifications_file, "w") as file:
            json.dump(pending_notifications, file, indent=4)

        self.previous_stock = current_stock

    def monitor_stock(self, interval=60):
        """Continuously monitor stock updates."""
        while True:
            self.check_stock_updates()
            time.sleep(interval)  # Wait before checking again
