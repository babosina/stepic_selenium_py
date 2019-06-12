# from selenium import webdriver

# browser = webdriver.Chrome()
#
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/cats.html")
# btn = browser.find_element_by_id("button")

# browser.find_element_by_id("check").click()
# message = browser.find_element_by_id("check_message").text
#
# assert "успешно" in message



from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text