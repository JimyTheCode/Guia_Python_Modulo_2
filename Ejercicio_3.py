# Ejercicio 3: Validador de Contraseñas
# Escribe un programa que pida al usuario crear una contraseña y la valide usando un bucle while. El bucle solo terminará cuando la contraseña cumpla todos los criterios:
# •	Mínimo 8 caracteres de longitud.
# •	Contiene al menos una letra mayúscula.
# •	Contiene al menos un número.
# •	En cada intento fallido, el programa debe indicar qué regla no se cumplió.
# Conceptos aplicados: Bucle while True, if/elif/else, len(), métodos de string (isupper(), islower(), isdigit()), break.


def leer_password() -> str:
    """
    Solicita al usuario que cree una contraseña y valida que no esté vacía.

    El proceso continúa en bucle hasta que el usuario ingrese un valor válido.

    Returns:
        str: La contraseña ingresada por el usuario.
    """
    while True:
        contra = input("Cree una contraseña: ").strip()

        if not contra:
            print("Error: la contraseña no puede estar vacía.")
            continue

        return contra


def validar_password(contra: str) -> list[str]:
    """
    Valida si una contraseña cumple con las reglas de seguridad definidas.

    Reglas de validación:
        - Debe tener al menos 8 caracteres.
        - Debe contener al menos una letra mayúscula.
        - Debe contener al menos un número.

    Args:
        contra (str): La contraseña ingresada por el usuario.

    Returns:
        list[str]: Lista de mensajes de error.
                   Si la lista está vacía, la contraseña cumple todas las reglas.
    """
    errores: list[str] = []

    # Regla 1: mínimo 8 caracteres
    if len(contra) < 8:
        errores.append("Debe tener al menos 8 caracteres de longitud.")

    # Regla 2: al menos una letra mayúscula
    if not any(c.isupper() for c in contra):
        errores.append("Debe contener al menos una letra mayúscula.")

    # Regla 3: al menos un número
    if not any(c.isdigit() for c in contra):
        errores.append("Debe contener al menos un número.")

    return errores


def main() -> None:
    """
    Función principal del programa.

    Muestra las reglas para la creación de contraseñas, solicita al usuario
    que cree una, la valida según las reglas de seguridad, e indica si es
    aceptada o cuáles reglas incumple.

    El proceso se repite hasta que el usuario ingrese una contraseña válida.

    Returns:
        None
    """
    print("=== Validador de Contraseñas ===")
    print("Reglas que debe cumplir su contraseña:")
    print("- Mínimo 8 caracteres.")
    print("- Al menos una letra mayúscula.")
    print("- Al menos un número.")
    print("--------------------------------")

    while True:
        contra = leer_password()
        errores = validar_password(contra)

        if not errores:
            print("Contraseña válida. Creada correctamente.")
            break

        print("La contraseña no cumple con las siguientes reglas:")
        for e in errores:
            print(f"- {e}")
        print("Intente de nuevo.\n")


if __name__ == "__main__":
    main()

