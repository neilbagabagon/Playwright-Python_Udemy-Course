import time
from shlex import split

from playwright.sync_api import Page, expect

# Write CSS-Selector by  #[ID]  .[ClassName]  [Tag Name]
def test_dynamic_script(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")  # rahulshettyacademy
    page.get_by_label("Password:").fill("Learning@830$3mK2")  # Learning@830$3mK2
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.locator(".media-body").filter(has_text="iphone X"))
    expect(page.locator(".media-body").filter(has_text="Nokia Edge"))

def test_child_window(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # handling Child Window
    with page.expect_popup() as newPage:
        page.get_by_text("Free Access to Inter").click() #trigger new page

        child_page = newPage.value
        child_page.locator(".page-title").text_content()
        expect(child_page.get_by_text("Documents request")).to_be_visible()

        email_text = child_page.locator(".red").text_content()
        words = email_text.split(" at ")
        email = words[1].split(" with ")[0] # .strip() can be used to remove all blank spaces
        assert email == "mentor@rahulshettyacademy.com"