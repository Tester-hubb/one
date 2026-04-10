from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
link_stepic = "https://stepik.org/lesson/236895/step/1"

def test_autor_step(browser):

    wait = WebDriverWait(browser, 10)
    browser.get(link_stepic)
    browser.implicitly_wait(10)
    #wait.until(EC.presence_of_element_located((By.ID, "ember501")))
    get_in = browser.find_element(By.ID, "ember501")
    get_in.click()
    print("\nOpen window for authorization")
    email = browser.find_element(By.ID, "id_login_email")
    password = browser.find_element(By.ID, "id_login_password")
    button = browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']")

    email.send_keys("test151293@gmail.com")
    password.send_keys("Cnhtktw123")
    button.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt = 'User avatar']" )))
    print("\nSearch avatar")

