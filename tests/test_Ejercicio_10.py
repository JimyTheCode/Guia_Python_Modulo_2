import pytest
from Ejercicio_10 import (
    validar_matriz,
    transponer_matriz_for,
    transponer_matriz_comprehension,
)


def test_validar_matriz_correcta():
    matriz = [[1, 2], [3, 4]]
    assert validar_matriz(matriz) == matriz


def test_validar_matriz_vacia():
    with pytest.raises(ValueError):
        validar_matriz([])


def test_validar_matriz_no_lista():
    with pytest.raises(ValueError):
        validar_matriz("no es matriz")


def test_validar_matriz_filas_no_listas():
    with pytest.raises(ValueError):
        validar_matriz([[1, 2], "fila_mala"])


def test_validar_matriz_longitudes_diferentes():
    with pytest.raises(ValueError):
        validar_matriz([[1, 2], [3, 4, 5]])


def test_transponer_matriz_for():
    matriz = [[1, 2, 3], [4, 5, 6]]
    esperado = [[1, 4], [2, 5], [3, 6]]
    assert transponer_matriz_for(matriz) == esperado


def test_transponer_matriz_comprehension():
    matriz = [[1, 2, 3], [4, 5, 6]]
    esperado = [[1, 4], [2, 5], [3, 6]]
    assert transponer_matriz_comprehension(matriz) == esperado


def test_ambas_funciones_dan_el_mismo_resultado():
    matriz = [[7, 8], [9, 10], [11, 12]]
    assert transponer_matriz_for(matriz) == transponer_matriz_comprehension(matriz)


def test_transpuesta_matriz_1x1():
    matriz = [[42]]
    esperado = [[42]]
    assert transponer_matriz_for(matriz) == esperado
    assert transponer_matriz_comprehension(matriz) == esperado
