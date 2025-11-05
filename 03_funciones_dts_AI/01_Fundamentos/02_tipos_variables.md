# Tipos de Variables en Data Science

**Curso:** Lenguaje y Notación Matemática / Fundamentos de Matemáticas  
**Fecha:** 30 de octubre de 2025  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto General](#concepto-general)
2. [Clasificación de Variables](#clasificación-de-variables)
3. [Variables Cualitativas](#variables-cualitativas)
4. [Variables Cuantitativas](#variables-cuantitativas)
5. [Variables Especiales](#variables-especiales)
6. [Casos de Uso en Data Science](#casos-de-uso-en-data-science)
7. [Ejercicios Prácticos](#ejercicios-prácticos)
8. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto General

Una **variable** es una característica o atributo que puede tomar diferentes valores en un conjunto de datos. Es lo que observamos, medimos o registramos.

**Ejemplos:**
- Color del LED: puede ser rojo, verde o azul
- Altura de un objeto: puede ser alto, medio o bajo
- Edad de un cliente: puede ser 25, 30, 45 años
- Estado de un servidor: puede ser "activo" o "inactivo"

### ¿Por qué clasificar variables?

Porque el **tipo de variable determina**:
- Qué análisis puedes hacer
- Qué gráficos puedes crear
- Qué modelos estadísticos aplicar
- Cómo preprocesar los datos

---

## Clasificación de Variables

```
VARIABLES
├── CUALITATIVAS (Describen cualidades)
│   ├── Nominales (sin orden)
│   ├── Ordinales (con orden)
│   └── Binarias (2 valores)
│
└── CUANTITATIVAS (Representan cantidad)
    ├── Discretas (valores finitos/separados)
    └── Continuas (valores infinitos)
```

---

## Variables Cualitativas

Las variables **cualitativas** describen **cualidades o características** de los datos. **No son números**, son categorías.

### 1. Variables Nominales

**Definición:** Variables que representan categorías sin ningún orden o jerarquía.

**Característica clave:** No hay relación de orden entre los valores.

**Ejemplos:**
- Colores de un LED: rojo, verde, azul
- Marca de smartphone: Apple, Samsung, Xiaomi
- País de origen: España, Colombia, México
- Tipo de departamento: Ventas, Soporte, Producto, RRHH
- Género: Masculino, Femenino, Otro

**¿Puedes ordenarlas?** NO. "Rojo" no es ni mayor ni menor que "azul".

**En código:**

```python
import pandas as pd

# Crear DataFrame con variable nominal
df_productos = pd.DataFrame({
    'producto_id': [1, 2, 3, 4, 5],
    'color': ['rojo', 'verde', 'azul', 'rojo', 'verde'],
    'marca': ['Apple', 'Samsung', 'Xiaomi', 'Apple', 'Samsung']
})

print(df_productos.dtypes)  # object (texto)
print(df_productos['color'].unique())  # ['rojo' 'verde' 'azul']
print(df_productos['color'].value_counts())  # Contar ocurrencias
```

### 2. Variables Ordinales

**Definición:** Variables que representan categorías **CON un orden o jerarquía** implícita.

**Característica clave:** Existe una relación de orden entre los valores.

**Ejemplos:**
- Altura de un objeto: Bajo < Medio < Alto
- Nivel de satisfacción: Muy Insatisfecho < Insatisfecho < Neutral < Satisfecho < Muy Satisfecho
- Educación: Primaria < Secundaria < Universidad < Posgrado
- Criticidad de un ticket: Baja < Media < Alta < Crítica
- Tamaño de empresa: Pequeña < Mediana < Grande < Empresa

**¿Puedes ordenarlas?** SÍ. "Medio" es mayor que "Bajo".

**En código:**

```python
import pandas as pd
from pandas.api.types import CategoricalDtype

# Crear DataFrame con variable ordinal
df_empleados = pd.DataFrame({
    'empleado_id': [1, 2, 3, 4, 5],
    'nombre': ['Juan', 'María', 'Carlos', 'Ana', 'Luis'],
    'nivel_satisfaccion': ['Bajo', 'Medio', 'Alto', 'Bajo', 'Muy Alto']
})

# Definir orden correcto (IMPORTANTE)
orden_satisfaccion = ['Bajo', 'Medio', 'Alto', 'Muy Alto']
df_empleados['nivel_satisfaccion'] = pd.Categorical(
    df_empleados['nivel_satisfaccion'],
    categories=orden_satisfaccion,
    ordered=True
)

print(df_empleados.dtypes)  # category
print(df_empleados['nivel_satisfaccion'].value_counts().sort_index())
```

### 3. Variables Binarias

**Definición:** Variables que **solo pueden tomar dos valores**, generalmente True/False, Sí/No, 0/1.

**Característica clave:** Representan presencia/ausencia o estados opuestos.

**Ejemplos:**
- Existe o no existe: True/False
- Está frío o caliente: True/False
- Uno o cero: 1/0
- Cliente activo o inactivo: Active/Inactive
- Email verificado o no: Yes/No
- Ticket resuelto o no: Resuelto/No Resuelto
- Servidor encendido o apagado: On/Off

**¿Puedes ordenarlas?** Técnicamente sí, pero representa estados opuestos, no una escala.

**En código:**

```python
import pandas as pd

# Crear DataFrame con variable binaria
df_clientes = pd.DataFrame({
    'cliente_id': [1, 2, 3, 4, 5, 6],
    'nombre': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Enrique', 'Fiona'],
    'email_verificado': [True, False, True, True, False, True],
    'es_cliente_activo': [1, 0, 1, 1, 0, 1],  # También puedes usar 1/0
    'ticket_resuelto': ['Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
})

print(df_clientes.dtypes)
print(df_clientes['email_verificado'].value_counts())  # Contar True/False

# Convertir a numérico para análisis
df_clientes['email_verificado_num'] = df_clientes['email_verificado'].astype(int)
print(df_clientes['email_verificado_num'].sum())  # Contar Trues
```

---

## Variables Cuantitativas

Las variables **cuantitativas** representan **cantidades numéricas**. Responden a "¿cuánto?" o "¿cuál es el valor?"

### 1. Variables Discretas

**Definición:** Variables que toman **valores finitos y separados**, generalmente números enteros.

**Característica clave:** Existe un "paso" o salto entre valores. No puede haber valores intermedios.

**La pregunta clave:** ¿Hay "paso" entre valores?

**Ejemplos:**
- Cantidad de amigos: 0, 1, 2, 3... (no puedes tener 3.5 amigos)
- Número de tickets abiertos: 0, 1, 2, 5, 10...
- Cantidad de compras: 1, 2, 3, 100...
- Número de llamadas recibidas: 0, 5, 12, 87...
- Cantidad de errores en código: 0, 1, 3, 15...
- Número de empleados: 50, 100, 250...

**¿Valores intermedios?** NO. No tiene sentido 3.7 amigos o 5.3 tickets.

**En código:**

```python
import pandas as pd
import numpy as np

# Crear DataFrame con variable discreta
df_tiendas = pd.DataFrame({
    'tienda_id': [1, 2, 3, 4, 5],
    'nombre': ['Tienda A', 'Tienda B', 'Tienda C', 'Tienda D', 'Tienda E'],
    'cantidad_productos': [50, 150, 87, 200, 120],  # Discreta
    'numero_empleados': [5, 15, 8, 20, 12],  # Discreta
    'tickets_abiertos': [3, 7, 2, 10, 5]  # Discreta
})

print(df_tiendas.dtypes)  # int64
print(df_tiendas['cantidad_productos'].describe())
print(df_tiendas['cantidad_productos'].value_counts().sort_index())

# Visualizar distribución
import matplotlib.pyplot as plt
plt.bar(df_tiendas['tienda_id'], df_tiendas['cantidad_productos'])
plt.title('Cantidad de Productos (Variable Discreta)')
plt.xlabel('Tienda ID')
plt.ylabel('Cantidad')
plt.show()
```

### 2. Variables Continuas

**Definición:** Variables que pueden tomar **infinitos valores** dentro de un rango. Son números reales.

**Característica clave:** NO hay "paso" entre valores. Pueden ser tan precisos como quieras.

**Ejemplos:**
- Estatura de una persona: 1.75 m, 1.751 m, 1.7512 m, 1.75123456...
- Peso: 75.5 kg, 75.52 kg, 75.523 kg...
- Tiempo de respuesta: 2.3 segundos, 2.34 segundos, 2.345 segundos...
- Temperatura: 20.5°C, 20.53°C, 20.537°C...
- Puntuación CSAT normalizada: 0.5, 0.55, 0.556, 0.5567...
- Precio de producto: $49.99, $49.999, $49.9999...

**¿Valores intermedios?** SÍ, infinitos. Entre 1.75 y 1.76 hay infinitos números.

**En código:**

```python
import pandas as pd
import numpy as np

# Crear DataFrame con variable continua
df_mediciones = pd.DataFrame({
    'persona_id': [1, 2, 3, 4, 5],
    'nombre': ['Juan', 'María', 'Carlos', 'Ana', 'Luis'],
    'estatura_m': [1.75, 1.62, 1.88, 1.70, 1.92],  # Continua
    'peso_kg': [75.5, 62.3, 85.7, 68.2, 92.1],  # Continua
    'tiempo_respuesta_s': [2.345, 1.234, 3.456, 1.892, 2.567]  # Continua
})

print(df_mediciones.dtypes)  # float64
print(df_mediciones['estatura_m'].describe())

# Visualizar distribución
import matplotlib.pyplot as plt
plt.hist(df_mediciones['estatura_m'], bins=10, edgecolor='black')
plt.title('Distribución de Estatura (Variable Continua)')
plt.xlabel('Estatura (m)')
plt.ylabel('Frecuencia')
plt.show()
```

---

## Variables Especiales

### Dominio y Rango (Contexto de Funciones)

Cuando trabajas con **funciones**, las variables tienen características especiales:

**Dominio (X - Variable Independiente):**
- Conjunto de valores que **puedes introducir** en la función
- Depende de la definición de la función
- Ejemplo: En `f(x) = 1/x`, el dominio es todos los números reales EXCEPTO 0

**Rango (Y - Variable Dependiente):**
- Conjunto de **resultados** que genera la función
- Depende de qué hace la función
- Ejemplo: En `f(x) = x²`, el rango es todos los números reales positivos (≥ 0)

**Ejemplo práctico:**

```python
# Función CSAT con restricciones de dominio
def calcular_csat_normalizado(puntuacion):
    """
    Dominio: números entre 1 y 10
    Rango: números entre 0 y 1
    """
    if puntuacion < 1 or puntuacion > 10:
        raise ValueError(f"Puntuación fuera del dominio: {puntuacion}")
    
    normalizado = (puntuacion - 1) / 9
    return normalizado

# Dominio válido
print(calcular_csat_normalizado(5))  # ✓ 0.4444
print(calcular_csat_normalizado(10))  # ✓ 1.0
print(calcular_csat_normalizado(1))  # ✓ 0.0

# Fuera del dominio
try:
    print(calcular_csat_normalizado(0))  # ✗ Error
except ValueError as e:
    print(f"Error: {e}")
```

---

## Casos de Uso en Data Science

### Caso de Uso 1: Análisis de Encuestas CSAT (Tu Proyecto)

**Contexto:** Tu proyecto recolecta encuestas con múltiples tipos de variables.

**Datos:**
```python
import pandas as pd

df_encuestas = pd.DataFrame({
    # Variable Ordinal: Satisfacción
    'satisfaccion': ['Bajo', 'Alto', 'Medio', 'Alto', 'Bajo'],
    
    # Variable Nominal: Departamento
    'departamento': ['Ventas', 'Soporte', 'Producto', 'Ventas', 'RH'],
    
    # Variable Binaria: Email verificado
    'email_verificado': [True, True, False, True, False],
    
    # Variable Discreta: Número de tickets
    'tickets_abiertos': [3, 0, 5, 1, 2],
    
    # Variable Continua: Puntuación CSAT (1-10)
    'puntuacion_csat': [3.5, 9.2, 6.7, 8.9, 2.1],
    
    # Variable Continua: Tiempo de respuesta (horas)
    'tiempo_respuesta_h': [24.5, 1.2, 18.3, 0.5, 36.7]
})

print("Tipos de variables en tu dataset CSAT:")
print(df_encuestas.dtypes)
print()

# Análisis por tipo de variable
print("NOMINALES - Conteo por departamento:")
print(df_encuestas['departamento'].value_counts())
print()

print("ORDINALES - Distribución de satisfacción:")
print(df_encuestas['satisfaccion'].value_counts())
print()

print("BINARIAS - Emails verificados:")
print(df_encuestas['email_verificado'].value_counts())
print()

print("DISCRETAS - Estadísticas de tickets:")
print(df_encuestas['tickets_abiertos'].describe())
print()

print("CONTINUAS - Estadísticas de tiempo de respuesta:")
print(df_encuestas['tiempo_respuesta_h'].describe())
```

**Salida esperada:**
```
Tipos de variables en tu dataset CSAT:
satisfaccion             object
departamento             object
email_verificado           bool
tickets_abiertos          int64
puntuacion_csat         float64
tiempo_respuesta_h      float64

NOMINALES - Conteo por departamento:
Ventas     2
Soporte    1
Producto   1
RH         1

ORDINALES - Distribución de satisfacción:
Alto    2
Bajo    2
Medio   1

BINARIAS - Emails verificados:
True     3
False    2

DISCRETAS - Estadísticas de tickets:
count    5.000000
mean     2.200000
std      1.923538
min      0.000000
max      5.000000

CONTINUAS - Estadísticas de tiempo de respuesta:
count     5.000000
mean     16.240000
std      14.905862
min       0.500000
max      36.700000
```

### Caso de Uso 2: Preparación de Datos para Modelo ML

**Contexto:** Diferentes tipos de variables requieren diferente tratamiento antes de entrenar un modelo.

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Dataset con todos los tipos de variables
df = pd.DataFrame({
    'cliente_id': [1, 2, 3, 4, 5],
    
    # Nominal: No ordenada
    'ciudad': ['NYC', 'LA', 'NYC', 'Chicago', 'LA'],
    
    # Ordinal: Tiene orden
    'nivel_cliente': ['Bronze', 'Silver', 'Gold', 'Bronze', 'Platinum'],
    
    # Binaria: Solo 2 valores
    'vip': [0, 1, 1, 0, 1],
    
    # Discreta: Números enteros con "paso"
    'num_compras': [5, 12, 3, 8, 20],
    
    # Continua: Números reales
    'gasto_promedio': [150.75, 320.50, 89.99, 210.25, 450.00],
    'tasa_satisfaccion': [0.65, 0.92, 0.45, 0.78, 0.88]
})

print("Dataset original:")
print(df)
print(f"\nTipos: {df.dtypes.to_dict()}\n")

# PROCESAMIENTO SEGÚN TIPO DE VARIABLE

# 1. Variables Nominales → One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['ciudad'], prefix='ciudad')
print("Después de One-Hot Encoding (Nominal):")
print(df_encoded[['ciudad_LA', 'ciudad_NYC', 'ciudad_Chicago']])
print()

# 2. Variables Ordinales → Label Encoding (mantener orden)
ordenes_nivel = {'Bronze': 1, 'Silver': 2, 'Gold': 3, 'Platinum': 4}
df_encoded['nivel_cliente_encoded'] = df['nivel_cliente'].map(ordenes_nivel)
print("Después de Label Encoding (Ordinal):")
print(df_encoded['nivel_cliente_encoded'])
print()

# 3. Variables Binarias → Ya están bien (0/1)
print("Variable Binaria (sin cambios):")
print(df['vip'])
print()

# 4. Variables Discretas → A veces normalizar
scaler = StandardScaler()
df_encoded['num_compras_normalizado'] = scaler.fit_transform(df[['num_compras']])
print("Variable Discreta (normalizada):")
print(df_encoded['num_compras_normalizado'])
print()

# 5. Variables Continuas → Normalizar
df_encoded['gasto_promedio_normalizado'] = scaler.fit_transform(df[['gasto_promedio']])
print("Variable Continua (normalizada):")
print(df_encoded['gasto_promedio_normalizado'])
```

---

## Ejercicios Prácticos

### Ejercicio 1: Identificar Tipo de Variable [Nivel Básico]

**Enunciado:** Para cada una de las siguientes variables, identifica si es Nominal, Ordinal, Binaria, Discreta o Continua:

1. Marca de automóvil (Toyota, Honda, BMW)
2. Número de empleados en una empresa
3. Temperatura en grados Celsius
4. Estado civil (Soltero, Casado, Divorciado)
5. Cuenta bancaria activa (Sí/No)
6. Calificación del hotel (⭐⭐, ⭐⭐⭐, ⭐⭐⭐⭐, ⭐⭐⭐⭐⭐)
7. Edad de un cliente
8. Color de ojos (Azul, Marrón, Verde)

**Pistas:**
- ¿Tiene orden? → Probablemente Ordinal
- ¿Solo 2 valores? → Binaria
- ¿Números enteros sin decimales? → Probablemente Discreta
- ¿Puede tener decimales infinitos? → Continua
- ¿Categorías sin orden? → Nominal

<details>
<summary>💡 Ver solución</summary>

```python
# Clasificación de variables

respuestas = {
    'Marca de automóvil': 'NOMINAL (categorías sin orden)',
    'Número de empleados': 'DISCRETA (números enteros)',
    'Temperatura en Celsius': 'CONTINUA (puede tener decimales)',
    'Estado civil': 'NOMINAL (categorías sin orden)',
    'Cuenta bancaria activa': 'BINARIA (Sí/No)',
    'Calificación del hotel': 'ORDINAL (tiene orden: ⭐ < ⭐⭐ < ...)',
    'Edad de cliente': 'CONTINUA (puede ser 25.7 años)',
    'Color de ojos': 'NOMINAL (categorías sin orden)'
}

for variable, clasificacion in respuestas.items():
    print(f"{variable:30} → {clasificacion}")
```

**Explicación:**
- Marca de automóvil: No hay razón para que Toyota > Honda
- Calificación hotel: ⭐⭐⭐ es mejor que ⭐⭐
- Edad: 25.7 años es válido (continua)
- Temperatura: 20.5°C es válido (continua)

</details>

---

### Ejercicio 2: Crear DataFrame con Tipos de Variables [Nivel Básico-Intermedio]

**Enunciado:** Crea un DataFrame con datos de clientes que tenga al menos un ejemplo de cada tipo de variable (Nominal, Ordinal, Binaria, Discreta, Continua). Luego imprime los tipos de datos y realiza un análisis básico.

**Pistas:**
- Usa `pd.DataFrame()` con diccionarios de listas
- Las Ordinales deben definirse con `pd.Categorical` y `ordered=True`
- Imprime `df.dtypes` para verificar tipos
- Usa `.value_counts()` para contar categorías

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd

# Crear DataFrame con todos los tipos de variables
df_clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'nombre': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Enrique'],
    
    # NOMINAL
    'ciudad': ['NYC', 'LA', 'Chicago', 'NYC', 'Boston'],
    
    # ORDINAL
    'nivel_membresia': ['Bronze', 'Silver', 'Gold', 'Silver', 'Platinum'],
    
    # BINARIA
    'es_vip': [0, 1, 1, 0, 1],
    
    # DISCRETA
    'num_compras': [5, 12, 3, 8, 20],
    
    # CONTINUA
    'gasto_total': [150.75, 320.50, 89.99, 210.25, 450.00]
})

# Convertir ORDINAL a tipo correcto
orden_membresia = ['Bronze', 'Silver', 'Gold', 'Platinum']
df_clientes['nivel_membresia'] = pd.Categorical(
    df_clientes['nivel_membresia'],
    categories=orden_membresia,
    ordered=True
)

print("=" * 60)
print("ESTRUCTURA DEL DATAFRAME")
print("=" * 60)
print(df_clientes.dtypes)
print()

print("=" * 60)
print("VISTA GENERAL")
print("=" * 60)
print(df_clientes)
print()

print("=" * 60)
print("ANÁLISIS POR TIPO DE VARIABLE")
print("=" * 60)

print("\n1. NOMINAL (ciudad) - Conteos:")
print(df_clientes['ciudad'].value_counts())

print("\n2. ORDINAL (nivel_membresia) - Distribuición ordenada:")
print(df_clientes['nivel_membresia'].value_counts().sort_index())

print("\n3. BINARIA (es_vip) - Conteos:")
print(df_clientes['es_vip'].value_counts())

print("\n4. DISCRETA (num_compras) - Estadísticas:")
print(df_clientes['num_compras'].describe())

print("\n5. CONTINUA (gasto_total) - Estadísticas:")
print(df_clientes['gasto_total'].describe())
```

**Explicación:**
- `pd.Categorical()` con `ordered=True` asegura que Ordinal tenga orden
- `.value_counts()` cuenta ocurrencias en categorías
- `.describe()` da estadísticas en numéricas
- Los tipos de datos son diferentes: object, category, int64, float64

</details>

---

### Ejercicio 3: Filtrar y Agrupar por Tipo de Variable [Nivel Intermedio]

**Enunciado:** Usando el DataFrame anterior, realiza los siguientes análisis:
1. Cuenta cuántos clientes hay por ciudad (Nominal)
2. Calcula gasto promedio por nivel de membresía (Ordinal vs Continua)
3. Compara gasto entre clientes VIP y no VIP (Binaria vs Continua)
4. Encuentra el cliente con más compras (Discreta)

**Pistas:**
- Usa `groupby()` para agrupar
- Usa `mean()` para calcular promedios
- Usa `max()` y `idxmax()` para encontrar máximos
- Usa `[]` para filtrar por valor

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd

# Crear DataFrame
df_clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'nombre': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Enrique'],
    'ciudad': ['NYC', 'LA', 'Chicago', 'NYC', 'Boston'],
    'nivel_membresia': ['Bronze', 'Silver', 'Gold', 'Silver', 'Platinum'],
    'es_vip': [0, 1, 1, 0, 1],
    'num_compras': [5, 12, 3, 8, 20],
    'gasto_total': [150.75, 320.50, 89.99, 210.25, 450.00]
})

print("=" * 60)
print("ANÁLISIS 1: Clientes por Ciudad (NOMINAL)")
print("=" * 60)
clientes_por_ciudad = df_clientes['ciudad'].value_counts()
print(clientes_por_ciudad)
print()

print("=" * 60)
print("ANÁLISIS 2: Gasto Promedio por Membresía (ORDINAL vs CONTINUA)")
print("=" * 60)
gasto_por_membresia = df_clientes.groupby('nivel_membresia')['gasto_total'].mean()
print(gasto_por_membresia)
print()

print("=" * 60)
print("ANÁLISIS 3: Gasto de VIP vs No-VIP (BINARIA vs CONTINUA)")
print("=" * 60)
vip_status = {0: 'No VIP', 1: 'VIP'}
gasto_por_vip = df_clientes.groupby('es_vip')['gasto_total'].agg(['mean', 'sum', 'count'])
gasto_por_vip.index = gasto_por_vip.index.map(vip_status)
print(gasto_por_vip)
print()

print("=" * 60)
print("ANÁLISIS 4: Cliente con Más Compras (DISCRETA)")
print("=" * 60)
idx_max_compras = df_clientes['num_compras'].idxmax()
cliente_max = df_clientes.loc[idx_max_compras]
print(f"Cliente: {cliente_max['nombre']}")
print(f"Compras: {cliente_max['num_compras']}")
print(f"Gasto: ${cliente_max['gasto_total']:.2f}")
```

**Explicación:**
- `groupby('columna').agg()` es muy potente para resúmenes
- `idxmax()` retorna el índice del máximo
- `.loc[]` accede por índice
- Estos análisis son típicos en exploratory data analysis (EDA)

</details>

---

### Ejercicio 4: Transformar Variables Según su Tipo [Nivel Intermedio-Avanzado]

**Enunciado:** Dado un dataset crudo, aplica transformaciones apropiadas según el tipo de variable:
- Nominal: Codificar con One-Hot Encoding
- Ordinal: Codificar manteniendo orden numérico
- Binaria: Mantener como está o convertir a 0/1
- Discreta: Normalizar con StandardScaler
- Continua: Normalizar con Min-Max scaling

**Pistas:**
- Usa `pd.get_dummies()` para Nominales
- Usa `.map()` con diccionario para Ordinales
- Usa `sklearn.preprocessing.StandardScaler` y `MinMaxScaler`
- Crea una función que clasifique y transforme

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Dataset crudo
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'ciudad': ['NYC', 'LA', 'NYC', 'Chicago', 'LA'],  # NOMINAL
    'nivel': ['Bajo', 'Alto', 'Medio', 'Bajo', 'Alto'],  # ORDINAL
    'activo': [1, 0, 1, 1, 0],  # BINARIA
    'compras': [5, 12, 3, 8, 20],  # DISCRETA
    'gasto': [150.75, 320.50, 89.99, 210.25, 450.00]  # CONTINUA
})

print("Dataset original:")
print(df)
print("\n" + "=" * 80 + "\n")

# PASO 1: One-Hot Encoding para NOMINAL
df_encoded = pd.get_dummies(df, columns=['ciudad'], prefix='ciudad', drop_first=True)
print("Después de One-Hot Encoding (Nominal):")
print(df_encoded[['ciudad_LA', 'ciudad_NYC']].head())
print("\n" + "=" * 80 + "\n")

# PASO 2: Label Encoding para ORDINAL
orden_nivel = {'Bajo': 1, 'Medio': 2, 'Alto': 3}
df_encoded['nivel_encoded'] = df['nivel'].map(orden_nivel)
print("Después de Label Encoding (Ordinal):")
print(df_encoded['nivel_encoded'])
print("\n" + "=" * 80 + "\n")

# PASO 3: BINARIA (dejar como está)
print("Variable Binaria (sin cambios):")
print(df_encoded['activo'])
print("\n" + "=" * 80 + "\n")

# PASO 4: StandardScaler para DISCRETA
scaler_standard = StandardScaler()
df_encoded['compras_scaled'] = scaler_standard.fit_transform(df[['compras']])
print("Después de StandardScaler (Discreta):")
print(df_encoded['compras_scaled'])
print("\n" + "=" * 80 + "\n")

# PASO 5: MinMaxScaler para CONTINUA
scaler_minmax = MinMaxScaler()
df_encoded['gasto_scaled'] = scaler_minmax.fit_transform(df[['gasto']])
print("Después de MinMaxScaler (Continua):")
print(df_encoded['gasto_scaled'])
print("\n" + "=" * 80 + "\n")

print("Dataset transformado final:")
print(df_encoded[[
    'id', 
    'ciudad_LA', 'ciudad_NYC',
    'nivel_encoded',
    'activo',
    'compras_scaled',
    'gasto_scaled'
]])
```

**Explicación:**
- Cada tipo de variable tiene su transformación apropiada
- Nominales necesitan expandirse (One-Hot)
- Ordinales necesitan mantener orden (etiquetas numéricas)
- Continuas y Discretas se normalizan según el contexto
- Este es el flujo típico en preparación de datos para ML

</details>

---

### Ejercicio 5: Caso Real - Análisis Completo de Dataset CSAT [Nivel Desafío]

**Enunciado:** Usando un dataset similar al de tu proyecto CSAT, realiza un análisis completo que incluya:
1. Identificar el tipo de cada variable
2. Hacer estadísticas descriptivas
3. Encontrar relaciones entre variables (ej: ¿VIPs tienen CSAT más alto?)
4. Preparar datos para un modelo ML (transformar según tipo)
5. Crear visualizaciones por tipo de variable

**Pistas:**
- Crea un dataset más realista con 20-30 filas
- Usa `df.info()` y `df.dtypes` para identificar tipos
- Usa múltiples `groupby()` para encontrar relaciones
- Transforma variables como en el ejercicio anterior
- Usa `matplotlib` o `seaborn` para visualizaciones

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import seaborn as sns

# Crear dataset CSAT realista
np.random.seed(42)
n = 20

df_csat = pd.DataFrame({
    'encuesta_id': range(1, n+1),
    
    # NOMINAL
    'departamento': np.random.choice(['Ventas', 'Soporte', 'Producto'], n),
    'ciudad_cliente': np.random.choice(['NYC', 'LA', 'Chicago'], n),
    
    # ORDINAL
    'satisfaccion': np.random.choice(['Muy Bajo', 'Bajo', 'Medio', 'Alto', 'Muy Alto'], n),
    
    # BINARIA
    'es_vip': np.random.choice([0, 1], n),
    
    # DISCRETA
    'num_interacciones': np.random.randint(1, 20, n),
    
    # CONTINUA
    'csat_score': np.round(np.random.uniform(1, 10, n), 2),
    'tiempo_respuesta_h': np.round(np.random.uniform(0.5, 48, n), 2)
})

print("=" * 80)
print("1. INFORMACIÓN DEL DATASET")
print("=" * 80)
print(f"Shape: {df_csat.shape}")
print(f"\nTipos de datos:\n{df_csat.dtypes}")
print(f"\nPrimeras 5 filas:")
print(df_csat.head())
print("\n")

# Convertir ORDINAL correctamente
orden_satisfaccion = ['Muy Bajo', 'Bajo', 'Medio', 'Alto', 'Muy Alto']
df_csat['satisfaccion'] = pd.Categorical(
    df_csat['satisfaccion'],
    categories=orden_satisfaccion,
    ordered=True
)

print("=" * 80)
print("2. ESTADÍSTICAS DESCRIPTIVAS POR TIPO")
print("=" * 80)

print("\nNOMINAL - Departamentos:")
print(df_csat['departamento'].value_counts())

print("\nNOMINAL - Ciudades:")
print(df_csat['ciudad_cliente'].value_counts())

print("\nORDINAL - Satisfacción:")
print(df_csat['satisfaccion'].value_counts().sort_index())

print("\nBINARIA - VIP Status:")
print(df_csat['es_vip'].value_counts())

print("\nDISCRETA - Interacciones:")
print(df_csat['num_interacciones'].describe())

print("\nCONTINUA - CSAT Score:")
print(df_csat['csat_score'].describe())

print("\nCONTINUA - Tiempo Respuesta:")
print(df_csat['tiempo_respuesta_h'].describe())
print("\n")

print("=" * 80)
print("3. RELACIONES ENTRE VARIABLES")
print("=" * 80)

print("\nCSAT promedio por DEPARTAMENTO (NOMINAL):")
print(df_csat.groupby('departamento')['csat_score'].agg(['mean', 'count']))

print("\nCSAT promedio por SATISFACCIÓN (ORDINAL):")
print(df_csat.groupby('satisfaccion')['csat_score'].mean())

print("\nCSAT promedio: VIP vs No VIP (BINARIA):")
vip_label = {0: 'No VIP', 1: 'VIP'}
csat_por_vip = df_csat.groupby('es_vip')['csat_score'].mean()
print(csat_por_vip.rename(index=vip_label))

print("\nCorrelación entre DISCRETAS y CONTINUAS:")
print(f"Correlación (Interacciones vs CSAT): {df_csat['num_interacciones'].corr(df_csat['csat_score']):.4f}")
print(f"Correlación (Tiempo Respuesta vs CSAT): {df_csat['tiempo_respuesta_h'].corr(df_csat['csat_score']):.4f}")
print("\n")

print("=" * 80)
print("4. PREPARACIÓN DE DATOS PARA ML")
print("=" * 80)

df_ml = df_csat.copy()

# NOMINAL: One-Hot Encoding
df_ml = pd.get_dummies(df_ml, columns=['departamento', 'ciudad_cliente'], drop_first=True)

# ORDINAL: Label Encoding
orden_map = {v: i for i, v in enumerate(orden_satisfaccion)}
df_ml['satisfaccion_encoded'] = df_csat['satisfaccion'].map(orden_map)

# BINARIA: Ya está bien (0/1)
# DISCRETA: Normalizar
scaler_std = StandardScaler()
df_ml['num_interacciones_scaled'] = scaler_std.fit_transform(df_csat[['num_interacciones']])

# CONTINUA: Normalizar
scaler_mm = MinMaxScaler()
df_ml['csat_score_scaled'] = scaler_mm.fit_transform(df_csat[['csat_score']])
df_ml['tiempo_respuesta_scaled'] = scaler_mm.fit_transform(df_csat[['tiempo_respuesta_h']])

print("Columnas transformadas:")
print(df_ml.columns.tolist())
print("\nPrimeras filas del dataset preparado:")
print(df_ml[[
    'es_vip',
    'satisfaccion_encoded',
    'num_interacciones_scaled',
    'csat_score_scaled'
]].head())
print("\n")

print("=" * 80)
print("5. VISUALIZACIONES")
print("=" * 80)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Nominal
df_csat['departamento'].value_counts().plot(kind='bar', ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('NOMINAL: Encuestas por Departamento')
axes[0, 0].set_ylabel('Cantidad')

# Ordinal
df_csat['satisfaccion'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 1], color='lightgreen')
axes[0, 1].set_title('ORDINAL: Distribución de Satisfacción')
axes[0, 1].set_ylabel('Cantidad')

# Binaria
df_csat['es_vip'].value_counts().plot(kind='bar', ax=axes[0, 2], color='coral')
axes[0, 2].set_title('BINARIA: VIP vs No VIP')
axes[0, 2].set_ylabel('Cantidad')
axes[0, 2].set_xticklabels(['No VIP', 'VIP'], rotation=0)

# Discreta
axes[1, 0].hist(df_csat['num_interacciones'], bins=10, color='gold', edgecolor='black')
axes[1, 0].set_title('DISCRETA: Número de Interacciones')
axes[1, 0].set_xlabel('Interacciones')
axes[1, 0].set_ylabel('Frecuencia')

# Continua 1
axes[1, 1].hist(df_csat['csat_score'], bins=10, color='lightblue', edgecolor='black')
axes[1, 1].set_title('CONTINUA: Distribución CSAT Score')
axes[1, 1].set_xlabel('CSAT Score')
axes[1, 1].set_ylabel('Frecuencia')

# Continua 2
axes[1, 2].hist(df_csat['tiempo_respuesta_h'], bins=10, color='plum', edgecolor='black')
axes[1, 2].set_title('CONTINUA: Tiempo de Respuesta')
axes[1, 2].set_xlabel('Horas')
axes[1, 2].set_ylabel('Frecuencia')

plt.tight_layout()
plt.savefig('analisis_tipos_variables.png', dpi=100, bbox_inches='tight')
plt.show()

print("✓ Gráfico guardado como 'analisis_tipos_variables.png'")
```

**Explicación:**
- Este ejercicio integra TODO lo aprendido sobre tipos de variables
- Muestra cómo cada tipo se analiza, se relaciona y se transforma
- Es muy similar a lo que harás con tu proyecto CSAT real
- La visualización muestra cómo cada tipo de variable se ve diferente

</details>

---

## Recursos Adicionales

- **Documentación oficial Pandas**: [Data Types](https://pandas.pydata.org/docs/user_guide/basics.html#dtypes)
- **Scikit-learn Preprocessing**: [Transformers](https://scikit-learn.org/stable/modules/preprocessing.html)
- **Archivos relacionados**:
  - `07_lenguaje_notacion_matematica.md`
  - `10_funciones_matematicas_ds_ia.md`
- **Próximos temas**:
  - Estadística Descriptiva (cálculos por tipo de variable)
  - Visualización de datos (gráficos según tipo)
  - Feature Engineering (transformar variables para ML)

---

**Actualizado:** 30 de octubre de 2025  
**Progreso de la ruta:** 42% completado (8/19 cursos)  
**Estado:** Completado ✅