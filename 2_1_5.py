from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # находим на странице и получаем значение x:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # подставляем в фцию:
    y = calc(x)

    # теперь y нужно вписать в инпут который надо тоже найти на странице
    # ищем нужный инпут и отправляем значение y:
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # далее находим чекбокс и отмечаем его:
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()

    # далее находим радиобатон и отмечаем его:
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
