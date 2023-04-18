from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
timeout = 30

def test_button_add_to_basket_exist(browser):
    browser.get(link)
    time.sleep(timeout)
    try:
        _ = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.ID, "add_to_basket_form"))
        )
        assert True
    except:
        assert False, "Button is not exist"