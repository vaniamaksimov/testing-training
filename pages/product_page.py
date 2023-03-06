from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_add_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ), "No button add to basket on page"
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ).click()

    def should_be_correct_output(self):
        assert self.is_element_present(
            *ProductPageLocators.BOOK_NAME_IN_MESSAGE
        ), "No message that book added to basket"
        page_book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME
        ).text
        message_book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME_IN_MESSAGE
        ).text
        assert (
            page_book_name == message_book_name
        ), f"No {page_book_name} in {message_book_name}"
        assert self.is_element_present(
            *ProductPageLocators.BASKET_PRICE_IN_MESSAGE
        ), "No message with basket price"
        page_book_price = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE
        ).text
        message_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE_IN_MESSAGE
        ).text
        assert page_book_price == message_price
        assert self.is_element_present(
            *ProductPageLocators.PROMO_MESSAGE
        ), "No promo message"
