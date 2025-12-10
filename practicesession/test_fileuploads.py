from playwright.sync_api import Page,expect
import pytest
import os
@pytest.mark.skip
def test_uploads(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.locator("#singleFileInput").set_input_files("uploads/file.txt")
    page.wait_for_timeout(5000)
    page.locator("//button[text()='Upload Single File']").click()
    page.pause()

def test_multipleuploads(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    files=["uploads/file.txt,uploads/file2.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.wait_for_timeout(5000)
    page.locator("//button[text()='Upload Multiple Files']").click()
    page.pause()