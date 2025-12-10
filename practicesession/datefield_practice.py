from playwright.sync_api import Page, expect

def select_date(page, selDate, selMonth, selYear, is_future):
    while True:
        current_month = page.locator(".ui-datepicker-month").inner_text()
        current_year = page.locator(".ui-datepicker-year").inner_text()

        if current_month == selMonth and current_year == selYear:
            break

        if is_future:
            page.locator("a[data-handler='next']").click()
        else:
            page.locator("a[data-handler='prev']").click()

    # After reaching correct month/year — select the day
    page.locator(f"//a[text()='{selDate}']").click()
    page.wait_for_timeout(3000)


def test_datapicker(page: Page):

    page.goto("https://testautomationpractice.blogspot.com")
    wt = page.locator("#datepicker")
    wt.click()

    Date = "11"
    Month = "November"
    Year = "2024"
    is_future = False

    select_date(page, Date, Month, Year, is_future)

    print("Selected:", wt.input_value())
    page.wait_for_timeout(5000)
