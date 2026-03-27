import random
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from locators.all_locators import Locators, customColumnLocatorGenerator
from page_objects.common_page import CommonMethods


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
    assert "iframe" in driver.current_url


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
    assert "iframe" in driver.current_url

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
    print(
        driver.find_element(By.CSS_SELECTOR, '[class*="elementor-heading-title"]').text
    )

    # get count of all elements with same id
    print(
        len(driver.find_elements(By.CSS_SELECTOR, '[class*="elementor-heading-title"]'))
    )


def test_alert(driver):
    alertButton = driver.find_element(By.XPATH, Locators.alertButton)
    # alertButton = driver.find_element(By.NAME,'Click To Open Window Alert')
    ActionChains(driver).scroll_to_element(alertButton).perform()
    assert alertButton.is_displayed()
    WebDriverWait(driver, 5)

    alertButton.click()
    # WebDriverWait(driver,2).until(EC.alert_is_present())
    # driver.get_screenshot_as_png()
    print(driver.switch_to.alert.text)


def test_dropdown(driver):
    drop_down_element = driver.find_element(By.CSS_SELECTOR, Locators.dropdown)
    drop_down = Select(driver.find_element(By.CSS_SELECTOR, Locators.dropdown))
    ActionChains(driver).scroll_to_element(drop_down_element).perform()
    # adding sleep just to see scroll actually happens and then person further actions
    time.sleep(3)
    drop_down.select_by_visible_text("Audi")
    driver.get_screenshot_as_png()


@pytest.mark.xfail
def test_uploadFile(driver):
    fileupload = driver.find_element(By.CSS_SELECTOR, Locators.fileUpload)
    ActionChains(driver).scroll_to_element(fileupload).perform()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, Locators.fileUpload).send_keys(
        "C:\/Users\shivam_acharya\PycharmProjects\Python_Selenium\pytest.ini"
    )
    time.sleep(3)


def test_tabledata(driver):
    # Verify table data
    table = driver.find_element(By.CSS_SELECTOR, Locators.userTable)
    ActionChains(driver).scroll_to_element(table).perform()
    columnDataLocator, columnHeaderLocator = customColumnLocatorGenerator(
        random.randrange(2, 5)
    )
    cm = CommonMethods(driver)
    columnData, columnHeader = cm.getColumnData(columnDataLocator, columnHeaderLocator)
    print(f"\nData for column {columnHeader}: ", columnData)
    assert columnData, f"\nData for column {columnData} is missing"
    assert columnHeader, f"\n{columnHeader} Column header name missing "

    # Verify Username link navigation
    currentWindow = driver.current_window_handle
    cm.clickOnRandomUserInTable()
    WebDriverWait(driver, 10).until(lambda w: len(w.window_handles) > 1)
    new_window = [w for w in driver.window_handles if w != currentWindow][0]
    driver.switch_to.window(new_window)
    assert (
        "bit.ly" in driver.current_url
        or "youtube" in driver.current_url
        or "udemy" in driver.current_url
    ), "Expected url is not loaded"
    driver.switch_to.window(currentWindow)


@pytest.mark.only
def test_shadowDom(driver):
    SR_elm = driver.find_element(By.CSS_SELECTOR, Locators.sd_element)
    ActionChains(driver).scroll_to_element(SR_elm).perform()
    shadowRoot = SR_elm.shadow_root
    SR_UsernameInput = shadowRoot.find_element(
        By.CSS_SELECTOR, Locators.sd_usernameInput
    )
    SR_UsernameInput.send_keys("dsfdsfdsfds")
    time.sleep(3)
    print(SR_UsernameInput.get_property("value"))


def test_tableSearching(driver):
    sortTable = driver.find_element(By.CSS_SELECTOR, Locators.searchableTable)
    ActionChains(driver).scroll_to_element(sortTable).perform()
    assert sortTable.is_displayed()
    cm = CommonMethods(driver)
    OSResult = cm.searchTableDataByOS(search_string="mac")
    print(OSResult)
    assert all(
        item == "mac" for item in OSResult
    ), f"found different item in {OSResult}"
