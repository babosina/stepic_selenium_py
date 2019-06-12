from selenium.webdriver.support.ui import Select
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

x = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
select = Select(browser.find_element_by_id('dropdown'))
select.select_by_value(str(x))

browser.find_element_by_css_selector("button.btn").click()

