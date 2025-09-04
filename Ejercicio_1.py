# Ejercicio 1: Sistema de Precios de Entradas de Cine
# Crea un programa que calcule el precio de una entrada de cine basándose en la edad del cliente y si es estudiante:
# Reglas:
# •	Niños (menores de 12 años): $10.000.
# •	Jóvenes (12 a 17 años): $15.000.
# •	Adultos (18 años en adelante): $20.000.
# •	Si el cliente es estudiante (independientemente de la edad), tiene un 10% de descuento.
# El programa debe pedir la edad y si es estudiante ('si' o 'no').
# Conceptos aplicados: if/elif/else anidados, operadores lógicos (and, or), input(), int(), lower(), f-strings.



def obtener_edad():
    """
    Solicita y valida la edad del cliente.

    Reglas de validación:
        - No puede estar vacío.
        - Debe ser un número entero positivo.
        - Debe ser mayor que 0 y menor o igual a 90.

    Returns:
        int: La edad validada del cliente.
    """
    while True:
        edad = input("Ingrese la edad del cliente (solo números enteros positivos): ").strip()

        if not edad:
            print("Error: No puede dejar el campo vacío. Intente de nuevo.")
            continue

        if not edad.isdigit():
            print("Error: La edad debe contener únicamente números enteros positivos.")
            continue

        edad = int(edad)

        if edad <= 0:
            print("Error: La edad debe ser un número mayor a 0.")
            continue
        if edad > 90:
            print("Error: La edad ingresada no es válida (máximo permitido: 90 años).")
            continue

        return edad


def obtener_estudiante():
    """
    Pregunta al cliente si es estudiante y valida la respuesta.

    Reglas de validación:
        - No puede estar vacío.
        - Solo se acepta 'si' o 'no' (en minúsculas).

    Returns:
        bool: True si el cliente es estudiante, False en caso contrario.
    """
    while True:
        respuesta = input("¿Es estudiante? (si/no): ").strip().lower()

        if not respuesta:
            print("Error: No puede dejar el campo vacío. Intente de nuevo.")
            continue

        if respuesta not in ("si", "no"):
            print("Error: Responda únicamente con 'si' o 'no'.")
            continue

        return respuesta == "si"


def calcular_precio(edad, es_estudiante):
    """
    Calcula el precio de la entrada en función de la edad y condición de estudiante.

    Reglas de precios:
        - Menores de 12 años: $10,000
        - De 12 a 17 años: $15,000
        - Mayores de 17 años: $20,000
        - Descuento del 10% si es estudiante.

    Args:
        edad (int): Edad validada del cliente.
        es_estudiante (bool): Indica si el cliente es estudiante.

    Returns:
        int: Precio final de la entrada.
    """
    if edad < 12:
        precio = 10000
    elif edad <= 17:
        precio = 15000
    else:
        precio = 20000

    precio_final = precio * 0.9 if es_estudiante else precio
    return int(precio_final)


def procesar_una_entrada():
    """
    Procesa la compra de una sola entrada.

    Flujo:
        - Solicita edad y condición de estudiante.
        - Calcula el precio con posibles descuentos.
        - Muestra el detalle de la compra.

    Returns:
        int: Precio final de la entrada comprada.
    """
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
    """
    Procesa la compra de varias entradas (grupo o familia).

    Reglas de validación:
        - La cantidad debe ser un número entero positivo.
        - Mínimo 1 persona, máximo 15 personas por grupo.

    Flujo:
        - Solicita la cantidad de personas.
        - Procesa los datos de cada persona individualmente.
        - Calcula y muestra el total del grupo.

    Returns:
        None
    """
    while True:
        cantidad = input("Ingrese la cantidad de personas en el grupo: ").strip()

        if not cantidad:
            print("Error: No puede dejar el campo vacío.")
            continue

        if not cantidad.isdigit():
            print("Error: Debe ingresar únicamente números enteros positivos.")
            continue

        cantidad = int(cantidad)

        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor a 0.")
            continue
        if cantidad > 15:
            print("Error: El máximo permitido es 15 personas en un solo grupo.")
            continue

        break

    total = 0
    print("\n--- Detalle de cada persona ---")
    for i in range(1, cantidad + 1):
        print(f"\nPersona {i}:")
        precio = procesar_una_entrada()
        total += precio

    print("\n====================================================")
    print(f"Total a pagar por {cantidad} entradas: ${total:,}")
    print("====================================================")


def menu_opcion():
    """
    Solicita y valida la opción elegida en el menú principal.

    Reglas de validación:
        - No puede estar vacío.
        - Solo se permiten números enteros.
        - La opción debe ser 1, 2 o 3.

    Returns:
        int: Opción elegida por el usuario.
    """
    while True:
        opcion = input("Seleccione una opción (1, 2 o 3): ").strip()

        if not opcion:
            print("Error: No puede dejar el campo vacío.")
            continue

        if not opcion.isdigit():
            print("Error: Solo se permiten números (1, 2 o 3).")
            continue

        opcion = int(opcion)

        if opcion not in (1, 2, 3):
            print("Error: Opción inválida. Debe elegir alguna de las opciones 1, 2 o 3.")
            continue

        return opcion


def main():
    """
    Función principal del programa.

    Flujo:
        - Muestra un menú principal con opciones.
        - Permite comprar una entrada, varias entradas o salir.
        - Llama a las funciones correspondientes según la elección.

    Returns:
        None
    """
    print("Bienvenido al Sistema de Precios de Entradas de Cine")
    print("----------------------------------------------------")

    while True:
        print("\nMenú principal:")
        print("Elija el número de la opción que desea realizar")
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

