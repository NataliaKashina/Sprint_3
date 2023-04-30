from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import TestLocators as TL

class TestDifferentWaysToLogin:
    def test_successful_login_via_login_button(self, browser, exist_user):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.LOGIN_BUTTON).click()
        user_email = exist_user.get("email")
        user_password = exist_user.get("password")
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
        browser.find_element(*TL.ENTER_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(TL.PLACE_ORDER))
        assert browser.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    def test_successful_login_via_personal_acc_button(self, browser, exist_user):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.PERSONAL_ACC).click()
        user_email = exist_user.get("email")
        user_password = exist_user.get("password")
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
        browser.find_element(*TL.ENTER_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(TL.PLACE_ORDER))
        assert browser.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    def test_successful_login_from_registration_page(self, browser, exist_user):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.LOGIN_BUTTON).click()
        browser.find_element(*TL.REGISTRATION_LINK).click()
        browser.find_element(*TL.LOGIN_FROM_REGISTRATION).click()
        user_email = exist_user.get("email")
        user_password = exist_user.get("password")
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
        browser.find_element(*TL.ENTER_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(TL.PLACE_ORDER))
        assert browser.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    def test_successful_login_via_recover_pass(self, browser, exist_user):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.PERSONAL_ACC).click()
        browser.find_element(*TL.RESTORE_PASS).click()
        browser.find_element(*TL.LOGIN_FROM_REGISTRATION).click()
        user_email = exist_user.get("email")
        user_password = exist_user.get("password")
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
        browser.find_element(*TL.ENTER_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(TL.PLACE_ORDER))
        assert browser.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"

class TestLogout:
    def test_successful_logout(self, browser, credentials):
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
        browser.find_element(*TL.PERSONAL_ACC).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(TL.LOGOUT_BUTTON))
        browser.find_element(*TL.LOGOUT_BUTTON).click()
        WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.ENTER_BUTTON))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'