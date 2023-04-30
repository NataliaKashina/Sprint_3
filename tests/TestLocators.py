from selenium.webdriver.common.by import By

class TestLocators:
    # Локаторы Главной страницы:
    LOGIN_BUTTON = By.XPATH, "// button[contains(text(), 'Войти в аккаунт')]" # кнопка "Войти в Аккаунт"
    PERSONAL_ACC = By.XPATH, '// *[ @class ="AppHeader_header__linkText__3q_va ml-2"][text()="Личный Кабинет"]' # кнопка "Личный Кабинет"
    PLACE_ORDER = By.CLASS_NAME, "button_button__33qZ0"  # кнопка "Оформить Заказ"
    SAUCES = By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div" # кнопка перехода на "Соусы"
    SAUCE = By.XPATH, "//p[contains(text(), 'Соус Spicy-X')]" # Соус Spicy-X
    TOPPINGS = By.XPATH, "//span[contains(@class, 'text_type_main-default') and contains(text(), 'Начинки')]" # кнопка перехода на "Начинки"
    TOPPING = By.XPATH, "//p[contains(text(), 'Говяжий метеорит')]" # начинка "Говяжий Метеорит"
    BUNS = By.XPATH, "//span[contains(text(), 'Булки')]" # кнопка перехода на "Булки"
    BUN = By.XPATH, "//p[text()='Флюоресцентная булка R2-D3' ]"  # булка "Флюоресцентная булка"
    # Локаторы страницы Авторизации и Регистрации:
    REGISTRATION_LINK = By.XPATH, ".//a[text()='Зарегистрироваться']"   # кнопка перехода на страницу регистирации
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input"   # поле ввода Email
    PASSWORD_FIELD = By.XPATH, "//label[text()='Пароль']/following-sibling::input"   # поле ввода Пароля
    NAME_FIELD = By.CSS_SELECTOR, "input[name='name']" # поле ввода Имени
    REGISTRATION_BUTTON = By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]" # кнопка "Зарегистироваться"
    WRONG_PASS = By.XPATH, '//*[contains(text(), "Некорректный пароль")]' # валидационное сообщение для пароля при регистрации
    LOGIN_FROM_REGISTRATION = By.XPATH, "//a[text()='Войти']"  # кнопка  "Войти" на странице Регистрации
    ENTER_BUTTON = By.XPATH, "//button[contains(text(),'Войти')]"  # кнопка  "Войти"на странице Авторизации
    RESTORE_PASS = By.XPATH, "//a[@href='/forgot-password']" # кнопка "Восстановить Пароль" на странице Авторизации
    # Локаторы Личного кабинета:
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]" # кнопка "Конструктор"
    LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a" # логотип Stellar Burgers