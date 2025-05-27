import os, pickle
from constants import RTC
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class RecoveryMainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL")  or RTC.URL_ELK_WEB

        super().__init__(web_driver, url)

    # Кнопка войти
    by_pass_button = WebElement(id="standard_auth_btn")

    # Кнопка перехода в Ключ
    key_form_enter_button = WebElement(css_selector="a.go_kab")

    # Забыл пароль
    forgot_password = WebElement(id="forgot_password")

    # Название
    title_top = WebElement(css_selector="h1.card-container__title")

    # Войти в ЛК
    tab_personal_account = WebElement(id="t-btn-tab-ls")

    # Captha
    captcha_img = WebElement(css_selector='img[alt="Captcha"]')

    # Неверный ввод captcha
    captcha_symbols_input_field = \
        WebElement(css_selector="div.rt-captcha__input span.rt-input__placeholder")

    # Кнопка назад
    continue_button = WebElement(xpath="//button[@id='reset']")

    # Кнопка "Вернуться назад"
    go_back_button = WebElement(xpath="//button[@id='reset-back']")












