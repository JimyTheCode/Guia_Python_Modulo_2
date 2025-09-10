# Ejercicio 12: Simulador de Lanzamiento de Dados
# •	Crea un programa que simule el lanzamiento de dos dados 10,000 veces.
# •	Usa un diccionario para contar la frecuencia de cada posible suma de los dados (de 2 a 12).
# •	Al final, imprime un reporte con la frecuencia de cada suma.
# Conceptos aplicados: random.randint(), bucles, diccionarios como contadores, método get().

import random


def lanzar_dados():
    """
    Simula el lanzamiento de dos dados.

    Returns:
        int: La suma de los valores de los dos dados (entre 2 y 12).
    """
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2


def simular_lanzamientos(n=10000):
    """
    Simula múltiples lanzamientos de dos dados y cuenta la frecuencia
    de cada suma posible (2 a 12).

    Args:
        n (int): Número de lanzamientos a simular (por defecto 10,000).

    Returns:
        dict: Diccionario con la suma como clave y la frecuencia como valor.
    """
    if n <= 0:
        raise ValueError("El número de lanzamientos debe ser positivo.")

    # inicializamos el contador con comprehension
    frecuencias = {suma: 0 for suma in range(2, 13)}

    for _ in range(n):
        suma = lanzar_dados()
        frecuencias[suma] += 1

    return frecuencias


def mostrar_reporte(frecuencias):
    """
    Imprime un reporte de las frecuencias de cada suma.

    Args:
        frecuencias (dict): Diccionario con las frecuencias.
    """
    print("\n--- Reporte de Frecuencias ---")
    for suma in range(2, 13):
        print(f"Suma {suma:2}: {frecuencias.get(suma, 0)} veces")


def main():
    """
    Función principal que ejecuta la simulación y muestra el reporte.
    """
    try:
        num_lanzamientos = 10000
        frecuencias = simular_lanzamientos(num_lanzamientos)
        mostrar_reporte(frecuencias)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
