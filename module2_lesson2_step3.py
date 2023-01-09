from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    num1 = browser.find_element(by=By.ID, value='num1').text
    num2 = browser.find_element(by=By.ID, value='num2').text
    answer = int(num1) + int(num2)
    select = Select(browser.find_element(by=By.TAG_NAME, value='select'))
    select.select_by_value(str(answer))
    browser.find_element(by=By.TAG_NAME, value='button').click()
finally:
    time.sleep(5)
    browser.quit()