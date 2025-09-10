# Ejercicio 5: Clasificador de Números (Par/Impar con Ternario)
# Crea un programa que pida un número y, usando un operador ternario, asigne a una variable el texto "Par" o "Impar". Luego, imprime el resultado. Adicionalmente, si el número es múltiplo de 5, debe imprimir un mensaje extra.
# Conceptos aplicados: Operador ternario, operador módulo (%), if.


def clasificar_numero(numero: int) -> tuple[str, bool]:
    """
    Clasifica un número como Par o Impar, y determina si es múltiplo de 5.

    Args:
        numero (int): Número entero a clasificar.

    Returns:
        tuple:
            - str: "Par" o "Impar".
            - bool: True si es múltiplo de 5, False en caso contrario.
    """
    clasificacion = "Par" if numero % 2 == 0 else "Impar"
    multiplo_5 = numero % 5 == 0
    return clasificacion, multiplo_5


def validaciones():
    """
    Solicita al usuario un número y valida la entrada.

    Reglas de validación:
    - No puede estar vacío.
    - Debe contener solo dígitos (sin letras ni símbolos).
    - No se permiten decimales ni números negativos.

    Returns:
        int: Número validado ingresado por el usuario.
    """
    while True:
        entrada = input("Ingrese un número: ").strip()

        if not entrada:
            print("Error: No puede dejar el campo vacío. Intente de nuevo.")
            continue

        if not entrada.isdigit():
            print("Error: El valor debe ser un número entero positivo válido.")
            continue

        return int(entrada)


def main():
    """
    Programa principal que clasifica un número.

    - Determina si es par o impar.
    - Verifica si es múltiplo de 5.
    """
    numero = validaciones()
    clasificacion, multiplo_5 = clasificar_numero(numero)

    print(f"El número {numero} es {clasificacion}.")

    if multiplo_5:
        print("Además, es múltiplo de 5.")


if __name__ == "__main__":
    main()










