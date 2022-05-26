import requests
import pytest

class Test_hotels():
    def test_hotels(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        x = requests.get(url)
        assert x.status_code == 200
        assert x.elapsed.total_seconds() < 10
        print(x)

