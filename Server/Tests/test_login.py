import requests
import pytest


class Testlogin():
    def test_login(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        myobj = {"email": "gonathan46@gmail.com", "password": "123456"}
        x = requests.post(url,json= myobj)
        print(x.text)

    def test_valid(self):
        url = "https://trip-yoetz.herokuapp.com/auth/login"
        myobj = {"email": "gonathan46@gmail.com", "password": "123456"}
        x = requests.post(url,json=myobj)
        assert x.status_code == 200
        assert x.elapsed.total_seconds() < 15

