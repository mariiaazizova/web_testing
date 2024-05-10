import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from selenium.webdriver import Chrome
#создания фикстуры, предоставляющей экземпляр браузера перед каждым тестом
@pytest.fixture
def browser():
    driver = Chrome()
    #установка неявного ожидания
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_basic_duckduckgo_search(browser):
    # Настройте данные для тест-кейса
    PHRASE = 'panda'

    # Поиск фразы
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Проверка, что результаты появились
    result_page = DuckDuckGoResultPage(browser)

    #проверяет,что количество результатов поиска больше 0
    assert result_page.search_results_count() > 0

    #проверяет, что количество ссылок, содержащих поисковой запрос (фразу),
    # в результатах поиска больше 0
    assert result_page.phrase_result_count(PHRASE) > 0

    #проверяется, что значение в поисковой строке совпадает с
    # пользовательским запросом (фразой).
    assert result_page.search_input_value() == PHRASE