# test_ejercicio12.py
import pytest
from Ejercicio_12 import lanzar_dados, simular_lanzamientos


def test_lanzar_dados_rango():
    """Verifica que lanzar_dados siempre devuelva valores entre 2 y 12."""
    for _ in range(1000):
        resultado = lanzar_dados()
        assert 2 <= resultado <= 12


def test_simular_lanzamientos_diccionario():
    """Verifica que simular_lanzamientos retorne un diccionario válido."""
    n = 5000
    frecuencias = simular_lanzamientos(n)

    # Debe contener todas las claves de 2 a 12
    assert set(frecuencias.keys()) == set(range(2, 13))

    # La suma de las frecuencias debe coincidir con el total de lanzamientos
    assert sum(frecuencias.values()) == n

    # Todas las frecuencias deben ser enteros no negativos
    assert all(isinstance(v, int) and v >= 0 for v in frecuencias.values())


def test_simular_lanzamientos_valor_invalido():
    """Verifica que simular_lanzamientos lance ValueError con valores inválidos."""
    with pytest.raises(ValueError):
        simular_lanzamientos(0)
    with pytest.raises(ValueError):
        simular_lanzamientos(-10)
