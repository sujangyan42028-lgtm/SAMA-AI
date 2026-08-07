import requests

URL = "https://api.coingecko.com/api/v3/coins/markets"

COINS = {
    "bitcoin": "bitcoin",
    "btc": "bitcoin",
    "ethereum": "ethereum",
    "eth": "ethereum",
    "solana": "solana",
    "bnb": "binancecoin",
    "dogecoin": "dogecoin",
    "xrp": "ripple",
    "cardano": "cardano"
}


def run(user):

    user = user.lower()

    coin = "bitcoin"

    for key, value in COINS.items():
        if key in user:
            coin = value
            break

    try:

        r = requests.get(
            URL,
            params={
                "vs_currency": "usd",
                "ids": coin
            },
            timeout=10
        )

        data = r.json()

        if not data:
            return "Coin nahi mila."

        coin_data = data[0]

        name = coin_data["name"]
        usd = coin_data["current_price"]
        inr = round(usd * 83.5)   # Approx INR conversion
        change = coin_data["price_change_percentage_24h"]
        market_cap = coin_data["market_cap"]

        return (
            f"{name} Live Price\n\n"
            f"₹ {inr:,}\n"
            f"$ {usd:,}\n\n"
            f"24h Change: {change:.2f}%\n"
            f"Market Cap: ${market_cap:,}"
        )

    except Exception as e:

        print("[CRYPTO ERROR]", e)
        return "Crypto data fetch nahi ho paya."