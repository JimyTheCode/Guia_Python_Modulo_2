# Ejercicio 11: Validador de Cédula (Algoritmo Simple)
# Escribe una función que valide un número de cédula (como string) basado en una regla simple: la suma de sus dígitos debe ser un número par. La función debe devolver True si es válido y False si no:
# •	Adicionalmente, el programa principal debe pedir al usuario su cédula hasta que ingrese una válida, usando un bucle.
# Conceptos aplicados: Funciones, bucle while, conversión de tipos (str a int), bucle for sobre un string.



def validar_cedula(cedula) :
    """
    Valida que la cédula cumpla con las condiciones:
    - Debe ser un string compuesto únicamente por dígitos.
    - Debe tener una longitud entre 6 y 15 caracteres.
    - La suma de sus dígitos debe ser par.

    Args:
        cedula (str): Número de cédula en formato string.

    Returns:
        bool: True si es válida, False si no.
    """
    if not cedula.isdigit():
        print("Error: La cédula solo puede contener números (positivos).")
        return False
    if len(cedula) < 6 or len(cedula) > 15:
        print("Error: La cédula debe tener entre 6 y 15 dígitos.")
        return False

    suma_digitos = sum(int(digito) for digito in cedula)

    if suma_digitos % 2 != 0:
        print("Error: La suma de los dígitos debe ser un número par.")
        return False

    return True


def main():
    """
    Función principal que solicita al usuario ingresar su cédula
    hasta que se valide correctamente.
    """
    while True:
        cedula = input("Ingrese su número de cédula: ").strip()
        if validar_cedula(cedula):
            print("Cédula válida. Proceso finalizado.")
            break


if __name__ == "__main__":
    main()
