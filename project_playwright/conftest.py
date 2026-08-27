import pytest


@pytest.fixture(scope="session")
def user_credential(request):
    return request.param