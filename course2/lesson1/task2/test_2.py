import pytest
import requests
import yaml

# def get(token):
#     g = requests.get("https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}, params={"owner": "notMe"})
#     listcontent = [i["content"] for i in g.json()["data"]]
#     return listcontent
def create_new_post(token):
    res = requests.post("https://test-stand.gb.ru/gateway/posts", data={"title": "Автотесты",
                                                                        "description": "Это курс по автотестам",
                                                                        "content": "Надеюсь у меня что-то получилось"},
                        headers={"X-Auth-Token": token})
    return res.status_code
def check_new_post(token):
    new_post = requests.get("https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token})
    listdescr = [i["description"] for i in new_post.json()["data"]]
    return listdescr


# def test_step2(text_2, login):
#     assert text_2 in get(login)

def test_03(resp, login):
    assert resp == create_new_post(login)

def test_04(text_3, login):
    assert text_3 in check_new_post(login)




