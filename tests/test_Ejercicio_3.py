import pytest
from Ejercicio_3 import validar_password


def test_password_vacia():
    assert "vacía" in validar_password("")[0]
    assert "vacía" in validar_password("   ")[0]
    assert "vacía" in validar_password(None)[0]


def test_password_muy_corta():
    errores = validar_password("Abc12")
    assert any("8 caracteres" in e for e in errores)


def test_password_sin_mayuscula():
    errores = validar_password("abcdefg1")
    assert any("mayúscula" in e for e in errores)


def test_password_sin_numero():
    errores = validar_password("Abcdefgh")
    assert any("número" in e for e in errores)


def test_password_varios_errores():
    errores = validar_password("abc")
    assert any("8 caracteres" in e for e in errores)
    assert any("mayúscula" in e for e in errores)
    assert any("número" in e for e in errores)


def test_password_valida():
    errores = validar_password("Clave123")
    assert errores == []
