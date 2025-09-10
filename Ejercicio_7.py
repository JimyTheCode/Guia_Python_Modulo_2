# Ejercicio 7: Combinador de Listas con zip
# Dadas dos listas, una con nombres de estudiantes y otra con sus respectivas notas finales, crea una función que las combine para generar un diccionario. Las claves serán los nombres y los valores las notas:
# •	Luego, itera sobre el diccionario resultante para imprimir un reporte del tipo: "El estudiante [Nombre] tiene una nota de [Nota]".
# Conceptos aplicados: Funciones, zip(), dict(), bucle for sobre diccionarios.



def validar_nombre(nombre):
    """
    Valida que un nombre sea correcto según las siguientes reglas:

    - No debe estar vacío.
    - Solo puede contener letras (sin números, espacios ni símbolos).
    - Debe tener entre 2 y 30 caracteres.

    Parameters
    ----------
    nombre : str
        Nombre del estudiante a validar.

    Returns
    -------
    str
        El nombre validado.
    """
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if not nombre.isalpha():
        raise ValueError("El nombre solo puede contener letras (sin números ni símbolos).")
    if len(nombre) < 2 or len(nombre) > 30:
        raise ValueError("El nombre debe tener entre 2 y 30 caracteres.")
    return nombre


def validar_nota(nota):
    """
    Valida que una nota sea un número válido dentro del rango permitido (0.0 a 5.0).

    Parameters
    ----------
    nota : int or float
        Nota a validar.

    Returns
    -------
    float
        La nota validada convertida a float.
    """
    if not isinstance(nota, (int, float)):
        raise ValueError("La nota debe ser un número.")
    if nota < 0.0 or nota > 5.0:
        raise ValueError("La nota debe estar entre 0.0 y 5.0.")
    return float(nota)


def combinar_listas(nombres, notas):
    """
    Combina dos listas en un diccionario donde:

    - Las claves son los nombres de los estudiantes (validados).
    - Los valores son las notas correspondientes (validadas).

    Parameters
    ----------
    nombres : list of str
        Lista de nombres de estudiantes.
    notas : list of int or float
        Lista de notas correspondientes a los estudiantes.

    Returns
    -------
    dict
        Diccionario en el que las claves son nombres y los valores son notas.
    """
    return {
        validar_nombre(nombre): validar_nota(nota)
        for nombre, nota in zip(nombres, notas)
    }


def mostrar_reporte(estudiantes):
    """
    Imprime un reporte legible de los estudiantes y sus notas.

    Parameters
    ----------
    estudiantes : dict
        Diccionario con los nombres como claves y las notas como valores.

    Returns
    -------
    None
        Esta función imprime en consola, no retorna nada.
    """
    print("\nReporte de Notas")
    print("-" * 30)

    reporte = {
        nombre: f"El estudiante {nombre} tiene una nota de {nota:.2f}"
        for nombre, nota in estudiantes.items()
    }

    for linea in reporte.values():
        print(linea)


def main():
    """
    Función principal que ejecuta el flujo del programa:

    1. Define listas de nombres y notas.
    2. Combina y valida los datos en un diccionario.
    3. Muestra el reporte final de estudiantes y notas.

    Returns
    -------
    None
    """
    try:
        nombres = ["Ana", "Carlos", "Beatriz", "Luis"]
        notas = [4.5, 3.8, 5.0, 2.9]

        estudiantes = combinar_listas(nombres, notas)
        mostrar_reporte(estudiantes)

    except ValueError as e:
        print(f"Error en los datos: {e}")

