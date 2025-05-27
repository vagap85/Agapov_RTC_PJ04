import pytest
from constants import RTC
from pages.rtc_signin_page import SigninMainPage
import pickle
import time


def test_write_cookies(web_browser):
    """ Test write cookies."""

    # Go to site
    page = SigninMainPage(web_browser, RTC.URL_ELK_WEB)
    page.by_pass_button.click()

    # Filling authorization form
    page.username_field = RTC.VALID_EMAIL
    page.password_field = RTC.VALID_PASSWORD

    # Try to log
    page.enter_button.click()
    time.sleep(10)

    get_cookies = web_browser.get_cookies()
    # Save cookies of the browser after the login
    with open(RTC.COOKIES_FILE, 'wb') as cookies:
        pickle.dump(get_cookies, cookies)

    page.personal_cabinet_username_link.click()
    page.personal_cabinet_exit_button.click()
    time.sleep(20)

    print(f"\n#################################################")
    print(f"'{get_cookies}'\n")
    page_new = SigninMainPage(web_browser, RTC.URL_ELK_WEB)
    for cookie in get_cookies:
        print(f"{cookie}")
        page_new._web_driver.add_cookie(cookie)

    page_new._web_driver.refresh()
    assert page_new.personal_cabinet.is_presented()



def test_sign_in_by_cookies(web_browser):
    """ Test sign-in by cookies."""

    # Go to site
    page = SigninMainPage(web_browser, RTC.URL_ELK_WEB)
    # time.sleep(5)

    with open(RTC.COOKIES_FILE, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)

    print(f"\n#################################################")
    print(f"\n'{cookies}'\n")

    for cookie in cookies:
        page._web_driver.add_cookie(cookie)
        # web_browser.add_cookie(cookie)

    page._web_driver.refresh()
    # web_browser.refresh()
    # time.sleep(10)

