from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    LOGIN_EMAIL = (By.XPATH, "//input[@id='id_login-username']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@id='id_login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@name='login_submit']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")
    REGISTER_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTER_PASSWORD = (By.XPATH, "//input[@id='id_registration-password1']")
    REGISTER_PASSWORD_CONFIRMATION = (
        By.XPATH,
        "//input[@id='id_registration-password2']",
    )
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
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
