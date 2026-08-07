import requests
from urllib.parse import quote

print("🔥 WIKIPEDIA PLUGIN LOADED")


def run(user):

    print("🔥 WIKIPEDIA PLUGIN RUNNING")

    query = user.lower().strip()

    remove_phrases = [
        "wikipedia par",
        "wikipedia",
        "ke baare mein batao",
        "ke bare mein batao",
        "ke baare me batao",
        "ke bare me batao",
        "ke baare mein",
        "ke bare mein",
        "ke baare me",
        "ke bare me",
        "kya hai",
        "kaun hai",
        "kon hai",
        "batao",
        "bata",
        "tell me about",
        "about",
        "search",
        "find",
        "please"
    ]

    for phrase in remove_phrases:
        query = query.replace(phrase, " ")

    query = " ".join(query.split())

    if not query:
        return "Kis topic ke baare mein jaanna hai?"

    try:

        search_url = "https://en.wikipedia.org/w/api.php"

        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": f'"{query}"',
            "format": "json",
            "utf8": 1,
            "srlimit": 5
        }

        response = requests.get(
            search_url,
            params=search_params,
            headers={
                "User-Agent": "SAMA-AI/1.0"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        results = data.get("query", {}).get("search", [])

        if not results:
            return f"Wikipedia par '{query}' nahi mila."

        # Exact/closest title choose karo
        title = results[0]["title"]

        for result in results:

            result_title = result["title"].lower()

            if query.lower() == result_title:
                title = result["title"]
                break

            query_words = query.lower().split()

            if all(word in result_title for word in query_words):
                title = result["title"]
                break

        summary_url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + quote(title.replace(" ", "_"))
        )

        summary_response = requests.get(
            summary_url,
            headers={
                "User-Agent": "SAMA-AI/1.0"
            },
            timeout=10
        )

        summary_response.raise_for_status()

        summary_data = summary_response.json()

        extract = summary_data.get("extract")

        if not extract:
            return "Wikipedia par information nahi mili."

        page_url = (
            summary_data
            .get("content_urls", {})
            .get("desktop", {})
            .get("page", "")
        )

        answer = f"{title}\n\n{extract}"

        if page_url:
            answer += f"\n\nSource: {page_url}"

        return answer

    except requests.exceptions.RequestException as e:

        print("[WIKIPEDIA NETWORK ERROR]", e)

        return "Wikipedia se connection nahi ho paya."

    except Exception as e:

        print("[WIKIPEDIA ERROR]", e)

        return "Wikipedia se information fetch nahi ho payi."