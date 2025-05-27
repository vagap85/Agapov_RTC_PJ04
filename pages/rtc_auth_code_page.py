import os, pickle
from constants import RTC
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class GetCodeMainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL")  or RTC.URL_ELK_WEB

        super().__init__(web_driver, url)

    # Title top
    title_top = WebElement(css_selector="h1.card-container__title")

    # Get code button
    get_code_button = WebElement(id="otp_get_code")

    # Input field
    input_field = WebElement(id="address")

    # Enter by pass button
    enter_by_pass = WebElement(id="standard_auth_btn")

    # Enter button for Key Web form $x('//a[@class="go_kab"]')
    key_form_enter_button = WebElement(css_selector="a.go_kab")













