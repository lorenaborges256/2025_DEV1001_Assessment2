import logging
import sys

# Setup logging
logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")

class StockChecker:
    def __init__(self, stock_file="stock.txt"):
        self.stock_file = stock_file
        self.stock_data = self.check_stock()  # Load stock data on initialization

    def check_stock(self):
        """Load stock data while ensuring valid formatting."""
        stock_data = {}

        try:
            with open(self.stock_file, "r") as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]  # Remove empty lines

                if not lines:
                    logging.critical("-- user is not seeing this message --⚠ Stock file is empty. No products available!")
                    sys.exit("-- user is not seeing this message --🚨 Critical Error: Stock file is empty. Exiting program.")

                for line in lines:
                    try:
                        product, quantity = line.split(",")
                        product, quantity = product.strip().lower(), quantity.strip()

                        if not quantity.isdigit():
                            logging.critical(f"-- user is not seeing this message -- ❌ Invalid quantity in stock file: {line} (Quantity must be a number)")
                            sys.exit("-- user is not seeing this message --🚨 Critical Error: Non-numeric stock quantity found. Exiting program.")

                        stock_data[product] = int(quantity)

                    except ValueError:
                        logging.critical(f"-- user is not seeing this message --❌ Incorrect format in stock file: {line} (Expected format: Product,Quantity)")
                        sys.exit("-- user is not seeing this message --🚨 Critical Error: Stock file contains invalid format. Exiting program.")

        except FileNotFoundError:
            logging.critical("-- user is not seeing this message --❌ Stock file not found! Ensure stock.txt exists.")
            sys.exit("-- user is not seeing this message --🚨 Critical Error: Stock file missing. Exiting program.")

        logging.info(f"-- user is not seeing this message --🔍 Debug - Loaded Stock Data: {stock_data}")
        return stock_data

    def validate_product(self, product_name):
        """Check if the given product exists in stock data."""
        if product_name not in self.stock_data:
            logging.warning(f"🚨 Invalid product name entered: {product_name}")
            return False  # Product does not exist
        return True  # Product exists