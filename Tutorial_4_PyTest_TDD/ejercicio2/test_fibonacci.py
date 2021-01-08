import pytest

@pytest.fixture
def fibonnaci():
    lista = [0,1]
    for i in range (2,50):
        lista.append(lista[i-1]+lista[i-2])
    return lista

def test_fibonnaci(fibonnaci):
    assert fibonnaci[5] == 5

def test_fibonnaci_falla(fibonnaci):
    assert fibonnaci[7] == 14