def min_operations(a, b, v, r):
    if abs(a-b) <= v:
        return "It is impossible to reach the target temperature."
    min_temp = max(abs(a-b) // 7, 1)
    max_temp = abs(a-b) // v
    if abs(a-b) % v == 0:
        max_temp -= 1
    operations = float("inf")
    for i in range(min_temp, max_temp+1):
        temp = abs(a-b) / i
        if v < temp < r:
            operations = min(operations, i)
    if operations == float("inf"):
        return "It is impossible to reach the target temperature."
    return operations

def main():
    t = int(input())  # Leer número de casos de prueba

    for i in range(t):
        l, r, v = map(int, input().split())  # Leer rango y mínimo cambio de temperatura
        a, b = map(int, input().split())  # Leer temperaturas inicial y objetivo
        operations = min_operations(a, b, v, r)
        if operations == float("inf"):
            print("-1")
        else:
            print(operations)
"""def main():
    t = int(input())  # Leer número de casos de prueba

    for _ in range(t):
        l, r, v = map(int, input().split())  # Leer rango y mínimo cambio de temperatura
        a, b = map(int, input().split())  # Leer temperaturas inicial y objetivo
        print(min_operations(a, b, v, r))  # Imprimir número mínimo de operaciones necesarias
"""

if __name__ == '__main__':
    main()
