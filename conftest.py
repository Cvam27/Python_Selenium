import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument(argument="--headless=new")

@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    yield driver
    driver.quit()