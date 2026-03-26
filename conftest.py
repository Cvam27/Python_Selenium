import pytest
from selenium import webdriver


# options = Options()
# options.add_argument(argument="--start-maximized")
# # options.add_argument(argument="--headless=new")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    yield driver
    driver.quit()
