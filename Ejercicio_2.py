# Ejercicio 2: Intérprete de Comandos Sencillo
# Desarrolla un programa que simule un menú de consola usando la estructura match-case.
# El programa mostrará una lista de comandos disponibles ("guardar", "cargar", "salir")
# y el usuario ingresará uno. El programa debe ejecutar una acción simulada para cada comando.
# Si el comando no es válido, debe mostrar un mensaje de error.
# El programa debe seguir pidiendo comandos hasta que el usuario escriba "salir".
# Conceptos aplicados: Bucle while, match-case, input(), lower().


def validar_comando(valor):
    """
    Valida que el comando ingresado sea correcto.
    Reglas:
        - No puede estar vacío.
        - Solo puede contener letras (sin números ni símbolos).
        - Se devuelve en minúsculas.

    Args:
        valor (str): Comando ingresado por el usuario.

    Returns:
        str: Comando validado en minúsculas.

    Raises:
        ValueError: Si el comando es vacío o contiene caracteres no permitidos.
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError("El comando no puede estar vacío.")

    valor = str(valor).strip().lower()

    if not valor.isalpha():
        raise ValueError("El comando solo puede contener letras (sin números ni símbolos).")

    return valor


def obtener_comando():
    """
    Solicita un comando al usuario y lo valida mediante `validar_comando`.

    Returns:
        str: Comando válido ingresado por el usuario.
    """
    while True:
        comando = input("Ingrese un comando (guardar, cargar, salir): ")
        try:
            return validar_comando(comando)
        except ValueError as e:
            print(f"Error: {e}")


def ejecutar_comando(comando):
    """
    Ejecuta la acción correspondiente según el comando ingresado.

    Args:
        comando (str): El comando validado previamente.

    Returns:
        str: Mensaje con el resultado de la acción.
    """
    match comando:
        case "guardar":
            return "Guardando archivo... Operación completada."
        case "cargar":
            return "Cargando archivo... Operación completada."
        case "salir":
            return "Saliendo del programa. ¡Hasta luego!"
        case _:
            return "Error: Comando no reconocido. Intente de nuevo."


def main():
    """
    Función principal del programa.

    Muestra un menú de consola con comandos disponibles,
    solicita al usuario que ingrese uno, lo valida y lo ejecuta.
    El programa continúa en bucle hasta que el usuario escriba "salir".
    """
    print("=== Menú de Consola ===")
    print("Comandos disponibles: guardar, cargar, salir")

    while True:
        comando = obtener_comando()
        mensaje = ejecutar_comando(comando)
        print(mensaje)

        if comando == "salir":
            break


if __name__ == "__main__":
    main()


