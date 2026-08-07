import requests

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

SPECIAL_CITIES = {
    "kashmir": "Srinagar",
    "kashmiri": "Srinagar",
    "jk": "Srinagar",
    "j&k": "Srinagar"
}


def run(user):

    user = user.lower()

    city = None

    words = user.split()

    for word in words:

        if word not in [
            "weather",
            "temperature",
            "forecast",
            "rain",
            "mausam",
            "today",
            "in",
            "ka",
            "ki",
            "aaj"
        ]:
            city = word.capitalize()

    if city is None:
        city = "Srinagar"

    if city.lower() in SPECIAL_CITIES:
        city = SPECIAL_CITIES[city.lower()]

    try:

        geo = requests.get(
            GEO_URL,
            params={
                "name": city,
                "count": 1,
                "countryCode": "IN"
            },
            timeout=10
        ).json()

        if "results" not in geo:
            return "City nahi mila."

        location = geo["results"][0]

        lat = location["latitude"]
        lon = location["longitude"]
        name = location["name"]
        country = location["country"]

        weather = requests.get(
            WEATHER_URL,
            params={
                "latitude": lat,
                "longitude": lon,
                "current": [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "wind_speed_10m"
                ]
            },
            timeout=10
        ).json()

        current = weather["current"]

        return (
            f"Weather in {name}, {country}\n\n"
            f"🌡 Temperature : {current['temperature_2m']}°C\n"
            f"💧 Humidity : {current['relative_humidity_2m']}%\n"
            f"🌬 Wind : {current['wind_speed_10m']} km/h"
        )

    except Exception as e:

        print("[WEATHER ERROR]", e)

        return "Weather data fetch nahi ho paya."