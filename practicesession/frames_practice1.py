from playwright.sync_api import Page, expect

def test_frames1(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1.html")
    inputbox1 = frame1.locator("input[name='mytext1']")
    inputbox1.fill("hii")
    expect(inputbox1).to_have_value("hii")

    frame2 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_2.html")
    inputbox2 = frame2.locator("input[name='mytext2']")
    inputbox2.fill("hello")

    expect(inputbox2).to_have_value("hello")
