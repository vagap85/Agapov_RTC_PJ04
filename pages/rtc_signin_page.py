import os, pickle

from selenium.webdriver.common.by import By
from constants import RTC
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class SigninMainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL")  or RTC.URL_ELK_WEB

        super().__init__(web_driver, url)

        # Войти по паролю
    by_pass_button = WebElement(id="standard_auth_btn")
    # Title top
    title_top = WebElement(css_selector="h1.card-container__title")

    # Войти по временному коду
    temp_code = WebElement(id="back_to_otp_btn")

    # Поле логин
    username_field = WebElement(id='username')

    # Поле пароль
    password_field = WebElement(id="password")

    # Показать скрытый пароль
    show_pass_glass = \
        WebElement(css_selector="div.rt-input__action svg.rt-base-icon")

    # Чек-бокс "Запомнить меня"
    check_box_remember_me = WebElement(css_selector='span.rt-checkbox__shape')

    # Забыл пароль
    forgot_password = WebElement(id="forgot_password")

    # Нажать кнопку "Войти"
    enter_button = WebElement(id="kc-login")

    #По временному коду
    enter_by_temp_code_button = WebElement(id="back_to_otp_btn")

    # Пользовательское соглашение
    user_agreement = WebElement(css_selector="div.auth-policy .rt-link")

    #  Личный кабинет
    personal_cabinet = WebElement(css_selector="div.app-header_profile_header_chevron-wrapper")

    # Выход из ЛК
    personal_cabinet_exit_button = \
        WebElement(xpath="//div[contains(text(),'Выйти из аккаунта')]")

    # Enter button for Key Web form
    key_form_enter_button = WebElement(css_selector="a.go_kab")

    # We are inside - slogan Rostelecom KEY
    rostelecom_slogan_key = WebElement(xpath="a[@class='go_mobile_kabinet']")

    # Сменить учётную запись
    exit_Key_Web = \
        WebElement(xpath="//span[contains(text(),'Сменить учётную запись')]")

    # Ошибка поля телефон/email
    error_email_phone = WebElement(
        locator=(By.XPATH,
                 "//div[contains(@class, 'email-phone-con')]//span[contains(@class, 'rt-input-container__meta--error')]"),
        description="Сообщение об ошибке email/телефона"
    )


    # Personal cabinet Online Web
    personal_cabinet_online = WebElement(xpath="//a[contains(text(),'Перейти')]")

    # Personal cabinet SmartHome Web
    personal_cabinet_smarthome = WebElement(id="submit_button")

    # Ошибка авторизации
    auth_error_message = WebElement(id="form-error-message")

    # Неверный пароль
    passw_err_mess = \
        WebElement(css_selector=
                   'div.new-password-container__password span.rt-input-container__meta--error')

    # Ошибка "Подтвердите пароль"
    confirm_passw_err_mess = \
        WebElement(css_selector=
                   'div.new-password-container__confirmed-password span.rt-input-container__meta--error')


