from selenium.webdriver.common.by import By


class CommonMethods:
    def __init__(self,driver):
        self.driver = driver
    def getColumnData(self, column_name):
        column = self.driver.find_elements(By.CSS_SELECTOR, column_name)
        return [columnData.text for columnData in column]
