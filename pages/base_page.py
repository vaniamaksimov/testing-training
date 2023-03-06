import math
from abc import ABC, abstractmethod
from typing import TypeVar

from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchElementException,
)
from selenium.webdriver.remote.webdriver import WebDriver


Driver = TypeVar("Driver", bound=WebDriver)


class Page(ABC):
    def __init__(
        self, browser: Driver, url: str, timeout: int | float = 15
    ) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    @abstractmethod
    def open(self):
        """Метод для открытия страницы."""

    @abstractmethod
    def is_element_present(self, method, selector):
        """Метод для проверки присутствия элемента на странице."""


class BasePage(Page):
    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, method: str, selector: str) -> bool:
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
