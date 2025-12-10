
from playwright.sync_api import Page, expect, playwright, Playwright


def test_windowhandling(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page= context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("//button[text()='New Tab']").click()
    page.wait_for_timeout(4000)

    page.on("page",lambda page:page.wait_for_load_state())
    totalpages=context.pages
    print("Number of tabs/pages:====>",len(totalpages))

    print("childpages",totalpages[1].title())
    childtab=totalpages[1]
    c2=childtab.locator("#main-message").inner_text()
    print("Number of tabs/pages:====>",c2)

    print("child tab message", childtab.url)
    page.wait_for_timeout(5000)