import random
import pytest
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