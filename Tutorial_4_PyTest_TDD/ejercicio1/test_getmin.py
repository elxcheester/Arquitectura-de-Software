import pytest

@pytest.fixture
def get_min():
    values = [58,3,74,12,7,1,5]
    input = values[0]
    for i in range (1, (len(values)-1)):
        if values[i]<input:
            input = values[i]
    return input


def test_min(get_min):
   assert get_min == 1