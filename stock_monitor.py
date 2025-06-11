import json
import time
from stock_checker import StockChecker
from notifier import Notifier

class StockMonitor:
    def __init__(self, stock_file="stock.txt", notifications_file="notifications.json"):
        self.stock_checker = StockChecker(stock_file)
        self.notifications_file = notifications_file
        self.previous_stock = self.stock_checker.stock_data  # Store initial stock levels

    def send_email_notification(self, email, product):
        """Send an email notification only if stock has been updated."""
        notifier = Notifier()
        notifier.send_email("Customer", email, product)
        print(f"📧 Notification sent to {email} for {product}.")

    def check_stock_updates(self):
        """Waits for stock to change from 0 → positive before sending notifications."""
        print("🔍 Checking stock updates...")

        current_stock = self.stock_checker.check_stock()
        print(f"📦 Current stock levels: {current_stock}")

        try:
            with open(self.notifications_file, "r") as file:
                pending_notifications = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pending_notifications = []

        updated_products = []

        for request in pending_notifications:
            product = request["product"]
            email = request["email"]

            stock_updated = product in self.previous_stock and self.previous_stock[product] == 0 and current_stock.get(product, 0) > 0
            if stock_updated:
                updated_products.append((product, email))

        if updated_products:
            for product, email in updated_products:
                self.send_email_notification(email, product)  # Call the method within the class
                print(f"📩 Sent notification for {product} to {email}")

            pending_notifications = [req for req in pending_notifications if req["product"] not in current_stock or current_stock[req["product"]] == 0]

            with open(self.notifications_file, "w") as file:
                json.dump(pending_notifications, file, indent=4)

            return True  # Stop monitoring once stock updates

        print("⚠ No stock updates detected. Continuing to monitor...")
        self.previous_stock = current_stock
        return False  # Keep monitoring

    def monitor_stock(self, interval=10, timeout=20):
        """Monitor stock until an update occurs or timeout is reached."""
        print("🚀 Stock monitoring started... Checking every 10 seconds.")
        start_time = time.time()

        while True:
            if self.check_stock_updates():
                break

            if time.time() - start_time >= timeout:
                print("⏳ No stock update detected within 20 seconds. Stopping monitoring.")
                break

            time.sleep(interval)