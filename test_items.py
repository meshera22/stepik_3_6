import time


def test_basket_button(browser, language):
    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    # time.sleep(30)
    button = browser.find_elements_by_xpath("//button[@type='submit']")
    assert button, "Button is not found."
