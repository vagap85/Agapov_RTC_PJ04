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

    # Sign-in by password button
    by_pass_button = WebElement(id="standard_auth_btn")

    # Enter button for Key Web form $x('//a[@class="go_kab"]')
    key_form_enter_button = WebElement(css_selector="a.go_kab")

    # Forgot password
    forgot_password = WebElement(id="forgot_password")

    # Title top
    title_top = WebElement(css_selector="h1.card-container__title")

    # Teb personal account
    tab_personal_account = WebElement(id="t-btn-tab-ls")

    # Captha image
    captcha_img = WebElement(css_selector='img[alt="Captcha"]')

    # Input field captcha inner text
    captcha_symbols_input_field = \
        WebElement(css_selector="div.rt-captcha__input span.rt-input__placeholder")

    # Continue button
    continue_button = WebElement(xpath="//button[@id='reset']")

    # Go back button
    go_back_button = WebElement(xpath="//button[@id='reset-back']")












