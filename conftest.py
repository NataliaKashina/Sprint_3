import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


@pytest.fixture(scope="session")
def credentials():
    email = f"natalia_kashina_{random.randint(1, 99)}_{random.randint(100, 999)}@yandex.ru"
    name = "Наталья"
    password = "mypass1"
    return {"email": email, "name": name, "password": password}

@pytest.fixture(scope="session")
def exist_user():
    email = "natalia_kashina_005@yandex.ru"
    password = "666666"
    return {"email": email, "password": password}

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()