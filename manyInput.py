import time


from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    #
    for element in elements:
        element.send_keys("ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    #time.sleep(4)
    button.click()
finally:
    time.sleep(15)
    browser.quit()

