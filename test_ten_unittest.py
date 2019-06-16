from selenium import webdriver
import time
import unittest


class TestTen(unittest.TestCase):

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
        input3.send_keys("test@test.test")
        input4 = browser.find_element_by_css_selector("[placeholder='Введите телефон\:']")
        input4.send_keys("9999999999")
        input5 = browser.find_element_by_css_selector("[placeholder='Введите адрес\:']")
        input5.send_keys("test")
        #  Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        #  Проверяем, что смогли зарегистрироваться# ждем загрузки страницы
        time.sleep(1)
        #  находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        #  записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        #  с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайт
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_reg2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
        input3.send_keys("test@test.test")
        input4 = browser.find_element_by_css_selector("[placeholder='Введите телефон\:']")
        input4.send_keys("9999999999")
        input5 = browser.find_element_by_css_selector("[placeholder='Введите адрес\:']")
        input5.send_keys("test")
        #  Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        #  Проверяем, что смогли зарегистрироваться# ждем загрузки страницы
        time.sleep(1)
        #  находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        #  записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        #  с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайт
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)


if __name__ == "__main__":
    unittest.main()
