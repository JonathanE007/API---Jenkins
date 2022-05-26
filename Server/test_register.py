import requests
import pytest

class TestRegister():
    def test_register(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        myobj = {"name": "jona", "lastName": "el ", "birthDate": "2003-12-30", "email": "gonathan10@gmail.com"}
        x = requests.post(url,data=myobj)
        print(x.text)
