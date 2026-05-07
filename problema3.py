# Universidad del Valle de Guatemala
# Departamento de Computación
# Análisis de Algoritmos
# Parcial 2 - Problema 3: nokia combinaciones
# Angie Vela, 23764
# Problema resuelto implementando programación dinámica

def nokia_combinations(n):
    # vecinos validos para cada dígito
    neighbors = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [0, 5, 7, 8, 9],
        9: [6, 8, 9],
    }

    # dp[step][d] = cantidad de combinaciones de longitud step que terminan en digito d
    dp = [[0] * 10 for _ in range(n + 1)]

    for d in range(10):
        dp[1][d] = 1

    for step in range(2, n + 1):
        for d in range(10):
            dp[step][d] = sum(dp[step - 1][nb] for nb in neighbors[d])

    return sum(dp[n][d] for d in range(10))


