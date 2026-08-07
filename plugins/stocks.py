import requests

URL = "https://query1.finance.yahoo.com/v8/finance/chart/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

STOCKS = {
    "apple": "AAPL",
    "tesla": "TSLA",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "amazon": "AMZN",
    "nvidia": "NVDA",
    "meta": "META",
    "reliance": "RELIANCE.NS",
    "tcs": "TCS.NS",
    "infosys": "INFY.NS",
    "nifty": "^NSEI",
    "sensex": "^BSESN"
}


def run(user):

    user = user.lower()

    symbol = None

    for key, value in STOCKS.items():
        if key in user:
            symbol = value
            break

    if symbol is None:
        return "Kaunsi company ka stock dekhna hai?"

    try:

        r = requests.get(
            URL + symbol,
            headers=HEADERS,
            timeout=10
        )

        print("Status:", r.status_code)
        print(r.text[:200])

        if r.status_code != 200:
            return f"Yahoo API Error: {r.status_code}"

        data = r.json()

        if "chart" not in data or data["chart"]["result"] is None:
            return "Stock data available nahi hai."

        result = data["chart"]["result"][0]["meta"]

        name = result.get("symbol", symbol)
        price = result.get("regularMarketPrice")
        previous = result.get("previousClose")

        if price is None or previous is None:
            return "Price data nahi mili."

        change = price - previous
        percent = (change / previous) * 100

        return (
            f"{name} Live Price\n\n"
            f"Price : {price}\n"
            f"Previous Close : {previous}\n"
            f"Change : {change:.2f} ({percent:.2f}%)"
        )

    except Exception as e:

        print("[STOCK ERROR]", e)

        return "Stock data fetch nahi ho paya."