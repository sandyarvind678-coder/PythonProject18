from playwright.sync_api import Page,expect
import pytest
@pytest.mark.skip
def test_mouseaction(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    ms=page.locator(".dropbtn")
    ms.hover()

    option=page.locator(".dropdown-content a:nth-child(2)")
    option.hover()
    option.click()
    print("output:",option.inner_text())
    page.wait_for_timeout(5000)
@pytest.mark.skip
def test_mouseaction2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    db=page.locator("button[ondblclick='myFunction1()']")
    db.dblclick()

    fn=page.locator("#field2")
    expect(fn).to_have_value("Hello World!")
    page.wait_for_timeout(5000)

def test_mouseaction2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    source=page.locator("#draggable")
    target=page.locator("#droppable")

    source.drag_to(target)
    page.wait_for_timeout(5000)