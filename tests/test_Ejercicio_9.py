import pytest
from Ejercicio_9 import validar_nombre, validar_precio, aplicar_iva


# Pruebas de validar_nombre
def test_validar_nombre_valido():
    assert validar_nombre("manzana") == "Manzana"
    assert validar_nombre("   pera   ") == "Pera"

def test_validar_nombre_vacio():
    with pytest.raises(ValueError, match="no puede estar vacío"):
        validar_nombre("   ")

def test_validar_nombre_con_numeros():
    with pytest.raises(ValueError, match="solo puede contener letras"):
        validar_nombre("pan123")

def test_validar_nombre_corto_largo():
    with pytest.raises(ValueError, match="entre 2 y 30"):
        validar_nombre("A")
    with pytest.raises(ValueError, match="entre 2 y 30"):
        validar_nombre("x" * 31)


# Pruebas de validar_precio

def test_validar_precio_valido():
    assert validar_precio("10") == 10.00
    assert validar_precio("15.567") == 15.57  # redondeo a 2 decimales

def test_validar_precio_invalido_texto():
    with pytest.raises(ValueError, match="número válido"):
        validar_precio("abc")

def test_validar_precio_negativo():
    with pytest.raises(ValueError, match="no puede ser negativo"):
        validar_precio("-5")


# Pruebas de aplicar_iva
def test_aplicar_iva():
    productos = [
        {"nombre": "Manzana", "precio": 1000},
        {"nombre": "Pera", "precio": 2000}
    ]
    resultado = aplicar_iva(productos, iva=0.19)
    assert resultado == {"Manzana": 1190.0, "Pera": 2380.0}

def test_aplicar_iva_con_otro_porcentaje():
    productos = [{"nombre": "Banano", "precio": 1000}]
    resultado = aplicar_iva(productos, iva=0.10)
    assert resultado == {"Banano": 1100.0}
