import pytest
import allure
import uuid
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchDriverException

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def chrome_options():
    """Настройка опций Chrome браузера."""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--log-level=DEBUG')
    return options


@pytest.fixture(scope="session")
def browser(chrome_options):
    #Инициализация и настройка браузера с обработкой ошибок.

    driver = None
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()  # Максимизируем окно браузера
        yield driver
    except Exception as e:
        pytest.fail(f"Ошибка инициализации браузера: {str(e)}")
    finally:
        if driver is not None:
            driver.quit()


@pytest.fixture
def web_browser(browser, request):
    """Фикстура браузера с дополнительными функциями для тестов."""
    browser.set_window_position(-7, -3)
    yield browser

    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        try:
            os.makedirs('screenshots', exist_ok=True)
            screenshot_path = f'screenshots/{str(uuid.uuid4())}.png'
            browser.save_screenshot(screenshot_path)

            allure.attach(
                browser.get_screenshot_as_png(),
                name=request.node.name,
                attachment_type=allure.attachment_type.PNG
            )

            logger.info(f'URL в момент ошибки: {browser.current_url}')
            logger.info('Консольные логи браузера:')
            for log in browser.get_log('browser'):
                logger.info(log)
        except Exception as e:
            logger.error(f'Не удалось сохранить скриншот и логи: {str(e)}')


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Хук для обработки результатов тестов."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    return rep


def get_test_case_docstring(item):
    """Форматирование docstring для читаемых отчётов."""
    if not item._obj.__doc__:
        return item._nodeid

    name = str(item._obj.__doc__.split('.')[0]).strip()
    full_name = ' '.join(name.split())

    if hasattr(item, 'callspec'):
        params = item.callspec.params
        res = [f'{k}="{v}"' for k, v in params.items()]
        full_name += ' | Parameters: ' + ', '.join(res)

    return full_name


def pytest_itemcollected(item):
    """Хук для модификации отображаемых имён тестов."""
    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """Обработка --collect-only режима."""
    if session.config.option.collectonly:
        for item in session.items:
            if item._obj.__doc__:
                print(get_test_case_docstring(item))
        pytest.exit('Collection completed.')