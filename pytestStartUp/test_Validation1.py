import pytest
from _pytest import fixtures


# @pytest.mark.val1 -----To run all test that are marked as "val1"
def test_FirstCheck(preSetupWork, secondWork):
    print("\nTested the First Check")
    assert preSetupWork == "Pass"

# @pytest.mark.skip -----To skip this test
def test_SecondCheck(preSetupWork, secondWork):
    print("Tested the Second Check")

