import pytest
from Ejercicio_15 import (
    crear_tablero,
    colocar_barco,
    validar_disparo,
    resultado_final,
    FILAS,
    COLUMNAS,
)

# Test crear_tablero

def test_crear_tablero_dimensiones():
    tablero = crear_tablero()
    assert len(tablero) == FILAS
    assert all(len(fila) == COLUMNAS for fila in tablero)
    assert all(celda == "~" for fila in tablero for celda in fila)


# Test colocar_barco

def test_colocar_barco_tamano_y_rango():
    barco = colocar_barco()
    assert len(barco) == 3
    for fila, col in barco:
        assert 0 <= fila < FILAS
        assert 0 <= col < COLUMNAS


def test_colocar_barco_horizontal_o_vertical():
    barco = colocar_barco()
    filas = [f for f, _ in barco]
    cols = [c for _, c in barco]
    # O todas las filas iguales (horizontal), o todas las columnas iguales (vertical)
    assert (len(set(filas)) == 1) or (len(set(cols)) == 1)


# Test validar_disparo

def test_validar_disparo_valido():
    disparos = set()
    fila, col = validar_disparo(disparos, entrada_manual="B3")
    assert (fila, col) == (1, 2)  # B=1, 3=columna 2 (0-index)
    assert "B3" in disparos


def test_validar_disparo_invalido_fuera_rango(capsys):
    disparos = set()
    # Probamos algo fuera de rango y luego válido
    entrada = ["Z9", "A1"]
    for e in entrada:
        try:
            res = validar_disparo(disparos, entrada_manual=e)
            if res:
                assert res == (0, 0)  # A1 = (0,0)
        except Exception:
            pass
    captured = capsys.readouterr()
    assert "Formato inválido" in captured.out or "Coordenada fuera de rango" in captured.out


# Test resultado_final
def test_resultado_final_gano(capsys):
    tablero = crear_tablero()
    barco = [(0, 0), (0, 1), (0, 2)]
    resultado_final(tablero, barco, True)
    captured = capsys.readouterr()
    assert "¡Ganaste" in captured.out


def test_resultado_final_perdio(capsys):
    tablero = crear_tablero()
    barco = [(0, 0), (0, 1), (0, 2)]
    resultado_final(tablero, barco, False)
    captured = capsys.readouterr()
    assert "Perdiste" in captured.out
    # Asegurar que barco se marcó en tablero
    for fila, col in barco:
        assert tablero[fila][col] == "O"


