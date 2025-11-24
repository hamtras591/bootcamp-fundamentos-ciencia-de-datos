# Visualizaciones en Estadística Descriptiva

**Curso:** Matemáticas para Data Science: Estadística Descriptiva  
**Fecha:** Noviembre 2025  
**Módulo:** Estadística Descriptiva para Analítica  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [¿Por qué visualizar?](#por-qué-visualizar)
3. [Clasificación de Visualizaciones](#clasificación-de-visualizaciones)
4. [Histogramas](#histogramas)
5. [Diagramas de Caja (Box Plots)](#diagramas-de-caja-box-plots)
6. [Diagramas de Dispersión (Scatter Plots)](#diagramas-de-dispersión-scatter-plots)
7. [Diagramas de Pastel (Pie Charts)](#diagramas-de-pastel-pie-charts)
8. [Diagramas de Barras](#diagramas-de-barras)
9. [Joint Plots](#joint-plots)
10. [Otros Tipos de Visualizaciones](#otros-tipos-de-visualizaciones)
11. [Mejores Prácticas](#mejores-prácticas)
12. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

La **visualización de datos** es el proceso de representar información de manera gráfica para facilitar su comprensión e identificar patrones que no son evidentes en tablas numéricas.

### La frase clave:

> **"Una imagen vale más que mil palabras"**

En estadística descriptiva, esta frase adquiere un significado especial: un buen gráfico puede comunicar insights complejos de manera instantánea y universal.

---

## ¿Por qué visualizar?

### 1. Facilita la comprensión

```
❌ Tabla con 1000 números → Difícil de interpretar
✅ Histograma → Patrón visible inmediatamente
```

---

### 2. Revela patrones ocultos

Las visualizaciones permiten detectar:
- Tendencias
- Valores atípicos (outliers)
- Agrupaciones (clusters)
- Correlaciones
- Distribuciones

---

### 3. Comunica efectivamente

- **A ejecutivos:** Gráficos simples y claros
- **A técnicos:** Visualizaciones detalladas
- **Al público general:** Infografías comprensibles

---

### 4. Toma de decisiones

Un dashboard con visualizaciones permite tomar decisiones informadas en tiempo real.

---

## Clasificación de Visualizaciones

La estadística descriptiva se divide en **dos bloques complementarios**:

### 1. Bloque Analítico (Numérico)
- Medidas de tendencia central (media, mediana, moda)
- Medidas de dispersión (varianza, desviación estándar)
- Cuartiles y percentiles

### 2. Bloque Visual (Gráfico)
- Interpreta los datos numéricos a través de gráficos
- Hace los conceptos más comprensibles y atractivos
- Permite comparaciones rápidas

**Ambos bloques se complementan:** Los números dan precisión, los gráficos dan contexto.

---

## Tipos de Visualizaciones Según el Propósito

| Propósito | Visualización Recomendada |
|-----------|--------------------------|
| **Distribución de una variable** | Histograma, Box Plot |
| **Comparar categorías** | Diagrama de Barras, Box Plot |
| **Mostrar proporciones** | Diagrama de Pastel |
| **Relación entre dos variables** | Diagrama de Dispersión, Joint Plot |
| **Evolución temporal** | Gráfico de Líneas |
| **Flujos de información** | Diagrama Aluvial, Sankey |
| **Datos geográficos** | Mapas de Calor, Coropletas |

---

## Histogramas

### Definición

Un **histograma** muestra la distribución de frecuencias de una variable numérica continua, agrupando los datos en intervalos (bins).

---

### Cuándo usar

✅ **Usar para:**
- Ver la distribución de una variable numérica
- Identificar si los datos son simétricos o sesgados
- Detectar modas (picos)
- Estimar la normalidad de los datos

---

### Implementación en Python

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv('cars.csv')

# Histograma básico
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=30, kde=False, color='skyblue', edgecolor='black')
plt.title('Distribución de Precios de Autos', fontsize=14, fontweight='bold')
plt.xlabel('Precio (USD)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

### Histograma con KDE (Kernel Density Estimation)

```python
# Histograma con curva de densidad suavizada
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=30, kde=True, color='skyblue', edgecolor='black')
plt.title('Distribución de Precios con Curva de Densidad', fontsize=14, fontweight='bold')
plt.xlabel('Precio (USD)')
plt.ylabel('Frecuencia / Densidad')
plt.show()
```

---

### Interpretación

**Formas comunes de distribución:**

```
Simétrica (Normal):        Sesgada a la derecha:    Sesgada a la izquierda:
    ╱╲                          ╱╲                         ╱╲
   ╱  ╲                        ╱  ╲___                  ___╱  ╲
  ╱    ╲                      ╱       ╲                ╱       ╲
```

---

### Mejores prácticas

⚠️ **Evitar:**
- Demasiados bins → Gráfico ruidoso
- Muy pocos bins → Pérdida de información

✅ **Recomendación:** Probar diferentes números de bins (20-50 para datasets grandes)

---

## Diagramas de Caja (Box Plots)

### Definición

Un **box plot** muestra la distribución de datos basándose en cuartiles, revelando:
- Mediana (Q2)
- Rango intercuartílico (IQR = Q3 - Q1)
- Outliers
- Simetría de la distribución

---

### Cuándo usar

✅ **Usar para:**
- Comparar distribuciones entre grupos
- Identificar outliers visualmente
- Ver la dispersión y simetría de los datos
- Comparar múltiples variables/categorías

---

### Implementación básica

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Box plot simple
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Price'], color='lightblue')
plt.title('Distribución de Precios (Box Plot)', fontsize=14, fontweight='bold')
plt.xlabel('Precio (USD)')
plt.show()
```

---

### Box plot por categorías

```python
# Comparar precios por tipo de motor
plt.figure(figsize=(12, 6))
sns.boxplot(x='EngineType', y='Price', data=df, palette='Set2')
plt.title('Distribución de Precios por Tipo de Motor', fontsize=14, fontweight='bold')
plt.xlabel('Tipo de Motor')
plt.ylabel('Precio (USD)')
plt.xticks(rotation=45)
plt.show()
```

---

### Interpretación

```
        Outliers (•)
           |
      ┌────┴────┐  ← Q3 (75%)
      │         │
      │    ―    │  ← Q2 (Mediana, 50%)
      │         │
      └────┬────┘  ← Q1 (25%)
           |
        Outliers (•)
```

**Ventaja principal:** Comparación visual rápida de múltiples distribuciones.

---

## Diagramas de Dispersión (Scatter Plots)

### Definición

Un **diagrama de dispersión** muestra la relación entre **dos variables numéricas**, donde cada punto representa una observación.

---

### Cuándo usar

✅ **Usar para:**
- Analizar correlación entre dos variables
- Identificar patrones o tendencias
- Detectar outliers bivariados
- Visualizar agrupaciones (clusters)

---

### Implementación básica

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset iris (ejemplo clásico)
iris = sns.load_dataset("iris")

# Scatter plot básico
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='petal_length')
plt.title('Relación entre Longitud de Sépalo y Pétalo', fontsize=14, fontweight='bold')
plt.xlabel('Longitud de Sépalo (cm)')
plt.ylabel('Longitud de Pétalo (cm)')
plt.grid(alpha=0.3)
plt.show()
```

---

### Scatter plot con categorías (hue)

```python
# Agregar color por especie
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='petal_length', hue='species', 
                palette='Set1', s=100, alpha=0.7)
plt.title('Relación Sépalo-Pétalo por Especie', fontsize=14, fontweight='bold')
plt.xlabel('Longitud de Sépalo (cm)')
plt.ylabel('Longitud de Pétalo (cm)')
plt.legend(title='Especie')
plt.grid(alpha=0.3)
plt.show()
```

---

### Interpretación de patrones

**Correlación positiva:**
```
    •
  •   •
•   •   •
```
A mayor X, mayor Y

**Correlación negativa:**
```
•   •   •
  •   •
    •
```
A mayor X, menor Y

**Sin correlación:**
```
  •   •
•   •   •
  •   •
```
No hay patrón claro

---

## Joint Plots

### Definición

Un **joint plot** combina:
- Diagrama de dispersión (centro)
- Histogramas o KDE en los márgenes (distribuciones univariadas)

---

### Ventaja

Permite ver **simultáneamente**:
1. La relación entre dos variables (scatter)
2. La distribución de cada variable individual (histogramas)

---

### Implementación

```python
import seaborn as sns

# Joint plot básico
sns.jointplot(data=iris, x='sepal_length', y='petal_length', 
              kind='scatter', height=8)
plt.show()
```

---

### Variantes

```python
# Con KDE (densidad)
sns.jointplot(data=iris, x='sepal_length', y='petal_length', 
              kind='kde', height=8, cmap='Blues')
plt.show()

# Con hexbins (para muchos datos)
sns.jointplot(data=iris, x='sepal_length', y='petal_length', 
              kind='hex', height=8, cmap='Reds')
plt.show()

# Con regresión
sns.jointplot(data=iris, x='sepal_length', y='petal_length', 
              kind='reg', height=8)
plt.show()
```

---

### Con categorías

```python
# Separar por especie
sns.jointplot(data=iris, x='sepal_length', y='petal_length', 
              hue='species', height=8)
plt.show()
```

---

## Diagramas de Pastel (Pie Charts)

### Definición

Un **diagrama de pastel** muestra proporciones como segmentos de un círculo, donde cada segmento representa un porcentaje del total.

---

### Cuándo usar

✅ **Usar para:**
- Mostrar proporciones de un total (partes de un todo)
- Comparar pocas categorías (3-5 ideal, máximo 7)
- Datos categóricos con porcentajes

⚠️ **Evitar cuando:**
- Hay muchas categorías (>7)
- Necesitas comparaciones precisas (usa barras)
- Los porcentajes son similares

---

### Implementación

```python
import matplotlib.pyplot as plt

# Datos de ejemplo: Ventas por región
regiones = ['Norte', 'Sur', 'Este', 'Oeste']
ventas = [35, 25, 20, 20]

plt.figure(figsize=(8, 8))
plt.pie(ventas, labels=regiones, autopct='%1.1f%%', startangle=90,
        colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
plt.title('Distribución de Ventas por Región', fontsize=14, fontweight='bold')
plt.axis('equal')  # Para que sea circular
plt.show()
```

---

### Mejores prácticas

✅ **Hacer:**
- Usar colores distintos
- Mostrar porcentajes
- Ordenar de mayor a menor
- Resaltar el segmento más importante

❌ **Evitar:**
- Efectos 3D (distorsionan)
- Demasiados segmentos
- Colores muy similares

---

## Diagramas de Barras

### Definición

Un **diagrama de barras** compara valores de diferentes categorías mediante barras horizontales o verticales.

---

### Cuándo usar

✅ **Usar para:**
- Comparar cantidades entre categorías
- Mostrar rankings
- Visualizar frecuencias de datos categóricos

---

### Implementación

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Contar frecuencias de una variable categórica
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='EngineType', order=df['EngineType'].value_counts().index,
              palette='viridis')
plt.title('Frecuencia de Tipos de Motor', fontsize=14, fontweight='bold')
plt.xlabel('Tipo de Motor')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
```

---

### Barplot con promedios

```python
# Mostrar promedio de precio por tipo de motor
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='EngineType', y='Price', estimator='mean',
            palette='Set2', errorbar=('ci', 95))
plt.title('Precio Promedio por Tipo de Motor', fontsize=14, fontweight='bold')
plt.xlabel('Tipo de Motor')
plt.ylabel('Precio Promedio (USD)')
plt.xticks(rotation=45)
plt.show()
```

---

### Barras horizontales

```python
# Para muchas categorías, usar barras horizontales
top_10 = df['manufacturer_name'].value_counts().head(10)

plt.figure(figsize=(10, 8))
top_10.plot(kind='barh', color='coral')
plt.title('Top 10 Fabricantes de Autos', fontsize=14, fontweight='bold')
plt.xlabel('Cantidad de Autos')
plt.ylabel('Fabricante')
plt.gca().invert_yaxis()  # El mayor arriba
plt.show()
```

---

## Otros Tipos de Visualizaciones

### Diagramas Radiales (Radar Charts)

**Uso:** Comparar múltiples atributos de un elemento (ej. stats de videojuegos)

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo: Atributos de un personaje
categorias = ['Fuerza', 'Defensa', 'Velocidad', 'Inteligencia', 'Magia']
valores = [8, 6, 9, 7, 5]

# Configurar gráfico radar
angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
valores += valores[:1]  # Cerrar el círculo
angulos += angulos[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
ax.fill(angulos, valores, color='blue', alpha=0.25)
ax.plot(angulos, valores, color='blue', linewidth=2)
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(categorias)
ax.set_ylim(0, 10)
plt.title('Atributos del Personaje', fontsize=14, fontweight='bold', pad=20)
plt.show()
```

---

### Heatmaps (Mapas de Calor)

**Uso:** Visualizar matrices de correlación o tablas de frecuencias

```python
import seaborn as sns

# Matriz de correlación
plt.figure(figsize=(10, 8))
correlacion = df[['Price', 'Mileage', 'EngineVolume']].corr()
sns.heatmap(correlacion, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1)
plt.title('Matriz de Correlación', fontsize=14, fontweight='bold')
plt.show()
```

---

## Mejores Prácticas

### 1. Elige el gráfico correcto

| Pregunta | Gráfico |
|----------|---------|
| ¿Cómo se distribuyen mis datos? | Histograma, Box Plot |
| ¿Hay relación entre X e Y? | Scatter Plot, Joint Plot |
| ¿Qué categoría es más común? | Diagrama de Barras |
| ¿Cuál es la proporción de cada parte? | Diagrama de Pastel |

---

### 2. Simplifica

❌ **Evitar:**
- Sobrecarga de información
- Demasiados colores
- Efectos 3D innecesarios
- Fuentes difíciles de leer

✅ **Hacer:**
- Un mensaje claro por gráfico
- Paletas de colores coherentes
- Etiquetas legibles
- Títulos descriptivos

---

### 3. Contexto es clave

Siempre incluir:
- **Título** descriptivo
- **Etiquetas** en ejes
- **Unidades** (USD, kg, %)
- **Leyenda** si hay múltiples categorías

---

### 4. Audiencia

- **Ejecutivos:** Gráficos simples y claros (barras, pastel)
- **Técnicos:** Visualizaciones detalladas (box plots, scatter)
- **Público general:** Infografías atractivas

---

## Recursos Adicionales

### 🌐 Herramientas Online

- **[Data Viz Project](https://datavizproject.com/)** - Catálogo de visualizaciones
  - Filtrar por naturaleza (diagrama, geoespacial, tabla)
  - Clasificar por forma de datos
  - Explorar por estilo visual

---

### 📚 Librerías Python

- **Matplotlib:** Base de visualizaciones en Python
- **Seaborn:** Visualizaciones estadísticas elegantes
- **Plotly:** Gráficos interactivos
- **Altair:** Visualizaciones declarativas

---

### 🔗 Documentación

- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Python Graph Gallery](https://www.python-graph-gallery.com/)

---

### 📂 Archivos relacionados

- `05_medidas_tendencia_central.md`
- `06_medidas_dispersion.md`
- Notebook: `ejercicios_estadistica_descriptiva.ipynb`
- Dataset: `cars.csv`

---

### 🎯 Resumen rápido

| Visualización | Propósito | Variables |
|---------------|-----------|-----------|
| **Histograma** | Distribución | 1 numérica |
| **Box Plot** | Distribución + outliers | 1 numérica (+ 1 categórica opcional) |
| **Scatter Plot** | Correlación | 2 numéricas |
| **Bar Plot** | Comparar categorías | 1 categórica + 1 numérica |
| **Pie Chart** | Proporciones | 1 categórica |
| **Joint Plot** | Correlación + distribuciones | 2 numéricas |

---

**Actualizado:** Noviembre 2025  
**Progreso de la ruta:** 68% completado (13/19 cursos)