import smtplib
import json
from email.mime.text import MIMEText

class Notifier:
    def __init__(self, sent_notifications_file="sent_notifications.json", credentials_file="credentials.txt"):
        self.sent_notifications_file = sent_notifications_file
        self.sent_notifications = self.load_sent_notifications()
        self.smtp_credentials = self.load_credentials(credentials_file)

    def load_credentials(self, filename):
        """Read SMTP credentials from a file."""
        credentials = {}
        try:
            with open(filename, "r") as file:
                for line in file:
                    key, value = line.strip().split("=")
                    credentials[key] = value
        except Exception as e:
            print(f"❌ Failed to load SMTP credentials: {e}")
        return credentials

    def load_sent_notifications(self):
        """Load previously sent email notifications to avoid duplicates."""
        try:
            with open(self.sent_notifications_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_sent_notifications(self):
        """Save sent email notifications to prevent duplicates."""
        with open(self.sent_notifications_file, "w") as file:
            json.dump(self.sent_notifications, file, indent=4)

    def send_email(self, name, email, product):
        """Send an email notification using stored credentials."""
        email_key = f"{email}:{product}"

        # if email_key in self.sent_notifications:
        #     print(f"🔔 Email already sent to {email} for {product}. Skipping...")
        #     return

        msg = MIMEText(f"Hello {name},\n\n Good news! {product} is back in stock. Get it now before it’s gone!")
        msg["Subject"] = f"{product} is back in stock!"
        msg["From"] = self.smtp_credentials.get("USERNAME")
        msg["To"] = email

        try:
            with smtplib.SMTP(self.smtp_credentials.get("SMTP_SERVER"), int(self.smtp_credentials.get("SMTP_PORT"))) as server:
                server.starttls()
                server.login(self.smtp_credentials.get("USERNAME"), self.smtp_credentials.get("PASSWORD"))
                server.sendmail(msg["From"], [msg["To"]], msg.as_string())

            print(f"📩 !!!! Email successfully sent to {name} ({email}) for {product}.")
            self.sent_notifications[email_key] = True  # Track sent emails
            self.save_sent_notifications()
        except Exception as e:
            print(f"❌ Failed to send email to {email}: {e}")
