from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

'''
Откройте страницу с вариантом и определите вручную с использованием
DevTools селекторы для каждой предметной карточки.
Требуется проверить отображение 6 предметных карточек.
На одной карточке находятся графическое изображение и текст.
Для каждой из них вебразработчик реализовал уникальные атрибуты.
Для подтверждения достоверности отображения карточки достаточно
провести тестирования по одному из селекторов карточки: атрибутам,
 тегам, CSS-селекторов, XPath-пути
'''
# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'

# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Создание экземпляра браузера
browser = webdriver.Chrome(service=chrome_service)

# Адрес сайта
URL = " https://qa-test-selectors.netlify.app/"
# Номер варианта
VARIANT = 1
try:
    # Открытие веб-страницы
    browser.get(URL)

    # Неявное ожидание для загрузки элементов страницы
    browser.implicitly_wait(10)

    # Выбор кнопки с 1 вариантом, как 0 элемента из списка всех кнопок страницы
    #button = browser.find_elements(By.TAG_NAME,'button')[VARIANT-1]

    # Выбор кнопки с 1 вариантом, по XPATH
    button = browser.find_element(By.XPATH,f'//button[@class="variant__btn"][text()="{VARIANT}"]')

    # Выбор кнопки с 1 вариантом, по CSS-селектору
    #button = browser.find_element(By.CSS_SELECTOR, f'.variant__btn:nth-child({VARIANT})')

    # Нажатие на кнопку с вариантом
    button.click()

    print("-----------------------------")

    print("тестирование по атрибутам")
    # Элементы с ID advantage
    elements_by_id = browser.find_elements(By.ID, "smile")
    print("Элементы с ID smile:", len(elements_by_id))

    # Элементы с именем smile-cat"
    elements_by_name = browser.find_elements(By.NAME, "smile-cat")
    print("Элементы с именем smile-cat:",len(elements_by_name))
    print("-----------------------------")

    print("тестирование по тегам")
    # Элементы с тегом h1 (заголовки)
    elements_by_tag = browser.find_elements(By.TAG_NAME,"h1")
    print("Элементы с тегом h1:", len(elements_by_tag))
    print("-----------------------------")

    print("тестирование по CSS-селекторам")
    # Элементы с data-type="trees"
    elements_by_selector = browser.find_elements(By.CSS_SELECTOR, '#smile')
    print("Элементы  с #smile:",len(elements_by_selector))
    print("-----------------------------")

    print("тестирование по XPath-пути")
    elements_by_xpath = browser.find_element(By.XPATH, '//*[@id="smile"]')
    print("Имя тега элемента  по XPath-пути:", elements_by_xpath.tag_name)
    print("-----------------------------")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
