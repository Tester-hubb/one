import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_find_el1(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".first_block .form-control")
        for element in elements:
            element.send_keys("data")
        button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        time.sleep(1)
        responce = self.driver.find_element(By.TAG_NAME, "h1")
                # записываем в переменную text текст из элемента responce
        text = responce.text
                # с помощью assertEqual проверяем, что ожидаемый текст в переменной совпадает с текстом на странице сайта
        self.assertEqual(text,"Congratulations! You have successfully registered!", "Текст на странице не совпадает с ожидаемым")

    def test_find_el2(self):
        self.driver.get("http://suninjuly.github.io/wait1.html")

        button = self.driver.find_element(By.ID, "verify")
        button.click()
        message = self.driver.find_element(By.ID, "verify_message")
#проверка что в переменной присутствует текст, если текст не найден то сообщение
        self.assertIn("successful", message.text, "не найден текст на странице" )



if __name__ == "__main__":
    unittest.main()
