# Ejercicio 4: Juego de Piedra, Papel o Tijeras
# Implementa el clásico juego para jugar contra la computadora.
# •	El usuario elige una opción y la computadora elige una al azar.
# •	El programa determina el ganador basándose en las reglas (piedra vence a tijeras, tijeras a papel, papel a piedra).
# •	Se debe llevar un conteo de las victorias del jugador y de la computadora. El juego termina cuando uno de los dos llegue a 3 victorias.
# Conceptos aplicados: random.choice(), bucle while, if/elif/else, contadores, f-strings


import random


def validar_opcion(opcion: str) -> str:
    """
    Valida la opción elegida por el jugador.

    Reglas de validación:
        - No puede estar vacía.
        - Debe ser exactamente: 'piedra', 'papel' o 'tijeras' (en minúsculas).

    Args:
        opcion (str): Opción ingresada por el jugador.

    Returns:
        str: Opción validada.

    Raises:
        ValueError: Si la opción es inválida.
    """
    if opcion is None or str(opcion).strip() == "":
        raise ValueError("La opción no puede estar vacía.")

    opcion = opcion.strip().lower()
    opciones_validas = ("piedra", "papel", "tijeras")

    if opcion not in opciones_validas:
        raise ValueError("Opción inválida. Solo se permite: piedra, papel o tijeras.")

    return opcion


def jugar_ronda(jugador: str, computadora: str) -> str:
    """
    Determina el resultado de una ronda de Piedra, Papel o Tijeras.

    Reglas:
        - Piedra vence a Tijeras.
        - Tijeras vencen a Papel.
        - Papel vence a Piedra.
        - Si ambos eligen lo mismo, es empate.

    Args:
        jugador (str): Elección del jugador.
        computadora (str): Elección de la computadora.

    Returns:
        str:
            - "jugador" si el jugador gana la ronda.
            - "computadora" si la computadora gana la ronda.
            - "empate" si ambos eligieron la misma opción.
    """
    jugador = validar_opcion(jugador)
    computadora = validar_opcion(computadora)

    if jugador == computadora:
        return "empate"

    if (
            (jugador == "piedra" and computadora == "tijeras")
            or (jugador == "tijeras" and computadora == "papel")
            or (jugador == "papel" and computadora == "piedra")
    ):
        return "jugador"

    return "computadora"


def main():
    """
    Función principal del juego Piedra, Papel o Tijeras.

    - Muestra las reglas al inicio.
    - Ejecuta rondas hasta que el jugador o la computadora ganen 3 veces.
    - Lleva un marcador actualizado después de cada ronda.
    - Declara un ganador final cuando alguno llega a 3 victorias.
    """
    print("=== Juego: Piedra, Papel o Tijeras ===")
    print("Reglas: piedra vence a tijeras, tijeras vence a papel, papel vence a piedra.")
    print("El primero que llegue a 3 victorias gana el juego.\n")

    victorias_jugador = 0
    victorias_computadora = 0

    while victorias_jugador < 3 and victorias_computadora < 3:
        try:
            jugador = input("Elige piedra, papel o tijeras: ").strip().lower()
            jugador = validar_opcion(jugador)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        computadora = random.choice(["piedra", "papel", "tijeras"])
        print(f"Computadora eligió: {computadora}")

        ganador = jugar_ronda(jugador, computadora)

        if ganador == "jugador":
            victorias_jugador += 1
            print("Ganaste esta ronda!")
        elif ganador == "computadora":
            victorias_computadora += 1
            print("La computadora gana esta ronda.")
        else:
            print("Es un empate.")

        print(f"Marcador → Jugador: {victorias_jugador} | Computadora: {victorias_computadora}\n")

    if victorias_jugador == 3:
        print("¡Felicidades! Ganaste el juego")
    else:
        print("La computadora ganó el juego. Intenta de nuevo.")


if __name__ == "__main__":
    main()



