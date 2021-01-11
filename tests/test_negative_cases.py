import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


link = ProductPageLocators.URL


@pytest.mark.xfail(reason="it's ok")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_that_success_message_is_not_present()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.check_that_success_message_is_not_present()


@pytest.mark.xfail(reason="it's ok")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_that_success_message_disappeared()
