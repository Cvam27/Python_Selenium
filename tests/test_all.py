import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.all_locators import Locators, customColumn
from page_objects.common import CommonMethods


def test_current_url(driver):
    assert "practice" in driver.current_url


def test_new_page_switch(driver):
    iframeButton = driver.find_element(By.CSS_SELECTOR, '[data-id="1f9693c"] a')
    ActionChains(driver).scroll_to_element(iframeButton).perform()
    wait = WebDriverWait(driver, 10)
    wait.until(lambda _: iframeButton.is_displayed())
    assert iframeButton.is_displayed(), "Button is not visible"
    iframeButton.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    assert 'iframe' in driver.current_url


def test_iframe(driver):
    # Navigate to iFrame page
    iframeButton = driver.find_element(By.CSS_SELECTOR, '[data-id="1f9693c"] a')
    ActionChains(driver).scroll_to_element(iframeButton).perform()
    wait = WebDriverWait(driver, 10)
    wait.until(lambda _: iframeButton.is_displayed())
    assert iframeButton.is_displayed(), "Button is not visible"
    iframeButton.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    assert 'iframe' in driver.current_url

    # test iFrame
    iframe = driver.find_element(By.CSS_SELECTOR, '[id="pact1"]')
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR, '[id="inp_val"]').send_keys("this is test")

    # test nested iframe
    nested_iframe = driver.find_element(By.CSS_SELECTOR, '[id="pact2"]')
    driver.switch_to.frame(nested_iframe)
    print(driver.find_element(By.CSS_SELECTOR, '[id="connect"]').text)

    # switch back to parent iframe
    driver.switch_to.parent_frame()
    # print(driver.find_element(By.CSS_SELECTOR,'[id="connect"]').text) # expect to be failed
    print(driver.find_element(By.CSS_SELECTOR, '[id="lost"]').text)

    # Switch to Default content
    driver.switch_to.default_content()
    # print(driver.find_element(By.CSS_SELECTOR, '[id="lost"]').text) # expect to be failed
    print(driver.find_element(By.CSS_SELECTOR, '[class*="elementor-heading-title"]').text)

    # get count of all elements with same id
    print(len(driver.find_elements(By.CSS_SELECTOR, '[class*="elementor-heading-title"]')))


def test_alert(driver):
    alertButton = driver.find_element(By.CSS_SELECTOR, '[onclick="windowAlertFunction()"]')
    # alertButton = driver.find_element(By.NAME,'Click To Open Window Alert')
    ActionChains(driver).scroll_to_element(alertButton).perform()
    assert alertButton.is_displayed()
    WebDriverWait(driver, 5)

    alertButton.click()
    # WebDriverWait(driver,2).until(EC.alert_is_present())
    # driver.get_screenshot_as_png()
    print(driver.switch_to.alert.text)


def test_dropdown(driver):
    drop_down_element = driver.find_element(By.CSS_SELECTOR, '[id="cars"]')
    drop_down = Select(driver.find_element(By.CSS_SELECTOR, '[id="cars"]'))
    ActionChains(driver).scroll_to_element(drop_down_element).perform()
    # adding sleep just to see scroll actually happens and then person further actions
    time.sleep(3)
    drop_down.select_by_visible_text('Audi')


def test_uploadFile(driver):
    fileupload = driver.find_element(By.CSS_SELECTOR, '[id="myFile"]')
    ActionChains(driver).scroll_to_element(fileupload).perform()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '[id="myFile"]').send_keys(
        "C:\/Users\shivam_acharya\PycharmProjects\Python_Selenium\pytest.ini")
    time.sleep(3)


def test_tabledata(driver):
    table = driver.find_element(By.CSS_SELECTOR, Locators.table)
    columnId = customColumn(3) #use index id to get column data
    ActionChains(driver).scroll_to_element(table).perform()
    cm = CommonMethods(driver)
    usernameList = cm.getColumnData(columnId)
    print(usernameList)
