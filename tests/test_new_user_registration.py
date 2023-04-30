from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import TestLocators as TL
class TestRegistration:
    def test_successful_registration_with_correct_creds(self, browser, credentials):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.LOGIN_BUTTON).click()
        browser.find_element(*TL.REGISTRATION_LINK).click()
        user_email = credentials.get("email")
        user_name = credentials.get("name")
        user_password = credentials.get("password")
        browser.find_element(*TL.NAME_FIELD).send_keys(user_name)
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
        browser.find_element(*TL.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(TL.ENTER_BUTTON))
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
        browser.find_element(*TL.ENTER_BUTTON).click()
        assert browser.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    def test_unsuccessful_registration_with_short_password(self, browser, credentials):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.LOGIN_BUTTON).click()
        browser.find_element(*TL.REGISTRATION_LINK).click()
        user_email = credentials.get("email")
        user_name = credentials.get("name")
        browser.find_element(*TL.NAME_FIELD).send_keys(user_name)
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys("short")
        browser.find_element(*TL.REGISTRATION_BUTTON).click()
        assert browser.find_element(*TL.WRONG_PASS).text == 'Некорректный пароль'
    def test_unsuccessful_registration_with_empty_password(self, browser, credentials):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.LOGIN_BUTTON).click()
        browser.find_element(*TL.REGISTRATION_LINK).click()
        user_email = credentials.get("email")
        user_name = credentials.get("name")
        browser.find_element(*TL.NAME_FIELD).send_keys(user_name)
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys("")
        browser.find_element(*TL.REGISTRATION_BUTTON).click()
        assert browser.current_url != 'https://stellarburgers.nomoreparties.site/login'