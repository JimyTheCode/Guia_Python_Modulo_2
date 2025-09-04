"""
Ejercicio 14: Juego del Ahorcado (Hangman)
Diseña una versión para consola del clásico juego del "Ahorcado". El programa debe ser capaz de gestionar toda la lógica del juego, desde la selección de la palabra hasta determinar si el jugador ha ganado o perdido.
Lógica del Juego:
•	El programa debe tener una lista predefinida de palabras secretas y seleccionar una al azar para cada partida.
•	Debe mostrar al jugador el "tablero", que consiste en guiones bajos representando las letras de la palabra secreta y una lista de las letras ya intentadas.
•	El jugador tiene un número limitado de intentos (ej. 6 vidas).
•	En cada turno, el jugador ingresa una letra. El programa debe validar si la entrada es una sola letra y si no ha sido intentada antes.
•	Si la letra está en la palabra secreta, se revelan todas sus apariciones (ej. _ _ _ _ _ -> _ a _ a _). Si no está, el jugador pierde una vida.
•	El juego termina cuando el jugador adivina todas las letras (gana) o se queda sin vidas (pierde).
Conceptos integrados: Lógica de juegos, random.choice, listas y/o sets (para letras adivinadas), manipulación de strings, bucles while, condicionales if/else, funciones para modularizar (ej. mostrar_tablero(), validar_entrada()), manejo de estado del juego.

"""

import random

# Colores ANSI
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"

AHORCADO_ASCII = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def seleccionar_palabra() -> str:
    """
    Selecciona una palabra secreta de una lista predefinida.

    Returns:
        str: Palabra secreta elegida aleatoriamente.
    """
    palabras = ["python", "ahorcado", "computadora", "teclado", "juego", "programacion"]
    return random.choice(palabras)


def mostrar_tablero(palabra, letras_adivinadas, vidas) -> None:
    """
    Muestra el estado actual del juego.

    - Dibuja el ahorcado en ASCII según las vidas restantes.
    - Muestra la palabra secreta parcialmente adivinada.
    - Lista las letras que el jugador ya intentó.

    Args:
        palabra (str): La palabra secreta que se debe adivinar.
        letras_adivinadas (set[str]): Conjunto de letras que el jugador ya adivinó.
        vidas (int): Número de vidas restantes.
    """
    print(AHORCADO_ASCII[len(AHORCADO_ASCII) - vidas - 1])
    palabra_mostrada = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])
    print(f"\nPalabra: {AMARILLO}{palabra_mostrada}{RESET}")
    print(f"Letras usadas: {', '.join(sorted(letras_adivinadas)) if letras_adivinadas else 'Ninguna'}")
    print(f"Vidas restantes: {VERDE}{vidas}{RESET}\n")


def validar_letra(letras_usadas) :
    """
    Solicita al jugador una letra y valida la entrada.

    Reglas de validación:
    - No puede estar vacía.
    - Solo se permite una letra.
    - No se permiten números, símbolos o espacios (solo letras).
    - No puede ser una letra ya usada.

    Args:
        letras_usadas (set[str]): Conjunto de letras que el jugador ya intentó.

    Returns:
        str: Letra válida en minúsculas.
    """
    while True:
        entrada = input(f"{AZUL}Ingresa una letra:{RESET} ").strip().lower()

        if not entrada:
            print(f"{ROJO}No puedes dejar el campo vacío. Intenta de nuevo.{RESET}")
            continue

        if len(entrada) != 1:
            print(f"{ROJO}Debes ingresar solo una letra.{RESET}")
            continue

        if not entrada.isalpha():
            print(f"{ROJO}Solo se permiten letras (sin números ni símbolos).{RESET}")
            continue

        if entrada in letras_usadas:
            print(f"{AMARILLO}Ya intentaste la letra '{entrada}'. Elige otra.{RESET}")
            continue

        return entrada


def jugar() -> None:
    """
    Función principal que ejecuta el juego del ahorcado.

    - Selecciona una palabra secreta al azar.
    - Controla el bucle principal del juego.
    - Permite al jugador adivinar letras hasta ganar o perder.
    """
    print(f"{AZUL}Bienvenido al juego del Ahorcado.{RESET}")
    print("Adivina la palabra secreta antes de quedarte sin vidas.\n")

    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    vidas = 6

    while vidas > 0:
        mostrar_tablero(palabra, letras_adivinadas, vidas)

        letra = validar_letra(letras_adivinadas)
        letras_adivinadas.add(letra)

        if letra in palabra:
            print(f"{VERDE}¡Bien hecho! La letra '{letra}' está en la palabra.{RESET}")
        else:
            vidas -= 1
            print(f"{ROJO}Fallaste. La letra '{letra}' no está en la palabra.{RESET}")

        # Verificar si todas las letras han sido adivinadas
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"\n{VERDE}¡Felicidades! Adivinaste la palabra: {palabra}{RESET}")
            break
    else:
        mostrar_tablero(palabra, letras_adivinadas, 0)
        print(f"\n{ROJO}Te quedaste sin vidas. La palabra era: {palabra}{RESET}")


def main() -> None:
    """
    Punto de entrada principal del programa.

    Permite al jugador jugar varias partidas si lo desea.
    """
    while True:
        jugar()
        opcion = input(f"\n{AZUL}¿Quieres jugar de nuevo? (s/n): {RESET}").strip().lower()
        if opcion != "s":
            print(f"{AMARILLO}Gracias por jugar. ¡Hasta la próxima!{RESET}")
            break


if __name__ == "__main__":
    main()
