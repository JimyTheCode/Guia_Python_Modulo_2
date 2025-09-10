# test_Ejercicio_11.py
import pytest
from Ejercicio_11 import validar_cedula


def test_cedula_valida():
    # longitud correcta y suma de dígitos par
    assert validar_cedula("123455") is True
    assert validar_cedula("24681012") is True


def test_cedula_invalida_no_digitos():
    # contiene letras
    assert validar_cedula("12A456") is False
    # contiene símbolos
    assert validar_cedula("1234-56") is False


def test_cedula_invalida_longitud():
    # muy corta
    assert validar_cedula("123") is False
    # muy larga
    assert validar_cedula("1234567890123456") is False


def test_cedula_invalida_suma_impar():
    # suma de dígitos = 1+2+3+4+5+7 = 22 -> par (válida)
    assert validar_cedula("123457") is True
    # suma de dígitos = 1+2+3+4+5+8 = 23 -> impar (inválida)
    assert validar_cedula("123458") is False
