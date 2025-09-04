"""
Ejercicio 15: Proyecto Final - Batalla Naval Simplificada
Crea una versión del juego "Batalla Naval" en una cuadrícula de 5x5:
•	El programa debe "esconder" un barco de 3 casillas en una fila o columna aleatoria.
•	El jugador tiene 10 turnos para adivinar las coordenadas (ej. "A3") y hundir el barco.
•	El programa debe gestionar el tablero (una lista de listas), validar la entrada del usuario, indicar si un disparo fue "Agua" o "Tocado", y llevar la cuenta de los turnos.

•	Al final, debe declarar si el jugador ganó o perdió.
Conceptos integrados: Lógica de juegos, listas anidadas, funciones, bucles while y for, condicionales, random, manipulación de strings.

"""

import random

# Colores ANSI
AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
RESET = "\033[0m"

# Constantes
FILAS = 5
COLUMNAS = 5
TURNOS = 10


def crear_tablero():
    """
    Crea un tablero vacío de FILAS x COLUMNAS.

    Returns:
        list[list[str]]: Tablero inicial con "~" en todas las casillas.
    """
    return [["~" for _ in range(COLUMNAS)] for _ in range(FILAS)]


def colocar_barco() :
    """
    Coloca un barco de 3 casillas en una posición aleatoria (horizontal o vertical).

    Returns:
        list[tuple[int, int]]: Lista de coordenadas del barco.
    """
    orientacion = random.choice(["H", "V"])
    if orientacion == "H":  # Horizontal
        fila = random.randint(0, FILAS - 1)
        col = random.randint(0, COLUMNAS - 3)
        return [(fila, col + i) for i in range(3)]
    else:  # Vertical
        fila = random.randint(0, FILAS - 3)
        col = random.randint(0, COLUMNAS - 1)
        return [(fila + i, col) for i in range(3)]


def mostrar_tablero(tablero) -> None:
    """
    Muestra el tablero en consola con encabezados de filas y columnas.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.
    """
    print(f"    {AMARILLO}{'  '.join(str(i+1) for i in range(COLUMNAS))}{RESET}")
    for idx, fila in enumerate(tablero):
        letra = chr(65 + idx)  # A, B, C...
        print(f"{AMARILLO}{letra}{RESET}  " + "  ".join(fila))
    print()


def validar_disparo(disparos) :
    """
    Solicita al usuario una coordenada y valida la entrada.

    Reglas:
    - Formato correcto: letra A-E + número 1-5 (ej. A3).
    - No puede estar vacía.
    - No puede repetirse.

    Args:
        disparos (set[str]): Conjunto de disparos ya realizados.

    Returns:
        tuple[int, int]: Coordenadas validadas en formato (fila, columna).
    """
    while True:
        entrada = input(f"{AZUL}Ingresa una coordenada (ejemplo A3): {RESET}").strip().upper()

        if not entrada:
            print(f"{ROJO}No puedes dejar el campo vacío.{RESET}")
            continue

        if len(entrada) < 2 or len(entrada) > 3:
            print(f"{ROJO}Formato inválido. Usa letra A-E seguida de número 1-5 (ej. B4).{RESET}")
            continue

        letra, numero = entrada[0], entrada[1:]
        if letra not in "ABCDE" or not numero.isdigit():
            print(f"{ROJO}Formato inválido. Usa una letra (A-E) y un número (1-5).{RESET}")
            continue

        fila = ord(letra) - 65
        columna = int(numero) - 1

        if not (0 <= fila < FILAS and 0 <= columna < COLUMNAS):
            print(f"{ROJO}Coordenada fuera de rango. Usa A-E y 1-5.{RESET}")
            continue

        if entrada in disparos:
            print(f"{AMARILLO}Ya intentaste esa coordenada. Elige otra.{RESET}")
            continue

        disparos.add(entrada)
        return fila, columna


def jugar() -> None:
    """
    Controla el flujo principal del juego:
    - Coloca el barco.
    - Muestra el tablero.
    - Permite hasta TURNOS intentos.
    - Indica Agua, Tocado o Hundido.
    """
    tablero = crear_tablero()
    barco = colocar_barco()
    partes_restantes = set(barco)
    disparos = set()

    print(f"{AZUL}Bienvenido a Batalla Naval (5x5){RESET}")
    print(f"Debes hundir un barco de 3 casillas en {TURNOS} turnos o menos.\n")

    for turno in range(1, TURNOS + 1):
        print(f"{AMARILLO}Turno {turno} de {TURNOS}{RESET}")
        mostrar_tablero(tablero)

        fila, columna = validar_disparo(disparos)

        if (fila, columna) in partes_restantes:
            tablero[fila][columna] = "O"
            partes_restantes.remove((fila, columna))
            print(f"{VERDE}¡Le Diste!{RESET}")
            if not partes_restantes:
                print(f"{VERDE}¡Hundiste el barco completo! Ganaste en {turno} turnos.{RESET}")
                mostrar_tablero(tablero)
                return
        else:
            tablero[fila][columna] = "X"
            print(f"{ROJO}Agua...{RESET}")

    print(f"{ROJO}Se acabaron los turnos. Perdiste.{RESET}")
    print("La ubicación del barco era:")
    for fila, columna in barco:
        tablero[fila][columna] = "O"
    mostrar_tablero(tablero)


def main() -> None:
    """
    Punto de entrada principal. Permite jugar varias partidas.
    """
    while True:
        jugar()
        opcion = input(f"{AZUL}¿Quieres jugar otra vez? (s/n): {RESET}").strip().lower()
        if opcion != "s":
            print(f"{AMARILLO}Gracias por jugar. ¡Hasta la próxima!{RESET}")
            break


if __name__ == "__main__":
    main()
