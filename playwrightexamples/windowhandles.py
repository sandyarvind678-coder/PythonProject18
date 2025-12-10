from playwright.sync_api import Playwright, Page, expect

def test_open(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)  # 👈 add this line
    page: Page = context.new_page()

    page.goto("https://www.rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newpage_info:
     page.locator("//a[@class='blinkingText']").click()
     childwindow=  newpage_info.value
     text=childwindow.locator(".red").text_content()
     print(text)
     ex1= text.split("at ")
     ex2= ex1[1].split(" ")[0]
     print(ex2)