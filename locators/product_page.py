from selenium.webdriver.common.by import By

from .base_locator import BasePageLocators


class ProductPageLocators(BasePageLocators):
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[text()[contains(.,'has been added to your basket')]]",
    )
    ADD_TO_BASKET_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'btn-add-to-basket')]",
    )
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_PRICE = (
        By.XPATH,
        '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]',
    )
    BOOK_NAME_IN_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PROMO_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[2]/div/strong')
    BASKET_PRICE_IN_MESSAGE = (
        By.XPATH,
        '//*[@id="messages"]/div[3]/div/p[1]/strong',
    )
