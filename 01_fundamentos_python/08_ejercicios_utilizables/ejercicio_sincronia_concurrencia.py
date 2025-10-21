import asyncio
import time
import random
import multiprocessing

# Crear función asíncrona para verificar el inventario
async def check_inventory(item):
    print(f'Verificando inventario para: {item}...')
    await asyncio.sleep(random.randint(3, 6))
    print(f'--> Inventario verificado para: {item}.')
    # Simular disponibilidad del producto
    return random.choice([True, False])

# Siguiente función asíncrona para procesar el pago
async def process_payment(order_id):
    print(f'Prosando pago para la orden: {order_id}...')
    # Simular tiempo de espera que puede tener un servicio de pago
    await asyncio.sleep(random.randint(3, 6))
    print(f'--> Pago procesado para la orden: {order_id}.')
    return True

# Función intensiva en CPU para calcular el costo total del pedido
def calculate_total(items):
    print(f'Calculando costo total para: {len(items)} articulos...')
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f'Costo total calculado para: {total}')
    return total

async def process_order(order_id, items):
    print(f'Iniciando el procesamiento de la orden: {order_id}...')
    # Verificar inventario para cada uno de los actículo de forma asíncrona
    inventory_checks = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_checks)

    if not all(inventory_results):
        print(f'Orden {order_id} cancelada. No hay inventario suficiente.')

    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (items,))

    # Procesar el pago asincronicamente

    payment_result = await process_payment(order_id)

    if payment_result:
        print(f'Orden {order_id} completada con existo. Total {total}')
    else:
        print(f'Orden {order_id} cancelada. No se pudo procesar el pago.')

async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
    ]

    #Procesar multiples órdenes concurrentemente
    task = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*task)

# Crear event loop
if __name__ == '__main__':
    asyncio.run(main())


