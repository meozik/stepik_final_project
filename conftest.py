import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    if language == "en":
        print("\nstart browser with English localization for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        print(browser.execute_script("return navigator.userAgent"))
    elif language == "fr":
        print("\nstart browser with French localization for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        print(browser.execute_script("return navigator.userAgent"))
    else:
        raise pytest.UsageError("--language should be en or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()
