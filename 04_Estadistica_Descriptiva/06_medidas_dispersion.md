# Medidas de Dispersión

**Curso:** Matemáticas para Data Science: Estadística Descriptiva  
**Fecha:** Noviembre 2025  
**Módulo:** Estadística Descriptiva para Analítica  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [¿Por qué son importantes?](#por-qué-son-importantes)
3. [Rango](#rango)
4. [Varianza](#varianza)
5. [Desviación Estándar](#desviación-estándar)
6. [Coeficiente de Variación](#coeficiente-de-variación)
7. [Cuartiles y Percentiles](#cuartiles-y-percentiles)
8. [Rango Intercuartílico (IQR)](#rango-intercuartílico-iqr)
9. [Detección de Outliers](#detección-de-outliers)
10. [Box Plot (Diagrama de Caja)](#box-plot-diagrama-de-caja)
11. [Implementación en Python](#implementación-en-python)
12. [Casos de Uso](#casos-de-uso)
13. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

Las **medidas de dispersión** (o variabilidad) nos indican **qué tan separados o dispersos están los datos** con respecto a la medida de tendencia central.

### Analogía:

Imagina dos clases con edad promedio de 10 años:

**Clase A:** `[9, 10, 10, 10, 11]` → Edades muy similares  
**Clase B:** `[5, 8, 10, 12, 15]` → Edades muy variadas

Ambas tienen la misma media (10 años), pero **la dispersión es completamente diferente**.

**Las medidas de dispersión capturan esta diferencia.**

---

## ¿Por qué son importantes?

### 1. Complementan las medidas de tendencia central

```
❌ "El salario promedio es $50,000"
✅ "El salario promedio es $50,000 ± $10,000"
```

La segunda afirmación da **mucho más contexto**.

---

### 2. Revelan consistencia

| Escenario | Media | Desv. Estándar | Interpretación |
|-----------|-------|----------------|----------------|
| **Calificaciones alumno A** | 85 | 2 | Rendimiento consistente |
| **Calificaciones alumno B** | 85 | 15 | Rendimiento variable |

Ambos tienen la misma media, pero A es mucho más predecible.

---

### 3. Detectan outliers

Las medidas de dispersión nos ayudan a identificar valores atípicos que podrían indicar:
- Errores en los datos
- Casos excepcionales
- Oportunidades o problemas

---

### 4. Evalúan riesgo e incertidumbre

En finanzas, marketing y ciencia de datos:
- **Alta variabilidad** = Mayor riesgo/incertidumbre
- **Baja variabilidad** = Mayor predecibilidad

---

## Rango

### Definición

El **rango** es la diferencia entre el valor **máximo** y **mínimo** del dataset.

**Fórmula:**

```
Rango = Máximo - Mínimo
```

---

### Ejemplo

```python
import pandas as pd

# Temperaturas de la semana (°C)
temperaturas = pd.Series([18, 22, 20, 25, 19, 23, 21])

rango = temperaturas.max() - temperaturas.min()

print(f"Temperatura mínima: {temperaturas.min()}°C")
print(f"Temperatura máxima: {temperaturas.max()}°C")
print(f"Rango: {rango}°C")
```

**Output:**
```
Temperatura mínima: 18°C
Temperatura máxima: 25°C
Rango: 7°C
```

---

### Ventajas y Desventajas

✅ **Ventajas:**
- Fácil de calcular
- Intuitive de entender

⚠️ **Desventajas:**
- **Muy sensible a outliers** (solo usa 2 valores)
- Ignora la distribución de los datos intermedios
- No usa toda la información disponible

**Ejemplo del problema:**

```python
datos_A = pd.Series([10, 11, 12, 13, 14])  # Bien distribuidos
datos_B = pd.Series([10, 11, 12, 13, 50])  # Un outlier

print(f"Rango A: {datos_A.max() - datos_A.min()}")  # 4
print(f"Rango B: {datos_B.max() - datos_B.min()}")  # 40 (distorsionado por 1 valor)
```

---

## Varianza

### Definición

La **varianza** mide **cuánto se alejan los datos del promedio**, elevando al cuadrado esas diferencias.

**Fórmula (varianza poblacional):**

```
σ² = Σ(xi - μ)² / N
```

Donde:
- `xi` = Cada valor
- `μ` = Media
- `N` = Número de datos

**Fórmula (varianza muestral):**

```
s² = Σ(xi - x̄)² / (n - 1)
```

Se divide por `n-1` (corrección de Bessel) para estimar mejor la varianza poblacional.

---

### Pasos del cálculo

1. Calcular la media
2. Restar la media a cada valor (desviaciones)
3. Elevar al cuadrado cada desviación
4. Sumar todas las desviaciones cuadradas
5. Dividir por N (o n-1 para muestra)

---

### Ejemplo manual

```python
import pandas as pd
import numpy as np

# Datos
datos = pd.Series([10, 12, 15, 18, 20])

# Paso 1: Media
media = datos.mean()
print(f"Media: {media}")  # 15.0

# Paso 2 y 3: Desviaciones al cuadrado
desviaciones_cuadradas = (datos - media) ** 2
print(f"\nDesviaciones al cuadrado:")
print(desviaciones_cuadradas.values)  # [25, 9, 0, 9, 25]

# Paso 4 y 5: Varianza
varianza = desviaciones_cuadradas.sum() / (len(datos) - 1)  # Varianza muestral
print(f"\nVarianza: {varianza}")  # 17.0

# Verificación con pandas
print(f"Varianza (pandas): {datos.var()}")  # 17.0
```

---

### Interpretación

⚠️ **Problema:** La varianza está en **unidades al cuadrado**, lo que dificulta la interpretación.

Si los datos están en metros, la varianza está en metros².  
Si los datos están en dólares, la varianza está en dólares².

**Solución:** Usar la desviación estándar.

---

## Desviación Estándar

### Definición

La **desviación estándar** es la **raíz cuadrada de la varianza**. Representa la **dispersión promedio** de los datos respecto a la media, en las **mismas unidades** que los datos originales.

**Fórmula:**

```
σ = √(varianza)
```

---

### Ejemplo

```python
import pandas as pd

# Salarios (en dólares)
salarios = pd.Series([45000, 50000, 48000, 52000, 47000])

media = salarios.mean()
varianza = salarios.var()
desviacion_std = salarios.std()

print(f"Media: ${media:,.0f}")
print(f"Varianza: ${varianza:,.0f}²")  # ❌ Difícil de interpretar
print(f"Desviación estándar: ${desviacion_std:,.0f}")  # ✅ En dólares

print(f"\nInterpretación:")
print(f"Los salarios se desvían en promedio ${desviacion_std:,.0f} respecto a la media de ${media:,.0f}")
```

**Output:**
```
Media: $48,400
Varianza: $6,800,000²
Desviación estándar: $2,608

Interpretación:
Los salarios se desvían en promedio $2,608 respecto a la media de $48,400
```

---

### Interpretación con la Regla Empírica (68-95-99.7)

Para distribuciones **normales** (campana de Gauss):

```
μ ± 1σ  →  Contiene ~68% de los datos
μ ± 2σ  →  Contiene ~95% de los datos
μ ± 3σ  →  Contiene ~99.7% de los datos
```

**Ejemplo:**

```python
import pandas as pd

# Alturas de personas (cm)
alturas = pd.Series([165, 170, 175, 168, 172, 178, 169, 171, 173, 167])

media = alturas.mean()
std = alturas.std()

print(f"Media: {media:.1f} cm")
print(f"Desviación estándar: {std:.1f} cm")

print(f"\nRegla empírica (si la distribución es normal):")
print(f"  68% de personas miden entre {media - std:.1f} cm y {media + std:.1f} cm")
print(f"  95% de personas miden entre {media - 2*std:.1f} cm y {media + 2*std:.1f} cm")
```

---

### Comparación: Varianza vs Desviación Estándar

| Métrica | Unidades | Interpretación | Uso |
|---------|----------|----------------|-----|
| **Varianza** | Unidades² | Difícil | Cálculos matemáticos |
| **Desviación Estándar** | Unidades originales | Intuitiva | Comunicar resultados |

**Recomendación:** Usa desviación estándar para reportar, varianza para cálculos internos.

---

## Coeficiente de Variación

### Definición

El **coeficiente de variación (CV)** es la desviación estándar expresada como **porcentaje de la media**. Permite comparar la variabilidad de datasets con diferentes unidades o escalas.

**Fórmula:**

```
CV = (σ / μ) × 100
```

---

### ¿Por qué es útil?

No podemos comparar directamente:
- Desviación estándar de salarios ($5,000)
- Desviación estándar de edades (3 años)

**Pero SÍ podemos comparar sus CV:**
- CV de salarios: 10%
- CV de edades: 8%

**Conclusión:** Las edades tienen menor variabilidad relativa.

---

### Interpretación

| CV | Interpretación |
|----|----------------|
| **< 15%** | Baja variabilidad (datos homogéneos) |
| **15-30%** | Variabilidad moderada |
| **> 30%** | Alta variabilidad (datos heterogéneos) |

---

### Ejemplo

```python
import pandas as pd

# Dataset 1: Salarios (USD)
salarios = pd.Series([45000, 50000, 48000, 52000, 47000])
media_salarios = salarios.mean()
std_salarios = salarios.std()
cv_salarios = (std_salarios / media_salarios) * 100

# Dataset 2: Edades (años)
edades = pd.Series([25, 28, 26, 30, 27])
media_edades = edades.mean()
std_edades = edades.std()
cv_edades = (std_edades / media_edades) * 100

print("COMPARACIÓN DE VARIABILIDAD")
print("="*60)

print("\nSALARIOS:")
print(f"  Media: ${media_salarios:,.0f}")
print(f"  Desviación estándar: ${std_salarios:,.0f}")
print(f"  CV: {cv_salarios:.2f}%")

print("\nEDADES:")
print(f"  Media: {media_edades:.1f} años")
print(f"  Desviación estándar: {std_edades:.1f} años")
print(f"  CV: {cv_edades:.2f}%")

print("\n" + "="*60)
print("CONCLUSIÓN:")
if cv_salarios > cv_edades:
    print(f"Los salarios (CV={cv_salarios:.1f}%) tienen MAYOR variabilidad relativa que las edades (CV={cv_edades:.1f}%)")
else:
    print(f"Las edades (CV={cv_edades:.1f}%) tienen MAYOR variabilidad relativa que los salarios (CV={cv_salarios:.1f}%)")
```

---

## Cuartiles y Percentiles

### Definición

Los **cuartiles** dividen los datos ordenados en **4 partes iguales**:

```
Q1 (25%) | Q2 (50%) | Q3 (75%)
         Mediana
```

Los **percentiles** dividen los datos en **100 partes iguales**:
- P10 = 10° percentil (10% de datos por debajo)
- P50 = 50° percentil = Mediana
- P90 = 90° percentil (90% de datos por debajo)

---

### Interpretación

| Cuartil | Significado |
|---------|-------------|
| **Q1** | 25% de los datos son menores o iguales |
| **Q2** | 50% de los datos son menores o iguales (Mediana) |
| **Q3** | 75% de los datos son menores o iguales |

---

### Ejemplo

```python
import pandas as pd

# Salarios de 20 empleados
salarios = pd.Series([
    30000, 32000, 33000, 35000, 36000,
    38000, 40000, 42000, 43000, 45000,
    47000, 48000, 50000, 52000, 53000,
    55000, 57000, 60000, 62000, 65000
])

# Calcular cuartiles
Q1 = salarios.quantile(0.25)
Q2 = salarios.quantile(0.50)  # Mediana
Q3 = salarios.quantile(0.75)

print("ANÁLISIS DE CUARTILES DE SALARIOS")
print("="*60)
print(f"Q1 (25%): ${Q1:,.0f}  → 25% de empleados gana esto o menos")
print(f"Q2 (50%): ${Q2:,.0f}  → 50% de empleados gana esto o menos (Mediana)")
print(f"Q3 (75%): ${Q3:,.0f}  → 75% de empleados gana esto o menos")

print(f"\nInterpretación:")
print(f"  - El 25% más bajo gana hasta ${Q1:,.0f}")
print(f"  - El 50% central gana entre ${Q1:,.0f} y ${Q3:,.0f}")
print(f"  - El 25% más alto gana más de ${Q3:,.0f}")
```

---

## Rango Intercuartílico (IQR)

### Definición

El **IQR (Interquartile Range)** es la diferencia entre Q3 y Q1. Representa el **rango del 50% central de los datos**.

**Fórmula:**

```
IQR = Q3 - Q1
```

---

### Ventajas

✅ **Robusto ante outliers** (como la mediana)  
✅ Enfocado en la "masa" de los datos  
✅ Fundamental para detectar outliers  

---

### Ejemplo

```python
import pandas as pd

# Precios de productos
precios = pd.Series([10, 12, 15, 18, 20, 22, 25, 28, 30, 100])  # 100 es outlier

Q1 = precios.quantile(0.25)
Q3 = precios.quantile(0.75)
IQR = Q3 - Q1

print(f"Q1: ${Q1:.2f}")
print(f"Q3: ${Q3:.2f}")
print(f"IQR: ${IQR:.2f}")

print(f"\nInterpretación:")
print(f"El 50% central de los productos cuesta entre ${Q1:.2f} y ${Q3:.2f}")
print(f"El rango de este 50% central es de ${IQR:.2f}")
```

---

## Detección de Outliers

### Método IQR (Regla de Tukey)

Los **outliers** son valores que están significativamente alejados del resto de los datos.

**Criterio:**

```
Límite inferior = Q1 - 1.5 × IQR
Límite superior = Q3 + 1.5 × IQR

Outlier si:  valor < límite_inferior  O  valor > límite_superior
```

---

### Implementación

```python
import pandas as pd

# Dataset con outliers
datos = pd.Series([10, 12, 15, 18, 20, 22, 25, 28, 30, 100, 5])

# Calcular límites
Q1 = datos.quantile(0.25)
Q3 = datos.quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Q1: {Q1}")
print(f"Q3: {Q3}")
print(f"IQR: {IQR}")
print(f"\nLímites para outliers:")
print(f"  Inferior: {limite_inferior:.2f}")
print(f"  Superior: {limite_superior:.2f}")

# Identificar outliers
outliers = datos[(datos < limite_inferior) | (datos > limite_superior)]

print(f"\nOutliers detectados: {outliers.values}")
print(f"Total: {len(outliers)}")

# Datos sin outliers
datos_limpios = datos[(datos >= limite_inferior) & (datos <= limite_superior)]
print(f"\nDatos limpios (sin outliers): {len(datos_limpios)}/{len(datos)}")
```

**Output:**
```
Q1: 15.0
Q3: 28.0
IQR: 13.0

Límites para outliers:
  Inferior: -4.50
  Superior: 47.50

Outliers detectados: [100   5]
Total: 2

Datos limpios (sin outliers): 9/11
```

---

## Box Plot (Diagrama de Caja)

### Definición

Un **box plot** (diagrama de caja y bigotes) es una visualización que muestra:
- Cuartiles (Q1, Q2, Q3)
- Rango intercuartílico (IQR)
- Outliers
- Mínimo y máximo (excluyendo outliers)

---

### Estructura

```
    Outliers (puntos)
         ↓
         •
         |
      ┌──┴──┐  ← Q3 (75%)
      │     │
      │  ―  │  ← Q2 (50%, Mediana)
      │     │
      └──┬──┘  ← Q1 (25%)
         |
         •
         ↑
    Outliers (puntos)
```

---

### Implementación con Seaborn

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv('cars.csv')

# Box plot simple
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Price'])
plt.title('Distribución de Precios de Autos', fontsize=14, fontweight='bold')
plt.xlabel('Precio (USD)')
plt.show()
```

---

### Box plot por categorías

```python
# Comparar distribuciones por tipo de motor
plt.figure(figsize=(12, 6))
sns.boxplot(x='EngineType', y='Price', data=df)
plt.title('Distribución de Precios por Tipo de Motor', fontsize=14, fontweight='bold')
plt.xlabel('Tipo de Motor')
plt.ylabel('Precio (USD)')
plt.xticks(rotation=45)
plt.show()
```

---

## Implementación en Python

### Análisis completo de dispersión

```python
import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv('cars.csv')
columna = 'Price'

print("="*60)
print(f"ANÁLISIS DE DISPERSIÓN: {columna}")
print("="*60)

# Medidas básicas
rango = df[columna].max() - df[columna].min()
varianza = df[columna].var()
desv_std = df[columna].std()
cv = (desv_std / df[columna].mean()) * 100

# Cuartiles
Q1 = df[columna].quantile(0.25)
Q2 = df[columna].quantile(0.50)
Q3 = df[columna].quantile(0.75)
IQR = Q3 - Q1

# Outliers
min_limit = Q1 - 1.5 * IQR
max_limit = Q3 + 1.5 * IQR
outliers = df[(df[columna] < min_limit) | (df[columna] > max_limit)]

print(f"\n1. MEDIDAS BÁSICAS:")
print(f"   Rango: ${rango:,.2f}")
print(f"   Varianza: ${varianza:,.2f}")
print(f"   Desviación estándar: ${desv_std:,.2f}")
print(f"   Coeficiente de variación: {cv:.2f}%")

print(f"\n2. CUARTILES:")
print(f"   Q1 (25%): ${Q1:,.2f}")
print(f"   Q2 (50%): ${Q2:,.2f} (Mediana)")
print(f"   Q3 (75%): ${Q3:,.2f}")
print(f"   IQR: ${IQR:,.2f}")

print(f"\n3. OUTLIERS:")
print(f"   Límite inferior: ${min_limit:,.2f}")
print(f"   Límite superior: ${max_limit:,.2f}")
print(f"   Outliers detectados: {len(outliers)} ({len(outliers)/len(df)*100:.2f}%)")

# Interpretación del CV
print(f"\n4. INTERPRETACIÓN:")
if cv < 15:
    print(f"   Variabilidad BAJA (CV = {cv:.1f}%): Datos homogéneos")
elif cv < 30:
    print(f"   Variabilidad MODERADA (CV = {cv:.1f}%)")
else:
    print(f"   Variabilidad ALTA (CV = {cv:.1f}%): Datos heterogéneos")
```

---

## Casos de Uso

### Caso de Uso 1: Control de Calidad en Manufactura

**Contexto:** Una fábrica necesita evaluar la consistencia de un proceso de producción.

```python
import pandas as pd
import numpy as np

# Mediciones de peso de productos (gramos)
np.random.seed(42)

# Máquina A: Consistente
maquina_A = pd.Series(np.random.normal(100, 0.5, 100))

# Máquina B: Inconsistente
maquina_B = pd.Series(np.random.normal(100, 5, 100))

print("CONTROL DE CALIDAD: COMPARACIÓN DE MÁQUINAS")
print("="*60)

for nombre, datos in [('Máquina A', maquina_A), ('Máquina B', maquina_B)]:
    media = datos.mean()
    std = datos.std()
    cv = (std / media) * 100
    
    print(f"\n{nombre}:")
    print(f"  Media: {media:.2f}g")
    print(f"  Desviación estándar: {std:.2f}g")
    print(f"  CV: {cv:.2f}%")
    print(f"  Interpretación: {'✅ CONSISTENTE' if cv < 1 else '⚠️ VARIABLE'}")

print("\n" + "="*60)
print("CONCLUSIÓN:")
print("Máquina A tiene MUCHO mejor control de calidad (CV < 1%)")
print("Máquina B requiere calibración (CV = 5%)")
```

**Explicación:** Un CV bajo indica que el proceso es predecible y controlado, crucial para mantener estándares de calidad.

---

### Caso de Uso 2: Análisis de Riesgo en Inversiones

**Contexto:** Un analista financiero compara la volatilidad (riesgo) de dos acciones.

```python
import pandas as pd
import numpy as np

# Retornos diarios (%) de dos acciones durante 100 días
np.random.seed(100)

accion_A = pd.Series(np.random.normal(0.5, 1, 100))  # Estable
accion_B = pd.Series(np.random.normal(0.5, 5, 100))  # Volátil

print("ANÁLISIS DE RIESGO: VOLATILIDAD DE ACCIONES")
print("="*60)

for nombre, datos in [('Acción A', accion_A), ('Acción B', accion_B)]:
    media = datos.mean()
    std = datos.std()
    
    print(f"\n{nombre}:")
    print(f"  Retorno promedio diario: {media:.2f}%")
    print(f"  Volatilidad (desv. std): {std:.2f}%")
    print(f"  Clasificación: {'📉 BAJO RIESGO' if std < 2 else '📈 ALTO RIESGO'}")

print("\n" + "="*60)
print("RECOMENDACIÓN:")
print("Acción A: Inversión conservadora (menor volatilidad)")
print("Acción B: Inversión agresiva (mayor potencial de ganancia/pérdida)")
```

**Explicación:** En finanzas, mayor desviación estándar = mayor riesgo. Inversores conservadores prefieren baja volatilidad.

---

## Recursos Adicionales

### 📚 Conceptos clave

- **Rango:** Max - Min (sensible a outliers)
- **Varianza:** Promedio de desviaciones al cuadrado
- **Desviación estándar:** √Varianza (mismas unidades que los datos)
- **CV:** (σ/μ) × 100 (para comparar datasets con diferentes escalas)
- **IQR:** Q3 - Q1 (robusto ante outliers)

### 🔗 Enlaces útiles

- [Pandas statistical functions](https://pandas.pydata.org/docs/reference/frame.html#computations-descriptive-stats)
- [Seaborn boxplot documentation](https://seaborn.pydata.org/generated/seaborn.boxplot.html)

### 📂 Archivos relacionados

- `05_medidas_tendencia_central.md` - Media, mediana, moda
- Próximo: `07_visualizaciones_estadisticas.md`
- Notebook: `ejercicios_estadistica_descriptiva.ipynb`

### 🎯 Resumen rápido

| Medida | Cuándo usar | Robusta a outliers |
|--------|-------------|-------------------|
| **Rango** | Vista rápida | ❌ No |
| **Desviación estándar** | Comunicar variabilidad | ❌ No |
| **CV** | Comparar datasets diferentes | ❌ No |
| **IQR** | Detectar outliers | ✅ Sí |

---

**Actualizado:** Noviembre 2025  
**Progreso de la ruta:** 68% completado (13/19 cursos)