import requests

URL = "https://api.gold-api.com/price"


def run(user):

    user = user.lower()

    # Default Gold
    metal = "XAU"

    # Silver keywords
    if any(word in user for word in [
        "silver",
        "chandi",
        "chandi ka rate",
        "silver price",
        "silver rate"
    ]):
        metal = "XAG"

    try:

        r = requests.get(
            f"{URL}/{metal}",
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        if r.status_code != 200:
            return f"API Error: {r.status_code}"

        data = r.json()

        name = "Gold" if metal == "XAU" else "Silver"

        price = data.get("price")
        currency = data.get("currency", "USD")

        high = data.get("high_price")
        low = data.get("low_price")

        response = (
            f"{name} Live Price\n\n"
            f"Price : {price:,.2f} {currency}"
        )

        if high:
            response += f"\nHigh : {high:,.2f} {currency}"

        if low:
            response += f"\nLow : {low:,.2f} {currency}"

        return response

    except Exception as e:

        print("[METALS ERROR]", e)

        return "Metal data fetch nahi ho paya."