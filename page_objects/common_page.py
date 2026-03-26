import random

from selenium.webdriver.common.by import By

from conftest import driver
from locators.all_locators import Locators


class CommonMethods:
    def __init__(self, driver):
        self.driver = driver

    def getColumnData(self, column_data, column_header):
        column = self.driver.find_elements(By.CSS_SELECTOR, column_data)
        columnHeader = self.driver.find_element(By.CSS_SELECTOR, column_header)
        return [columnData.text for columnData in column], columnHeader.text

    def searchTableDataByOS(self, search_string):
        self.driver.find_element(By.CSS_SELECTOR, Locators.searchableTable_searchInput).send_keys(search_string)

        # get userTable OS column data
        OSColumn = self.driver.find_elements(By.CSS_SELECTOR, Locators.searchableTable_OSColumn)
        return [os.text for os in OSColumn]

    def clickOnRandomUserInTable(self):
        allUsernames = self.driver.find_elements(By.CSS_SELECTOR, Locators.tableUsernameCell)
        selectedUsername = random.choice(allUsernames)
        print("\nSelected user: ", selectedUsername.text)
        selectedUsername.click()
