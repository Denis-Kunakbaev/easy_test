from proj.request import EasyTest
import pytest


class TestDzen:
    easy_test = EasyTest()
    response = easy_test.request()
    data = response.json()
    username = 'John'

    def test_response(self):
        assert self.response.status_code == 200
        assert self.data[0]['id'] == 1

    @pytest.mark.usefixture('username')
    def test_username(self, username):
        assert self.username != username
        pass
