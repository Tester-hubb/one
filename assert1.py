import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://suninjuly.github.io/registration2.html")

try:
    elements = driver.find_elements(By.CSS_SELECTOR, ".first_block .form-control" )
    for element in elements:
        element.send_keys("data")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(1)
    responce = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную text текст из элемента responce
    text = responce.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == text


finally:
    time.sleep(10)
    driver.quit()
