from playwright.sync_api import sync_playwright

def open_website(url):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

    return f"Opening {url}"