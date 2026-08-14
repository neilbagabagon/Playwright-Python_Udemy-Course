from tkinter import dialog

from playwright.sync_api import Page, expect, Playwright


# Handling Placeholders, Visible/Invisible
def test_validation_ui(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    hide_show = page.get_by_placeholder("Hide/Show Example")
    expect(hide_show).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(hide_show).not_to_be_visible()
    page.get_by_role("button", name="Show").click()
    expect(hide_show).to_be_visible()

# Handling Alert Boxes
def test_alert(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

# Handling Hover
def test_mouse_hover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

# Handling Frames
def test_frames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frame_page = page.frame_locator("#courses-iframe")
    frame_page.get_by_role("link", name="All Access Plan").click()
    expect(frame_page.locator("body")).to_contain_text("All Access Subscription")

# Handling Tables with Data
def test_data_table(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for each_column in range(page.locator("th").count()):
        if page.locator("th").nth(each_column).filter(has_text="Price").count() > 0:
            column_value = each_column
            print(f"Column Value: {column_value}")
            break

    row_value = page.locator("tr").filter(has_text="Rice")
    expect(row_value.locator("td").nth(column_value)).to_have_text("37")