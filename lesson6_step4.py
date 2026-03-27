import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    driver = webdriver.Firefox()
    link = "https://suninjuly.github.io/simple_form_find_task.html"
    driver.get(link)

    areaFirst = driver.find_element(By.NAME,"first_name")
    areaFirst.send_keys("имя")

    areaLast = driver.find_element(By.NAME, "last_name")
    areaLast.send_keys("Фамилия")

    city = driver.find_element(By.NAME, "firstname")
    city.send_keys("киров")

    country = driver.find_element(By.ID, "country")
    country.send_keys("Russia")

    button = driver.find_element(By.ID, "submit_button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()