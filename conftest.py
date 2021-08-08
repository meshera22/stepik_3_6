import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                       help='Choose language to test')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nStarting browser for test...")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nStarting browser for test...")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nexit browser")
    browser.quit()

@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("language")