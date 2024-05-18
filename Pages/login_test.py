from pkg_resources import yield_lines
import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Tests.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    time.sleep(3)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(3)
    login_page.enter_username("test")
    time.sleep(3)
    login_page.enter_password("test")
    time.sleep(3)
    login_page.click_login()

    # driver.get("https://trytestingthis.netlify.app/")   
    # username_field = driver.find_element(By.ID,"uname")
    # password_field = driver.find_element(By.ID,"pwd") 
    # submit_button = driver.find_element(By.XPATH,"//input[@value='Login']")

    # username_field.send_keys(username)
    # password_field.send_keys(password)
    # time.sleep(4)
    # submit_button.click()
    assert "Successful" in driver.page_source
    time.sleep(3)
 
