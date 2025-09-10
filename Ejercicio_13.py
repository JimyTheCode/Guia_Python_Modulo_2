"""
Ejercicio 13: Aventura de Texto Simple
Diseña un pequeño juego de aventura basado en texto. El jugador comienza en una habitación y puede tomar decisiones ('ir al norte', 'abrir cofre'):
•	El juego debe tener al menos 3 habitaciones y un estado final (ganar o perder).
•	Utiliza un bucle while para el bucle principal del juego y estructuras if/elif/else para manejar las decisiones del jugador y el estado del juego.
Conceptos integrados: Bucles, condicionales, manejo de estado con variables, input().

"""

import re

# Colores ANSI para mejorar la visualización
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"

def obtener_comando(mensaje, opciones_validas):
    while True:
        comando = input(f"{AZUL}{mensaje}\n> {RESET}").strip().lower()
        if not comando:
            print(f"{ROJO}No puedes dejar el campo vacío. Intenta de nuevo.{RESET}")
            continue
        if not re.match(r"^[a-záéíóúñ\s]+$", comando):
            print(f"{ROJO}Solo se permiten letras y espacios. Ejemplo: 'norte', 'volver'.{RESET}")
            continue
        if comando not in opciones_validas:
            print(f"{AMARILLO}Opción no válida. Opciones permitidas: {', '.join(opciones_validas)}.{RESET}")
            continue
        return comando

def mostrar_mapa(posicion):
    mapa = {
        "inicial": " [Inicio*] --- [???] \n     |             \n  [???] --- [???]",
        "cofre": " [Inicio] --- [Cofre*] \n     |               \n  [???] --- [???]",
        "llave": " [Inicio] --- [???] \n     |             \n  [Llave*] --- [???]",
        "final": " [Inicio] --- [???] \n     |             \n  [???] --- [Salida*]",
    }
    print(f"\n{AZUL}Mapa del juego:{RESET}")
    print(mapa.get(posicion, mapa["inicial"]))
    print(f"{AMARILLO}(* indica tu ubicación actual){RESET}\n")

def habitacion_inicial():
    print(f"{VERDE}\nTe encuentras en una habitación oscura con dos caminos.{RESET}")
    return obtener_comando("Escribe la dirección a la cual deseas ir (norte/sur):", ["norte", "sur"])

def habitacion_del_cofre(inventario):
    print(f"{AMARILLO}\nEncuentras un cofre misterioso en el centro de la sala.{RESET}")
    accion = obtener_comando("¿Quieres 'abrir' el cofre o 'volver'?", ["abrir", "volver"])
    if accion == "abrir":
        print(f"{ROJO}El cofre estaba envenenado... ¡has perdido la partida!{RESET}")
        return "perder"
    return "inicial"

def habitacion_de_la_llave(inventario):
    print(f"{VERDE}\nHas llegado a una sala iluminada con una mesa de piedra.{RESET}")
    if "llave" not in inventario:
        print("Sobre la mesa ves un objeto brillante.")
        accion = obtener_comando("¿Quieres 'tomar' la llave o 'volver'?", ["tomar", "volver"])
        if accion == "tomar":
            inventario.append("llave")
            print(f"{AZUL}Has recogido la llave dorada.{RESET}")
    else:
        print("Ya recogiste la llave de esta sala.")
        obtener_comando("Escribe 'volver' para regresar.", ["volver"])
    return "inicial"

def habitacion_final(inventario):
    print(f"{AMARILLO}\nLlegas a una sala con una gran puerta dorada frente a ti.{RESET}")
    if "llave" in inventario:
        accion = obtener_comando("¿Quieres 'usar' la llave o 'volver'?", ["usar", "volver"])
        if accion == "usar":
            print(f"{VERDE}La puerta se abre lentamente... ¡Has escapado con éxito!{RESET}")
            return "ganar"
    else:
        print(f"{ROJO}La puerta está cerrada con llave. Necesitas encontrarla primero.{RESET}")
        obtener_comando("Escribe 'volver' para regresar.", ["volver"])
    return "inicial"

def main():
    print(f"{AZUL}Bienvenido a la Aventura Misteriosa.{RESET}")
    print("Explora las salas, encuentra la llave y abre la puerta final.\n")
    estado = "inicial"
    inventario = []

    while True:
        mostrar_mapa(estado)
        if estado == "inicial":
            decision = habitacion_inicial()
            if decision == "norte":
                estado = "cofre"
            elif decision == "sur":
                estado = "llave"
            if estado == "inicial":
                salir = obtener_comando("¿Quieres ir al 'este' o 'quedarte'?", ["este", "quedarte"])
                if salir == "este":
                    estado = "final"
        elif estado == "cofre":
            estado = habitacion_del_cofre(inventario)
            if estado == "perder":
                break
        elif estado == "llave":
            estado = habitacion_de_la_llave(inventario)
        elif estado == "final":
            estado = habitacion_final(inventario)
            if estado == "ganar":
                break
    print(f"\n{AZUL}Gracias por jugar. Fin de la aventura.{RESET}")

if __name__ == "__main__":
    main()







