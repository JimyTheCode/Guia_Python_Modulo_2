# Ejercicio 8: Filtrado de Datos con List Comprehensions
# Dada una lista de números [-5, 10, -15, 20, -25, 30], utiliza una list comprehension para crear tres nuevas listas:
# •	Una lista con solo los números positivos.
# •	Una lista con los cuadrados de todos los números.
# •	Una lista de strings que diga "positivo" o "negativo" para cada número, usando un ternario dentro de la comprensión.
# •	Conceptos aplicados: List comprehensions, operador ternario.



def validar_lista_numeros(lista) :
    """
    Valida que todos los elementos de una lista sean enteros o flotantes.

    Args:
        lista (list[int | float]): Lista de números.

    Returns:
        list[int | float]: Lista validada.

    Raises:
        ValueError: Si algún elemento no es numérico.
    """
    for num in lista:
        if not isinstance(num):
            raise ValueError(f"El valor {num} no es un número válido.")
    return lista


def filtrar_datos(lista) :
    """
    Genera tres listas a partir de la lista original usando list comprehensions.

    Args:
        lista (list[int | float]): Lista de números.

    Returns:
        tuple:
            - lista_positivos (list[int | float]): Solo los números positivos.
            - lista_cuadrados (list[int | float]): Cuadrados de todos los números.
            - lista_signos (list[str]): "positivo" o "negativo" según el número.
    """
    lista_validada = validar_lista_numeros(lista)

    lista_positivos = [num for num in lista_validada if num > 0]
    lista_cuadrados = [num ** 2 for num in lista_validada]
    lista_signos = ["positivo" if num >= 0 else "negativo" for num in lista_validada]

    return lista_positivos, lista_cuadrados, lista_signos


def mostrar_resultados(positivos: list[int | float],
                       cuadrados: list[int | float],
                       signos: list[str]) -> None:
    """
    Imprime los resultados de las listas generadas.

    Args:
        positivos (list[int | float]): Números positivos.
        cuadrados (list[int | float]): Cuadrados de los números.
        signos (list[str]): Estado de cada número ("positivo" o "negativo").
    """
    print("\n Resultados del Filtrado con List Comprehensions")
    print("-" * 50)
    print(f" Lista de positivos: {positivos}")
    print(f" Lista de cuadrados: {cuadrados}")
    print(f" Lista de signos: {signos}")


def main():
    """
    Función principal que define la lista inicial, aplica el filtrado
    y muestra los resultados.
    """
    try:
        lista_original = [-5, 10, -15, 20, -25, 30]

        positivos, cuadrados, signos = filtrar_datos(lista_original)
        mostrar_resultados(positivos, cuadrados, signos)

    except ValueError as e:
        print(f"Error en los datos: {e}")


if __name__ == "__main__":
    main()
