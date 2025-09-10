# test_Ejercicio_4.py
import pytest
from Ejercicio_4 import jugar_ronda

# TESTS de jugar_ronda()

def test_empate():
    assert jugar_ronda("piedra", "piedra") == "empate"
    assert jugar_ronda("papel", "papel") == "empate"
    assert jugar_ronda("tijeras", "tijeras") == "empate"

def test_gana_jugador():
    assert jugar_ronda("piedra", "tijeras") == "jugador"
    assert jugar_ronda("tijeras", "papel") == "jugador"
    assert jugar_ronda("papel", "piedra") == "jugador"

def test_gana_computadora():
    assert jugar_ronda("tijeras", "piedra") == "computadora"
    assert jugar_ronda("papel", "tijeras") == "computadora"
    assert jugar_ronda("piedra", "papel") == "computadora"

# TESTS de validaciones adicionales

@pytest.mark.parametrize("jugador,computadora", [
    ("PIEDRA", "papel"),   # mayúsculas → debería normalizarse antes en el main
    (" piedra ", "tijeras"), # espacios extra
])
def test_normalizacion(jugador, computadora):
    jugador = jugador.strip().lower()
    assert jugador in ("piedra", "papel", "tijeras")
    assert jugar_ronda(jugador, computadora) in ("jugador", "computadora", "empate")

@pytest.mark.parametrize("jugador,computadora", [
    ("", "piedra"),        # vacío
    ("123", "papel"),      # números
    ("@@@", "tijeras"),    # símbolos
    ("lagarto", "piedra"), # palabra inválida
])
def test_valores_invalidos(jugador, computadora):
    jugador = jugador.strip().lower()
    assert jugador not in ("piedra", "papel", "tijeras")
