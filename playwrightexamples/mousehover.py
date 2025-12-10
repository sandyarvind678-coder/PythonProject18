from playwright.sync_api import Page, Playwright, expect
import time
def test_open(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()



