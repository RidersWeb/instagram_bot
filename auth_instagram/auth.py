from lib2to3.pgen2 import driver
from tkinter import Button
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import login, password
from selenium.webdriver.common.by import By
import time, random


def auth(login, password):
    browser = webdriver.Chrome("/home/ridersweb/skill/auth_instagram/chromedriver")
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com')
    time.sleep(random.randrange(3,5))

#  Находим поля и заполняем
    
    #  Вводим логин 
    _login = browser.find_element(By.NAME, "username")
    _login.clear()
    _login.send_keys(login)
    
    # таймаут от 1 до 3 сек
    time.sleep(random.randrange(1, 3))
    
    # Вводим пароль
    _pass = browser.find_element(By.NAME, "password")
    _pass.clear()
    _pass.send_keys(password)

    time.sleep(random.randrange(1, 3))

    _pass.send_keys(Keys.ENTER)
    
    # Таймаут от 1до 3 сек
    # time.sleep(random.randrange(1, 3))
    # Поиск по селектору кнопку и нажатие на нее
    # _button = browser.find_element_by_css_selector('Button[type="submit"]')
    # _button.click()

    time.sleep(100)

    browser.close()
    browser.quit()

def main():
    auth(login, password)

if __name__ == "__main__":
    main()