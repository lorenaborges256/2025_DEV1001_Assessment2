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
stock_data = stock_checker.stock_data  # Get valid stock data

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
            print("\n🔔 Client/User is not viewing this and the following messages. \n For test purpose it is time to manually update stock.txt to receive stock. Keep stock.txt as it is and update only its stock number...")
            stock_monitor.monitor_stock()  # Check for stock updates one last time
            print("📩 Sending pending notifications...")
            stock_monitor.send_email_notification(email, product)  # Send email if stock was updated
            print("✅ All pending notifications sent! Check your email for updates.")
            break

# Start product stock check loop
check_product_stock()