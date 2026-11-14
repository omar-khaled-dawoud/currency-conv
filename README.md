# 💱 Currency Converter

A simple Python app that converts money between currencies using **ExchangeRate-API**.

## ✨ Features

- Convert an amount from one currency to another.
- Get exchange rates from a REST API.
- Check user input and display a clear result.
- Keep your API key in a `.env` file.

## 📁 Project Files

```text
CurrencyConverter/
├── main.py
├── requirements.txt
├── .env           # Your private API key 
├── .gitignore
└── .venv/         # Created locally
```

## 🚀 How to Run

**1. Create and activate a virtual environment** (Windows PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**2. Install the libraries:**

```powershell
python -m pip install -r requirements.txt
```

**3. Get a free API key** from [ExchangeRate-API](https://www.exchangerate-api.com/), then create a `.env` file:

```env
EXCHANGE_RATE_API_KEY=YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your own key. 

**4. Run the app:**

```powershell
python main.py
```

## 🔗 How the API Works

1. Enter an amount, a **base currency** (e.g. `USD`), and a **target currency** (e.g. `EGP`).
2. Python sends an **HTTP GET** request to the API:

   ```text
   https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD
   ```
3. The API returns **JSON** containing exchange rates. Example (sample numbers only):

   ```json
   {
     "result": "success",
     "conversion_rates": {
       "USD": 1,
       "EGP": 50.25
     }
   }
   ```
4. `response.json()` parses the JSON into a Python dictionary.
5. `rates.get(target_currency)` retrieves the requested rate.
6. The `CurrencyConverter` class calculates **amount × rate** and prints the result.

**Example output** (illustrative rate, not live):

```text
===== Currency Conversion =====
Amount        : 100.00
From Currency : USD
To Currency   : EGP
Exchange Rate : 50.25
Result        : 5025.00 EGP
===============================
```

## 🛠️ Common Issues

- **API Key not found:** Check the `.env` file and variable name.
- **HTTP error:** Check your API key, connection, or currency code.
- **Currency not supported:** Try another three-letter currency code.
