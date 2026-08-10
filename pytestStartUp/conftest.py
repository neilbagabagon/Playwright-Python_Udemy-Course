import pytest

@pytest.fixture(scope="module")
def preSetupWork():
    print("\nOpening browser")
    return "Pass"

@pytest.fixture(scope="function")
def secondWork():
    print("\nOpening second instance")
    yield
    print("\nClosing second instance")