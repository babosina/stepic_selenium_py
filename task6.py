import os
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element_by_css_selector(".form-control:nth-child(2)").send_keys('toto')
browser.find_element_by_css_selector(".form-control:nth-child(4)").send_keys('stan')
browser.find_element_by_css_selector(".form-control:nth-child(6)").send_keys('toto@m.v')

cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'file.txt')

browser.find_element_by_id("file").send_keys(file_path)

browser.find_element_by_css_selector("button.btn").click()
