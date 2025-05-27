import os
from constants import RTC
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class RegisterMainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL")  or RTC.URL_ELK_WEB

        super().__init__(web_driver, url)

    # Кнопка Войти
    by_pass_button = WebElement(id="standard_auth_btn")

    # Кнопка Ключ
    key_form_enter_button = WebElement(css_selector="a.go_kab")

    #Зарегистрироваться
    register_link = WebElement(id="kc-register")

    # Название Регистрация
    title_register_name = \
        WebElement(css_selector="h1.card-container__title")

    # Личные данные
    personal_data = WebElement(xpath="//p[contains(text(),'Личные данные')]")

    # кнопка "Зарегестрироваться"
    register_button = WebElement(xpath='//button[@name="register"]')

    # ввод Имени
    input_field_name = WebElement(xpath='//input[@name="firstName"]')

    # Ошибка ввода имени(login)
    errors_names = ManyWebElements(xpath="//span[contains(text(), "
                                         "'Необходимо заполнить поле')]")
    error_name = WebElement(xpath="//span[contains(text(), "
                                  "'Необходимо заполнить поле')]")

    # Ввод фамилии
    input_field_lastname = WebElement(xpath='//input[@name="lastName"]')

    # Ввод E-mail и телефон
    input_field_email_phone = WebElement(id="address")

    # ошибка email/телефон
    error_email_phone = \
        WebElement(css_selector="div.email-phone-con "
                                "span.rt-input-container__meta--error")

    # Поле ввода пароля
    input_field_password = WebElement(id="password")

    # Поле ввода поддтвердить пароль
    input_field_confirm_pass = WebElement(id="password-confirm")

    # ошибка нового пароля
    passw_err_mess = \
        WebElement(css_selector=
                   'div.new-password-container__password span.rt-input-container__meta--error')

    # ошибка поддтверждение пароля
    confirm_passw_err_mess = \
        WebElement(css_selector=
                   'div.new-password-container__confirmed-password span.rt-input-container__meta--error')