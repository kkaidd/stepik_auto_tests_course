import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chrome_options
@pytest.fixture
def chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--windows-size=800,600')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):   #usr->local->bin
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver
@pytest.fixture

def setup(request, get_webdriver):
    driver = get_webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()