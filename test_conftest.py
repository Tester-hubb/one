from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    find = browser.find_element(By.CSS_SELECTOR, "[value = 'Найти']")
    find.click()