from playwright.sync_api import Page


def test_open(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context() #like an instance / incognito
    page = context.new_page()
    page.goto("https://www.google.com")

def test_open_browser(page:Page):
    page.goto("https://mlm-web.exequielarroyo.workers.dev/")