import json

import pytest
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

# JSON file -> util -> access to test
with open("credentials.json") as file:
    credentials_all_data = json.load(file)
    print(credentials_all_data)
    user_all_credentials = credentials_all_data["credentials"]

@pytest.mark.parametrize("user_credential", user_all_credentials)
def test_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create Order -> Order ID
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credential[0])
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
