def plan(user):

    user = user.lower()

    # Open app + search
    if "search" in user and "open" in user:
        return {
            "type": "multi",
            "steps": [
                "open_app",
                "google_search"
            ]
        }

    # Google search
    if user.startswith("what") or user.startswith("who") or user.startswith("why"):
        return {
            "type": "internet"
        }

    # Open application
    if "open" in user:
        return {
            "type": "app"
        }

    # Calculator
    if any(x in user for x in ["+", "-", "*", "/", "calculate"]):
        return {
            "type": "calculator"
        }
    # File Manager
    if "create folder" in user or "delete folder" in user:
        return {
            "type": "app"
        }
    return {
        "type": "ai"
    }