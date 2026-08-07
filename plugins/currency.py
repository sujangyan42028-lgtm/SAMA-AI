import requests

URL = "https://open.er-api.com/v6/latest/USD"

CURRENCIES = {
    "usd": "USD",
    "dollar": "USD",
    "eur": "EUR",
    "euro": "EUR",
    "gbp": "GBP",
    "pound": "GBP",
    "jpy": "JPY",
    "yen": "JPY",
    "inr": "INR",
    "rupee": "INR",
    "rupees": "INR"
}


def run(user):

    user = user.lower()

    try:

        r = requests.get(URL, timeout=10)

        data = r.json()

        rates = data["rates"]

        if "dollar" in user or "usd" in user:

            return f"1 USD = {rates['INR']:.2f} INR"

        if "euro" in user or "eur" in user:

            eur_to_inr = rates["INR"] / rates["EUR"]

            return f"1 EUR = {eur_to_inr:.2f} INR"

        if "pound" in user or "gbp" in user:

            gbp_to_inr = rates["INR"] / rates["GBP"]

            return f"1 GBP = {gbp_to_inr:.2f} INR"

        if "yen" in user or "jpy" in user:

            jpy_to_inr = rates["INR"] / rates["JPY"]

            return f"1 JPY = {jpy_to_inr:.2f} INR"

        return "Kaunsi currency convert karni hai?"

    except Exception as e:

        print("[CURRENCY ERROR]", e)

        return "Currency data fetch nahi ho paya."