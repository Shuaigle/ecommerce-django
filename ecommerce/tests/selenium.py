import pytest
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options()

    # headless allows us run chrome without open gui
    options.headless = False

    # use webdriver_manager to automatically install PATH with chrome_driver
    # use options instead of chrome_options
    browser = webdriver.Chrome(
        ChromeDriverManager().install(), options=options
    )
    yield browser
    browser.close()
