# Ejercicio 6: Analizador de Posiciones de Letras con enumerate
# Crea una función que reciba una frase y una letra. La función debe devolver una lista con todos los índices (posiciones) en los que aparece esa letra en la frase.
# •	Ejemplo: encontrar_indices("Hola SENA", "a") debería devolver [3, 8].
# Conceptos aplicados: Funciones, enumerate(), bucle for, list.append().

def encontrar_indices(frase, letra) :
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


def main() -> None:
    while True:
        frase = input("Ingrese una frase (sin números): ").strip()
        if not frase:
            print("Error: la frase no puede estar vacía.")
            continue
        if any(ch.isdigit() for ch in frase):
            print("Error: la frase no puede contener números.")
            continue
        break

    while True:
        letra = input("Ingrese una letra a buscar (solo letras, sin números): ").strip()
        if len(letra) != 1:
            print("Error: debe ingresar exactamente una letra.")
            continue
        if not letra.isalpha():
            print("Error: debe ingresar una letra del alfabeto (sin números ni símbolos).")
            continue
        break

    posiciones = encontrar_indices(frase, letra)

    if posiciones:
        print(f"La letra '{letra}' aparece {len(posiciones)} veces en las posiciones: {posiciones}")
    else:
        print(f"La letra '{letra}' no aparece en la frase.")


if __name__ == "__main__":
    main()
