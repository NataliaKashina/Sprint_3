from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import TestLocators as TL

def test_successful_navigation_to_main_page_via_constructor(exist_user):
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
    # Переходим по кнопке Конструктор
    driver.find_element(*TL.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TL.PERSONAL_ACC))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_successful_navigation_to_main_page_via_logo(exist_user):
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
    # Переходим по Логотипу на главную страницу
    driver.find_element(*TL.LOGO).click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TL.PERSONAL_ACC))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_navigation_to_constructor_sauces():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TL.SAUCES).click()
    element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TL.SAUCE))
    assert element.text == "Соус Spicy-X"
    driver.quit()

def test_navigation_to_constructor_toppings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TL.TOPPINGS).click()
    element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TL.TOPPING))
    assert element.text == "Говяжий метеорит (отбивная)"
    driver.quit()

def test_navigation_to_constructor_buns():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*TL.TOPPINGS).click()
    driver.find_element(*TL.BUNS).click()
    element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TL.BUN))
    assert element.text == "Флюоресцентная булка R2-D3"
    driver.quit()