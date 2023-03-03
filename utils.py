from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver(user_language: str) -> webdriver.Chrome:
    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": user_language}
    )
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    browser = webdriver.Chrome(options=options)
    return browser


def get_firefox_driver(user_language: str) -> webdriver.Firefox:
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    return browser
