# Universidad del Valle de Guatemala
# Departamento de Computación
# Análisis de Algoritmos
# Parcial 2 - Problema 1: Hacer cambio
# Angie Vela, 23764
# Problema implementado desde el enfoque de DP (también se pudo haber hecho con greedy)

def hacer_cambio(m, monedas=(1, 5, 10, 25)):
    dp = [float('inf')] * (m + 1)
    dp[0] = 0

    for i in range(1, m + 1):
        for c in monedas:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1

    return dp[m]


if __name__ == "__main__":
    test_cases = [11, 32, 99]

    for m in test_cases:
        result = hacer_cambio(m)
        print(f"m = {m:3d}:  monedas minimas = {result}")
