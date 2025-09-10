import pytest
from Ejercicio_1 import (
    validar_edad,
    validar_estudiante,
    validar_cantidad,
    validar_opcion,
    calcular_precio,
)


# Tests validar_edad

def test_validar_edad_valida():
    assert validar_edad("10") == 10
    assert validar_edad("90") == 90
    assert validar_edad(25) == 25


def test_validar_edad_vacia():
    with pytest.raises(ValueError, match="vacía"):
        validar_edad("")


def test_validar_edad_no_numero():
    with pytest.raises(ValueError, match="entero positivo"):
        validar_edad("abc")
    with pytest.raises(ValueError, match="entero positivo"):
        validar_edad("12.5")
    with pytest.raises(ValueError, match="entero positivo"):
        validar_edad("@#!")


def test_validar_edad_fuera_rango():
    with pytest.raises(ValueError, match="mayor que 0"):
        validar_edad("0")
    with pytest.raises(ValueError, match="mayor que 0"):
        validar_edad("-5")
    with pytest.raises(ValueError, match="90 años"):
        validar_edad("91")


# Tests validar_estudiante

def test_validar_estudiante_valido():
    assert validar_estudiante("si") is True
    assert validar_estudiante("no") is False
    assert validar_estudiante(" SI ") is True  # mayúsculas y espacios


def test_validar_estudiante_vacio():
    with pytest.raises(ValueError, match="vacía"):
        validar_estudiante("")


def test_validar_estudiante_invalido():
    with pytest.raises(ValueError, match="si' o 'no"):
        validar_estudiante("tal vez")


# Tests validar_cantidad

def test_validar_cantidad_valida():
    assert validar_cantidad("1") == 1
    assert validar_cantidad("15") == 15
    assert validar_cantidad(7) == 7


def test_validar_cantidad_vacia():
    with pytest.raises(ValueError, match="vacía"):
        validar_cantidad("")


def test_validar_cantidad_no_numero():
    with pytest.raises(ValueError, match="positivo"):
        validar_cantidad("abc")
    with pytest.raises(ValueError, match="positivo"):
        validar_cantidad("12.3")


def test_validar_cantidad_fuera_rango():
    with pytest.raises(ValueError, match="mayor a 0"):
        validar_cantidad("0")
    with pytest.raises(ValueError, match="mayor a 0"):
        validar_cantidad("-3")
    with pytest.raises(ValueError, match="15 personas"):
        validar_cantidad("16")


# Tests validar_opcion

def test_validar_opcion_valida():
    assert validar_opcion("1") == 1
    assert validar_opcion("2") == 2
    assert validar_opcion("3") == 3


def test_validar_opcion_vacia():
    with pytest.raises(ValueError, match="vacía"):
        validar_opcion("")


def test_validar_opcion_no_numero():
    with pytest.raises(ValueError, match="número"):
        validar_opcion("abc")


def test_validar_opcion_invalida():
    with pytest.raises(ValueError, match="1, 2 o 3"):
        validar_opcion("5")


# Tests calcular_precio

def test_calcular_precio_sin_descuento():
    assert calcular_precio(10, False) == 10000
    assert calcular_precio(15, False) == 15000
    assert calcular_precio(25, False) == 20000


def test_calcular_precio_con_descuento():
    assert calcular_precio(10, True) == 9000   # 10% de 10000
    assert calcular_precio(15, True) == 13500 # 10% de 15000
    assert calcular_precio(25, True) == 18000 # 10% de 20000




