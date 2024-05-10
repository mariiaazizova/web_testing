import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'

# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Создание экземпляра браузера
browser = webdriver.Chrome(service=chrome_service)
URL = "https://qa-course.netlify.app/registration-form-timer"

try:
    # Открытие веб-страницы
    browser.get(URL)

    # Явное ожидание для загрузки элементов страницы
    time.sleep(1)

    # Выбор первого встреченного input по тегу
    input1 = browser.find_element(By.NAME, "firstName")
    input1.send_keys("Mariia")

    # Выбор элемента по имени "lastName"
    input2 = browser.find_element(By.NAME, "lastName")
    input2.send_keys("Azizova")

    # Выбор элемента ввода, найденного по XPath "//input[@name='city']"
    input3 = browser.find_element(By.NAME, "city")
    input3.send_keys("SPb")

    # Выбор элемента по имени "email"
    input4 = browser.find_element(By.NAME, "email")
    input4.send_keys("mail@mail.com")
    # Явное ожидание для появления кнопки
    time.sleep(1)

    # Вызов JS-скрипта поиска и нажатия кнопки подтверждения
    script = '''document.querySelector('button[type="submit"]').click();'''
    browser.execute_script(script)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Задержка перед закрытием браузера
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
