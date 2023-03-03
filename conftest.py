from typing import Callable, Dict

import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest

from config import IMPLICITY_WAIT
from utils import get_chrome_driver, get_firefox_driver


BROWSERS: Dict[str, Callable] = {
    "chrome": get_chrome_driver,
    "firefox": get_firefox_driver,
}


def pytest_addoption(parser: Parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser",
    )
    parser.addoption(
        "--language", action="store", default="en", help="Choose language"
    )


@pytest.fixture(scope="function")
def browser(request: SubRequest):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    if browser_name in BROWSERS:
        browser = BROWSERS.get(browser_name)(user_language)
    else:
        raise pytest.UsageError("incorect browser name")
    browser.implicitly_wait(IMPLICITY_WAIT)
    yield browser
    browser.quit()
