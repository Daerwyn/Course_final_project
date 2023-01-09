import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='en', help="Choose language, default - 'en'")


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument('--start-maximized')
    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()
