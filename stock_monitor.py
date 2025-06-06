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

            # Trigger notification only when stock increases from 0 → positive
            if product in self.previous_stock and self.previous_stock[product] == 0 and current_stock.get(product, 0) > 0:
                updated_products.append((product, email))

        if updated_products:
            # print(f"✅ Stock update detected for: {updated_products}")
            for product, email in updated_products:
                send_email_notification(email, product)
                print(f"📩 Sent notification for {product} to {email}")

            # Remove notified requests from `notifications.json`
            pending_notifications = [req for req in pending_notifications if req["product"] not in current_stock or current_stock[req["product"]] == 0]

            with open(self.notifications_file, "w") as file:
                json.dump(pending_notifications, file, indent=4)

            # print("🛑 Stock update processed. Stopping monitoring.")
            return True  # Stop monitoring once stock updates

        print("⚠ No stock updates detected. Continuing to monitor...")
        self.previous_stock = current_stock  # Update stored stock data
        return False  # Keep monitoring

    def monitor_stock(self, interval=10):
        """Monitor stock until an update occurs, then stop."""
        print("🚀 Stock monitoring started... Checking every 10 seconds.")
        
        while True:
            if self.check_stock_updates():
                break  # Stop monitoring once a stock update is detected
            time.sleep(interval)
