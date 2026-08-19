from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create Order -> Order ID
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("bagabagon111000@gmail.com")
    page.locator("#userPassword").fill("Pass_1234")
    page.get_by_role("button", name="login").click()

    # Order History Page -> Order is present
    page.get_by_role("button", name="  ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
    print(order_id)

    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()