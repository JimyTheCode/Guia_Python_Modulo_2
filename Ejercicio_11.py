# Ejercicio 11: Validador de Cédula (Algoritmo Simple)
# Escribe una función que valide un número de cédula (como string) basado en una regla simple: la suma de sus dígitos debe ser un número par. La función debe devolver True si es válido y False si no:
# •	Adicionalmente, el programa principal debe pedir al usuario su cédula hasta que ingrese una válida, usando un bucle.
# Conceptos aplicados: Funciones, bucle while, conversión de tipos (str a int), bucle for sobre un string.


def validar_cedula(cedula):
    """
    Valida un número de cédula bajo reglas simples.

    Args:
        cedula (str): Número de cédula en formato string.

    Returns:
        bool: True si la cédula es válida, False en caso contrario.
    """
    if not cedula.isdigit():
        print("Error: La cédula solo puede contener números.")
        return False

    if not (6 <= len(cedula) <= 15):
        print("Error: La cédula debe tener entre 6 y 15 dígitos.")
        return False

    suma_digitos = sum(int(d) for d in cedula)

    if suma_digitos % 2 != 0:
        print("Error: La suma de los dígitos debe ser par.")
        return False

    return True


def main():
    """
    Solicita la cédula al usuario hasta que sea válida.
    """
    while True:
        cedula = input("Ingrese su número de cédula: ").strip()
        if validar_cedula(cedula):
            print("Cédula válida. Proceso finalizado.")
            break


if __name__ == "__main__":
    main()

