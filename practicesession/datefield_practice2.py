from playwright.sync_api import Page, expect

def select_date(page,Date, Month, Year, is_future):

    while True:

        current_month=page.locator(".ui-datepicker-month").inner_text()
        current_year=page.locator(".ui-datepicker-year").inner_text()

        if current_month == Month and current_year == Year:
         break

        if is_future:
            page.locator("a[data-handler='next']").click()
        else:
            page.locator("a[data-handler='prev']").click()

    # After reaching correct month/year — select the day
    page.locator(f"//a[text()='{Date}']").click()




def test_datapicker(page: Page):

    page.goto("https://testautomationpractice.blogspot.com")
    wt = page.locator("#datepicker")
    wt.click()

    is_future=True
    Date="6"
    Month="July"
    Year="2026"
    select_date(page,Date, Month, Year, is_future)
    print("sample out:", wt.input_value())
    page.wait_for_timeout(4000)