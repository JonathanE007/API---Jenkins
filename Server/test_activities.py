import requests
import pytest

class Test_activities():
    def test_activities(self):
        url = "https://trip-yoetz.herokuapp.com/auth/register"
        x = requests.get(url)
        assert x.status_code == 200
        assert x.elapsed.total_seconds() < 10