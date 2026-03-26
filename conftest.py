import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    yield driver
    driver.quit()
