# test_ejercicio8.py
import pytest
from Ejercicio_8 import validar_lista_numeros, filtrar_datos


# Tests para validar_lista_numeros
def test_validar_lista_correcta():
    lista = [1, -2, 3.5, 0]
    assert validar_lista_numeros(lista) == lista


def test_validar_lista_con_elemento_no_numerico():
    with pytest.raises(ValueError, match="no es un número válido"):
        validar_lista_numeros([1, "dos", 3])


def test_validar_entrada_no_lista():
    with pytest.raises(ValueError, match="La entrada debe ser una lista."):
        validar_lista_numeros("no soy una lista")


# Tests para filtrar_datos
def test_filtrar_datos_listas_correctas():
    lista = [-5, 10, -15, 20, -25, 30]
    positivos, cuadrados, signos = filtrar_datos(lista)

    assert positivos == [10, 20, 30]
    assert cuadrados == [25, 100, 225, 400, 625, 900]
    assert signos == ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo"]


def test_filtrar_datos_lista_vacia():
    lista = []
    positivos, cuadrados, signos = filtrar_datos(lista)

    assert positivos == []
    assert cuadrados == []
    assert signos == []


def test_filtrar_datos_lista_con_ceros():
    lista = [0, -1, 2]
    positivos, cuadrados, signos = filtrar_datos(lista)

    assert positivos == [2]  # 0 no es positivo
    assert cuadrados == [0, 1, 4]
    assert signos == ["positivo", "negativo", "positivo"]
