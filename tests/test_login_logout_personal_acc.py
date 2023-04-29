from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import TestLocators as TL

def test_successful_login_via_login_button(exist_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке Войти в аккаунт
    driver.find_element(*TL.LOGIN_BUTTON).click()
    # Авторизация
    user_email = exist_user.get("email")
    user_password = exist_user.get("password")
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
    driver.find_element(*TL.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TL.PLACE_ORDER))
    assert driver.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    driver.quit()

def test_successful_login_via_personal_acc_button(exist_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке Личный Кабинет
    driver.find_element(*TL.PERSONAL_ACC).click()
    # Авторизация
    user_email = exist_user.get("email")
    user_password = exist_user.get("password")
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
    driver.find_element(*TL.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TL.PLACE_ORDER))
    assert driver.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    driver.quit()

def test_successful_login_from_registration_page(exist_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке "Войти в аккаунт"
    driver.find_element(*TL.LOGIN_BUTTON).click()
    # Переходим по кнопке  "Зарегистрироваться"
    driver.find_element(*TL.REGISTRATION_LINK).click()
    # Переходим по кнопке "Войти"
    driver.find_element(*TL.LOGIN_FROM_REGISTRATION).click()
    # Авторизация
    user_email = exist_user.get("email")
    user_password = exist_user.get("password")
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
    driver.find_element(*TL.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TL.PLACE_ORDER))
    assert driver.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    driver.quit()

def test_successful_login_via_recover_pass(exist_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке "Личный Кабинет"
    driver.find_element(*TL.PERSONAL_ACC).click()
    # Переходим по кнопке "Восстановить Пароль"
    driver.find_element(*TL.RESTORE_PASS).click()
    # Переходим по кнопке "Войти"
    driver.find_element(*TL.LOGIN_FROM_REGISTRATION).click()
    # Авторизация
    user_email = exist_user.get("email")
    user_password = exist_user.get("password")
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
    driver.find_element(*TL.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TL.PLACE_ORDER))
    assert driver.find_element(*TL.PLACE_ORDER) is not None, "кнопка Сделать заказ не найдена"
    driver.quit()

def test_successful_navigation_to_personal_acc(exist_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке Личный Кабинет
    driver.find_element(*TL.PERSONAL_ACC).click()
    # Авторизация
    user_email = exist_user.get("email")
    user_password = exist_user.get("password")
    driver.find_element(*TL.EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*TL.PASSWORD_FIELD).send_keys(user_password)
    driver.find_element(*TL.ENTER_BUTTON).click()
    # Переходим по кнопке Личный Кабинет
    driver.find_element(*TL.PERSONAL_ACC).click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TL.LOGOUT_BUTTON))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    driver.quit()

def test_successful_logout(credentials):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Переходим по кнопке Войти в аккаунт
    driver.find_element(*TL.LOGIN_BUTTON).click()
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
    # Переходим в "Личный кабинет"
    driver.find_element(*TL.PERSONAL_ACC).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TL.LOGOUT_BUTTON))
    # Нажимаем кнопку "Выход"
    driver.find_element(*TL.LOGOUT_BUTTON).click()
    # Проверяем, что перекинуло на страницу логина
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TL.ENTER_BUTTON))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()