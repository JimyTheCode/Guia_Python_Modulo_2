# Ejercicio 2: Intérprete de Comandos Sencillo
# Desarrolla un programa que simule un menú de consola usando la estructura match-case. El programa mostrará una lista de comandos disponibles ("guardar", "cargar", "salir") y el usuario ingresará uno
# •	El programa debe ejecutar una acción simulada para cada comando (ej. imprimir "Guardando archivo...").
# •	Si el comando no es válido, debe mostrar un mensaje de error.
# •	El programa debe seguir pidiendo comandos hasta que el usuario escriba "salir".
# •	Conceptos aplicados: Bucle while, match-case, input(), lower().



def obtener_comando():
    """
    Solicita al usuario un comando y valida que sea válido.

    El comando debe cumplir las siguientes reglas:
        - No puede estar vacío.
        - Solo puede contener letras (sin números ni símbolos).
        - Debe estar en minúsculas tras la conversión.

    Returns:
        str: El comando validado ingresado por el usuario.
    """
    while True:
        comando = input("Ingrese un comando (guardar, cargar, salir): ").strip().lower()

        if not comando:
            print("Error: No puede dejar el campo vacío. Intente de nuevo.")
            continue

        if not comando.isalpha():
            print("Error: El comando solo puede contener letras (sin números ni símbolos).")
            continue

        return comando


def ejecutar_comando(comando):
    """
    Ejecuta la acción correspondiente según el comando ingresado.

    Usa una estructura match-case para seleccionar la acción:
        - "guardar": simula el guardado de un archivo.
        - "cargar": simula la carga de un archivo.
        - "salir": termina el programa.
        - Otro valor: muestra un error.

    Args:
        comando (str): El comando validado previamente por el usuario.

    Returns:
        None
    """
    match comando:
        case "guardar":
            print("Guardando archivo... Operación completada.")
        case "cargar":
            print("Cargando archivo... Operación completada.")
        case "salir":
            print("Saliendo del programa. ¡Hasta luego!")
        case _:
            print("Error: Comando no reconocido. Intente de nuevo.")


def main():
    """
    Función principal del programa.

    Muestra un menú de consola con comandos disponibles,
    solicita al usuario que ingrese uno, lo valida y lo ejecuta.
    El programa continúa en bucle hasta que el usuario escriba "salir".

    Returns:
        None
    """
    print("=== Menú de Consola ===")
    print("Comandos disponibles: guardar, cargar, salir")

    while True:
        comando = obtener_comando()
        ejecutar_comando(comando)

        if comando == "salir":
            break


if __name__ == "__main__":
    main()


