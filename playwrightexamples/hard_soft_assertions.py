

from playwright.sync_api import Page, Playwright, expect

def test_open(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()


    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #hardassertion
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("//input[@id='hide-textbox']").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    #softassertion
    #expect.soft(page.locator("//input[@id='hide-textbox']")).to_be_visible()