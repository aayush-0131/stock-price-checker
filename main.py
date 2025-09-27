import os
import sys
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

# --- Main Logic ---


def get_stock_price(ticker_symbol):
    """
    Fetches the latest stock price for a given ticker symbol from Alpha Vantage.
    """
    # Check if API_KEY is loaded
    if not API_KEY:
        print("Error: API_KEY not found. Please set it in your .env file.")
        return

    # Parameters for the API request
    params = {"function": "GLOBAL_QUOTE", "symbol": ticker_symbol, "apikey": API_KEY}

    try:
        # Make the API request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        data = response.json()

        # The data is nested under the "Global Quote" key
        global_quote = data.get("Global Quote")

        if not global_quote:
            print(
                f"Error: Could not retrieve data for ticker '{ticker_symbol}'. It might be an invalid symbol or an API issue."
            )
            print("API Response:", data)  # Print the full response for debugging
            return

        # Extract the relevant fields
        symbol = global_quote.get("01. symbol")
        price = global_quote.get("05. price")

        if symbol and price:
            print("--- Stock Price ---")
            print(f"Ticker: {symbol}")
            print(f"Price:  ${price}")
            print("-------------------")
        else:
            print("Error: Price or Symbol not found in the API response.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the network request: {e}")
    except KeyError:
        print("Error: Unexpected format in API response. Could not parse data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ensure a ticker symbol is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <TICKER_SYMBOL>")
        # Example: python main.py AAPL
        sys.exit(1)  # Exit the script indicating an error

    # The first argument (sys.argv[0]) is the script name, so the ticker is the second (sys.argv[1])
    stock_ticker = sys.argv[1].upper()
    get_stock_price(stock_ticker)
