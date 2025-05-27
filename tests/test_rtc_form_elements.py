from constants import RTC
from pages.rtc_register_page import RegisterMainPage
from pages.rtc_recovery_form_page import RecoveryMainPage
from pages.rtc_auth_code_page import GetCodeMainPage
from pages.rtc_signin_page import SigninMainPage
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging




# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




def wait_for_element(driver, locator, timeout=15):
   #Ожидание появления элемента
   try:
       return WebDriverWait(driver, timeout).until(
           EC.visibility_of_element_located(locator)
       )
   except TimeoutException as e:
       logger.error(f"Элемент не найден: {locator}")
       raise




@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_START_WEB,
                                    RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_form_elements(web_browser, product):
   #Тест элементов формы регистрации
   try:
       logger.info(f"Starting registration test for {product}")


       page = RegisterMainPage(web_browser, product)


       if product == RTC.URL_KEY_WEB:
           assert page.key_form_enter_button.is_presented(), "Кнопка входа не найдена"
           page.key_form_enter_button.click()


       assert page.by_pass_button.is_presented(), "Кнопка 'Войти' не найдена"
       page.by_pass_button.click()


       assert page.register_link.is_presented(), "Ссылка на регистрацию не найдена"
       page.register_link.click()


       # Проверка элементов формы регистрации
       assert page.title_register_name.is_presented(), "Заголовок формы не найден"
       assert page.title_register_name.get_text() == RTC.REGISTRATION_TEXT, "Неверный текст заголовка"
       assert page.personal_data.is_presented(), "Ссылка на политику не найдена"
       assert page.register_button.is_presented(), "Кнопка регистрации не найдена"
       assert page.register_button.get_text() == RTC.REGISTER_BUTTON_TEXT, "Неверный текст кнопки"


   except Exception as e:
       web_browser.save_screenshot('register_error.png')
       logger.error(f"Ошибка в тесте регистрации: {str(e)}")
       pytest.fail(f"Тест регистрации не пройден: {str(e)}")




@pytest.mark.parametrize("product", [
   RTC.URL_ELK_WEB,
   RTC.URL_START_WEB,
   RTC.URL_SMARTHOME_WEB,
   RTC.URL_KEY_WEB,
   pytest.param(RTC.URL_ONLIME_WEB, marks=pytest.mark.xfail(reason="Особая структура страницы"))
])
def test_recovery_form_elements(web_browser, product):
   #Тест формы восстановления пароля
   try:
       logger.info(f"Starting recovery test for {product}")


       page = RecoveryMainPage(web_browser, product)


       if product == RTC.URL_KEY_WEB:
           page.key_form_enter_button.click()


       page.by_pass_button.click()
       page.forgot_password.click()


       # Проверка элементов формы восстановления
       assert page.title_top.is_presented(), "Заголовок не найден"
       assert page.title_top.get_text() == RTC.RECOVERY_INSCRIPTION_TEXT, "Неверный текст заголовка"
       assert page.captcha_img.is_presented(), "Капча не отображена"
       assert page.captcha_symbols_input_field.is_presented(), "Поле ввода капчи не найдено"


   except Exception as e:
       web_browser.save_screenshot('recovery_error.png')
       logger.error(f"Ошибка в тесте восстановления: {str(e)}")
       pytest.fail(f"Тест восстановления не пройден: {str(e)}")




@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_ONLIME_WEB,
                                    RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB,
                                    RTC.URL_KEY_WEB])
def test_auth_code_form_elements(web_browser, product):
  #Тест формы авторизации по коду
   try:
       logger.info(f"Starting auth by code test for {product}")


       page = GetCodeMainPage(web_browser, product)


       if product == RTC.URL_KEY_WEB:
           page.key_form_enter_button.click()


       # Проверка элементов формы
       assert page.title_top.is_presented(), "Заголовок не найден"
       expected_text = RTC.AUTH_BY_CODE_TEXTS.get(product, "Получить код")
       assert page.title_top.get_text() ==expected_text
       assert page.get_code_button.is_presented(), "Кнопка получения кода не найдена"
       assert page.get_code_button.get_text() == RTC.AUTH_GET_CODE, "Неверный текст кнопки"
       assert page.enter_by_pass.is_presented(), "Ссылка на вход по паролю не найдена"


   except Exception as e:
       web_browser.save_screenshot('auth_code_error.png')
       logger.error(f"Ошибка в тесте авторизации по коду: {str(e)}")
       pytest.fail(f"Тест авторизации по коду не пройден: {str(e)}")




@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_ONLIME_WEB,
                                    RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB,
                                    RTC.URL_KEY_WEB])
def test_auth_pass_form_elements(web_browser, product):
   """Тест формы авторизации по паролю"""
   try:
       logger.info(f"Starting auth by password test for {product}")


       page = SigninMainPage(web_browser, product)


       if product == RTC.URL_KEY_WEB:
           page.key_form_enter_button.click()


       page.by_pass_button.click()


       # Проверка элементов формы
       assert page.title_top.is_presented(), "Заголовок не найден"
       assert page.title_top.get_text() == RTC.AUTH_BY_PASS_TEXT, "Неверный текст заголовка"
       assert page.enter_button.is_presented(), "Кнопка входа не найдена"
       assert page.enter_button.get_text() == RTC.ENTER_TEXT, "Неверный текст кнопки"
       assert page.enter_by_temp_code_button.is_presented(), "Ссылка на вход по коду не найдена"


   except Exception as e:
       web_browser.save_screenshot('auth_pass_error.png')
       logger.error(f"Ошибка в тесте авторизации по паролю: {str(e)}")
       pytest.fail(f"Тест авторизации по паролю не пройден: {str(e)}")

