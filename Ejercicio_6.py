# Ejercicio 6: Analizador de Posiciones de Letras con enumerate
# Crea una función que reciba una frase y una letra. La función debe devolver una lista con todos los índices (posiciones) en los que aparece esa letra en la frase.
# •	Ejemplo: encontrar_indices("Hola SENA", "a") debería devolver [3, 8].
# Conceptos aplicados: Funciones, enumerate(), bucle for, list.append().


def encontrar_indices(frase: str, letra: str) -> list[int]:
    """
    Analiza una frase y devuelve todas las posiciones en las que aparece una letra específica.

    Parámetros:
        frase (str): Texto en el cual se va a buscar la letra. No debe contener dígitos.
        letra (str): Letra que se quiere localizar dentro de la frase. Debe ser exactamente
                     un carácter alfabético (sin dígitos ni símbolos). La búsqueda es
                     insensible a mayúsculas/minúsculas.

    Retorna:
        list[int]: Una lista con los índices (posiciones) donde se encontró la letra.
                   Si la letra no aparece en la frase, devuelve una lista vacía.

    Ejemplos:
        >>> encontrar_indices("Hola SENA", "a")
        [3, 8]

        >>> encontrar_indices("Python", "p")
        [0]
    """
    indices: list[int] = []

    for i, c in enumerate(frase):
        if c.lower() == letra.lower():
            indices.append(i)

    return indices


def validar_frase(frase: str) -> str:
    """
    Valida que la frase no esté vacía ni contenga dígitos.

    Args:
        frase (str): Texto ingresado por el usuario.

    Returns:
        str: La frase validada.

    Raises:
        ValueError: Si la frase está vacía o contiene números.
    """
    if not frase:
        raise ValueError("La frase no puede estar vacía.")
    if any(ch.isdigit() for ch in frase):
        raise ValueError("La frase no puede contener números.")
    return frase


def validar_letra(letra: str) -> str:
    """
    Valida que la letra sea un único carácter alfabético.

    Args:
        letra (str): Carácter ingresado por el usuario.

    Returns:
        str: La letra validada.

    Raises:
        ValueError: Si no es exactamente un carácter alfabético.
    """
    if len(letra) != 1:
        raise ValueError("Debe ingresar exactamente una letra.")
    if not letra.isalpha():
        raise ValueError("Debe ingresar una letra del alfabeto (sin números ni símbolos).")
    return letra


def main() -> None:
    """
    Programa principal que solicita al usuario una frase y una letra,
    valida ambas entradas y muestra todas las posiciones donde aparece la letra.
    """
    while True:
        try:
            frase = validar_frase(input("Ingrese una frase (sin números): ").strip())
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            letra = validar_letra(input("Ingrese una letra a buscar: ").strip())
            break
        except ValueError as e:
            print(f"Error: {e}")

    posiciones = encontrar_indices(frase, letra)

    if posiciones:
        print(f"La letra '{letra}' aparece {len(posiciones)} veces en las posiciones: {posiciones}")
    else:
        print(f"La letra '{letra}' no aparece en la frase.")


if __name__ == "__main__":
    main()

