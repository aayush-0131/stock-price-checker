# Command-Line Stock Price Checker

A simple Python script to fetch the latest stock price for a given ticker symbol using the Alpha Vantage API.

## Features
- Fetches the latest price for any stock ticker.
- Takes the ticker symbol as a command-line argument.
- Securely handles API keys using a `.env` file.
- Provides clear, formatted output.

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd stock-price-checker
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You would first need to run `pip freeze > requirements.txt` to create this file)*

4.  **Set up your API Key:**
    - Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
    - Create a file named `.env` in the project root.
    - Add your API key to the `.env` file like this:
      ```
      API_KEY="YOUR_ALPHA_VANTAGE_API_KEY"
      ```

## Usage

Run the script from your terminal, passing the stock ticker as an argument.

```bash
python main.py <TICKER_SYMBOL>

Example
Bash

python main.py GOOGL
Example Output:

--- Stock Price ---
Ticker: GOOGL
Price:  $177.9400
-------------------
