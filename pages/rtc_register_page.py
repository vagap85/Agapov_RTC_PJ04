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

    # Sign-in by password button
    by_pass_button = WebElement(id="standard_auth_btn")

    # Enter button for Key Web form $x('//a[@class="go_kab"]')
    key_form_enter_button = WebElement(css_selector="a.go_kab")

    # Registration link
    register_link = WebElement(id="kc-register")

    # Title name Registration
    title_register_name = \
        WebElement(css_selector="h1.card-container__title")

    # Inscription personal data
    personal_data = WebElement(xpath="//p[contains(text(),'Личные данные')]")

    # Register button
    register_button = WebElement(xpath='//button[@name="register"]')

    # Input field Name
    input_field_name = WebElement(xpath='//input[@name="firstName"]')

    # Error name notification
    errors_names = ManyWebElements(xpath="//span[contains(text(), "
                                         "'Необходимо заполнить поле')]")
    error_name = WebElement(xpath="//span[contains(text(), "
                                  "'Необходимо заполнить поле')]")

    # Input field Surname
    input_field_lastname = WebElement(xpath='//input[@name="lastName"]')

    # Input field E-mail or Phone
    input_field_email_phone = WebElement(id="address")

    # Error email/phone message
    error_email_phone = \
        WebElement(css_selector="div.email-or-phone "
                                "span.rt-input-container__meta")

    # Input field Password
    input_field_password = WebElement(id="password")

    # Input field Confirm Password
    input_field_confirm_pass = WebElement(id="password-confirm")

    # Error message new passw
    passw_err_mess = \
        WebElement(css_selector=
                   'div.new-password-container__password span.rt-input-container__meta--error')

    # Error message confirm passw
    confirm_passw_err_mess = \
        WebElement(css_selector=
                   'div.new-password-container__confirmed-password span.rt-input-container__meta--error')









