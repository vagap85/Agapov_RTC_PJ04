from constants import RTC
from pages.rtc_register_page import RegisterMainPage
import pytest
import time


@pytest.mark.parametrize("name",
 ["Аб", "Лсзвлмузхмтшййаяфэазыущцфосъшр"],
  ids=["Two cyrillics", "30 cyrillics"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_name_valid(web_browser, name, product):
    """ Make sure that name field checker works correctly with valid data. """

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_name.send_keys(name)
    page.register_button.click()

    # Make sure that error is presented
    assert len(page.errors_names.get_text()) <= 1


@pytest.mark.parametrize("name",
 ["а", "ёкбььуеэыгтддцдкечйчхъицекыанъщ", "", " ", "-", "--", "gYsQZn",
  "龍門大酒家", "صسغذئآ", "0123456789",],
  ids=["One cyrillic", "31 cyrillics", "Empty", "One space", "Hyphen",
       "Two hyphens", "Group of Latin", "Group of Chinese", "Group of Arabic",
       "Group of numbers"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_name_invalid(web_browser, name, product):
    """ Make sure that name field checker works correctly with invalid data."""

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_name.send_keys(name)
    page.register_button.click()

    # Make sure that error is presented
    assert len(page.errors_names.get_text()) > 0

@pytest.mark.parametrize("lastname",
 ["Аб", "Лсзвлмузхмтшййаяфэазыущцфосъшр"],
  ids=["Two cyrillics", "30 cyrillics"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_lastname_valid(web_browser, lastname, product):
    """ Make sure that lastname field checker works correctly
    with valid data. """

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_lastname.send_keys(lastname)
    page.register_button.click()

    # Make sure that error is presented
    assert len(page.errors_names.get_text()) <= 1


@pytest.mark.parametrize("lastname",
 ["а", "ёкбььуеэыгтддцдкечйчхъицекыанъщ", "", " ", "-", "--", "gYsQZn",
  "龍門大酒家", "صسغذئآ", "0123456789",],
  ids=["One cyrillic", "31 cyrillics", "Empty", "One space", "Hyphen",
       "Two hyphens", "Group of Latin", "Group of Chinese", "Group of Arabic",
       "Group of numbers"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_lastname_invalid(web_browser, lastname, product):
    """ Make sure that lastname field checker works correctly
    with invalid data."""

    # Go to site
    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    #Go to Register form
    page.by_pass_button.click()
    page.register_link.click()

    # Input data
    page.input_field_lastname.send_keys(lastname)
    page.register_button.click()

    # Make sure that error is presented
    assert len(page.errors_names.get_text()) > 0