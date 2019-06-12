from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")
x = int(browser.find_element_by_id("input_value").text)

y = calc(x)

browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("robotCheckbox").click()
browser.execute_script("window.scroll(0, 100);")

browser.find_element_by_id("robotsRule").click()

button = browser.find_element_by_css_selector("button.btn")

button.click()

