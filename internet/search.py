from ddgs import DDGS


def search_web(query):

    try:

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=5
                )
            )

        if not results:
            return None

        answer = ""

        for item in results:

            title = item.get("title", "")
            body = item.get("body", "")

            answer += f"{title}\n{body}\n\n"

        return answer.strip()

    except Exception as e:

        print("[SEARCH ERROR]", e)

        return None