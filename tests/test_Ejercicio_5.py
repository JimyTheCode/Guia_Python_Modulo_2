# test_clasificador_numeros.py
import pytest
from Ejercicio_5 import clasificar_numero


@pytest.mark.parametrize(
    "numero, esperado",
    [
        (2, ("Par", False)),    # Par pero no múltiplo de 5
        (4, ("Par", False)),    # Otro Par no múltiplo de 5
        (10, ("Par", True)),    # Par y múltiplo de 5
        (15, ("Impar", True)),  # Impar y múltiplo de 5
        (7, ("Impar", False)),  # Impar no múltiplo de 5
    ],
)
def test_clasificar_numero(numero, esperado):
    """Verifica la clasificación de números par/impar y múltiplos de 5."""
    assert clasificar_numero(numero) == esperado


def test_cero():
    """El número 0 debe considerarse Par y múltiplo de 5."""
    assert clasificar_numero(0) == ("Par", True)


def test_negativos():
    """Se permite comprobar lógica de números negativos en la función pura."""
    assert clasificar_numero(-2) == ("Par", False)
    assert clasificar_numero(-5) == ("Impar", True)


def test_valores_grandes():
    """La función debe soportar números muy grandes sin errores."""
    numero = 10**12
    assert clasificar_numero(numero) == ("Par", True)
    assert clasificar_numero(numero + 1) == ("Impar", False)
