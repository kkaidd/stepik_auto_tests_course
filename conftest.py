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
def get_webdriver(get_chrome_options):   #usr->local->bin через "Double Commader"
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

def pytest_addoption(parser):
    parser_addoption('--browser_name', action='store', default=None
                     help="Choose browser: chrome o firefox")

@pytest.fixture(scope="fuction"):
    def browser(request):
        browser_name = request.config.getoption("browser_name")
        browser_name = None
        if browser_name == "chrome":
            print("\nstart chrome browser for test...")
            browser = webdriver.Chrome()
        elif browser_name == "firefox":
            print("\nstart firefox browser for test...")
            browser = webdriver.Firefox()
        else:
            raise pytest.UsageError("--browser_name should be chrom or firefox")
        yield browser
        print("\nquit browser")
        browser.quit()


