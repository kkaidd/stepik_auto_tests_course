from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time
# переход на нужную страницу
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


# функция, которая находит значение выражения при заданном x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# находим значение x для выполнения задания
# x_in_first_test = browser.find_element_by_id("input_value")
# x_value = x_in_first_test.text

# высчитываем результат для первого задания
# first_test_result = calc(x_value)
# x_element = browser.find_element_by_id("input_value")\
x_element = browser.find_element("id", "input_value")
#print("x_elemet = ", x_element)
x = x_element.text
y = calc(x)
#print("y_element", y)

# вводим ответ к первому тесту
first_test_input = browser.find_element("id", "answer")
first_test_input.send_keys(y)

# выбираем checkbox
robot_checkbox = browser.find_element("id", "robotCheckbox")
robot_checkbox.click()

# выбираем radiobutton
robot_radiobutton = browser.find_element("id", "robotsRule")
robot_radiobutton.click()

# нажимаем кнопку отправить
send_button = browser.find_element(By.CLASS_NAME, "btn-default")
send_button.click()

    # успеваем скопировать код за 30 секунд
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()
