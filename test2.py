from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

 
link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)



# Ваш код, который заполняет обязательные поля
x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
x = x_element.text

y = calc(x)

robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
robot_checkbox.click()
robot_ratio = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
robot_ratio.click()

answer = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
answer.send_keys(y)
    # Отправляем заполненную форму
\
button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
time.sleep(6)
browser.quit()
