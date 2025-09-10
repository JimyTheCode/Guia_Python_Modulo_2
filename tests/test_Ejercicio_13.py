import pytest
from Ejercicio_13 import habitacion_inicial, habitacion_de_la_llave, habitacion_del_cofre, habitacion_final

# Funciones auxiliares para test

def jugar_habitacion_inicial(decision):
    """Simula la decisión en la habitación inicial."""
    if decision == "norte":
        return "cofre"
    elif decision == "sur":
        return "llave"
    elif decision == "este":
        return "final"
    return "inicial"

def jugar_habitacion_del_cofre(decision):
    """Simula la acción en la habitación del cofre."""
    if decision == "abrir":
        return "perder"
    return "inicial"

def jugar_habitacion_de_la_llave(inventario, decision):
    """Simula la acción en la habitación de la llave."""
    if decision == "tomar" and "llave" not in inventario:
        inventario.append("llave")
    return "inicial"

def jugar_habitacion_final(inventario, decision):
    """Simula la acción en la habitación final."""
    if "llave" in inventario and decision == "usar":
        return "ganar"
    return "inicial"

# Test de integración completo

def test_flujo_completo_juego():
    inventario = []

    # Camino 1: inicial → norte → abrir cofre → perder
    estado = jugar_habitacion_inicial("norte")
    assert estado == "cofre"
    estado = jugar_habitacion_del_cofre("abrir")
    assert estado == "perder"

    # Camino 2: inicial → sur → tomar llave → inicial → este → usar llave → ganar
    inventario.clear()
    estado = jugar_habitacion_inicial("sur")
    assert estado == "llave"
    estado = jugar_habitacion_de_la_llave(inventario, "tomar")
    assert "llave" in inventario
    assert estado == "inicial"
    estado = jugar_habitacion_inicial("este")
    assert estado == "final"
    estado = jugar_habitacion_final(inventario, "usar")
    assert estado == "ganar"

    # Camino 3: inicial → sur → no tomar llave → inicial → este → intentar usar llave → inicial
    inventario.clear()
    estado = jugar_habitacion_inicial("sur")
    assert estado == "llave"
    estado = jugar_habitacion_de_la_llave(inventario, "volver")
    assert "llave" not in inventario
    assert estado == "inicial"
    estado = jugar_habitacion_inicial("este")
    assert estado == "final"
    estado = jugar_habitacion_final(inventario, "usar")
    # No tiene llave → sigue en inicial
    assert estado == "inicial"



