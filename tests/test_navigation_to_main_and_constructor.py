from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import TestLocators as TL

class TestNavigationToMainPage:
    def test_successful_navigation_to_main_page_via_constructor(self, browser,exist_user):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.PERSONAL_ACC).click()
        user_email = exist_user.get("email")
        user_password = exist_user.get("password")
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
        browser.find_element(*TL.ENTER_BUTTON).click()
        browser.find_element(*TL.PERSONAL_ACC).click()
        WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.LOGOUT_BUTTON))
        browser.find_element(*TL.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.PERSONAL_ACC))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'
    def test_successful_navigation_to_main_page_via_logo(self, browser,exist_user):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.PERSONAL_ACC).click()
        user_email = exist_user.get("email")
        user_password = exist_user.get("password")
        browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
        browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
        browser.find_element(*TL.ENTER_BUTTON).click()
        browser.find_element(*TL.PERSONAL_ACC).click()
        WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.LOGOUT_BUTTON))
        browser.find_element(*TL.LOGO).click()
        WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.PERSONAL_ACC))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'

class TestNavigationBetweenConstructorParts:
    def test_navigation_to_constructor_sauces(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.SAUCES).click()
        element = WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.SAUCE))
        assert element.text == "Соус Spicy-X"
    def test_navigation_to_constructor_toppings(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.TOPPINGS).click()
        element = WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.TOPPING))
        assert element.text == "Говяжий метеорит (отбивная)"
    def test_navigation_to_constructor_buns(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*TL.TOPPINGS).click()
        browser.find_element(*TL.BUNS).click()
        element = WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.BUN))
        assert element.text == "Флюоресцентная булка R2-D3"

class TestNavigationToPersonalAccount:
     def test_successful_navigation_to_personal_acc(self, browser, exist_user):
         browser.get("https://stellarburgers.nomoreparties.site/")
         browser.find_element(*TL.PERSONAL_ACC).click()
         user_email = exist_user.get("email")
         user_password = exist_user.get("password")
         browser.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
         browser.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
         browser.find_element(*TL.ENTER_BUTTON).click()
         browser.find_element(*TL.PERSONAL_ACC).click()
         WebDriverWait(browser, 15).until(EC.visibility_of_element_located(TL.LOGOUT_BUTTON))
         assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
