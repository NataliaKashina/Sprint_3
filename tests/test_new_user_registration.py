from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import TestLocators as TL

def test_successful_registration_with_correct_creds(credentials):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке Войти в аккаунт
    driver.find_element(*TL.LOGIN_BUTTON).click()
    # Переходим по кнопке Зарегистрироваться
    driver.find_element(*TL.REGISTRATION_LINK).click()
    # Регистрация
    user_email = credentials.get("email")
    user_name = credentials.get("name")
    user_password = credentials.get("password")
    driver.find_element(*TL.NAME_FIELD).send_keys(user_name)
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
    driver.find_element(*TL.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TL.ENTER_BUTTON))
    # Авторизация
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
    driver.find_element(*TL.ENTER_BUTTON).click()
    assert driver.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    driver.quit()

def test_unsuccessful_registration_with_short_password(credentials):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке Войти в аккаунт
    driver.find_element(*TL.LOGIN_BUTTON).click()
    driver.find_element(*TL.REGISTRATION_LINK).click()
    # Регистрация с коротким паролем
    user_email = credentials.get("email")
    user_name = credentials.get("name")
    driver.find_element(*TL.NAME_FIELD).send_keys(user_name)
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys("short")
    driver.find_element(*TL.REGISTRATION_BUTTON).click()
    assert driver.find_element(*TL.WRONG_PASS).text == 'Некорректный пароль'
    driver.quit()

def test_unsuccessful_registration_with_empty_password(credentials):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке Войти в аккаунт
    driver.find_element(*TL.LOGIN_BUTTON).click()
    driver.find_element(*TL.REGISTRATION_LINK).click()
    # Регистрация с пустым паролем
    user_email = credentials.get("email")
    user_name = credentials.get("name")
    driver.find_element(*TL.NAME_FIELD).send_keys(user_name)
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys("")
    driver.find_element(*TL.REGISTRATION_BUTTON).click()
    # На сайте нет валидационного месаджа, поэтому проверям что не перешли на страницу авторизации
    assert driver.current_url != 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()