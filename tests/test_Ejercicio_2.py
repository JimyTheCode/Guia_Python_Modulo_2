import pytest
from Ejercicio_2 import validar_comando, ejecutar_comando


# Tests para validar_comando()

def test_validar_comando_valido():
    assert validar_comando("guardar") == "guardar"
    assert validar_comando("CARGAR") == "cargar"   # convierte a minúsculas
    assert validar_comando("  salir  ") == "salir" # quita espacios


def test_validar_comando_vacio():
    with pytest.raises(ValueError, match="no puede estar vacío"):
        validar_comando("")
    with pytest.raises(ValueError, match="no puede estar vacío"):
        validar_comando("   ")
    with pytest.raises(ValueError, match="no puede estar vacío"):
        validar_comando(None)


def test_validar_comando_con_numeros():
    with pytest.raises(ValueError, match="solo puede contener letras"):
        validar_comando("guardar123")


def test_validar_comando_con_simbolos():
    with pytest.raises(ValueError, match="solo puede contener letras"):
        validar_comando("cargar!")


def test_validar_comando_con_espacios_internos():
    with pytest.raises(ValueError, match="solo puede contener letras"):
        validar_comando("guardar archivo")


# Tests para ejecutar_comando()

def test_ejecutar_comando_guardar():
    assert ejecutar_comando("guardar") == "Guardando archivo... Operación completada."


def test_ejecutar_comando_cargar():
    assert ejecutar_comando("cargar") == "Cargando archivo... Operación completada."


def test_ejecutar_comando_salir():
    assert ejecutar_comando("salir") == "Saliendo del programa. ¡Hasta luego!"


def test_ejecutar_comando_invalido():
    assert ejecutar_comando("otro") == "Error: Comando no reconocido. Intente de nuevo."
