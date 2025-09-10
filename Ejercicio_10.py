# Ejercicio 10: Transposición de una Matriz
# Crea una función que reciba una matriz (lista de listas) y devuelva su transpuesta. La transpuesta se logra intercambiando filas por columnas.
# •	Ejemplo: [[1, 2, 3], [4, 5, 6]] se convierte en [[1, 4], [2, 5], [3, 6]].
# •	Resuelve este problema usando bucles for anidados y luego intenta resolverlo con una list comprehension anidada.
# Conceptos aplicados: Listas anidadas (matrices), bucles anidados, list comprehensions anidadas.


def validar_matriz(matriz):
    """
    Valida que la matriz sea una lista de listas con dimensiones correctas.

    Args:
        matriz (list[list]): Matriz a validar.

    Returns:
        list[list]: Matriz validada.
    """
    if not matriz or not isinstance(matriz, list):
        raise ValueError(" La matriz debe ser una lista no vacía.")
    if not all(isinstance(fila, list) for fila in matriz):
        raise ValueError(" Cada fila de la matriz debe ser una lista.")
    if not all(len(fila) == len(matriz[0]) for fila in matriz):
        raise ValueError(" Todas las filas deben tener la misma longitud.")
    return matriz


def transponer_matriz_for(matriz):
    """
    Transpone una matriz usando bucles for anidados.

    Args:
        matriz (list[list]): Matriz a transponer.

    Returns:
        list[list]: Matriz transpuesta.
    """
    matriz = validar_matriz(matriz)
    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = []
    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)

    return transpuesta


def transponer_matriz_comprehension(matriz):
    """
    Transpone una matriz usando list comprehension anidada.

    Args:
        matriz (list[list]): Matriz a transponer.

    Returns:
        list[list]: Matriz transpuesta.
    """
    matriz = validar_matriz(matriz)
    return [[fila[j] for fila in matriz] for j in range(len(matriz[0]))]


def mostrar_matriz(matriz, titulo) -> None:
    """
    Muestra una matriz en formato legible.

    Args:
        matriz (list[list]): Matriz a mostrar.
        titulo (str): Título descriptivo.
    """
    print(f"\n {titulo}")
    for fila in matriz:
        print(fila)


def main():
    """
    Función principal que prueba la transposición de matrices.
    """
    try:
        matriz = [[1, 2, 3], [4, 5, 6]]

        mostrar_matriz(matriz, "Matriz Original")

        transpuesta_for = transponer_matriz_for(matriz)
        mostrar_matriz(transpuesta_for, "Transpuesta con for anidados")

        transpuesta_compr = transponer_matriz_comprehension(matriz)
        mostrar_matriz(transpuesta_compr, "Transpuesta con list comprehension")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
