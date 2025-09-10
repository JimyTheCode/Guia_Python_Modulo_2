# Ejercicio 1: Sistema de Precios de Entradas de Cine
# Crea un programa que calcule el precio de una entrada de cine basándose en la edad del cliente y si es estudiante:
# Reglas:
# •	Niños (menores de 12 años): $10.000.
# •	Jóvenes (12 a 17 años): $15.000.
# •	Adultos (18 años en adelante): $20.000.
# •	Si el cliente es estudiante (independientemente de la edad), tiene un 10% de descuento.
# El programa debe pedir la edad y si es estudiante ('si' o 'no').
# Conceptos aplicados: if/elif/else anidados, operadores lógicos (and, or), input(), int(), lower(), f-strings.


def validar_edad(valor):
    """
    Valida la edad ingresada.
    - Debe ser un número entero positivo entre 1 y 90.
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError("La edad no puede estar vacía.")

    if not str(valor).lstrip("-").isdigit():
        raise ValueError("La edad debe ser un número entero positivo.")

    valor = int(valor)

    if valor <= 0:
        raise ValueError("La edad debe ser mayor que 0.")
    if valor > 90:
        raise ValueError("La edad ingresada no es válida (máximo permitido: 90 años).")

    return valor


def validar_estudiante(valor):
    """
    Valida si la persona es estudiante.
    Solo se acepta 'si' o 'no' (insensible a mayúsculas).
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError("La respuesta no puede estar vacía.")

    valor = str(valor).strip().lower()
    if valor not in ("si", "no"):
        raise ValueError("Solo se permite responder 'si' o 'no'.")

    return valor == "si"


def validar_cantidad(valor):
    """
    Valida la cantidad de personas para un grupo.
    - Debe ser entero positivo entre 1 y 15.
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError("La cantidad no puede estar vacía.")

    if not str(valor).lstrip("-").isdigit():
        raise ValueError("La cantidad debe ser un número entero positivo.")

    valor = int(valor)

    if valor <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")
    if valor > 15:
        raise ValueError("El máximo permitido es 15 personas en un solo grupo.")

    return valor


def validar_opcion(valor):
    """
    Valida la opción del menú principal.
    Solo se acepta 1, 2 o 3.
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError("La opción no puede estar vacía.")

    if not str(valor).isdigit():
        raise ValueError("La opción debe ser un número.")

    opcion = int(valor)
    if opcion not in (1, 2, 3):
        raise ValueError("Opción inválida. Debe ser 1, 2 o 3.")

    return opcion



def calcular_precio(edad, es_estudiante):
    """Calcula el precio de la entrada según reglas del cine."""
    if edad < 12:
        precio = 10000
    elif edad <= 17:
        precio = 15000
    else:
        precio = 20000

    return int(precio * 0.9) if es_estudiante else precio


def obtener_edad():
    while True:
        try:
            valor = input("Ingrese la edad del cliente: ")
            return validar_edad(valor)
        except ValueError as e:
            print("Error:", e)


def obtener_estudiante():
    while True:
        try:
            valor = input("¿Es estudiante? (si/no): ")
            return validar_estudiante(valor)
        except ValueError as e:
            print("Error:", e)


def menu_opcion():
    while True:
        try:
            valor = input("Seleccione una opción (1, 2 o 3): ")
            return validar_opcion(valor)
        except ValueError as e:
            print("Error:", e)


def procesar_una_entrada():
    edad = obtener_edad()
    es_estudiante = obtener_estudiante()
    precio = calcular_precio(edad, es_estudiante)

    print("----------------------------------------------------")
    print(f"Edad del cliente: {edad} años")
    print(f"Estudiante: {'Sí' if es_estudiante else 'No'}")
    print(f"Precio de la entrada: ${precio:,}")
    print("----------------------------------------------------")
    return precio


def procesar_varias_entradas():
    while True:
        try:
            valor = input("Ingrese la cantidad de personas en el grupo: ")
            cantidad = validar_cantidad(valor)
            break
        except ValueError as e:
            print("Error:", e)

    total = 0
    print("\n--- Detalle de cada persona ---")
    for i in range(1, cantidad + 1):
        print(f"\nPersona {i}:")
        precio = procesar_una_entrada()
        total += precio

    print("\n====================================================")
    print(f"Total a pagar por {cantidad} entradas: ${total:,}")
    print("====================================================")


def main():
    print("Bienvenido al Sistema de Precios de Entradas de Cine")
    print("----------------------------------------------------")

    while True:
        print("\nMenú principal:")
        print("1. Comprar una sola entrada")
        print("2. Comprar varias entradas (grupo/familia)")
        print("3. Salir")

        opcion = menu_opcion()

        if opcion == 1:
            procesar_una_entrada()
        elif opcion == 2:
            procesar_varias_entradas()
        elif opcion == 3:
            print("Gracias por usar nuestro sistema de entradas.")
            break


if __name__ == "__main__":
    main()


