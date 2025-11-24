# Estructura del Curso de Estadística Descriptiva

**Curso:** Matemáticas para Data Science: Estadística Descriptiva  
**Fecha:** Noviembre 2025  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [¿Qué hace único a este curso?](#qué-hace-único-a-este-curso)
2. [Estructura del Curso](#estructura-del-curso)
3. [Bloque 1: Ingesta de Datos y Validación](#bloque-1-ingesta-de-datos-y-validación)
4. [Bloque 2: Preparación de Datos y Análisis Exploratorio](#bloque-2-preparación-de-datos-y-análisis-exploratorio)
5. [¿Qué NO cubre este curso?](#qué-no-cubre-este-curso)
6. [Enfoque Práctico con Python](#enfoque-práctico-con-python)
7. [Filosofías Fundamentales](#filosofías-fundamentales)
8. [Mapa Conceptual del Curso](#mapa-conceptual-del-curso)
9. [Recursos Adicionales](#recursos-adicionales)

---

## ¿Qué hace único a este curso?

La **estadística descriptiva** es una parte esencial de las matemáticas que ofrece múltiples aplicaciones en la ciencia de datos. Aunque existe gran cantidad de material sobre este tema, **este curso es diferente**.

### Diferenciadores clave:

#### 1. Contextualización en Data Science
- No solo fórmulas matemáticas, sino **aplicaciones prácticas**
- Conexión directa con el flujo de trabajo en ciencia de datos
- Casos de uso reales y relevantes

#### 2. Enfoque en "la cara correcta" de las estadísticas
- Cómo identificar **qué estadístico usar según el contexto**
- No todas las medidas son apropiadas para todos los casos
- Interpretación crítica de resultados

#### 3. Inspirado en "The Naked Statistics"
- Profundiza en lo **realmente importante**
- Desmitifica conceptos complejos
- Enfoque práctico y aplicado

#### 4. Reconocimiento de uso implícito
- Muchos conceptos estadísticos ya se usan sin saberlo
- El curso ayuda a **hacer consciente lo inconsciente**
- Formaliza conocimientos prácticos existentes

---

## Estructura del Curso

El curso se divide en **dos grandes bloques**, cada uno enfocado en diferentes aspectos de la estadística descriptiva aplicada a la ciencia de datos.

```
┌─────────────────────────────────────────────────────┐
│         CURSO: ESTADÍSTICA DESCRIPTIVA               │
│              APLICADA A DATA SCIENCE                 │
└─────────────────────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌───────────────────┐         ┌────────────────────┐
│    BLOQUE 1       │         │     BLOQUE 2       │
│                   │         │                    │
│ Ingesta de Datos  │         │ Preparación de     │
│   y Validación    │         │  Datos y Análisis  │
│                   │         │    Exploratorio    │
└───────────────────┘         └────────────────────┘
        │                               │
        │                               │
    Incluye:                        Incluye:
    • Tipos de datos                • EDA
    • Pipeline                      • Correlaciones
    • Transformaciones              • Reducción de datos
```

---

## Bloque 1: Ingesta de Datos y Validación

### Objetivo principal
Que los estudiantes **reconozcan** que muchos elementos de la estadística descriptiva se han estado utilizando sin ser conscientes de ello.

---

### 1.1. Identificación de Tipos de Datos

Es crucial en data science reconocer con qué tipo de datos estamos trabajando.

#### Tipos de variables:

**Variables Numéricas:**
- **Continuas:** Pueden tomar cualquier valor en un rango (ej. altura, temperatura)
- **Discretas:** Solo valores enteros (ej. número de clientes, cantidad de productos)

**Cadenas de Texto:**
- **Categóricas:** Valores de un conjunto finito (ej. país, género, categoría de producto)
- **Texto libre:** Texto sin estructura fija (ej. reseñas, comentarios)

**Datos Estructurados:**
- Tablas, bases de datos relacionales
- Formato organizado y predecible

**Datos No Estructurados:**
- Imágenes, audio, video, texto libre
- Sin formato predefinido

#### Ejemplo en Python:

```python
import pandas as pd
import numpy as np

# Dataset de ejemplo
data = {
    'cliente_id': [1, 2, 3, 4, 5],                    # Numérico discreto
    'edad': [25, 34, 28, 45, 31],                     # Numérico discreto
    'ingreso_anual': [45000.50, 67000.75, 52000.00, 89000.25, 61000.50],  # Numérico continuo
    'pais': ['México', 'Colombia', 'España', 'Argentina', 'Perú'],  # Categórico
    'comentario': ['Excelente servicio', 'Muy bueno', 'Regular', 'Malo', 'Bueno']  # Texto
}

df = pd.DataFrame(data)

# Identificar tipos de datos
print("TIPOS DE DATOS EN EL DATAFRAME:")
print(df.dtypes)
print("\n" + "="*50)

# Información detallada
print("\nINFORMACIÓN DETALLADA:")
df.info()
```

#### Por qué es importante:

1. **Determina qué operaciones son válidas**
   - No puedes calcular la media de una variable categórica
   - No puedes hacer regresión con texto sin procesar

2. **Influye en el preprocesamiento**
   - Variables numéricas: normalización, escalamiento
   - Variables categóricas: one-hot encoding, label encoding
   - Texto: tokenización, vectorización

3. **Afecta la elección de visualizaciones**
   - Numéricas: histogramas, boxplots
   - Categóricas: gráficos de barras, pie charts

---

### 1.2. Definición del Pipeline de Procesamiento

Aquí se decide **qué se necesita hacer con los datos** para que sean útiles.

#### Componentes típicos del pipeline:

```python
# Pipeline conceptual de procesamiento

# 1. CARGA DE DATOS
df = pd.read_csv('datos_crudos.csv')

# 2. LIMPIEZA
# - Manejo de valores nulos
df = df.dropna()  # o df.fillna()

# - Eliminación de duplicados
df = df.drop_duplicates()

# - Corrección de tipos de datos
df['fecha'] = pd.to_datetime(df['fecha'])

# 3. TRANSFORMACIÓN
# - Normalización (valores entre 0 y 1)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['ingreso_normalizado'] = scaler.fit_transform(df[['ingreso_anual']])

# - Escalamiento (media=0, std=1)
from sklearn.preprocessing import StandardScaler
scaler_std = StandardScaler()
df['ingreso_escalado'] = scaler_std.fit_transform(df[['ingreso_anual']])

# 4. VALIDACIÓN
print(f"Filas procesadas: {len(df)}")
print(f"Columnas procesadas: {len(df.columns)}")
print(f"Valores nulos restantes: {df.isnull().sum().sum()}")
```

#### Transformaciones comunes con bases estadísticas:

**1. Normalización (Min-Max Scaling)**

Fórmula: `x_norm = (x - min) / (max - min)`

```python
import pandas as pd
import numpy as np

# Datos originales
datos = pd.Series([10, 20, 30, 40, 50])

# Normalización manual
datos_norm = (datos - datos.min()) / (datos.max() - datos.min())

print("Datos originales:", datos.values)
print("Datos normalizados:", datos_norm.values)
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

**2. Estandarización (Z-score Scaling)**

Fórmula: `z = (x - μ) / σ`

```python
# Estandarización manual
media = datos.mean()
std = datos.std()
datos_stand = (datos - media) / std

print("Datos originales:", datos.values)
print("Datos estandarizados:", datos_stand.round(2).values)
# Output: [-1.41, -0.71, 0.0, 0.71, 1.41]
```

**3. Log Transform (para datos sesgados)**

```python
# Datos con sesgo positivo
datos_sesgados = pd.Series([1, 10, 100, 1000, 10000])

# Transformación logarítmica
datos_log = np.log10(datos_sesgados)

print("Datos originales:", datos_sesgados.values)
print("Datos log-transformados:", datos_log.values)
# Output: [0.0, 1.0, 2.0, 3.0, 4.0]
```

#### Objetivo del Bloque 1:

> Reconocer que conceptos como **normalización**, **escalamiento**, **detección de outliers** y **validación de tipos** son aplicaciones directas de la estadística descriptiva que probablemente ya has usado.

---

## Bloque 2: Preparación de Datos y Análisis Exploratorio

### Objetivo principal
Comprender la importancia de la estadística descriptiva en la **exploración y análisis de datos**, para extraer insights valiosos o construir modelos efectivos.

---

### 2.1. Análisis Exploratorio de Datos (EDA)

El **EDA** es una herramienta esencial en data science que implica:

#### Actividades principales:

**1. Identificar correlaciones**

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset de ejemplo
np.random.seed(42)
df = pd.DataFrame({
    'edad': np.random.normal(35, 10, 100),
    'ingreso': np.random.normal(50000, 15000, 100),
    'gasto': np.random.normal(30000, 8000, 100)
})

# Correlación de ingreso con gasto (positiva esperada)
df['gasto'] = df['ingreso'] * 0.6 + np.random.normal(0, 5000, 100)

# Matriz de correlación
correlacion = df.corr()
print("MATRIZ DE CORRELACIÓN:")
print(correlacion.round(3))

# Visualización
sns.heatmap(correlacion, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlación')
plt.show()
```

**2. Resumir distribuciones**

```python
# Estadísticas descriptivas completas
print("\nESTADÍSTICAS DESCRIPTIVAS:")
print(df.describe())

# Medidas de tendencia central
print(f"\nMedia de ingreso: ${df['ingreso'].mean():,.2f}")
print(f"Mediana de ingreso: ${df['ingreso'].median():,.2f}")
print(f"Moda de edad: {df['edad'].mode()[0]:.1f} años")

# Medidas de dispersión
print(f"\nDesviación estándar de gasto: ${df['gasto'].std():,.2f}")
print(f"Rango de edad: {df['edad'].max() - df['edad'].min():.1f} años")
print(f"Coeficiente de variación (CV): {df['ingreso'].std() / df['ingreso'].mean() * 100:.2f}%")
```

**3. Reducir conjuntos de datos**

Cuando tienes demasiadas variables, necesitas reducir dimensionalidad:

```python
# Ejemplo conceptual: Reducción de variables correlacionadas
# Si 'ingreso_mensual' e 'ingreso_anual' están altamente correlacionados (r > 0.95)
# podemos eliminar uno sin perder información significativa

# Identificar variables altamente correlacionadas
umbral = 0.95
correlacion_alta = correlacion.abs() > umbral

# Excluir diagonal (una variable siempre está 100% correlacionada consigo misma)
np.fill_diagonal(correlacion_alta.values, False)

print("\nVARIABLES ALTAMENTE CORRELACIONADAS:")
print(correlacion_alta)
```

**4. Detectar outliers**

```python
# Método IQR (Rango Intercuartílico)
Q1 = df['ingreso'].quantile(0.25)
Q3 = df['ingreso'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['ingreso'] < limite_inferior) | (df['ingreso'] > limite_superior)]

print(f"\nOUTLIERS DETECTADOS: {len(outliers)}")
print(f"Límite inferior: ${limite_inferior:,.2f}")
print(f"Límite superior: ${limite_superior:,.2f}")
```

---

### 2.2. Preparación Final para Modelado

Antes de entrenar un modelo de machine learning, el EDA proporciona:

#### Insights clave:

1. **¿Qué variables son más importantes?**
   - Correlación con la variable objetivo
   - Poder predictivo de cada feature

2. **¿Hay variables redundantes?**
   - Altamente correlacionadas entre sí
   - Pueden eliminarse sin pérdida de información

3. **¿Los datos están balanceados?**
   - En problemas de clasificación
   - Distribución de clases

4. **¿Necesitamos transformaciones?**
   - Distribuciones sesgadas → log transform
   - Escalas diferentes → normalización

#### Ejemplo completo de EDA:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset simulado de clientes
np.random.seed(100)
n = 500

df_clientes = pd.DataFrame({
    'edad': np.random.normal(40, 15, n).clip(18, 80),
    'ingreso_anual': np.random.lognormal(10.5, 0.5, n),
    'antiguedad_meses': np.random.poisson(24, n),
    'num_productos': np.random.poisson(2, n),
    'satisfaccion': np.random.randint(1, 6, n),
    'recomendaria': np.random.choice([0, 1], n, p=[0.3, 0.7])
})

print("="*60)
print("ANÁLISIS EXPLORATORIO DE DATOS (EDA)")
print("="*60)

# 1. VISIÓN GENERAL
print("\n1. PRIMERAS 5 FILAS:")
print(df_clientes.head())

print("\n2. INFORMACIÓN GENERAL:")
df_clientes.info()

# 2. ESTADÍSTICAS DESCRIPTIVAS
print("\n3. ESTADÍSTICAS DESCRIPTIVAS:")
print(df_clientes.describe().round(2))

# 3. CORRELACIONES
print("\n4. MATRIZ DE CORRELACIÓN:")
correlaciones = df_clientes.corr()
print(correlaciones.round(3))

# Visualización de correlaciones
plt.figure(figsize=(10, 8))
sns.heatmap(correlaciones, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1)
plt.title('Matriz de Correlación - Datos de Clientes')
plt.tight_layout()
plt.show()

# 4. DISTRIBUCIONES
print("\n5. ANÁLISIS DE DISTRIBUCIONES:")
for columna in df_clientes.select_dtypes(include=[np.number]).columns:
    print(f"\n{columna.upper()}:")
    print(f"  Asimetría (skewness): {df_clientes[columna].skew():.3f}")
    print(f"  Curtosis: {df_clientes[columna].kurtosis():.3f}")

# 5. OUTLIERS
print("\n6. DETECCIÓN DE OUTLIERS (método IQR):")
for columna in ['ingreso_anual', 'antiguedad_meses']:
    Q1 = df_clientes[columna].quantile(0.25)
    Q3 = df_clientes[columna].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df_clientes[
        (df_clientes[columna] < Q1 - 1.5 * IQR) | 
        (df_clientes[columna] > Q3 + 1.5 * IQR)
    ]
    print(f"  {columna}: {len(outliers)} outliers detectados ({len(outliers)/len(df_clientes)*100:.1f}%)")

# 6. INSIGHTS CLAVE
print("\n7. INSIGHTS CLAVE:")
print(f"  • Cliente promedio: {df_clientes['edad'].mean():.1f} años")
print(f"  • Ingreso anual mediano: ${df_clientes['ingreso_anual'].median():,.2f}")
print(f"  • Tasa de recomendación: {df_clientes['recomendaria'].mean()*100:.1f}%")
print(f"  • Productos promedio por cliente: {df_clientes['num_productos'].mean():.2f}")
```

---

## ¿Qué NO cubre este curso?

Este curso se centra en la **estadística descriptiva** aplicada a ciencia de datos y **NO cubrirá**:

### Temas de Estadística Inferencial:

| Tema Excluido | Descripción |
|---------------|-------------|
| **Teoría de Probabilidad** | Distribuciones de probabilidad, teorema de Bayes |
| **Inferencia Estadística** | Estimación de parámetros, intervalos de confianza |
| **Tests de Hipótesis** | t-test, ANOVA, chi-cuadrado, p-valores |
| **Modelos Predictivos** | Regresión, clasificación, series temporales |

### Por qué esta separación:

La estadística se divide en dos ramas:

- **Descriptiva (este curso):** ¿Qué muestran los datos que tenemos?
- **Inferencial (otro curso):** ¿Qué podemos predecir o inferir sobre datos que no tenemos?

```
┌─────────────────────────────────────────┐
│         ESTADÍSTICA                     │
└─────────────────────────────────────────┘
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
┌──────────────┐  ┌──────────────┐
│ DESCRIPTIVA  │  │ INFERENCIAL  │
│ (Este curso) │  │(Otro curso)  │
└──────────────┘  └──────────────┘
        │                │
        │                │
    - Resumen        - Predicción
    - Visualización  - Pruebas
    - Exploración    - Inferencia
```

---

## Enfoque Práctico con Python

A lo largo del curso se abordarán diferentes componentes y prácticas esenciales en estadística descriptiva, **comenzando por los tipos de datos** y **trabajando con código en Python**.

### Herramientas principales:

```python
# Librerías fundamentales del curso
import pandas as pd          # Manipulación de datos
import numpy as np           # Cálculos numéricos
import matplotlib.pyplot as plt  # Visualización
import seaborn as sns        # Visualización estadística
```

### Metodología de aprendizaje:

1. **Concepto teórico** → Explicación clara del fundamento estadístico
2. **Implementación en Python** → Código práctico y ejecutable
3. **Ejercicios interactivos** → Aplicación inmediata del conocimiento
4. **Casos reales** → Contexto de data science

Este enfoque práctico permite:
- ✅ Aplicar inmediatamente lo aprendido
- ✅ Reforzar lecturas teóricas con práctica
- ✅ Mejorar comprensión y habilidades en data science

---

## Filosofías Fundamentales

El curso se enfoca en **dos filosofías fundamentales**:

### 1. Estadística para Ingesta y Procesamiento

**Objetivo:** Usar la estadística para preparar datos de calidad

```
Datos Crudos → [Estadística Descriptiva] → Datos Limpios
```

**Aplicaciones:**
- Identificación de tipos de datos
- Detección de anomalías
- Normalización y escalamiento
- Validación de calidad

---

### 2. Estadística para Analítica y Exploración

**Objetivo:** Usar la estadística para extraer insights

```
Datos Limpios → [Estadística Descriptiva] → Insights Accionables
```

**Aplicaciones:**
- Análisis exploratorio de datos (EDA)
- Identificación de patrones
- Correlaciones y relaciones
- Reducción de dimensionalidad

---

## Mapa Conceptual del Curso

```
                    ┌─────────────────────────────┐
                    │ ESTADÍSTICA DESCRIPTIVA      │
                    │   EN DATA SCIENCE            │
                    └──────────────┬──────────────┘
                                   │
                ┌──────────────────┴─────────────────┐
                │                                    │
                ▼                                    ▼
    ┌───────────────────────┐          ┌────────────────────────┐
    │      BLOQUE 1         │          │       BLOQUE 2         │
    │ Ingesta y Validación  │          │  Preparación y EDA     │
    └───────────────────────┘          └────────────────────────┘
                │                                    │
        ┌───────┴────────┐                  ┌────────┴────────┐
        │                │                  │                 │
        ▼                ▼                  ▼                 ▼
┌──────────────┐  ┌──────────┐    ┌─────────────┐  ┌──────────────┐
│Tipos de Datos│  │ Pipeline │    │     EDA     │  │ Correlaciones│
└──────────────┘  └──────────┘    └─────────────┘  └──────────────┘
        │                │                  │                 │
        └────────────────┴──────────────────┴─────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │    APLICACIÓN PRÁCTICA    │
                    │  Código Python + Casos    │
                    └──────────────────────────┘
```

---

## Recursos Adicionales

### 📚 Lectura recomendada

**"Naked Statistics" de Charles Wheelan**
- Desmitifica conceptos estadísticos
- Enfoque práctico y accesible
- Inspiración directa para este curso

### 🔗 Documentación oficial

- [Pandas: Statistical functions](https://pandas.pydata.org/docs/reference/frame.html#computations-descriptive-stats)
- [NumPy: Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [Seaborn: Statistical data visualization](https://seaborn.pydata.org/)

### 📂 Archivos relacionados

- `01_que_es_estadistica_descriptiva.md` - Introducción a estadística descriptiva
- `02_flujo_trabajo_ciencia_datos.md` - Contexto del flujo de trabajo
- Siguiente: Tipos de datos en Python

### 🎯 Resumen de objetivos del curso

| Bloque | Qué aprenderás | Aplicación práctica |
|--------|----------------|---------------------|
| **1** | Tipos de datos, pipelines, transformaciones | Preprocesamiento de datos |
| **2** | EDA, correlaciones, reducción de datos | Exploración antes de modelar |

---

**Actualizado:** Noviembre 2025  
**Progreso de la ruta:** 68% completado (13/19 cursos)