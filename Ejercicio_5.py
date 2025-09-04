# Ejercicio 5: Clasificador de Números (Par/Impar con Ternario)
# Crea un programa que pida un número y, usando un operador ternario, asigne a una variable el texto "Par" o "Impar". Luego, imprime el resultado. Adicionalmente, si el número es múltiplo de 5, debe imprimir un mensaje extra.
# Conceptos aplicados: Operador ternario, operador módulo (%), if.


def validaciones():
    """
    Solicita al usuario un número y valida la entrada.

    Reglas de validación:
    - No puede estar vacío.
    - Debe contener solo dígitos (sin letras ni símbolos).

    Returns:
        int: Número validado ingresado por el usuario.
    """
    while True:
        entrada = input("Ingrese un número: ").strip()

        if not entrada:
            print("Error: No puede dejar el campo vacío. Intente de nuevo.")
            continue

        if not entrada.isdigit():
            print("Error: El valor debe ser un número entero válido.")
            continue

        return int(entrada)


def main():
    """
    Programa principal que clasifica un número.

    - Determina si es par o impar.
    - Verifica si es múltiplo de 5.
    """
    numero = validaciones()

    clasificacion = "Par" if numero % 2 == 0 else "Impar"
    print(f"El número {numero} es {clasificacion}.")

    if numero % 5 == 0:
        print("Además, es múltiplo de 5.")


if __name__ == "__main__":
    main()










