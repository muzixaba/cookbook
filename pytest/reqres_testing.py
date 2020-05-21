import pytest
import json
import requests


def test_successful_login():
    email = "eve.holt@reqres.in"
    pword = 'cityslicka'
    url = "https://reqres.in/api/login"
    payload = dict(email=email, password=pword)
    response = requests.post(url, data=payload)
    j = json.loads(response.text)
    assert j['token'] == "QpwL5tke4Pnpja7X4"
    assert response.status_code == 200
    

def test_unsuccessful_login():
    url = "https://reqres.in/api/login"
    email = "peter@kaven"
    payload = dict(email=email)
    response = requests.post(url, data=payload)
    j = json.loads(response.text)
    assert j['error'] == "Missing password"
    assert response.status_code == 400


def test_single_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    j = json.loads(response.text)
    assert type(j['data']['id']) == int


def test_single_user_not_found():
    url = "https://reqres.in/api/users/23"
    response = requests.get(url)
    assert response.status_code == 404