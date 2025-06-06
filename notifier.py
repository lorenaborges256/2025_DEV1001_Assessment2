# Send Emails
import smtplib
import json
from email.mime.text import MIMEText

class Notifier:
    def __init__(self, sent_notifications_file="sent_notifications.json"):
        self.sent_notifications_file = sent_notifications_file
        self.sent_notifications = self.load_sent_notifications()

    def load_sent_notifications(self):
        """Load previously sent email notifications to avoid duplicates."""
        try:
            with open(self.sent_notifications_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_sent_notifications(self):
        """Save sent email notifications to avoid resending them."""
        with open(self.sent_notifications_file, "w") as file:
            json.dump(self.sent_notifications, file, indent=4)

    def send_email(self, name, email, product):
        """Send an email notification if not already sent for this product."""
        email_key = f"{email}:{product}"

        if email_key in self.sent_notifications:
            print(f"🔔 Email already sent to {email} for {product}. Skipping...")
            return

        msg = MIMEText(f"Hello {name},\n\nGood news! {product} is back in stock. Get it now before it’s gone!")
        msg["Subject"] = f"{product} is back in stock!"
        msg["From"] = "yourstore@example.com"
        msg["To"] = email

        try:
            with smtplib.SMTP("smtp.gmail.com") as server:
                server.starttls()
                server.login("yourstore@example.com", "yourpassword")  # Replace with real credentials
                server.sendmail(msg["From"], [msg["To"]], msg.as_string())
            print(f"📩 Email successfully sent to {name} ({email}) for {product}.")
            self.sent_notifications[email_key] = True  # Track sent emails
            self.save_sent_notifications()
        except Exception as e:
            print(f"❌ Failed to send email to {email}: {e}")

# Function for `stock_monitor.py`
def send_email_notification(email, product):
    """Send a quick email notification without requiring user name."""
    notifier = Notifier()
    notifier.send_email("Customer", email, product)