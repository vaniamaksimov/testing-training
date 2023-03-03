from abc import ABC, abstractmethod
from typing import TypeVar

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


Driver = TypeVar('Driver', bound=WebDriver)


class Page(ABC):
    def __init__(self, browser: Driver, url: str) -> None:
        self.browser = browser
        self.url = url

    @abstractmethod
    def open(self):
        """Метод для открытия страницы."""


class BasePage(Page):

    def open(self) -> None:
        self.browser.get(self.url)
