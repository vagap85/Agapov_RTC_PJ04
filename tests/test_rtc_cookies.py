import sys
import os
import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from constants import RTC
from pages.rtc_signin_page import SigninMainPage


@pytest.fixture(scope="session")
def web_browser(browser, request):
    """Фикстура браузера с областью видимости session"""
    yield browser


@pytest.fixture(scope="session")
def auth_cookies(web_browser):
    """Фикстура для получения cookies один раз для всех тестов"""
    try:
        page = SigninMainPage(web_browser)
        web_browser.get(RTC.URL_ELK_WEB)

        # Очищаем cookies перед началом
        web_browser.delete_all_cookies()

        # Ожидание загрузки
        WebDriverWait(web_browser, 30).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        # Попытка клика по кнопке входа
        try:
            WebDriverWait(web_browser, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='standard_auth_btn']"))
            ).click()
        except TimeoutException:
            pass

        WebDriverWait(web_browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]'))
        ).click()

        # Заполнение формы
        WebDriverWait(web_browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))
        ).send_keys(RTC.VALID_EMAIL)

        web_browser.find_element(By.XPATH, "//input[@id='password']").send_keys(RTC.VALID_PASSWORD)
        web_browser.find_element(By.XPATH, "//button[contains(@id, 'kc-login')]").click()

        # Проверка успешной авторизации
        WebDriverWait(web_browser, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'app-header_profile')]"))
        )

        current_url = web_browser.current_url
        assert "lk.rt.ru" in current_url, "Авторизация не прошла успешно"

        # Получение cookies
        cookies = web_browser.get_cookies()
        assert cookies, "Не получено ни одной cookie после авторизации"

        # Сохраняем cookies в файл rts_cookies.txt
        with open("rts_cookies.txt", "w", encoding="utf-8") as f:
            f.write("=== Cookies ===\n")
            for cookie in cookies:
                f.write(f"Name: {cookie['name']}\n")
                f.write(f"Value: {cookie['value']}\n")
                f.write(f"Domain: {cookie.get('domain', 'N/A')}\n")
                f.write(f"Path: {cookie.get('path', 'N/A')}\n")
                f.write(f"Expires: {cookie.get('expiry', 'Session cookie')}\n")
                f.write(f"Secure: {cookie.get('secure', False)}\n")
                f.write(f"HttpOnly: {cookie.get('httpOnly', False)}\n")
                f.write("----------------\n")

        return cookies

    except Exception as e:
        web_browser.save_screenshot("auth_error.png")
        pytest.fail(f"Ошибка получения cookies: {str(e)}")


def test_cookie_auth(web_browser, auth_cookies):
    """Тест авторизации через cookies"""
    try:
        web_browser.get(RTC.URL_ELK_WEB)

        # Очищаем все cookies перед добавлением новых
        web_browser.delete_all_cookies()

        # Добавление cookies
        for cookie in auth_cookies:
            # Удаляем поле 'domain' если оно есть, чтобы браузер сам определил домен
            if 'domain' in cookie:
                del cookie['domain']

            try:
                web_browser.add_cookie(cookie)
            except Exception as e:
                print(f"Warning: Не удалось добавить cookie {cookie.get('name')}: {str(e)}")
                continue

        # Обновляем страницу и проверяем авторизацию
        web_browser.refresh()

        WebDriverWait(web_browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'app-header_profile')]"))
        )

        # Дополнительная проверка - попытка перехода в личный кабинет
        profile_element = WebDriverWait(web_browser, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'app-header_profile')]"))
        )
        profile_element.click()

        # Проверяем, что мы на странице профиля
        WebDriverWait(web_browser, 20).until(
            EC.url_contains("lk.rt.ru")
        )

    except Exception as e:
        web_browser.save_screenshot("cookie_auth_error.png")
        pytest.fail(f"Ошибка авторизации по cookies: {str(e)}")