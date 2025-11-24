# Tipos de Datos en Ciencia de Datos

**Curso:** Matemáticas para Data Science: Estadística Descriptiva  
**Fecha:** Noviembre 2025  
**Módulo:** Estadística Descriptiva para Analítica  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [Clasificación de Datos](#clasificación-de-datos)
3. [Datos Categóricos](#datos-categóricos)
4. [Datos Numéricos](#datos-numéricos)
5. [Identificación de Tipos en Python](#identificación-de-tipos-en-python)
6. [Ejemplos Prácticos con pandas](#ejemplos-prácticos-con-pandas)
7. [Casos de Uso en Data Science](#casos-de-uso-en-data-science)
8. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

Antes de comenzar cualquier análisis de datos, es crucial entender **los tipos de datos** con los que trabajamos. La correcta identificación de tipos de datos determina:

- ✅ Qué operaciones estadísticas son válidas
- ✅ Qué visualizaciones son apropiadas
- ✅ Qué transformaciones podemos aplicar
- ✅ Qué algoritmos de machine learning usar

**Regla fundamental:** El tipo de dato dicta el análisis posible.

---

## Clasificación de Datos

Los datos se dividen en **dos categorías principales**:

```
                    ┌─────────────┐
                    │    DATOS    │
                    └──────┬──────┘
                           │
            ┌──────────────┴─────────────┐
            │                            │
            ▼                            ▼
    ┌───────────────┐          ┌─────────────────┐
    │  CATEGÓRICOS  │          │    NUMÉRICOS    │
    └───────┬───────┘          └────────┬────────┘
            │                           │
     ┌──────┴──────┐           ┌────────┴────────┐
     │             │           │                 │
     ▼             ▼           ▼                 ▼
┌─────────┐  ┌─────────┐  ┌─────────┐    ┌──────────┐
│NOMINALES│  │ORDINALES│  │DISCRETOS│    │CONTINUOS │
└─────────┘  └─────────┘  └─────────┘    └──────────┘
```

---

## Datos Categóricos

Los datos categóricos son aquellos que **no están representados por números** (o si lo están, los números actúan como etiquetas, no como cantidades). Son **categorías** o **etiquetas**.

### Características principales:

- No se pueden sumar, restar o promediar
- Representan grupos o clases
- Pueden ser texto o números usados como etiquetas

---

### Tipos de Datos Categóricos

#### 1. Datos Nominales

**Definición:** Categorías **sin orden natural**. No hay jerarquía entre ellas.

**Ejemplos:**

```python
# Género
genero = ['Masculino', 'Femenino', 'No binario']

# Color de coche
colores = ['Rojo', 'Azul', 'Verde', 'Negro', 'Blanco']

# Método de pago
metodo_pago = ['Tarjeta de Crédito', 'PayPal', 'Transferencia', 'Efectivo']

# Categoría de película
categorias_pelicula = ['Terror', 'Acción', 'Drama', 'Comedia', 'Ciencia Ficción']

# Tipo de motor
tipo_motor = ['Gasolina', 'Diésel', 'Eléctrico', 'Híbrido']
```

**Operaciones válidas:**
- ✅ Contar frecuencias
- ✅ Calcular moda (categoría más frecuente)
- ✅ Crear tablas de contingencia
- ❌ Ordenar con significado
- ❌ Calcular promedio

---

#### 2. Datos Ordinales

**Definición:** Categorías **con orden natural**. Existe una jerarquía o secuencia lógica.

**Ejemplos:**

```python
# Tamaño de ropa
tallas = ['XS', 'S', 'M', 'L', 'XL', 'XXL']  # Orden: de menor a mayor

# Nivel educativo
educacion = ['Primaria', 'Secundaria', 'Técnico', 'Universitario', 'Posgrado']

# Calificación de satisfacción
satisfaccion = ['Muy Insatisfecho', 'Insatisfecho', 'Neutral', 'Satisfecho', 'Muy Satisfecho']

# Nivel de experiencia
experiencia = ['Junior', 'Mid-level', 'Senior', 'Lead']

# Clasificación de películas
rating = ['G', 'PG', 'PG-13', 'R', 'NC-17']
```

**Operaciones válidas:**
- ✅ Contar frecuencias
- ✅ Calcular moda
- ✅ Ordenar con significado
- ✅ Calcular mediana (valor central)
- ✅ Comparaciones (>, <, ≥, ≤)
- ❌ Calcular promedio (no tiene sentido matemático)

---

### Ejemplo Comparativo

```python
import pandas as pd

# Datos nominales: No hay orden
colores = pd.Series(['Rojo', 'Azul', 'Verde', 'Rojo', 'Azul', 'Rojo'])
print("Moda de colores:", colores.mode()[0])  # ✅ Válido: "Rojo"
# print(colores.mean())  # ❌ Error: no se puede promediar colores

# Datos ordinales: Sí hay orden
tallas = pd.Series(['M', 'L', 'S', 'XL', 'M', 'S', 'L', 'M'])
tallas_ordenadas = pd.Categorical(tallas, categories=['S', 'M', 'L', 'XL'], ordered=True)
print("Moda de tallas:", tallas_ordenadas.mode()[0])  # ✅ Válido: "M"
print("Mediana (índice):", tallas_ordenadas.median())  # ✅ Válido con índices
```

---

## Datos Numéricos

Los datos numéricos se representan **exclusivamente con números** y deben tratarse numéricamente. Soportan operaciones matemáticas completas.

### Características principales:

- Se pueden sumar, restar, multiplicar, dividir
- Tienen magnitud y distancia
- Soportan todas las operaciones estadísticas

---

### Tipos de Datos Numéricos

#### 1. Datos Discretos

**Definición:** Solo pueden tomar **valores enteros**. No hay valores intermedios.

**Características:**
- Conteos
- Valores separados (no continuos)
- Tipo de variable: `int` en programación

**Ejemplos:**

```python
# Número de hijos
num_hijos = [0, 1, 2, 3, 4]  # No puedes tener 2.5 hijos

# Cantidad de productos vendidos
productos_vendidos = [10, 25, 30, 15, 8]

# Número de clientes
clientes_dia = [120, 145, 98, 167, 133]

# Edad (años cumplidos)
edades = [15, 20, 25, 30, 35]  # Aunque tengas 25.8 años, reportas 25

# Número de transacciones
transacciones = [5, 12, 8, 20, 3]
```

---

#### 2. Datos Continuos

**Definición:** Pueden tomar **cualquier valor** dentro de un rango, incluyendo decimales.

**Características:**
- Mediciones
- Valores infinitos posibles entre dos puntos
- Tipo de variable: `float` en programación

**Ejemplos:**

```python
# Altura (metros)
alturas = [1.65, 1.82, 1.75, 1.58, 1.90]

# Peso (kg)
pesos = [68.5, 82.3, 71.0, 59.8, 95.2]

# Temperatura (°C)
temperaturas = [23.5, 18.2, 30.7, 15.9, 27.3]

# Precio
precios = [19.99, 45.50, 120.00, 8.75, 299.99]

# Tiempo (segundos)
tiempos = [12.45, 15.89, 10.23, 18.76, 14.02]
```

---

### Ejemplo Comparativo

```python
import pandas as pd
import numpy as np

# Discretos: Solo enteros
num_productos = pd.Series([10, 15, 20, 25, 30])
print("Promedio de productos:", num_productos.mean())  # 20.0
print("Tipo de dato:", num_productos.dtype)  # int64

# Continuos: Con decimales
precios = pd.Series([19.99, 25.50, 30.00, 18.75, 22.99])
print("Promedio de precios:", precios.mean())  # 23.446
print("Tipo de dato:", precios.dtype)  # float64
```

---

## Identificación de Tipos en Python

### Tipos de datos en pandas

```python
import pandas as pd

# Crear DataFrame de ejemplo
data = {
    'cliente_id': [1, 2, 3, 4, 5],                           # Numérico discreto
    'genero': ['M', 'F', 'M', 'F', 'M'],                     # Categórico nominal
    'talla': ['M', 'L', 'S', 'XL', 'M'],                     # Categórico ordinal
    'edad': [25, 34, 28, 45, 31],                            # Numérico discreto
    'altura_m': [1.75, 1.62, 1.80, 1.68, 1.85],              # Numérico continuo
    'peso_kg': [72.5, 58.3, 85.0, 63.7, 92.1],               # Numérico continuo
    'num_compras': [3, 7, 2, 12, 5],                         # Numérico discreto
    'satisfaccion': ['Alto', 'Medio', 'Alto', 'Bajo', 'Medio']  # Categórico ordinal
}

df = pd.DataFrame(data)
```

---

### Verificar tipos de datos

```python
# Método 1: .dtypes
print("TIPOS DE DATOS:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

# Método 2: .info()
print("INFORMACIÓN DETALLADA:")
df.info()
```

**Output esperado:**

```
TIPOS DE DATOS:
cliente_id         int64
genero            object
talla             object
edad               int64
altura_m         float64
peso_kg          float64
num_compras        int64
satisfaccion      object

==================================================

INFORMACIÓN DETALLADA:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 8 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   cliente_id    5 non-null      int64  
 1   genero        5 non-null      object 
 2   talla         5 non-null      object 
 3   edad          5 non-null      int64  
 4   altura_m      5 non-null      float64
 5   peso_kg       5 non-null      float64
 6   num_compras   5 non-null      int64  
 7   satisfaccion  5 non-null      object 
```

---

### Conversión de tipos (casting)

```python
# Convertir a categórico ordinal
df['talla'] = pd.Categorical(
    df['talla'], 
    categories=['S', 'M', 'L', 'XL'], 
    ordered=True
)

df['satisfaccion'] = pd.Categorical(
    df['satisfaccion'],
    categories=['Bajo', 'Medio', 'Alto'],
    ordered=True
)

# Verificar conversión
print("Tipos después de conversión:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

# Ahora podemos ordenar con significado
print("DataFrame ordenado por talla:")
print(df.sort_values('talla'))
```

---

## Ejemplos Prácticos con pandas

### Ejemplo 1: Análisis de dataset cars.csv

```python
import pandas as pd

# Cargar dataset
df = pd.read_csv('cars.csv')

# Exploración inicial
print("DIMENSIONES DEL DATASET:")
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
print("\n" + "="*60 + "\n")

# Ver primeras filas
print("PRIMERAS 5 FILAS:")
print(df.head())
print("\n" + "="*60 + "\n")

# Tipos de datos
print("TIPOS DE DATOS:")
print(df.dtypes)
print("\n" + "="*60 + "\n")

# Información general
print("INFORMACIÓN DEL DATASET:")
df.info()
```

---

### Ejemplo 2: Identificar variables numéricas vs categóricas

```python
# Separar por tipo
variables_numericas = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
variables_categoricas = df.select_dtypes(include=['object']).columns.tolist()

print("VARIABLES NUMÉRICAS:")
print(variables_numericas)
print(f"Total: {len(variables_numericas)}\n")

print("VARIABLES CATEGÓRICAS:")
print(variables_categoricas)
print(f"Total: {len(variables_categoricas)}\n")
```

---

### Ejemplo 3: Estadísticas descriptivas según tipo

```python
# Para variables numéricas
print("ESTADÍSTICAS DESCRIPTIVAS - VARIABLES NUMÉRICAS:")
print(df[variables_numericas].describe())
print("\n" + "="*60 + "\n")

# Para variables categóricas
print("ESTADÍSTICAS DESCRIPTIVAS - VARIABLES CATEGÓRICAS:")
for col in variables_categoricas[:3]:  # Primeras 3 para no saturar
    print(f"\n{col}:")
    print(df[col].value_counts().head())
    print(f"  - Valores únicos: {df[col].nunique()}")
    print(f"  - Moda: {df[col].mode()[0]}")
```

---

## Casos de Uso en Data Science

### Caso de Uso 1: Preprocesamiento de Datos de Clientes

**Contexto:** Una empresa de e-commerce necesita limpiar y preparar sus datos de clientes para un análisis de segmentación.

**Solución:**

```python
import pandas as pd
import numpy as np

# Datos crudos con tipos mixtos
np.random.seed(42)
clientes_raw = pd.DataFrame({
    'id': range(1, 101),
    'edad': np.random.randint(18, 70, 100),
    'genero': np.random.choice(['M', 'F', 'Otro'], 100),
    'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla'], 100),
    'ingreso_mensual': np.random.uniform(1000, 10000, 100).round(2),
    'num_compras': np.random.poisson(5, 100),
    'nivel_educacion': np.random.choice(['Primaria', 'Secundaria', 'Universitario'], 100),
    'satisfaccion': np.random.choice([1, 2, 3, 4, 5], 100)
})

print("PASO 1: IDENTIFICAR TIPOS")
print("="*60)
print(clientes_raw.dtypes)
print("\n")

# PASO 2: Convertir variables ordinales
print("PASO 2: CONVERTIR VARIABLES ORDINALES")
print("="*60)

# Nivel educativo (ordinal)
clientes_raw['nivel_educacion'] = pd.Categorical(
    clientes_raw['nivel_educacion'],
    categories=['Primaria', 'Secundaria', 'Universitario'],
    ordered=True
)

# Satisfacción (ordinal)
clientes_raw['satisfaccion'] = pd.Categorical(
    clientes_raw['satisfaccion'],
    categories=[1, 2, 3, 4, 5],
    ordered=True
)

print("Tipos después de conversión:")
print(clientes_raw.dtypes)
print("\n")

# PASO 3: Crear segmentos basados en tipos de datos
print("PASO 3: SEGMENTACIÓN POR INGRESO")
print("="*60)

# Variable continua → Convertir a categórica
clientes_raw['segmento_ingreso'] = pd.cut(
    clientes_raw['ingreso_mensual'],
    bins=[0, 3000, 6000, float('inf')],
    labels=['Bajo', 'Medio', 'Alto']
)

print(clientes_raw.groupby('segmento_ingreso').agg({
    'edad': 'mean',
    'num_compras': 'mean',
    'ingreso_mensual': 'mean'
}).round(2))
```

**Explicación:** Este flujo demuestra cómo identificar correctamente los tipos de datos permite realizar transformaciones apropiadas y crear segmentaciones útiles para análisis de negocio.

---

### Caso de Uso 2: Validación de Tipos en Pipeline ETL

**Contexto:** Un pipeline de datos necesita validar que los datos cargados tengan los tipos correctos antes de procesarlos.

**Solución:**

```python
import pandas as pd

def validar_tipos_datos(df, esquema_esperado):
    """
    Valida que un DataFrame tenga los tipos de datos esperados.
    
    Args:
        df: DataFrame a validar
        esquema_esperado: dict con {columna: tipo_esperado}
    
    Returns:
        dict con errores encontrados
    """
    errores = {}
    
    for columna, tipo_esperado in esquema_esperado.items():
        if columna not in df.columns:
            errores[columna] = f"Columna no encontrada en el DataFrame"
        elif df[columna].dtype != tipo_esperado:
            errores[columna] = f"Tipo incorrecto: {df[columna].dtype}, esperado: {tipo_esperado}"
    
    return errores

# Esquema esperado
esquema = {
    'cliente_id': 'int64',
    'edad': 'int64',
    'ingreso_anual': 'float64',
    'genero': 'object',
    'num_compras': 'int64'
}

# Crear DataFrame de prueba
df_prueba = pd.DataFrame({
    'cliente_id': [1, 2, 3],
    'edad': [25, 30, 35],
    'ingreso_anual': [50000, 60000, 70000],  # float
    'genero': ['M', 'F', 'M'],
    'num_compras': [5, 8, 3]
})

# Validar
errores = validar_tipos_datos(df_prueba, esquema)

if errores:
    print("⚠️ ERRORES DE TIPO DETECTADOS:")
    for col, error in errores.items():
        print(f"  - {col}: {error}")
else:
    print("✅ TODOS LOS TIPOS DE DATOS SON CORRECTOS")
    print("\nResumen del DataFrame:")
    df_prueba.info()
```

**Explicación:** La validación de tipos es crucial en pipelines de producción para detectar problemas temprano y evitar errores en análisis posteriores.

---

## Recursos Adicionales

### 📚 Conceptos clave

- **Categórico Nominal:** Sin orden (colores, géneros)
- **Categórico Ordinal:** Con orden (tallas, niveles)
- **Numérico Discreto:** Enteros (conteos)
- **Numérico Continuo:** Decimales (mediciones)

### 🔗 Enlaces útiles

- [Pandas dtype reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)
- [Pandas Categorical data](https://pandas.pydata.org/docs/user_guide/categorical.html)
- [Dataset cars.csv en Kaggle](https://www.kaggle.com/lepchenkov/usedcarscatalog)

### 📂 Archivos relacionados

- `cars.csv` - Dataset de ejemplo usado en el curso
- Notebook de ejercicios: `ejercicios_estadistica_descriptiva.ipynb`

### 🎯 Puntos clave para recordar

1. **El tipo de dato determina el análisis posible**
2. **Categóricos nominales:** Sin orden (colores, género)
3. **Categóricos ordinales:** Con orden (tallas, satisfacción)
4. **Numéricos discretos:** Enteros (conteos)
5. **Numéricos continuos:** Decimales (mediciones)
6. **Siempre verificar tipos** con `.dtypes` o `.info()`
7. **Convertir cuando sea necesario** usando `pd.Categorical()` o `.astype()`

---

**Actualizado:** Noviembre 2025  
**Progreso de la ruta:** 68% completado (13/19 cursos)