from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# функция, которая находит значение выражения при заданном x
def calc(x):
	return str( math.log (abs ( 12 * math.sin( x ) ) ) )

# переход на нужную страницу
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
#Ждем пока упадет цена до 100$
button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 15).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button.click()

# находим значение x для выполнения задания
x_string = browser.find_element(By.ID, "input_value")
x_number = int( x_string.text )

# высчитываем результат для задания
answer = calc(x_number)

# вводим ответ к тесту
input_answer = browser.find_element(By.ID, "answer")
input_answer.send_keys(answer)

# нажимаем на кнопку
send_button = browser.find_element(By.ID, "solve")
send_button.click()

time.sleep(1)

# переключаемся на alert, достаем текст алерта
alert = browser.switch_to.alert
alert_text = alert.text

# достаем из текста алерта число, копируем в буфер обмена
addToClipboard = alert_text.split(": ")[-1]
pyperclip.copy(addToClipboard)