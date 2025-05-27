from constants import RTC
from pages.rtc_register_page import RegisterMainPage
import pytest
import time


@pytest.mark.parametrize("email",
 ["joe.doe@1secmail.com", "joe.doe@mail.com", "JOE.DOE@MAIL.COM",
  "joe1.doe@mail.com", "joe-doe@mail.com", "joe.doe@1-mail.com",
  "joe_doe@mail.com", "joe.doe@1_mail.com", "joe.doe@mail.com"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_KEY_WEB])
def test_register_email_valid(web_browser, email, product):
    """ Make sure that email field checker works correctly
    with valid data. """

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_email_phone.send_keys(email)
    page.register_button.click()

    # Make sure that error is presented
    assert not page.error_email_phone.is_presented()


@pytest.mark.parametrize("email",
                         ["",
                          "email.domain.com",
                          "@domain.com",
                          "#@%^%#$@#$@#.com",
                          "joe smith <email@domain.com>",
                          "email@domain.com (joe smith)",
                          "email@domain@domain.com",
                          ".email@domain.com",
                          "email.@domain.com",
                          "email..email@domain.com",
                          "あいうえお@domain.com",
                          "email@-domain.com",
                          "email@.domain.com",
                          "email@111.222.333.44444",
                          "email@domain..com"],
                         ids=["Empty",
                              "Missing @",
                              "Missing address",
                              "Garbage",
                              "Copy/paste from address book with name",
                              "Superfluous text",
                              "Two @",
                              "Leading dot in address",
                              "Trailing dot in address",
                              "Multiple dots",
                              "Unicode chars in address",
                              "Leading dash in domain",
                              "Leading dot in domain",
                              "Invalid IP format",
                              "Multiple dots in the domain"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_KEY_WEB])
def test_register_email_invalid(web_browser, email, product):
    """ Make sure that email field checker works correctly
    with invalid data."""

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_email_phone.send_keys(email)
    page.register_button.click()

    # Make sure that error is presented
    assert page.error_email_phone.is_presented()

