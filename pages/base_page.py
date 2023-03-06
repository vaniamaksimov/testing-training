from abc import ABC, abstractmethod
from typing import TypeVar

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

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
