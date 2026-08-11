from playwright.sync_api import Page, expect, Playwright


def test_open(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # like an instance / incognito
    page = context.new_page()
    page.goto("https://www.google.com")


def test_open_browser(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")  # rahulshettyacademy
    page.get_by_label("Password:").fill("Learning123123")  # Learning@830$3mK2
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


# To RUN in Firefox
def test_FirefoxBrowser(playwright: Playwright):
    FirefoxBrowser = playwright.firefox.launch(headless=False)
    context = FirefoxBrowser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")  # rahulshettyacademy
    page.get_by_label("Password:").fill("Learning123123")  # Learning@830$3mK2
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
