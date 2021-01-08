import pytest


@pytest.fixture
def inversed():
    palabra = "Hola que tal"
    return palabra[::-1]
    
def test_inversed(inversed):
    assert inversed == "lat euq aloH"    