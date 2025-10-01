# El comando %%writefile es una "magia" de Jupyter que guarda el contenido de esta celda en un archivo.

# --- Definición de Funciones ---
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

# --- Bloque de Ejecución Principal ---
# Este código SOLO se ejecutará si corremos 'calculadora.py' directamente.
# No se ejecutará si importamos este módulo desde otro archivo.
if __name__ == "__main__":
    print("Ejecutando la calculadora como script principal...")

    # Ejemplo de uso con suma
    res1 = sumar(15, 5)
    print(f"Suma de 15 + 5 = {res1}")

    # Ejemplo de uso con división
    res2 = dividir(20, 4)
    print(f"División de 20 / 4 = {res2}")
