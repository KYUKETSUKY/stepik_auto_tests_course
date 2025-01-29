from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

 
link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    
    first_element = browser.find_element(By.ID, "num1")
    first_element_value = first_element.text
    print(first_element_value)
    second_element = browser.find_element(By.ID, "num2")
    second_element_value = second_element.text
    print(second_element_value)
    itog=str(int(first_element_value)+int(second_element_value))
    print(itog)
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_visible_text(itog)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(6)
    browser.quit()
finally:
    print(1)

