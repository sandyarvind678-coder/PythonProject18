from playwright.sync_api import Page, expect
import os
def test_data(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("Sample download file")
    page.locator("#generateTxt").click()

    page.on("download",lambda download:download.save_as("downloads/testfile.txt"))

    page.locator("#txtDownloadLink").click()
    page.wait_for_timeout(4000)

    if os.path.exists("downloads/testfile.txt"):
        print("exist")
    else:
        print("not exist")
