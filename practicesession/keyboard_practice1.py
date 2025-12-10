from playwright.sync_api import Page,expect

def test_keyboard1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    input1=page.locator("#input1")
    input1.focus()

    page.keyboard.insert_text("Sucessfully data inserted")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")

    input2=page.locator("#input2")
    expect(input2).to_have_value("Sucessfully data inserted")
    input2 = page.locator("#input3")
    expect(input2).to_have_value("Sucessfully data inserted")
    page.wait_for_timeout(5000)

