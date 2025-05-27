import os, pickle
from constants import RTC
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class SigninMainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL")  or RTC.URL_ELK_WEB

        super().__init__(web_driver, url)

    # Sign-in by password button
    by_pass_button = WebElement(id="standard_auth_btn")

    # Title top
    title_top = WebElement(css_selector="h1.card-container__title")

    # Sign-in by temporary code
    temp_code = WebElement(id="back_to_otp_btn")

    # Username filed
    username_field = WebElement(id="username")

    # Password field
    password_field = WebElement(id="password")

    # Show password by clicking glass
    show_pass_glass = \
        WebElement(css_selector="div.rt-input__action svg.rt-base-icon")

    # Checkbox remember me
    check_box_remember_me = WebElement(css_selector='span.rt-checkbox__shape')

    # Forgot password
    forgot_password = WebElement(id="forgot_password")

    # Enter button
    enter_button = WebElement(id="kc-login")

    #
    enter_by_temp_code_button = WebElement(id="back_to_otp_btn")

    # User agreement
    user_agreement = WebElement(css_selector="div.auth-policy .rt-link")

    # Personal cabinet name
    personal_cabinet_username_link = WebElement(css_selector="h2.sc-bvFjSx")

    #  Personal cabinet tab after sign in
    personal_cabinet = WebElement(xpath="//div[contains(text(),'Личный кабинет')]")

    # Personal cabinet exit button
    personal_cabinet_exit_button = \
        WebElement(xpath="//span[contains(text(),'Выйти')]")

    # Enter button for Key Web form $x('//a[@class="go_kab"]')
    key_form_enter_button = WebElement(css_selector="a.go_kab")

    # We are inside - slogan Rostelecom KEY
    rostelecom_slogan_key = WebElement(css_selector='div.slogan--70NR0')

    # Change account link after the Key Web enterance (Exit)
    exit_Key_Web = \
        WebElement(xpath="//span[contains(text(),'Сменить учётную запись')]")

    # Error notification of invalid data: email/login/phone/personal account
    error_notification = WebElement(xpath="//span[@id='form-error-message']")

    # Personal cabinet Onlime Web
    personal_cabinet_onlime = WebElement(xpath="//a[contains(text(),'Перейти')]")

    # Personal cabinet SmartHome Web
    personal_cabinet_smarthome = WebElement(id="submit_button")

    # Authorisation fail
    auth_error_message = WebElement(id="form-error-message")


