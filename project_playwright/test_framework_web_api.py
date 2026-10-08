import json

import pytest
from playwright.sync_api import Playwright, expect

from project_playwright.pageObjects.dashboard import DashboardPage
from project_playwright.pageObjects.login import LoginPage
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

    userName = user_credential["userEmail"]
    userPassword = user_credential["password"]

    # Fetch existing orders dynamically for this user
    api_utils = APIUtils()
    existing_orders = api_utils.get_existing_orders(
        playwright,
        user_credential,
        limit=2
    )

    # Use the first order ID from existing orders
    if existing_orders:
        order_id = existing_orders[0]["productOrderedId"]
        print(f"Using existing order ID: {order_id}")
    else:
        raise Exception(f"No existing orders found for {user_credential['userEmail']}")

    # Login
    loginPage = LoginPage(page)
    loginPage.navigation()
    dashBoard = loginPage.login(userName, userPassword)

    # Order History Page -> Order is present
    orderHistory = dashBoard.selectOrderNavLink()
    orderDetails = orderHistory.selectOrder(order_id)
    orderDetails.verifyOrderMessage()

    context.close()


