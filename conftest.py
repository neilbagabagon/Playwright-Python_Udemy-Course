import pytest

@pytest.fixture(scope="module")
def preSetupWork():
    print("Opening browser")