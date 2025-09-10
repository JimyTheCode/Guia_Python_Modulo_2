# Ejercicio 9: Transformación de Datos con Dictionary Comprehensions
# Tienes una lista de productos, donde cada producto es un diccionario: [{"nombre": "Camisa", "precio": 50000}, {"nombre": "Pantalón", "precio": 80000}]:
# •	Usa una dictionary comprehension para crear un nuevo diccionario donde los nombres de los productos sean las claves y los precios con un 19% de IVA incluido sean los valores.
# Conceptos aplicados: Dictionary comprehensions, acceso a valores de diccionario.


def validar_nombre(nombre):
    """
    Valida que el nombre del producto sea correcto.

    Args:
        nombre (str): Nombre del producto.

    Returns:
        str: Nombre validado y capitalizado.
    """
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo puede contener letras y espacios.")
    if len(nombre) < 2 or len(nombre) > 30:
        raise ValueError("El nombre debe tener entre 2 y 30 caracteres.")
    return nombre.strip().capitalize()


def validar_precio(precio):
    """
    Valida que el precio ingresado sea un número positivo.

    Args:
        precio (str): Precio ingresado en formato texto.

    Returns:
        float: Precio válido con 2 decimales.
    """
    try:
        valor = float(precio)
    except ValueError:
        raise ValueError("El precio debe ser un número válido (usa punto para decimales).")

    if valor < 0:
        raise ValueError("El precio no puede ser negativo.")
    return round(valor, 2)


def ingresar_productos():
    """
    Permite al usuario ingresar productos y precios.

    Returns:
        list[dict]: Lista de productos con nombre y precio.
    """
    productos = []
    print("\nIngreso de productos (escribe 'fin' para terminar):")

    while True:
        nombre = input("\nIngrese el nombre del producto (o 'fin' para salir): ")
        if nombre.lower() == "fin":
            break

        try:
            nombre_valido = validar_nombre(nombre)
            precio = input(f"Ingrese el precio para '{nombre_valido}': ")
            precio_valido = validar_precio(precio)

            productos.append({"nombre": nombre_valido, "precio": precio_valido})
            print(f"Producto '{nombre_valido}' agregado correctamente.")

        except ValueError as e:
            print(e)

    return productos


def aplicar_iva(productos, iva=0.19):
    """
    Aplica el IVA a cada producto y devuelve un nuevo diccionario.

    Args:
        productos (list[dict]): Lista de productos con nombre y precio.
        iva (float): Porcentaje de IVA (por defecto 0.19).

    Returns:
        dict[str, float]: Diccionario con productos y precios con IVA.
    """
    return {p["nombre"]: round(p["precio"] * (1 + iva), 2) for p in productos}


def mostrar_reporte(productos_iva):
    """
    Muestra un reporte con los productos y sus precios con IVA.

    Args:
        productos_iva (dict[str, float]): Diccionario con productos y precios con IVA.
    """
    print("\nReporte de Productos con IVA")
    print("-" * 40)
    if not productos_iva:
        print("No se ingresaron productos.")
    else:
        for nombre, precio in productos_iva.items():
            print(f"{nombre}: ${precio:,.2f}")


def main():
    """
    Función principal que gestiona el flujo del programa.
    """
    productos = ingresar_productos()
    productos_iva = aplicar_iva(productos)
    mostrar_reporte(productos_iva)


if __name__ == "__main__":
    main()


