import math
from abc import ABC, abstractmethod
from typing import TypeVar

from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import IMPLICITY_WAIT

Driver = TypeVar("Driver", bound=WebDriver)


class Page(ABC):
    def __init__(
        self, browser: Driver, url: str, timeout: int | float = IMPLICITY_WAIT
    ) -> None:
        self.browser = browser
        self.url = url
        if timeout:
            self.browser.implicitly_wait(timeout)

    @abstractmethod
    def open(self):
        """Метод для открытия страницы."""

    @abstractmethod
    def is_element_present(self, method: By, selector: str):
        """Метод для проверки присутствия элемента на странице."""

    @abstractmethod
    def is_not_element_present(
        self, method: By, selector: str, timeout: int | float = 4
    ):
        """Метод для проверки отсуствия элемента на странице."""

    @abstractmethod
    def is_disappeared(
        self, method: By, selector: str, timeout: int | float = 4
    ):
        """Метод для проверки сокрытия элемента с ожиданием."""


class BasePage(Page):
    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, method: By, selector: str) -> bool:
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(
        self, method: By, selector: str, timeout: int | float = 4
    ):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((method, selector))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(
        self, method: By, selector: str, timeout: int | float = 4
    ):
        try:
            WebDriverWait(
                self.browser, timeout, 1, TimeoutException
            ).until_not(EC.presence_of_element_located((method, selector)))
        except TimeoutException:
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
