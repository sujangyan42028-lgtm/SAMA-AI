import requests

API_KEY = "pub_22f3d58776fd43bfa8cf1964c8e18f25"

URL = "https://newsdata.io/api/1/news"

print("🔥 NEWS PLUGIN LOADED")


def run(user):

    print("🔥 NEWS PLUGIN RUNNING")

    user = user.lower()

    category = None

    if "business" in user:
        category = "business"

    elif "technology" in user or "tech" in user:
        category = "technology"

    elif "sports" in user:
        category = "sports"

    try:

        params = {
            "apikey": API_KEY,
            "country": "in",
            "language": "en"
        }

        if category:
            params["category"] = category

        r = requests.get(
            URL,
            params=params,
            timeout=10
        )

        data = r.json()

        if "results" not in data:
            print(data)
            return "News fetch nahi ho paayi."

        news = data["results"][:5]

        answer = "📰 Latest News\n\n"

        for i, item in enumerate(news, start=1):

            answer += f"{i}. {item['title']}\n\n"

        return answer

    except Exception as e:

        print("[NEWS ERROR]", e)

        return "News API error."