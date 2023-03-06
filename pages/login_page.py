from .base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert (
            "/login" in self.browser.current_url
        ), "Must be /login in url addres"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL
        ), "No email field in login form"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD
        ), "No password field in login form"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_BUTTON
        ), "No button in login form"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_EMAIL
        ), "No email field in register form"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD
        ), "No password field in register form"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION
        ), "No password confirmation field in register form"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_BUTTON
        ), "No button in register form"
