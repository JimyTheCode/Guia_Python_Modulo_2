import pytest
from Ejercicio_6 import encontrar_indices, validar_frase, validar_letra


# Tests para encontrar_indices

def test_encontrar_indices_encontrados():
    assert encontrar_indices("Hola SENA", "a") == [3, 8]
    assert encontrar_indices("Python", "p") == [0]
    assert encontrar_indices("banana", "a") == [1, 3, 5]


def test_encontrar_indices_no_encontrados():
    assert encontrar_indices("Hola Mundo", "z") == []


def test_encontrar_indices_insensible_mayusculas():
    assert encontrar_indices("Hola SENA", "A") == [3, 8]
    assert encontrar_indices("PYTHON", "p") == [0]


# Tests para validar_frase

def test_validar_frase_valida():
    assert validar_frase("Hola mundo") == "Hola mundo"


def test_validar_frase_vacia():
    with pytest.raises(ValueError, match="no puede estar vacía"):
        validar_frase("")


def test_validar_frase_con_numeros():
    with pytest.raises(ValueError, match="no puede contener números"):
        validar_frase("Hola123")


# Tests para validar_letra

def test_validar_letra_valida():
    assert validar_letra("a") == "a"
    assert validar_letra("Z") == "Z"


def test_validar_letra_mas_de_un_caracter():
    with pytest.raises(ValueError, match="exactamente una letra"):
        validar_letra("ab")


def test_validar_letra_vacia():
    with pytest.raises(ValueError, match="exactamente una letra"):
        validar_letra("")


def test_validar_letra_no_alfabetica():
    with pytest.raises(ValueError, match="una letra del alfabeto"):
        validar_letra("1")
    with pytest.raises(ValueError, match="una letra del alfabeto"):
        validar_letra("!")
