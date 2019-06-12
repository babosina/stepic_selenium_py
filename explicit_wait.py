from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

btn = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, 'check'))
)
btn.click()
message = browser.find_element_by_id("check_message").text

assert 'успешно' in message
