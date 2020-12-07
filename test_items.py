import time
from selenium.common.exceptions import NoSuchElementException


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_presense_on_page(browser):
    browser.get(url)
    time.sleep(5)
    try:
        browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    except NoSuchElementException:
        return False

