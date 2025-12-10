from playwright.sync_api import Page,expect

def test_keyboard(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    page.focus("#field1")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.wait_for_timeout(5000)
    f2=page.locator("#field2")
    f1 = page.locator("#field1")
    expect(f2).to_have_value(f1.input_value())

