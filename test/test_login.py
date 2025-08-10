import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_login():
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    options = Options()
    options.add_argument("--headless=new")

    driver = None
    for _ in range(10):
        try:
            driver = webdriver.Remote(command_executor=selenium_url, options=options)
            break
        except Exception:
            time.sleep(2)
    else:
        raise Exception("No se pudo conectar con Selenium Hub después de varios intentos")

    driver.get("http://app:5000")
    driver.find_element(By.ID, "username").send_keys("user")
    driver.find_element(By.ID, "password").send_keys("pass")
    driver.find_element(By.ID, "submit").click()
    assert "Bienvenido" in driver.page_source
    driver.quit()
