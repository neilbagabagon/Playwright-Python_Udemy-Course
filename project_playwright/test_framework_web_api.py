import json

import pytest
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

# JSON file -> util -> access to test
with open("project_playwright/data/credentials.json") as file:
    credentials_all_data = json.load(file)
    print(credentials_all_data)
    user_all_credentials = credentials_all_data["credentials"]

@pytest.mark.parametrize("user_credential", user_all_credentials)
def test_web_api(playwright: Playwright, user_credential):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Fetch existing orders dynamically for this user
    api_utils = APIUtils()
    existing_orders = api_utils.get_existing_orders(
        playwright,
        user_credential["userEmail"],
        user_credential["password"],
        limit=2
    )

    # Use the first order ID from existing orders
    if existing_orders:
        order_id = existing_orders[0]["productOrderedId"]
        print(f"Using existing order ID: {order_id}")
    else:
        raise Exception(f"No existing orders found for {user_credential['userEmail']}")

    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credential["userEmail"])
    page.locator("#userPassword").fill(user_credential["password"])
    page.get_by_role("button", name="login").click()

    # Order History Page -> Order is present
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
    print(order_id)

    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()
