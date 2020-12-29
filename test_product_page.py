from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.URL_WITH_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_that_product_added_to_basket()
    page.check_that_basket_value_changed()
