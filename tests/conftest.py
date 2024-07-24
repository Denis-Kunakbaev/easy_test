import pytest


USERNAME = "--username"

def pytest_addoption(parser):
    parser.addoption(USERNAME, default='John')

@pytest.fixture
def username(request):
    return request.config.getoption(USERNAME)