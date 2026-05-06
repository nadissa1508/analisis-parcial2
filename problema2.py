# Universidad del Valle de Guatemala
# Departamento de Computación
# Análisis de Algoritmos
# Parcial 2 - Problema 2: knapsack fraccionario
# Angie Vela, 23764
# Problema resuelto implementando greedy

def fractional_knapsack(items, W):
    # items: son los elementos del problema, tupla con (precio, peso)
    # Ordenar descendente por densidad de valor (p_i / w_i)
    sorted_items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)

    total_value = 0
    remaining = W

    for p, w in sorted_items:
        if w <= remaining:
            total_value += p
            remaining -= w
        else:
            fraction = remaining / w
            total_value += fraction * p
            remaining = 0
            break

    return total_value


if __name__ == "__main__":
    test_cases = [
        # (Los elementos se muestran como (precio, peso), W)
        ([(60, 10), (100, 20), (120, 30)], 50),   # clasico: valor = 240
        ([(500, 30), (200, 20), (100, 10)], 25),   # capacidad limitada
        ([(10, 5), (40, 4), (30, 6), (50, 3)], 10) # varios articulos
    ]

    for items, W in test_cases:
        result = fractional_knapsack(items, W)
        print(f"W = {W:3d}  elementos = {items}")
        print(f"       valor maximo = {result:.2f}\n")
