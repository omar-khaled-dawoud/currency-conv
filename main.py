
import os
import requests
from decimal import Decimal as D, InvalidOperation
from dotenv import load_dotenv, find_dotenv


# CurrencyConv Class
class CurrencyConverter:
    def __init__(self, amount, base_currency, target_currency, rate):
        self.amount = amount
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.rate = rate

    def convert(self):
        return self.amount * self.rate


# Amount Input & Val
while True:
    try:
        amount = D(input("Enter amount: "))

        if not amount.is_finite() or amount < 0:
            print("Invalid amount. Try again.")
            continue

        break

    except InvalidOperation:
        print("Please enter a valid number.")


# Base Currency Input & Val
while True:
    base_currency = input("Enter base currency: ").strip().upper()

    if (
        len(base_currency) == 3
        and base_currency.isascii()
        and base_currency.isalpha()
    ):
        break

    print("Invalid base currency. Enter 3 English letters.")


# Target Currency Input & Val
while True:
    target_currency = input("Enter target currency: ").strip().upper()

    if (
        len(target_currency) == 3
        and target_currency.isascii()
        and target_currency.isalpha()
    ):
        break

    print("Invalid target currency. Enter 3 English letters.")


# Load API Key
load_dotenv()

api_key = os.getenv("EXCHANGE_RATE_API_KEY")

if not api_key:
    raise SystemExit("API Key not found")


# API Endpoint
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"


# API Request & JSON Parsing
try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:

        data = response.json()

        if isinstance(data, dict) and data.get("result") == "success":

            rates = data.get("conversion_rates")

            if not isinstance(rates, dict):
                print("Invalid exchange rates data.")

            else:
                rate = rates.get(target_currency)

                if rate is not None:

                    rate = D(str(rate))

                    # Create Object
                    converter = CurrencyConverter(
                        amount,
                        base_currency,
                        target_currency,
                        rate
                    )

                    # Convert Amount
                    result = converter.convert()

                    # Formatted Output
                    print("\n===== Currency Conversion =====")
                    print(f"Amount        : {converter.amount:.2f}")
                    print(f"From Currency : {converter.base_currency}")
                    print(f"To Currency   : {converter.target_currency}")
                    print(f"Exchange Rate : {converter.rate}")
                    print(f"Result        : {result:.2f} {converter.target_currency}")
                    print("===============================")

                else:
                    print("Currency not supported.")

        else:
            print("API returned an error.")

    else:
        print(f"HTTP Error: {response.status_code}")

except requests.exceptions.RequestException:
    print("Connection failed.")

except ValueError:
    print("Invalid JSON response.")
