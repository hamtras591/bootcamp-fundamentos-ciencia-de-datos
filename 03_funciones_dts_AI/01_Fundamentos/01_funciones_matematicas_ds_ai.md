# Funciones Matemáticas para Data Science e IA

**Curso:** Funciones Matemáticas para Data Science e IA  
**Fecha:** 30 de octubre de 2025  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [Definición Formal](#definición-formal)
3. [Elementos de una Función](#elementos-de-una-función)
4. [Sintaxis en Python](#sintaxis-en-python)
5. [Ejemplos Básicos](#ejemplos-básicos)
6. [Casos de Uso en Data Science](#casos-de-uso-en-data-science)
7. [Ejercicios Prácticos](#ejercicios-prácticos)
8. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

Una **función matemática** es una regla o relación que asocia elementos de un conjunto de entrada (dominio) con elementos de un conjunto de salida (codominio). En términos simples: para cada entrada existe **una y solo una salida**.

En el contexto de Data Science, las funciones son fundamentales porque:
- Transforman datos de un formato a otro
- Relacionan variables independientes (X) con variables dependientes (y)
- Modelan relaciones entre características y predicciones
- Permiten automatizar cálculos repetitivos

La notación matemática es: **f(x) = y**, donde:
- **f** es el nombre de la función
- **x** es la entrada (variable independiente)
- **y** es la salida (variable dependiente)

---

## Definición Formal

### Componentes de una Función

**Dominio (x):** El conjunto de valores de entrada que la función acepta.

**Codominio:** El conjunto de valores posibles de salida.

**Imagen/Rango:** El conjunto real de valores de salida que genera la función.

**Regla de correspondencia:** La operación o transformación que se aplica a x para obtener y.

### Ejemplo Visual

```
Dominio (x)    →    Función f()    →    Imagen (y)
    A          →         f              1
    B          →                         2
    C          →                         4
    D
```

En este diagrama:
- Si A→1, B→2, C→2, D→4, entonces cada entrada tiene **una sola salida**
- Es una función válida (aunque C y B compartan la salida 2)

---

## Elementos de una Función

### 1. Dominio

Es el conjunto de todos los valores posibles que podemos introducir en la función.

Ejemplo: Si tenemos una función que calcula CSAT (satisfaction score), el dominio podría ser puntuaciones de 1 a 10.

### 2. Codominio

Es el conjunto teórico de valores que la función puede producir.

Ejemplo: Puntuaciones de satisfacción normalizadas de 0 a 1.

### 3. Rango

Es el conjunto real de valores que la función efectivamente produce.

Ejemplo: Si en nuestros datos solo tenemos satisfacciones de 0.3 a 0.95, el rango es [0.3, 0.95], aunque el codominio sea [0, 1].

### 4. Regla de Correspondencia

Es la fórmula o algoritmo que transforma x en y.

Ejemplo: `f(x) = x / 10` (normalizar puntuación de 1-10 a 0-1)

---

## Sintaxis en Python

### Función Básica

```python
def nombre_funcion(x):
    """
    Descripción de qué hace la función
    
    Args:
        x: Descripción del parámetro
        
    Returns:
        Descripción del valor retornado
    """
    y = x + 1
    return y
```

### Función con Múltiples Parámetros

```python
def funcion_multiple(x1, x2):
    """Combina dos variables de entrada"""
    resultado = x1 + x2
    return resultado
```

### Función con Valor por Defecto

```python
def funcion_con_default(x, multiplicador=2):
    """Multiplica x por un valor (default es 2)"""
    return x * multiplicador
```

### Función con Type Hints

```python
def funcion_tipada(x: float) -> float:
    """Función con anotaciones de tipos"""
    return x ** 2
```

---

## Ejemplos Básicos

### Ejemplo 1: Función Lineal

Una función lineal tiene la forma `f(x) = mx + b`

```python
# Función lineal simple
def funcion_lineal(x, m=2, b=3):
    """
    Función lineal: f(x) = mx + b
    Args:
        x: valor de entrada
        m: pendiente (slope)
        b: intersección con eje Y (intercept)
    """
    return m * x + b

# Usar la función
resultado1 = funcion_lineal(5)  # 2*5 + 3 = 13
resultado2 = funcion_lineal(10, m=1, b=0)  # 1*10 + 0 = 10

print(f"f(5) = {resultado1}")
print(f"f(10) con m=1, b=0 = {resultado2}")
```

### Ejemplo 2: Función Cuadrática

Una función cuadrática tiene la forma `f(x) = ax² + bx + c`

```python
# Función cuadrática
def funcion_cuadratica(x, a=1, b=0, c=0):
    """
    Función cuadrática: f(x) = ax² + bx + c
    """
    return a * (x ** 2) + b * x + c

# Usar la función
resultado1 = funcion_cuadratica(3)  # 1*(3²) + 0*3 + 0 = 9
resultado2 = funcion_cuadratica(2, a=1, b=2, c=1)  # 1*4 + 2*2 + 1 = 9

print(f"f(3) = {resultado1}")
print(f"f(2) con a=1, b=2, c=1 = {resultado2}")
```

### Ejemplo 3: Función de Normalización (Común en Data Science)

```python
# Función de normalización min-max
def normalizar_minmax(x, x_min=0, x_max=100):
    """
    Normaliza un valor al rango [0, 1]
    Fórmula: (x - min) / (max - min)
    """
    return (x - x_min) / (x_max - x_min)

# Usar la función
valor_original = 50  # Puntuación CSAT entre 0-100
valor_normalizado = normalizar_minmax(valor_original, x_min=0, x_max=100)

print(f"Valor original: {valor_original}")
print(f"Valor normalizado: {valor_normalizado}")
```

---

## Casos de Uso en Data Science

### Caso de Uso 1: Función de Puntuación CSAT Normalizada

**Contexto:** En tu proyecto final, recibirás encuestas con puntuaciones CSAT (Customer Satisfaction) de 1 a 10. Necesitas normalizarlas a una escala de 0 a 1 para análisis posterior, y además aplicar una ponderación por departamento para el reporte ejecutivo.

**Problema:** 
- Las puntuaciones varían en escala
- Diferentes departamentos tienen diferentes pesos en la métrica final
- Necesitas una función reutilizable para todo el análisis

**Solución:**

```python
import pandas as pd

def calcular_csat_ponderado(puntuacion, departamento, pesos_departamento=None):
    """
    Calcula CSAT normalizado y ponderado por departamento
    
    Args:
        puntuacion: Valor de 1 a 10
        departamento: Nombre del departamento ('ventas', 'soporte', 'producto')
        pesos_departamento: Dict con pesos por departamento
        
    Returns:
        Float entre 0 y 1 con ponderación aplicada
    """
    # Pesos por defecto (suma = 1)
    if pesos_departamento is None:
        pesos_departamento = {
            'ventas': 0.3,
            'soporte': 0.5,
            'producto': 0.2
        }
    
    # Normalizar a escala 0-1
    csat_normalizado = (puntuacion - 1) / 9
    
    # Aplicar ponderación del departamento
    peso = pesos_departamento.get(departamento, 0.33)
    csat_ponderado = csat_normalizado * peso
    
    return csat_ponderado

# Ejemplo de uso
csat_ventas = calcular_csat_ponderado(8, 'ventas')
csat_soporte = calcular_csat_ponderado(7, 'soporte')
csat_producto = calcular_csat_ponderado(9, 'producto')

print(f"CSAT Ventas (ponderado): {csat_ventas:.4f}")
print(f"CSAT Soporte (ponderado): {csat_soporte:.4f}")
print(f"CSAT Producto (ponderado): {csat_producto:.4f}")

# Aplicar con Pandas (más realista)
df_encuestas = pd.DataFrame({
    'puntuacion': [8, 7, 9, 6, 10],
    'departamento': ['ventas', 'soporte', 'producto', 'ventas', 'soporte']
})

# Crear columna de CSAT ponderado usando apply
df_encuestas['csat_ponderado'] = df_encuestas.apply(
    lambda row: calcular_csat_ponderado(row['puntuacion'], row['departamento']),
    axis=1
)

print("\nDataFrame con CSAT ponderado:")
print(df_encuestas)
```

**Explicación:** 

Esta función es fundamental para tu proyecto porque:
1. **Normaliza** las puntuaciones (1-10 → 0-1) para que sean comparables
2. **Pondera** según departamento, reflejando que algunos departamentos son más críticos
3. **Reutilizable** con pandas `apply()` para procesar cientos de registros
4. **Flexible** con parámetros por defecto pero personalizables

---

### Caso de Uso 2: Función de Predicción de Satisfacción basada en Tiempo de Respuesta

**Contexto:** Observas que existe una relación entre el tiempo de respuesta (en horas) y la satisfacción del cliente. Quieres crear una función que prediga satisfacción basada en este tiempo para identificar qué tiempos de respuesta garantizan clientes satisfechos.

**Problema:**
- Relación no lineal entre tiempo y satisfacción
- Necesitas umbrales de decisión (ej: si predicción > 0.7 = cliente satisfecho)
- Parámetros deben ajustarse según datos reales

**Solución:**

```python
import numpy as np
import pandas as pd

def predecir_satisfaccion_por_tiempo(horas_respuesta, metodo='exponencial'):
    """
    Predice satisfacción del cliente (0-1) basada en tiempo de respuesta
    
    Args:
        horas_respuesta: Horas transcurridas para responder
        metodo: 'lineal' o 'exponencial'
        
    Returns:
        Float entre 0 y 1 representando satisfacción predicha
    """
    
    if metodo == 'lineal':
        # Función lineal: satisfacción decrece linealmente con tiempo
        # f(t) = 1 - (t / 24)  (asumiendo 24h es punto mínimo)
        satisfaccion = max(0, 1 - (horas_respuesta / 24))
    
    elif metodo == 'exponencial':
        # Función exponencial: satisfacción cae rápido inicialmente
        # f(t) = e^(-0.1*t)
        satisfaccion = np.exp(-0.1 * horas_respuesta)
    
    return round(satisfaccion, 4)

# Ejemplo: evaluar diferentes tiempos de respuesta
tiempos = [0.5, 1, 2, 4, 8, 12, 24]

print("Predicción de Satisfacción por Tiempo de Respuesta\n")
print("Horas  | Lineal | Exponencial")
print("-------|--------|------------")

for horas in tiempos:
    sat_lineal = predecir_satisfaccion_por_tiempo(horas, 'lineal')
    sat_exp = predecir_satisfaccion_por_tiempo(horas, 'exponencial')
    print(f"{horas:5.1f} | {sat_lineal:6.4f} | {sat_exp:6.4f}")

# Aplicar a un dataset
df_tickets = pd.DataFrame({
    'id_ticket': [1, 2, 3, 4, 5],
    'horas_respuesta': [0.5, 2, 8, 1, 24]
})

# Calcular predicciones
df_tickets['satisfaccion_predicha'] = df_tickets['horas_respuesta'].apply(
    lambda t: predecir_satisfaccion_por_tiempo(t, 'exponencial')
)

# Crear clasificación
df_tickets['cliente_satisfecho'] = df_tickets['satisfaccion_predicha'] > 0.7

print("\nDataset con Predicciones:")
print(df_tickets)

print("\nResumen:")
print(f"Clientes probablemente satisfechos: {df_tickets['cliente_satisfecho'].sum()} de {len(df_tickets)}")
```

**Explicación:**

Esta función es valiosa porque:
1. **Modela relaciones** complejas entre variables
2. **Predice comportamiento** antes de que suceda
3. **Compara métodos** (lineal vs exponencial) para elegir el mejor
4. **Genera insights** sobre qué tiempos de respuesta garantizan satisfacción
5. **Integrable** con pipelines de análisis en Pandas

---

## Ejercicios Prácticos

### Ejercicio 1: Función Básica de Conversión de Temperatura [Nivel Básico]

**Enunciado:** Crea una función que convierta grados Celsius a Fahrenheit usando la fórmula `F = (C × 9/5) + 32`. Pruébala con los valores 0, 100 y -40.

**Pistas:**
- La fórmula está dada: `(celsius * 9/5) + 32`
- Define la función con un parámetro llamado `celsius`
- Usa `return` para devolver el resultado

<details>
<summary>💡 Ver solución</summary>

```python
def celsius_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit
    
    Args:
        celsius: Temperatura en Celsius
        
    Returns:
        Temperatura equivalente en Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Pruebas
pruebas = [0, 100, -40]

for temp_c in pruebas:
    temp_f = celsius_a_fahrenheit(temp_c)
    print(f"{temp_c}°C = {temp_f}°F")
```

**Explicación:** 

- Definimos la función con el parámetro `celsius`
- Aplicamos la fórmula de conversión tal cual está
- `return` envía el resultado de vuelta al que llamó la función
- Probamos con valores conocidos: 0°C = 32°F, 100°C = 212°F, -40°C = -40°F

</details>

---

### Ejercicio 2: Función de Cálculo de Bonificación por Ventas [Nivel Básico-Intermedio]

**Enunciado:** Crea una función que calcule la bonificación de un vendedor basada en sus ventas. Si vende menos de $1000, bonificación es 5%. Si vende entre $1000 y $5000, es 10%. Si vende más de $5000, es 15%. La función debe retornar el monto de bonificación (no el porcentaje).

**Pistas:**
- Usa condicionales `if`, `elif`, `else`
- Primero determina el porcentaje según las ventas
- Luego calcula el monto: `ventas * porcentaje`
- Prueba con: 500, 3000, 7500

<details>
<summary>💡 Ver solución</summary>

```python
def calcular_bonificacion(ventas):
    """
    Calcula la bonificación de un vendedor según sus ventas
    
    Args:
        ventas: Monto total de ventas en pesos
        
    Returns:
        Monto de bonificación en pesos
    """
    if ventas < 1000:
        porcentaje = 0.05  # 5%
    elif ventas <= 5000:
        porcentaje = 0.10  # 10%
    else:
        porcentaje = 0.15  # 15%
    
    bonificacion = ventas * porcentaje
    return bonificacion

# Pruebas
montos_ventas = [500, 3000, 7500]

print("Ventas | Bonificación")
print("-------|-------------")

for venta in montos_ventas:
    bonus = calcular_bonificacion(venta)
    print(f"${venta:,} | ${bonus:,.2f}")
```

**Explicación:**

- Usamos `if/elif/else` para determinar el porcentaje según rangos
- La condición `elif ventas <= 5000` es importante: si ventas es 1000, no cae en la primera (< 1000) pero sí en esta (≤ 5000)
- Calculamos el monto multiplicando ventas por el porcentaje
- `.2f` en print formatea a 2 decimales para dinero
- Estructura: condición → porcentaje → monto = condición → acción

</details>

---

### Ejercicio 3: Función de Validación y Normalización de CSAT [Nivel Intermedio]

**Enunciado:** Crea una función que reciba una puntuación CSAT (1-10) y retorne dos valores: la puntuación normalizada (0-1) y un estado ('bajo', 'medio', 'alto'). Valida que la entrada esté en rango válido. Si no, lanza un error.

**Pistas:**
- Usa una función que retorne múltiples valores (tupla)
- Validación: si no está entre 1-10, usa `raise ValueError()`
- Normalización: `(puntuacion - 1) / 9`
- Clasificación: 'bajo' si < 0.33, 'medio' si 0.33-0.66, 'alto' si > 0.66
- Prueba con: 1, 5, 10, y también con 0 y 11 para verificar validación

<details>
<summary>💡 Ver solución</summary>

```python
def validar_y_normalizar_csat(puntuacion):
    """
    Valida y normaliza una puntuación CSAT
    
    Args:
        puntuacion: Valor entre 1 y 10
        
    Returns:
        Tupla con (normalizado, estado)
        
    Raises:
        ValueError: Si puntuación no está entre 1 y 10
    """
    # Validación
    if not isinstance(puntuacion, (int, float)) or puntuacion < 1 or puntuacion > 10:
        raise ValueError(f"CSAT debe ser un número entre 1 y 10, recibido: {puntuacion}")
    
    # Normalización
    normalizado = (puntuacion - 1) / 9
    
    # Clasificación
    if normalizado < 0.33:
        estado = 'bajo'
    elif normalizado <= 0.66:
        estado = 'medio'
    else:
        estado = 'alto'
    
    return normalizado, estado

# Pruebas
puntuaciones_validas = [1, 5, 10, 3, 8]

print("CSAT | Normalizado | Estado")
print("-----|-------------|--------")

for puntaje in puntuaciones_validas:
    norm, est = validar_y_normalizar_csat(puntaje)
    print(f"{puntaje:>4} | {norm:>11.4f} | {est}")

# Pruebas de error
print("\nPrueba con valores inválidos:")

puntuaciones_invalidas = [0, 11, -5, 15]

for puntaje in puntuaciones_invalidas:
    try:
        norm, est = validar_y_normalizar_csat(puntaje)
    except ValueError as e:
        print(f"❌ Error con {puntaje}: {e}")
```

**Explicación:**

- **Validación**: Verificamos tipo de dato y rango antes de procesar
- **Raise ValueError**: Cuando la entrada es inválida, lanzamos una excepción
- **Tupla de retorno**: La función devuelve dos valores que se pueden desempacar
- **Rangos de clasificación**: Los rangos están calibrados para mapear bien los valores normalizados
- **Try-except**: Capturamos el error sin que el programa se bloquee

</details>

---

### Ejercicio 4: Función Compuesta de Análisis de Departamentos [Nivel Intermedio-Avanzado]

**Enunciado:** Crea una función que reciba un DataFrame con columnas ['departamento', 'puntuacion'] y retorne un diccionario con el CSAT promedio por departamento, aplicando normalización y filtrando solo departamentos con más de 2 registros. La función debe usar otra función auxiliar (helper) para normalizar.

**Pistas:**
- Crea dos funciones: `normalizar_valor()` y `analizar_por_departamento()`
- Usa `df.groupby('departamento')` para agrupar
- Filtra con `len() > 2`
- Retorna un diccionario con estructura: `{'departamento': csat_normalizado}`
- Prueba primero con un DataFrame pequeño

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd

def normalizar_valor(puntuacion):
    """Función auxiliar: normaliza puntuación CSAT a [0, 1]"""
    return (puntuacion - 1) / 9

def analizar_por_departamento(df):
    """
    Analiza CSAT promedio por departamento con normalización
    
    Args:
        df: DataFrame con columnas ['departamento', 'puntuacion']
        
    Returns:
        Diccionario con CSAT normalizado por departamento
    """
    # Copiar para no modificar original
    df_temp = df.copy()
    
    # Normalizar puntuaciones
    df_temp['puntuacion_norm'] = df_temp['puntuacion'].apply(normalizar_valor)
    
    # Agrupar por departamento
    grupos = df_temp.groupby('departamento')
    
    # Filtrar y calcular promedio
    resultado = {}
    
    for departamento, grupo in grupos:
        if len(grupo) > 2:  # Filtro: más de 2 registros
            promedio = grupo['puntuacion_norm'].mean()
            resultado[departamento] = round(promedio, 4)
    
    return resultado

# Crear DataFrame de prueba
datos = {
    'departamento': ['ventas', 'ventas', 'soporte', 'soporte', 'soporte', 'producto', 'rh'],
    'puntuacion': [8, 9, 7, 6, 8, 10, 9]
}

df_encuestas = pd.DataFrame(datos)

print("DataFrame original:")
print(df_encuestas)
print()

# Analizar
resultado = analizar_por_departamento(df_encuestas)

print("CSAT Normalizado por Departamento (solo >2 registros):")
for depto, csat in resultado.items():
    print(f"  {depto.capitalize()}: {csat:.4f}")
```

**Explicación:**

- **Función auxiliar**: `normalizar_valor()` cumple un solo propósito (Single Responsibility)
- **Apply**: Aplicamos la función auxiliar a cada valor de la columna
- **GroupBy**: Agrupamos datos por departamento, lo que nos devuelve iterables
- **Filtro**: `if len(grupo) > 2` descarta departamentos sin suficientes datos
- **Diccionario**: Estructura ideal para retornar resultados con clave-valor

</details>

---

### Ejercicio 5: Función Predictiva Multi-variable para Retención de Clientes [Nivel Desafío]

**Enunciado:** Crea una función que prediga si un cliente será retenido (True/False) usando múltiples variables: CSAT (1-10), tiempo_cliente_meses, tickets_abiertos. 

La lógica debe ser:
- Cliente con CSAT < 4: retención = 50% (muy bajo)
- Cliente nuevo (< 3 meses) pero satisfecho: retención = 80%
- Cliente antiguo (> 12 meses) con tickets abiertos > 2: retención = 60%
- Cliente antiguo sin tickets abiertos: retención = 90%
- Genera un score 0-1, luego clasifica si score > 0.75 como "Retener" o "Vigilar"

Aplica esta función a un DataFrame y crea un reporte de resumen.

**Pistas:**
- Esta función tiene múltiples condicionales anidados
- Empieza creando la lógica en orden de prioridad
- Score final se calcula combinando factores
- Usa `apply()` con una lambda para DataFrame
- Reporte debe contar: "Retener", "Vigilar"

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd

def predecir_retencion_cliente(csat, tiempo_meses, tickets_abiertos):
    """
    Predice la probabilidad de retención de un cliente
    
    Args:
        csat: Puntuación de satisfacción (1-10)
        tiempo_meses: Meses que lleva siendo cliente
        tickets_abiertos: Número de tickets sin resolver
        
    Returns:
        Tupla (score_retencion, clasificacion)
    """
    
    # Validaciones
    if csat < 1 or csat > 10:
        raise ValueError("CSAT debe estar entre 1 y 10")
    if tiempo_meses < 0 or tickets_abiertos < 0:
        raise ValueError("Tiempo y tickets no pueden ser negativos")
    
    # Inicializar score
    score = 0.0
    
    # Lógica 1: CSAT bajo es crítico
    if csat < 4:
        score = 0.50
    
    # Lógica 2: Cliente nuevo pero satisfecho es buena retención
    elif tiempo_meses < 3 and csat >= 7:
        score = 0.80
    
    # Lógica 3: Cliente antiguo pero con muchos problemas
    elif tiempo_meses > 12 and tickets_abiertos > 2:
        score = 0.60
    
    # Lógica 4: Cliente antiguo sin problemas (ideal)
    elif tiempo_meses > 12 and tickets_abiertos <= 2:
        score = 0.90
    
    # Lógica 5: Casos intermedios (cliente establecido, satisfecho)
    else:
        # Normalizar CSAT a contribución (0.5-1.0)
        contribucion_csat = 0.5 + (csat / 10) * 0.5
        # Penalidad por tickets
        penalidad_tickets = max(0, 0.1 * tickets_abiertos)
        # Factor de lealtad por tiempo
        factor_tiempo = min(0.3, tiempo_meses / 50)  # Max 0.3 después de 50 meses
        
        score = contribucion_csat - penalidad_tickets + factor_tiempo
        score = max(0.0, min(1.0, score))  # Clamp entre 0 y 1
    
    # Clasificación final
    clasificacion = "Retener" if score > 0.75 else "Vigilar"
    
    return round(score, 4), clasificacion

# Crear dataset de ejemplo
datos_clientes = {
    'id_cliente': [1, 2, 3, 4, 5, 6, 7, 8],
    'csat': [9, 3, 8, 7, 5, 10, 4, 6],
    'tiempo_meses': [24, 6, 2, 30, 4, 60, 1, 12],
    'tickets_abiertos': [0, 5, 1, 3, 2, 0, 4, 1]
}

df_clientes = pd.DataFrame(datos_clientes)

print("Dataset original:")
print(df_clientes)
print("\n" + "="*70 + "\n")

# Aplicar predicción
df_clientes[['score_retencion', 'clasificacion']] = df_clientes.apply(
    lambda row: pd.Series(predecir_retencion_cliente(
        row['csat'], 
        row['tiempo_meses'], 
        row['tickets_abiertos']
    )),
    axis=1
)

print("Dataset con predicciones:")
print(df_clientes)
print("\n" + "="*70 + "\n")

# Reporte de resumen
print("REPORTE DE RETENCIÓN")
print(f"Total de clientes: {len(df_clientes)}")
print(f"Clientes para RETENER: {(df_clientes['clasificacion'] == 'Retener').sum()}")
print(f"Clientes a VIGILAR: {(df_clientes['clasificacion'] == 'Vigilar').sum()}")
print(f"Score promedio de retención: {df_clientes['score_retencion'].mean():.4f}")

print("\nDetalle de clientes a vigilar:")
vigilar = df_clientes[df_clientes['clasificacion'] == 'Vigilar']
for idx, row in vigilar.iterrows():
    print(f"  - Cliente {row['id_cliente']}: Score={row['score_retencion']}, CSAT={row['csat']}, Tickets={row['tickets_abiertos']}")
```

**Explicación:**

- **Múltiples condicionales**: La lógica se va refinando según cada escenario
- **Validación entrada**: Verificamos que los datos tengan sentido antes de procesar
- **Score compuesto**: En casos intermedios, combinamos múltiples factores
- **Clamp (0-1)**: `max(0.0, min(1.0, valor))` asegura que el score nunca salga de rango
- **Apply con axis=1**: Procesa fila por fila, accediendo a múltiples columnas
- **Reporte profesional**: Agregamos estadísticas y detalles útiles para la toma de decisiones
- **Caso real**: Este tipo de función es exactamente lo que necesitarás en tu proyecto CSAT

</details>

---

## Recursos Adicionales

- **Documentación oficial**: [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- **Archivos relacionados**: 
  - `07_lenguaje_notacion_matematica.md` (conceptos previos)
  - `08_python_ciencia_datos.md` (pandas y aplicación de funciones)
- **Próximos temas**: 
  - Estadística Descriptiva (aplicación de funciones a datasets)
  - Funciones Lambda y Map (funciones anónimas)
  - Funciones en librerías (NumPy, Pandas, Scikit-learn)

---

**Actualizado:** 30 de octubre de 2025  
**Progreso de la ruta:** 42% completado (8/19 cursos)  
**Estado:** Completado ✅
