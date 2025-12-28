from playwright.sync_api import sync_playwright, expect, Page, Playwright


# Browser--> context---> page/s

def test_browsercontext(playwright:Playwright):
    # chromium=playwright.chromium
    # browser=chromium.launch()

    browser=playwright.chromium.launch(headless=False)  # created browser
    context=browser.new_context() # created context

    page=context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    page.get_by_role()
