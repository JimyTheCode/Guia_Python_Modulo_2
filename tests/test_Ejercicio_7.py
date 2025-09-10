# test_Ejercicio_7.py
import pytest
from Ejercicio_7 import validar_nombre, validar_nota, combinar_listas


# Tests para validar_nombre

def test_validar_nombre_valido():
    assert validar_nombre("Carlos") == "Carlos"

def test_validar_nombre_vacio():
    with pytest.raises(ValueError, match="vacío"):
        validar_nombre("")

def test_validar_nombre_con_numeros():
    with pytest.raises(ValueError, match="solo puede contener letras"):
        validar_nombre("Ana123")

def test_validar_nombre_con_simbolos():
    with pytest.raises(ValueError, match="solo puede contener letras"):
        validar_nombre("Luis@")

def test_validar_nombre_muy_corto():
    with pytest.raises(ValueError, match="entre 2 y 30 caracteres"):
        validar_nombre("A")

def test_validar_nombre_muy_largo():
    with pytest.raises(ValueError, match="entre 2 y 30 caracteres"):
        validar_nombre("A" * 40)


# Tests para validar_nota

def test_validar_nota_valida():
    assert validar_nota(4.5) == 4.5
    assert validar_nota(3) == 3.0

def test_validar_nota_no_numero():
    with pytest.raises(ValueError, match="debe ser un número"):
        validar_nota("texto")

def test_validar_nota_menor_a_cero():
    with pytest.raises(ValueError, match="entre 0.0 y 5.0"):
        validar_nota(-1)

def test_validar_nota_mayor_a_cinco():
    with pytest.raises(ValueError, match="entre 0.0 y 5.0"):
        validar_nota(6)


# Tests para combinar_listas

def test_combinar_listas_correcto():
    nombres = ["Ana", "Luis"]
    notas = [4.0, 3.5]
    resultado = combinar_listas(nombres, notas)
    assert resultado == {"Ana": 4.0, "Luis": 3.5}

def test_combinar_listas_nombre_invalido():
    nombres = ["Ana", "Luis1"]
    notas = [4.0, 3.5]
    with pytest.raises(ValueError, match="solo puede contener letras"):
        combinar_listas(nombres, notas)

def test_combinar_listas_nota_invalida():
    nombres = ["Ana", "Luis"]
    notas = [4.0, 6.0]  # nota inválida
    with pytest.raises(ValueError, match="entre 0.0 y 5.0"):
        combinar_listas(nombres, notas)
