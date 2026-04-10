#Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



#Фикстура browser для создания экземпляра браузера(запуска)
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser")
    browser = webdriver.Firefox()

#всё что до yield выполняется перед тестов, то что после yield будет выполнено после теста.
    yield browser
    print("\nquit browser")
    browser.quit()