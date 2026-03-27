#подключение встроенного модуля для работы со временем
import time
#импортировать пакет Selenium WebDriver
from selenium import webdriver
#класс By импорт из библиотеки Selenium
from selenium.webdriver.common.by import By
# класс позволяет имитировать сложные действия пользователя, включая наведение мыши
from selenium.webdriver.common.action_chains import ActionChains
#запустить Selenium WebDriver и драйвер браузера
driver = webdriver.Firefox()
#открыть ссылку в браузере
driver.get("https://ru.wikipedia.org/wiki/%D0%9C%D0%BB")
#пауза 5 секунд
time.sleep(5)
#Метод find_element позволяет найти нужный элемент на сайте, он принимает в качестве аргументов способ поиска и значение, по которому мы будем искать,Ищем поле для ввода текста
textarea = driver.find_element(By.NAME,"search")
# Напишем текст ответа в найденное поле
textarea.send_keys("python lessons")
time.sleep(5)
# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.ID, "searchButton")
# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
#нашли элемент по атрибуту
selecttest = driver.find_element(By.XPATH, "//a[@title='Тестировщик']")
#Наведение курсора на элемент selecttest(title='Тестировщик)
actions = ActionChains(driver)
actions.move_to_element(selecttest).perform()
#пауза 5 секунд

logOn = driver.find_element(By.XPATH, "//a[@title='Здесь можно зарегистрироваться в системе, но это необязательно. [Alt+Shift+o]']")
time.sleep(3)
logOn.click()
time.sleep(5)
# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
