from stock_checker import StockChecker
from stock_monitor import StockMonitor
from user_auth import UserAuth
from customer_request import CustomerRequest
from header import Header

# App Header
header = Header()
header.display_welcome()

# Authenticate user
auth = UserAuth()
name, email = auth.login_or_register()

# Clear old notification requests at the start of the session
CustomerRequest.reset_notification_requests()

# Initialize StockChecker and StockMonitor
stock_checker = StockChecker()
stock_monitor = StockMonitor()
stock_data = stock_checker.check_stock()  # Call the method directly when checking stock updates # Get valid stock data

def main():
    
    def check_product_stock():
        while True:
            print("\n📦 See our Products Catalogue:")
            for product in stock_data.keys():
                print(f"- {product.title()}")  # Display product names in title case

            product = input("Enter the product name you want to check stock: ").strip().lower()

            # Validate user input before proceeding
            if not stock_checker.validate_product(product):  
                print("🚨 Invalid product name. Please enter a valid product from the catalogue.")
                continue  # Ask for input again

            # Check stock availability
            if stock_data[product] > 0:
                print(f"✅ {product} is in stock! Quantity: {stock_data[product]}. You can proceed to purchase it.")
            else:
                print(f"❌ Sorry, {product} is out of stock.")
                notify = input("Would you like to be notified when it's back in stock? (Yes/No): ").strip().lower()

                if notify == "yes":
                    request = CustomerRequest(name, email, product)
                    request.save_to_file()

            next_action = input("\nWould you like to check another product? (Yes/Exit): ").strip().lower()


            if next_action == "exit":
                print("\n🛠️ Stock monitoring will start. Please update stock.txt manually to test.")

                # Start stock monitoring (will run until update or timeout)
                stock_updated = stock_monitor.monitor_stock()

                if stock_updated:  # If stock update detected
                    print("📩 Sending pending notifications...")
                    stock_monitor.send_email_notification(email, product)  # Notify only if updated
                    print("✅ All pending notifications sent! Check your email for updates.")
                else:
                    print("⏳ Timeout reached. No stock update detected. No notifications sent.")
                break

    # Start product stock check loop
    check_product_stock()

if __name__ == "__main__":
    main()