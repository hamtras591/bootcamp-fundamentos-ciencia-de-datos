# Selección de Datos en Pandas: iloc y loc

**Curso:** Python para Ciencia de Datos  
**Fecha:** 08 de octubre de 2025  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Contexto y Objetivos](#contexto-y-objetivos)
2. [Conceptos Fundamentales](#conceptos-fundamentales)
3. [iloc - Indexación por Posición](#iloc---indexación-por-posición)
4. [loc - Indexación por Etiquetas](#loc---indexación-por-etiquetas)
5. [Diferencias Clave](#diferencias-clave)
6. [Casos de Uso Prácticos](#casos-de-uso-prácticos)
7. [Ejercicios Resueltos](#ejercicios-resueltos)
8. [Buenas Prácticas](#buenas-prácticas)
9. [Recursos Adicionales](#recursos-adicionales)

---

## Contexto y Objetivos

### ¿Por qué es importante?

La selección de datos es una operación fundamental en el análisis de datos. Saber cuándo usar `iloc` vs `loc` es crucial para:
- Manipular subconjuntos específicos de datos
- Realizar análisis segmentados
- Preparar datos para el proyecto "Customer Experience Analyzer"
- Filtrar información relevante de encuestas CSAT

### Objetivos de aprendizaje

Al finalizar esta lección, serás capaz de:
- ✅ Diferenciar entre indexación por posición y por etiquetas
- ✅ Usar `iloc` para seleccionar datos por índices numéricos
- ✅ Usar `loc` para seleccionar datos por nombres de columnas
- ✅ Aplicar ambos métodos en análisis de datos reales
- ✅ Elegir el método apropiado según el contexto

---

## Conceptos Fundamentales

### Anatomía de un DataFrame

```python
import pandas as pd

# Ejemplo de DataFrame
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'María'],
    'Edad': [25, 30, 28],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali']
})

# Índices (filas): 0, 1, 2
# Columnas: 'Nombre', 'Edad', 'Ciudad'
```

### Dos formas de seleccionar datos

| Método | Tipo de indexación | Sintaxis básica |
|--------|-------------------|-----------------|
| `iloc` | Por **posición** (enteros) | `df.iloc[fila, columna]` |
| `loc` | Por **etiqueta** (nombres) | `df.loc[fila, columna]` |

---

## iloc - Indexación por Posición

### Concepto

`iloc` (**i**nteger **loc**ation) selecciona datos usando índices numéricos, como si fueran posiciones en una lista.

### Sintaxis

```python
df.iloc[índice_fila, índice_columna]
```

### Ejemplos básicos

#### 1. Seleccionar una fila específica

```python
import pandas as pd
from data_loader import load_data

# Cargar datos
df = load_data('online_retail.csv')

# Primera fila (índice 0)
primera_fila = df.iloc[0]
print(primera_fila)
```

#### 2. Seleccionar múltiples filas

```python
# Primeras 5 filas
primeras_cinco = df.iloc[:5]
print(primeras_cinco)

# Filas de la 10 a la 15
rango_filas = df.iloc[10:15]
print(rango_filas)
```

#### 3. Seleccionar un valor específico

```python
# Valor en la primera fila, tercera columna
valor = df.iloc[0, 2]
print(f"Valor: {valor}")
# Output: 'WHITE HANGING HEART T-LIGHT HOLDER'
```

#### 4. Seleccionar subconjunto (filas y columnas)

```python
# Primeras 6 filas, primeras 3 columnas
subset = df.iloc[:6, :3]
print(subset)
```

**Salida del ejemplo:**
```
  InvoiceNo StockCode                          Description
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER
1    536365     71053                  WHITE METAL LANTERN
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.
5    536365     22752         SET 7 BABUSHKA NESTING BOXES
```

### Características clave de iloc

| Característica | Detalle |
|----------------|---------|
| **Tipo de índice** | Enteros (0, 1, 2, ...) |
| **Rango** | El último índice NO se incluye |
| **Ejemplo** | `df.iloc[0:5]` selecciona filas 0, 1, 2, 3, 4 |
| **Ventaja** | Útil cuando no conoces nombres de columnas |

---

## loc - Indexación por Etiquetas

### Concepto

`loc` (**loc**ation) selecciona datos usando nombres de índices y columnas.

### Sintaxis

```python
df.loc[índice_fila, nombre_columna]
```

### Ejemplos básicos

#### 1. Seleccionar una fila por su índice

```python
# Fila con índice 3
fila_3 = df.loc[3]
print(fila_3)
```

#### 2. Seleccionar múltiples filas

```python
# Filas de 0 a 4 (INCLUSIVO)
filas = df.loc[0:4]
print(filas)
```

⚠️ **Diferencia importante:** Con `loc`, el índice final SÍ se incluye.

#### 3. Seleccionar una columna por nombre

```python
# Toda la columna 'Quantity'
cantidades = df.loc[:, 'Quantity']
print(cantidades.head())
```

#### 4. Seleccionar múltiples columnas

```python
# Columnas 'Quantity' y 'UnitPrice'
subset = df.loc[:, ['Quantity', 'UnitPrice']]
print(subset.head())
```

#### 5. Seleccionar rango de columnas

```python
# Desde 'InvoiceNo' hasta 'Quantity'
rango = df.loc[:, 'InvoiceNo':'Quantity']
print(rango.head())
```

#### 6. Filtrado condicional + selección de columnas

```python
# Clientes del Reino Unido, solo columnas Quantity y UnitPrice
uk_data = df.loc[df['Country'] == 'United Kingdom', ['Quantity', 'UnitPrice']]
print(uk_data.head())
```

### Características clave de loc

| Característica | Detalle |
|----------------|---------|
| **Tipo de índice** | Etiquetas (nombres de columnas) |
| **Rango** | El último índice SÍ se incluye |
| **Ejemplo** | `df.loc[0:4]` selecciona filas 0, 1, 2, 3, 4 (5 filas) |
| **Ventaja** | Más legible y semántico |

---

## Diferencias Clave

### Tabla comparativa

| Aspecto | iloc | loc |
|---------|------|-----|
| **Tipo de indexación** | Posiciones (enteros) | Etiquetas (nombres) |
| **Inclusión del final** | Excluye el último índice | Incluye el último índice |
| **Sintaxis** | `df.iloc[0:5]` → 5 filas | `df.loc[0:4]` → 5 filas |
| **Uso con columnas** | `df.iloc[:, 0:3]` → 3 columnas | `df.loc[:, ['col1', 'col2']]` |
| **Filtrado** | No disponible directamente | `df.loc[condición, columnas]` ✅ |
| **Legibilidad** | Menos descriptivo | Más descriptivo ✅ |

### Ejemplo comparativo

```python
# ILOC - Por posición
df.iloc[:10, :2]  # Primeras 10 filas, primeras 2 columnas

# LOC - Por nombre
df.loc[:9, ['InvoiceNo', 'StockCode']]  # Equivalente
```

---

## Casos de Uso Prácticos

### Caso 1: Inspección inicial de datos

```python
# Ver las primeras filas y columnas relevantes
df.iloc[:5, :3]  # Rápido vistazo
```

### Caso 2: Análisis de columnas específicas

```python
# Seleccionar solo datos de ventas
ventas = df.loc[:, ['Quantity', 'UnitPrice']]
ventas['Total'] = ventas['Quantity'] * ventas['UnitPrice']
```

### Caso 3: Filtrado por condiciones

```python
# Clientes de UK con compras grandes
high_value_uk = df.loc[
    (df['Country'] == 'United Kingdom') & (df['Quantity'] > 10),
    ['StockCode', 'Description', 'Quantity']
]
```

### Caso 4: Acceso a un valor específico

```python
# Obtener el precio unitario de la primera compra
precio = df.iloc[0, 5]  # Posición conocida
# o
precio = df.loc[0, 'UnitPrice']  # Nombre de columna
```

---

## Ejercicios Resueltos

### Ejercicio 1: Selección básica con iloc

**Problema:** Selecciona las primeras 10 filas y las primeras 2 columnas.

```python
# Solución
subset = df.iloc[:10, :2]
print(subset)
```

### Ejercicio 2: Selección con loc

**Problema:** Selecciona todas las filas y solo las columnas 'Quantity' y 'UnitPrice'.

```python
# Solución
subset = df.loc[:, ['Quantity', 'UnitPrice']]
print(subset.head())
```

### Ejercicio 3: Acceso específico con iloc

**Problema:** Obtén el valor en la quinta fila y segunda columna.

```python
# Solución
valor = df.iloc[4, 1]  # Recuerda: índices empiezan en 0
print(f"Valor: {valor}")
```

### Ejercicio 4: Filtrado con loc

**Problema:** Filtra todas las filas donde el país es 'United Kingdom' y muestra solo 'Quantity' y 'UnitPrice'.

```python
# Solución
uk_subset = df.loc[df['Country'] == 'United Kingdom', ['Quantity', 'UnitPrice']]
print(uk_subset.head())
```

### Ejercicio Desafío: Contar ocurrencias de un dígito

**Problema:** ¿Cuántas veces aparece el número '7' en la columna 'StockCode'?

```python
# Solución
total_sietes = df['StockCode'].astype(str).str.count('7').sum()
print(f"El número 7 aparece {total_sietes} veces en StockCode.")
# Output: El número 7 aparece 180372 veces en la columna.
```

**Explicación paso a paso:**
1. `astype(str)`: Convierte todos los valores a texto
2. `.str.count('7')`: Cuenta cuántas veces aparece '7' en cada celda
3. `.sum()`: Suma todos los conteos

---

## Buenas Prácticas

### ✅ Recomendaciones

1. **Usa `loc` por defecto** cuando trabajes con nombres de columnas conocidos
   ```python
   # Preferido
   df.loc[:, 'Quantity']
   
   # Evitar (menos legible)
   df.iloc[:, 3]
   ```

2. **Usa `iloc` para operaciones matemáticas** sobre rangos
   ```python
   # Seleccionar primeras N filas para muestreo
   muestra = df.iloc[:100]
   ```

3. **Combina filtros con loc** para análisis más complejos
   ```python
   # Filtrar y seleccionar en una línea
   resultado = df.loc[df['UnitPrice'] > 10, ['Description', 'UnitPrice']]
   ```

4. **Evita encadenar selecciones** (puede causar SettingWithCopyWarning)
   ```python
   # ❌ Evitar
   df[df['Country'] == 'UK']['Quantity'] = 0
   
   # ✅ Mejor
   df.loc[df['Country'] == 'UK', 'Quantity'] = 0
   ```

### ⚠️ Errores comunes

```python
# Error 1: Confundir rangos en iloc vs loc
df.iloc[0:5]   # 5 filas (0, 1, 2, 3, 4)
df.loc[0:5]    # 6 filas (0, 1, 2, 3, 4, 5)

# Error 2: Usar iloc con nombres de columnas
df.iloc[:, 'Quantity']  # ❌ Error
df.loc[:, 'Quantity']   # ✅ Correcto

# Error 3: Olvidar la coma
df.loc[:, ['col1', 'col2']]  # ✅ Correcto
df.loc[['col1', 'col2']]     # ❌ Error (busca filas)
```

---

## Recursos Adicionales

### Documentación oficial
- [Pandas iloc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)
- [Pandas loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
- [Indexing and Selecting Data](https://pandas.pydata.org/docs/user_guide/indexing.html)

### Archivos relacionados
- `12_pd_seleccion_datos_loc_iloc.ipynb`: Jupyter notebook con ejemplos interactivos
- `data_loader.py`: Módulo personalizado para carga de datos
- `online_retail.csv`: Dataset de práctica

### Próximos temas
- Filtrado avanzado con máscaras booleanas
- Métodos de agregación (groupby, agg)
- Transformación de datos con apply y map

---

## Resumen Ejecutivo

### 🎯 Puntos clave

1. **iloc** = Selección por **posición** (enteros)
2. **loc** = Selección por **etiqueta** (nombres)
3. **loc incluye el final** en rangos, iloc no
4. **Usa loc** para código más legible
5. **Usa iloc** cuando trabajes con posiciones matemáticas

### 📊 Aplicación al proyecto CSAT

En tu proyecto "Customer Experience Analyzer", usarás estas técnicas para:
- Seleccionar columnas específicas de encuestas
- Filtrar respuestas por departamento
- Extraer subconjuntos para análisis estadístico
- Preparar datos para cálculo de CSAT promedio

### 🚀 Siguiente paso

Practica estos conceptos con el notebook `12_pd_seleccion_datos_loc_iloc.ipynb` y luego avanza al siguiente tema: **Filtrado y manipulación de datos**.

---

**Actualizado:** 08 de octubre de 2025  
**Progreso de la ruta:** 37% completado (7/19 cursos)