# Parelismo

import multiprocessing

# Función que calcule el cuadrado de un número

def calculate_squere(n):
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    # Crear un pool
    with multiprocessing.Pool() as pool:
        result = pool.map(calculate_squere, numbers)

    print(f"Resultados: {result}")