import yt_dlp


def run(user):

    query = user.lower()

    remove_words = [
        "youtube",
        "search",
        "find",
        "video",
        "videos",
        "on",
        "par",
        "karo",
        "karo",
        "please"
    ]

    for word in remove_words:
        query = query.replace(word, " ")

    query = " ".join(query.split())

    if not query:
        return "Kya search karna hai?"

    try:

        options = {
            "quiet": True,
            "no_warnings": True,
            "extract_flat": True
        }

        with yt_dlp.YoutubeDL(options) as ydl:

            data = ydl.extract_info(
                f"ytsearch5:{query}",
                download=False
            )

        entries = data.get("entries", [])

        if not entries:
            return "YouTube par kuch nahi mila."

        answer = "YouTube Search Results\n\n"

        for i, video in enumerate(entries, start=1):

            title = video.get("title", "Unknown")
            url = video.get("url")

            if url and not url.startswith("http"):
                url = f"https://www.youtube.com/watch?v={url}"

            answer += (
                f"{i}. {title}\n"
                f"{url}\n\n"
            )

        return answer.strip()

    except Exception as e:

        print("[YOUTUBE ERROR]", e)

        return "YouTube search nahi ho payi."