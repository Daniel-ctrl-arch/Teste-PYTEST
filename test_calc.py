from calc import soma

def test_soma():
    assert soma(2,3) == 5

def test_soma_negativo():
    assert soma(-1,1) == 0

from calc import subtrair

def test_subtrair():
    assert subtrair(2,3) == -1

def test_subtrair_positivo():
    assert subtrair(3,2) == 1

from calc import multiplicar

def test_multiplicar():
    assert multiplicar(5,6.7) == 33.5

def test_multiplicar_positivo():
    assert multiplicar(5,8) == 40
