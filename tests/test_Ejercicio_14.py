import pytest
from Ejercicio_14 import (
    mostrar_tablero,
    validar_letra,
)

# -------------------------
# Tests de mostrar_tablero
# -------------------------
def test_mostrar_tablero_con_letras_adivinadas(capsys):
    palabra = "python"
    letras_adivinadas = {"p", "y", "t"}
    vidas = 5

    mostrar_tablero(palabra, letras_adivinadas, vidas)
    salida = capsys.readouterr().out

    # Verifica que las letras correctas aparezcan en el tablero
    assert "p" in salida
    assert "y" in salida
    assert "t" in salida
    # Verifica que aparezcan guiones bajos por las letras faltantes
    assert "_" in salida
    # Verifica que las vidas se muestren
    assert "5" in salida


# -------------------------
# Tests de validar_letra
# -------------------------
def test_letra_valida(monkeypatch):
    # Simula que el usuario ingresa "a"
    monkeypatch.setattr("builtins.input", lambda _: "a")
    resultado = validar_letra(set())
    assert resultado == "a"


def test_letra_vacia(monkeypatch, capsys):
    # Simula que el usuario primero da Enter vacío, luego "b"
    entradas = iter(["", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validar_letra(set())
    salida = capsys.readouterr().out

    assert "No puedes dejar el campo vacío" in salida
    assert resultado == "b"


def test_mas_de_una_letra(monkeypatch, capsys):
    # Primero "ab", luego "c"
    entradas = iter(["ab", "c"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validar_letra(set())
    salida = capsys.readouterr().out

    assert "Debes ingresar solo una letra" in salida
    assert resultado == "c"


def test_caracter_no_alfabetico(monkeypatch, capsys):
    # Primero "1", luego "d"
    entradas = iter(["1", "d"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validar_letra(set())
    salida = capsys.readouterr().out

    assert "Solo se permiten letras" in salida
    assert resultado == "d"


def test_letra_repetida(monkeypatch, capsys):
    letras_usadas = {"e"}
    # Primero intenta "e" que ya está usada, luego "f"
    entradas = iter(["e", "f"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validar_letra(letras_usadas)
    salida = capsys.readouterr().out

    assert "Ya intentaste la letra" in salida
    assert resultado == "f"


