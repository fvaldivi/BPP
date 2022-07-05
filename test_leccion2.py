import pytest


def split_case(x):
    if not isinstance(x, str):
        raise TypeError("el dato no es correcto")
    return x.split(" ")

def sort_list(z):
    z.sort()
    return z

def sumacuadrados(x,y):
    if not isinstance(x, int):
        raise TypeError("el dato no es correcto")
    if not isinstance(y, int):
        raise TypeError("el dato no es correcto")
    else:
        total = x**2 + y**2
    return total




def test_split_case():
    assert split_case("hola que tal") == ["hola","que","tal"]

def test_sort_list():
    z = [3,2,5,6]
    assert sort_list(z) == ([2, 3, 5, 6])

def test_sumacuadrados():
    assert sumacuadrados(2,2) == 8

def test_control_sumacuadrados():
    with pytest.raises(TypeError):
        sumacuadrados("a","b")

def test_control_split_case():
    with pytest.raises(TypeError):
        split_case(1)




