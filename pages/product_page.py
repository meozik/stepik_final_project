from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_price = ""
    product_name = ""

    def add_to_basket(self):
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON).click()
        # print("------------------------ DEBUG INFO FOR add_to_basket function------------------------")
        # print("product_name variable value = " + self.product_name)
        # print("product_price variable value = " + self.product_price)

    def check_that_product_added_to_basket(self):
        # print("------------------------ DEBUG INFO FOR check_that_product_added_to_basket function------------------------")
        # print("Success message value " + self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)[0].text)
        assert self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)[0].text == self.product_name + " has been added to your basket."

    def check_that_basket_value_changed(self):
        # print("------------------------ DEBUG INFO FOR check_that_basket_value_changed function------------------------")
        # print(self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE_PRICE)[0].text)
        assert self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE_PRICE)[0].text == "Your basket total is now " + self.product_price

    def check_that_success_message_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is on page"

    def check_that_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message still on page"