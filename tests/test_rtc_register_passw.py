from constants import RTC
from pages.rtc_register_page import RegisterMainPage
import pytest
import time


@pytest.mark.parametrize("password",
  [RTC.VALID_PASSWORD_8, RTC.VALID_PASSWORD_20],
  ids=["8 symbols", "20 symbols"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_password_valid(web_browser, password, product):
    """ Make sure that password field checker works correctly
        with valid data. """

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_password.send_keys(password)
    page.register_button.click()

    # Make sure that error is presented
    assert not page.passw_err_mess.is_presented()


@pytest.mark.parametrize("password",
  ["_=d;-Ab", "$b_.A|S!-=/-a+,A`S|?;", "", "gYsQZndd", "龍門大酒家", "صسغذئآ",
   "0123456789", "АбвЦуКепрррр", "_=d;- A#b", " ", "swrfkj84:", "_=d;- A#b"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_password_invalid(web_browser, password, product):
    """ Make sure that password field checker works correctly
        with invalid data."""

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_password.send_keys(password)
    page.register_button.click()

    # Make sure that error is presented
    assert page.passw_err_mess.is_presented()


@pytest.mark.parametrize("password",
  [RTC.VALID_PASSWORD_8, RTC.VALID_PASSWORD_20],
  ids=["8 symbols", "20 symbols",])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_confirmed_password_valid(web_browser, password, product):
    """ Make sure that confirmed password field checker works correctly
        with valid data. """

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_confirm_pass.send_keys(password)
    page.register_button.click()

    # Make sure that error is presented
    assert not page.confirm_passw_err_mess.is_presented()


@pytest.mark.parametrize("password",
  ["_=d;-Ab", "$b_.A|S!-=/-a+,A`S|?;", "", " ", "gYsQZndd", "龍門大酒家", "صسغذئآ",
   "0123456789", "АбвЦуКепрррр", "_=d;- A#b", "swrfkj84:", "_=d;- A#b"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_confirmed_password_invalid(web_browser, password, product):
    """ Make sure that confirmed password field checker works correctly
        with invalid data."""

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_confirm_pass.send_keys(password)
    page.register_button.click()

    # Make sure that error is presented
    assert page.confirm_passw_err_mess.is_presented()


@pytest.mark.parametrize("password",
  [RTC.VALID_PASSWORD_8, RTC.VALID_PASSWORD_20],
  ids=["8 symbols", "20 symbols",])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_both_passw_same(web_browser, password, product):
    """ Make sure that both passwords are the same. """

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_password.send_keys(password)
    page.input_field_confirm_pass.send_keys(password)
    page.register_button.click()

    # Make sure that error is presented
    assert not page.confirm_passw_err_mess.is_presented()


@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_both_passw_different(web_browser, product):
    """ Make sure that both passwords are the different. """

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_password.send_keys(RTC.VALID_PASSWORD_8)
    page.input_field_confirm_pass.send_keys(RTC.VALID_PASSWORD_20)
    page.register_button.click()

    # Make sure that error is presented
    assert page.confirm_passw_err_mess.is_presented()