import asyncio
import time

# Esta es nuestra corrutina. Simula una tarea de I/O que tarda un tiempo.
async def procesar_data(id_tarea, delay):
    print(f"Iniciando tarea {id_tarea}, tardará {delay} segundos...")
    # await pausa esta función, pero permite que otras se ejecuten.
    await asyncio.sleep(delay)
    print(f"--> Tarea {id_tarea} terminada.")
    return id_tarea * 10

# --- Comparación de Tiempos ---

# 1. Forma Síncrona (Secuencial)
async def main_sincrono():
    start_time = time.time()
    # Esperamos a que cada tarea termine antes de empezar la siguiente
    await procesar_data("A", 2)
    await procesar_data("B", 3)
    print(f"Tiempo total síncrono: {time.time() - start_time:.2f} segundos.")

# 2. Forma Asíncrona (Concurrente)
async def main_asincrono():
    start_time = time.time()
    # Creamos las tareas para que se puedan ejecutar a la vez
    tareas = [
        procesar_data("A", 2),
        procesar_data("B", 3)
    ]
    # asyncio.gather() ejecuta las tareas concurrentemente
    resultados = await asyncio.gather(*tareas)
    print(f"Tiempo total asíncrono: {time.time() - start_time:.2f} segundos.")
    print(f"Resultados de las tareas: {resultados}")

# Ejecutamos ambas versiones para comparar
print("--- EJECUCIÓN SÍNCRONA ---")
asyncio.run(main_sincrono())

print("\n--- EJECUCIÓN ASÍNCRONA ---")
asyncio.run(main_asincrono())