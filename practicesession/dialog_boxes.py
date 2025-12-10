from playwright.sync_api import Page, expect

def test_datapicker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com")


    def dialoghandle(dialog):
       print("dialog", dialog.message())
       dialog.dismiss()

    page.on("Dialog", dialoghandle)



    page.locator("#confirmBtn").click()

    page.wait_for_timeout(4000)