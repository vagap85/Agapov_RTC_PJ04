from constants import RTC
from pages.rtc_register_page import RegisterMainPage
import pytest
import time


@pytest.mark.parametrize("phone",
  ["+7 (999) 123 45 67", "+7 (999) 123-4567", "+7 (999) 123-45-67",
   "+7 999-123-45-67", "+7 999 123 45 67", "+79091234567",
   "79091234567", "8 999 1234567", "8 (999) 1234567", "8 999 123-45-67",
   "9091234567"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_form_phone_valid(web_browser, phone, product):
    """ Make sure that phone field checker works correctly with valid data. """

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_email_phone.send_keys(phone)
    page.register_button.click()

    # Make sure that error is presented
    assert not page.error_email_phone.is_presented()


@pytest.mark.parametrize("phone", ["", "1", "+7 1", "81", "8 1", "8", "7",
  "8123456789", "812345678901", "712345678901", "+712345678901",
  "+7 123 456-78-901", "812345678901", "123 456-78-901"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_form_phone_invalid(web_browser, phone, product):
    """ Make sure that phone field checker works correctly with invalid data."""

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_email_phone.send_keys(phone)
    page.register_button.click()

    # Make sure that error is presented
    assert page.error_email_phone.is_presented()

