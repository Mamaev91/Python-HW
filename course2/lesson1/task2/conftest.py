import pytest
import requests
import yaml

with open("logpass.yaml") as f:
    data = yaml.safe_load(f)
user = data["user"]
passwd = data["passwd"]

@pytest.fixture()
def login():
    r = requests.post("https://test-stand.gb.ru/gateway/login", data={"username": user,
                                                                        "password": passwd})
    return r.json()["token"]
@pytest.fixture()
def text_2():
    return "Cheza"
@pytest.fixture()
def resp():
    return 200

@pytest.fixture()
def text_3():
    return "Это курс по автотестам"

