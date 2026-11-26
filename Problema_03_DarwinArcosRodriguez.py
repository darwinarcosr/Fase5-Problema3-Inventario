# Nombre: Darwin Emilio Arcos Rodríguez
# Grupo: 213022_773
# Programa: Ingeniería Electrónica
# Problema 3: Control de inventario

inventario = [
    ["A001", "Resistencia de 100 ohmios", 8, 20],
    ["A002", "Condensador de 10 microfaradios", 25, 15],
    ["A003", "Diodo LED rojo", 6, 18],
    ["A004", "Transistor 2N2222", 12, 12],
    ["A005", "Protoboard", 3, 10]
]


def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """Calcula la cantidad necesaria para reabastecer un artículo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def generar_informe(lista_inventario):
    """Muestra el estado y la cantidad que se debe pedir de cada artículo."""
    print("INFORME DE REABASTECIMIENTO")
    print("-" * 65)

    for articulo in lista_inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_pedir(
            stock_actual, stock_minimo
        )

        print(f"Código: {codigo}")
        print(f"Artículo: {nombre}")
        print(f"Stock actual: {stock_actual}")
        print(f"Stock mínimo: {stock_minimo}")
        print(f"Cantidad a solicitar: {cantidad_pedir}")
        print("-" * 65)


generar_informe(inventario)