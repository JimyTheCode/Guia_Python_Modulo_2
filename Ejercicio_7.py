# Ejercicio 7: Combinador de Listas con zip
# Dadas dos listas, una con nombres de estudiantes y otra con sus respectivas notas finales, crea una función que las combine para generar un diccionario. Las claves serán los nombres y los valores las notas:
# •	Luego, itera sobre el diccionario resultante para imprimir un reporte del tipo: "El estudiante [Nombre] tiene una nota de [Nota]".
# Conceptos aplicados: Funciones, zip(), dict(), bucle for sobre diccionarios.


def validar_nombre(nombre) :
    """
    Valida que el nombre contenga solo letras y cumpla con las restricciones.

    Args:
        nombre (str): Nombre del estudiante.

    Returns:
        str: Nombre válido.

    Raises:
        ValueError: Si el nombre no cumple las condiciones.
    """
    if not nombre.strip():
        raise ValueError(" El nombre no puede estar vacío.")
    if not nombre.isalpha():
        raise ValueError(" El nombre solo puede contener letras (sin números ni símbolos).")
    if len(nombre) < 2 or len(nombre) > 30:
        raise ValueError(" El nombre debe tener entre 2 y 30 caracteres.")
    return nombre


def validar_nota(nota) :
    """
    Valida que la nota sea un número flotante válido dentro del rango permitido.

    Args:
        nota (float): Nota del estudiante.

    Returns:
        float: Nota válida.

    Raises:
        ValueError: Si la nota no cumple las condiciones.
    """
    if not isinstance(nota):
        raise ValueError(" La nota debe ser un número.")
    if nota < 0.0 or nota > 5.0:
        raise ValueError(" La nota debe estar entre 0.0 y 5.0.")
    return float(nota)


def combinar_listas(nombres, notas) :
    """
    Combina dos listas en un diccionario donde los nombres son claves
    y las notas son valores, validando cada dato.

    Args:
        nombres (list[str]): Lista de nombres de estudiantes.
        notas (list[float]): Lista de notas finales.

    Returns:
        dict[str, float]: Diccionario con pares nombre-nota.
    """
    nombres_validados = [validar_nombre(n) for n in nombres]
    notas_validadas = [validar_nota(n) for n in notas]

    return dict(zip(nombres_validados, notas_validadas))


def mostrar_reporte(estudiantes) -> None:
    """
    Imprime un reporte con los estudiantes y sus respectivas notas.

    Args:
        estudiantes (dict[str, float]): Diccionario de estudiantes y notas.
    """
    print("\n Reporte de Notas")
    print("-" * 30)
    for nombre, nota in estudiantes.items():
        print(f" El estudiante {nombre} tiene una nota de {nota:.2f}")


def main():
    """
    Función principal que define las listas de ejemplo, combina los datos
    y muestra el reporte.
    """
    try:
        nombres = ["Ana", "Carlos", "Beatriz", "Luis"]
        notas = [4.5, 3.8, 5.0, 2.9]

        estudiantes = combinar_listas(nombres, notas)
        mostrar_reporte(estudiantes)

    except ValueError as e:
        print(f"Error en los datos: {e}")


if __name__ == "__main__":
    main()
