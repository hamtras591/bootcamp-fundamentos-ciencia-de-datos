# ¿Qué es la Estadística Descriptiva?

**Curso:** Matemáticas para Data Science: Estadística Descriptiva  
**Fecha:** Noviembre 2025  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [Diferencia entre Estadística Descriptiva e Inferencial](#diferencia-entre-estadística-descriptiva-e-inferencial)
3. [Aplicaciones Prácticas](#aplicaciones-prácticas)
4. [Ventajas y Limitaciones](#ventajas-y-limitaciones)
5. [Sintaxis en Python](#sintaxis-en-python)
6. [Ejemplos Básicos](#ejemplos-básicos)
7. [Casos de Uso en Data Science](#casos-de-uso-en-data-science)
8. [Ejercicios Prácticos](#ejercicios-prácticos)
9. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

La **estadística descriptiva** es una rama de la estadística que se encarga de **resumir, organizar y presentar datos** de manera que sean fáciles de entender. Su objetivo principal es describir las características principales de un conjunto de datos mediante:

- **Medidas numéricas** (media, mediana, desviación estándar)
- **Representaciones visuales** (gráficos, tablas)
- **Resúmenes concisos** de grandes volúmenes de información

**En esencia:** La estadística descriptiva responde "¿Qué pasó?" o "¿Qué está pasando?" con los datos que tenemos.

---

## Diferencia entre Estadística Descriptiva e Inferencial

| Aspecto | Estadística Descriptiva | Estadística Inferencial |
|---------|------------------------|------------------------|
| **Objetivo** | Resumir y organizar datos | Predecir y hacer inferencias |
| **Enfoque temporal** | Presente (aquí y ahora) | Futuro (predicciones) |
| **Herramientas** | Tablas, gráficos, métricas simples | Modelos predictivos, pruebas de hipótesis |
| **Pregunta clave** | "¿Qué muestran los datos?" | "¿Qué podemos predecir?" |
| **Ejemplo** | "El equipo anotó 50 goles esta temporada" | "¿Cuántos goles anotará la próxima temporada?" |

---

## Aplicaciones Prácticas

### 🏃 En Deportes
- **Rendimiento de jugadores:** Goles, asistencias, minutos jugados
- **Comparación entre equipos:** Posesión de balón, tiros a puerta
- **Eficiencia:** Goles por partido, pases exitosos

### 💼 En Negocios
- **Ventas:** Ingresos totales, productos más vendidos
- **Marketing:** Tasa de conversión, engagement en redes sociales
- **Recursos Humanos:** Rotación de personal, salarios promedio

### 🌍 En Contextos Sociales
- **Economía:** PIB, índice de desempleo
- **Desigualdad:** Índice de GINI
- **Salud pública:** Tasas de mortalidad, esperanza de vida

---

## Ventajas y Limitaciones

### ✅ Ventajas

1. **Simplifica grandes volúmenes de datos**
   - Convierte millones de registros en métricas comprensibles
   - Facilita la toma de decisiones rápidas

2. **Facilita comparaciones**
   - Permite comparar diferentes grupos o períodos de tiempo
   - Usa métricas estandarizadas (promedios, porcentajes)

3. **Comunicación efectiva**
   - Los gráficos y tablas son universalmente comprensibles
   - Reduce la complejidad técnica

4. **Relevancia social**
   - Ayuda a entender fenómenos económicos, políticos y sociales
   - Base para decisiones de política pública

### ⚠️ Limitaciones

1. **Subjetividad en las métricas**
   - Las definiciones pueden variar según el contexto
   - Ejemplo: ¿Qué hace a un "buen" jugador? (¿Goles? ¿Asistencias? ¿Defensa?)

2. **Potencial de manipulación**
   - Se puede presentar solo un lado de los datos
   - Los gráficos pueden ser engañosos (ejes truncados, escalas manipuladas)

3. **Pérdida de información**
   - Resumir implica perder detalles
   - Un promedio no muestra la distribución completa

4. **No hace predicciones**
   - Solo describe el pasado/presente
   - No explica relaciones causales

---

## Sintaxis en Python

Python ofrece librerías poderosas para estadística descriptiva:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Funciones básicas de pandas para estadística descriptiva

```python
# Crear un DataFrame de ejemplo
data = {
    'jugador': ['Messi', 'Ronaldo', 'Neymar', 'Mbappé', 'Haaland'],
    'goles': [25, 30, 18, 28, 35],
    'asistencias': [12, 8, 15, 10, 6],
    'minutos_jugados': [2800, 3000, 2400, 2900, 3100]
}

df = pd.DataFrame(data)
```

```python
# Resumen estadístico completo
df.describe()
```

```python
# Medidas individuales
promedio_goles = df['goles'].mean()
mediana_goles = df['goles'].median()
desviacion_goles = df['goles'].std()

print(f"Promedio de goles: {promedio_goles}")
print(f"Mediana de goles: {mediana_goles}")
print(f"Desviación estándar: {desviacion_goles}")
```

---

## Ejemplos Básicos

### Ejemplo 1: Análisis de ventas mensuales

```python
import pandas as pd
import numpy as np

# Datos de ventas mensuales (en miles de dólares)
ventas = pd.Series([120, 135, 128, 142, 150, 138, 145, 155, 148, 160, 170, 165])
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

df_ventas = pd.DataFrame({'Mes': meses, 'Ventas': ventas})
```

```python
# Estadísticas descriptivas
print("=== ESTADÍSTICAS DE VENTAS ANUALES ===")
print(f"Venta promedio mensual: ${ventas.mean():.2f}k")
print(f"Venta mediana: ${ventas.median():.2f}k")
print(f"Venta máxima: ${ventas.max():.2f}k")
print(f"Venta mínima: ${ventas.min():.2f}k")
print(f"Desviación estándar: ${ventas.std():.2f}k")
print(f"Rango: ${ventas.max() - ventas.min():.2f}k")
```

### Ejemplo 2: Comparación de rendimiento de estudiantes

```python
import pandas as pd

# Calificaciones de dos grupos
grupo_a = pd.Series([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
grupo_b = pd.Series([72, 68, 75, 80, 70, 73, 78, 76, 74, 79])

# Crear DataFrame comparativo
comparacion = pd.DataFrame({
    'Grupo A': [grupo_a.mean(), grupo_a.median(), grupo_a.std()],
    'Grupo B': [grupo_b.mean(), grupo_b.median(), grupo_b.std()]
}, index=['Promedio', 'Mediana', 'Desviación Estándar'])

print(comparacion.round(2))
```

---

## Casos de Uso en Data Science

### Caso de Uso 1: Análisis de Comportamiento de Usuarios en E-commerce

**Contexto:** Una tienda online quiere entender el comportamiento de compra de sus clientes durante el último trimestre para optimizar su inventario.

**Datos disponibles:**
- Número de transacciones por cliente
- Valor promedio de compra
- Productos más vendidos
- Tiempo de navegación antes de compra

**Solución:**

```python
import pandas as pd
import numpy as np

# Simular datos de 1000 clientes
np.random.seed(42)

clientes_data = {
    'cliente_id': range(1, 1001),
    'num_transacciones': np.random.poisson(3, 1000),
    'valor_promedio_compra': np.random.normal(75, 25, 1000),
    'tiempo_navegacion_min': np.random.gamma(2, 15, 1000)
}

df_clientes = pd.DataFrame(clientes_data)

# Asegurar valores positivos
df_clientes['valor_promedio_compra'] = df_clientes['valor_promedio_compra'].clip(lower=10)
```

```python
# Análisis estadístico descriptivo
print("=== ANÁLISIS DE COMPORTAMIENTO DE CLIENTES ===\n")

print("1. TRANSACCIONES:")
print(f"   - Promedio de transacciones por cliente: {df_clientes['num_transacciones'].mean():.2f}")
print(f"   - Mediana de transacciones: {df_clientes['num_transacciones'].median():.0f}")
print(f"   - Cliente más activo: {df_clientes['num_transacciones'].max()} transacciones\n")

print("2. VALOR DE COMPRA:")
print(f"   - Ticket promedio: ${df_clientes['valor_promedio_compra'].mean():.2f}")
print(f"   - Desviación estándar: ${df_clientes['valor_promedio_compra'].std():.2f}")
print(f"   - Rango de valores: ${df_clientes['valor_promedio_compra'].min():.2f} - ${df_clientes['valor_promedio_compra'].max():.2f}\n")

print("3. TIEMPO DE NAVEGACIÓN:")
print(f"   - Promedio: {df_clientes['tiempo_navegacion_min'].mean():.2f} minutos")
print(f"   - El 25% de usuarios navega menos de: {df_clientes['tiempo_navegacion_min'].quantile(0.25):.2f} min")
print(f"   - El 75% de usuarios navega menos de: {df_clientes['tiempo_navegacion_min'].quantile(0.75):.2f} min")
```

```python
# Segmentación básica por valor de compra
df_clientes['segmento'] = pd.cut(
    df_clientes['valor_promedio_compra'],
    bins=[0, 50, 100, float('inf')],
    labels=['Bajo', 'Medio', 'Alto']
)

print("\n4. SEGMENTACIÓN POR VALOR:")
print(df_clientes['segmento'].value_counts())
```

**Explicación:** Este análisis permite al negocio identificar patrones de comportamiento, segmentar clientes y tomar decisiones sobre inventario y estrategias de marketing. La estadística descriptiva resume miles de interacciones en métricas accionables.

---

### Caso de Uso 2: Análisis de Rendimiento de Campaña de Marketing

**Contexto:** Una empresa lanzó una campaña publicitaria en diferentes canales (Email, Redes Sociales, Google Ads) y necesita evaluar el rendimiento de cada uno para asignar presupuesto futuro.

**Datos disponibles:**
- Impresiones por canal
- Clicks por canal
- Conversiones (ventas) por canal
- Costo por canal

**Solución:**

```python
import pandas as pd

# Datos de la campaña
campana_data = {
    'Canal': ['Email', 'Facebook', 'Instagram', 'Google Ads', 'Twitter'],
    'Impresiones': [50000, 120000, 95000, 80000, 45000],
    'Clicks': [2500, 4800, 3800, 5600, 1350],
    'Conversiones': [125, 192, 152, 280, 54],
    'Costo_USD': [500, 2400, 1900, 4000, 900]
}

df_campana = pd.DataFrame(campana_data)
```

```python
# Calcular métricas derivadas
df_campana['CTR_%'] = (df_campana['Clicks'] / df_campana['Impresiones'] * 100).round(2)
df_campana['Conversion_Rate_%'] = (df_campana['Conversiones'] / df_campana['Clicks'] * 100).round(2)
df_campana['Costo_por_Conversion'] = (df_campana['Costo_USD'] / df_campana['Conversiones']).round(2)
df_campana['ROAS'] = (df_campana['Conversiones'] * 50 / df_campana['Costo_USD']).round(2)  # Asumiendo $50 por venta

print("=== ANÁLISIS DE CAMPAÑA DE MARKETING ===\n")
print(df_campana)
```

```python
# Análisis estadístico por métrica
print("\n=== RESUMEN ESTADÍSTICO ===\n")

print("CTR (Click-Through Rate):")
print(f"  - Promedio: {df_campana['CTR_%'].mean():.2f}%")
print(f"  - Mejor canal: {df_campana.loc[df_campana['CTR_%'].idxmax(), 'Canal']} ({df_campana['CTR_%'].max():.2f}%)")
print(f"  - Peor canal: {df_campana.loc[df_campana['CTR_%'].idxmin(), 'Canal']} ({df_campana['CTR_%'].min():.2f}%)\n")

print("Tasa de Conversión:")
print(f"  - Promedio: {df_campana['Conversion_Rate_%'].mean():.2f}%")
print(f"  - Mejor canal: {df_campana.loc[df_campana['Conversion_Rate_%'].idxmax(), 'Canal']} ({df_campana['Conversion_Rate_%'].max():.2f}%)\n")

print("Costo por Conversión:")
print(f"  - Promedio: ${df_campana['Costo_por_Conversion'].mean():.2f}")
print(f"  - Más eficiente: {df_campana.loc[df_campana['Costo_por_Conversion'].idxmin(), 'Canal']} (${df_campana['Costo_por_Conversion'].min():.2f})\n")

print("ROAS (Return on Ad Spend):")
print(f"  - Promedio: {df_campana['ROAS'].mean():.2f}x")
print(f"  - Mejor ROI: {df_campana.loc[df_campana['ROAS'].idxmax(), 'Canal']} ({df_campana['ROAS'].max():.2f}x)")
```

**Explicación:** Este análisis permite comparar el rendimiento de diferentes canales usando estadística descriptiva. Las métricas calculadas (CTR, tasa de conversión, costo por conversión, ROAS) son ejemplos perfectos de cómo la estadística descriptiva transforma datos crudos en insights accionables para la toma de decisiones de negocio.

---

## Ejercicios Prácticos

### Ejercicio 1: [Nivel Básico] - Análisis de Calificaciones

**Enunciado:** 

Tienes las calificaciones de 10 estudiantes en un examen de matemáticas:
`[78, 85, 92, 88, 76, 95, 82, 89, 91, 84]`

Calcula:
1. La calificación promedio
2. La calificación mediana
3. La calificación máxima y mínima
4. El rango de las calificaciones

**Pistas:**
- Usa una `pd.Series` para almacenar las calificaciones
- Los métodos `.mean()`, `.median()`, `.max()`, `.min()` son tus amigos
- El rango es la diferencia entre el máximo y el mínimo

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd

# Datos
calificaciones = pd.Series([78, 85, 92, 88, 76, 95, 82, 89, 91, 84])

# Cálculos
promedio = calificaciones.mean()
mediana = calificaciones.median()
maxima = calificaciones.max()
minima = calificaciones.min()
rango = maxima - minima

# Resultados
print("=== ANÁLISIS DE CALIFICACIONES ===")
print(f"Promedio: {promedio:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Calificación máxima: {maxima}")
print(f"Calificación mínima: {minima}")
print(f"Rango: {rango}")
```

**Explicación paso a paso:**

1. **Creamos una Series de pandas** con las calificaciones para facilitar los cálculos estadísticos
2. **Calculamos el promedio** usando `.mean()` - suma todas las calificaciones y divide por 10
3. **Calculamos la mediana** usando `.median()` - el valor central cuando ordenamos los datos
4. **Identificamos máximo y mínimo** para conocer el rango del rendimiento
5. **Calculamos el rango** (diferencia max-min) para medir la dispersión de los datos

**Interpretación:** Un promedio de ~86 indica buen rendimiento general. El rango de 19 puntos muestra una variabilidad moderada entre estudiantes.

</details>

---

### Ejercicio 2: [Nivel Básico-Intermedio] - Comparación de Ventas Trimestrales

**Enunciado:**

Una empresa tiene las siguientes ventas mensuales (en miles de USD) para dos productos durante un trimestre:

- **Producto A:** [45, 52, 48]
- **Producto B:** [38, 41, 39]

Calcula para cada producto:
1. Ventas totales del trimestre
2. Venta promedio mensual
3. ¿Qué producto tiene mayor variabilidad en sus ventas? (usa desviación estándar)
4. Crea un DataFrame comparativo con estas métricas

**Pistas:**
- Usa `.sum()` para el total
- La desviación estándar se calcula con `.std()`
- Un DataFrame con productos como columnas facilitará la comparación

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd

# Datos
producto_a = pd.Series([45, 52, 48], name='Producto A')
producto_b = pd.Series([38, 41, 39], name='Producto B')

# Cálculos
comparacion = pd.DataFrame({
    'Producto A': [
        producto_a.sum(),
        producto_a.mean(),
        producto_a.std()
    ],
    'Producto B': [
        producto_b.sum(),
        producto_b.mean(),
        producto_b.std()
    ]
}, index=['Ventas Totales', 'Promedio Mensual', 'Desviación Estándar'])

print("=== COMPARACIÓN DE VENTAS TRIMESTRALES ===")
print(comparacion.round(2))

# Análisis de variabilidad
print("\n=== ANÁLISIS DE VARIABILIDAD ===")
if producto_a.std() > producto_b.std():
    print(f"Producto A tiene mayor variabilidad (σ = {producto_a.std():.2f})")
else:
    print(f"Producto B tiene mayor variabilidad (σ = {producto_b.std():.2f})")
```

**Explicación paso a paso:**

1. **Creamos dos Series** con las ventas mensuales de cada producto
2. **Calculamos métricas clave:**
   - `.sum()`: Ventas totales del trimestre
   - `.mean()`: Promedio mensual (indica rendimiento típico)
   - `.std()`: Desviación estándar (mide consistencia en las ventas)
3. **Organizamos en DataFrame** para comparación visual clara
4. **Interpretamos la variabilidad:** Mayor desviación estándar = ventas menos predecibles

**Interpretación:** Producto A tiene mayores ventas totales (145k vs 118k) y mayor promedio mensual (48.33k vs 39.33k). Producto A también tiene mayor variabilidad (σ ≈ 3.51), lo que significa que sus ventas son menos consistentes mes a mes.

</details>

---

### Ejercicio 3: [Nivel Intermedio] - Análisis de Tiempos de Respuesta

**Enunciado:**

Un equipo de soporte técnico registró los tiempos de respuesta (en minutos) de 15 tickets durante una semana:

`[12, 8, 15, 45, 9, 11, 10, 120, 13, 14, 9, 16, 11, 10, 12]`

1. Calcula la media, mediana y desviación estándar
2. Identifica si hay valores atípicos (outliers)
3. ¿Cuál métrica es más representativa del desempeño típico del equipo: media o mediana? ¿Por qué?
4. Calcula los cuartiles (Q1, Q2, Q3) y el rango intercuartílico (IQR)

**Pistas:**
- Un outlier es un valor muy alejado del resto
- Cuando hay outliers, la mediana es más robusta que la media
- Los cuartiles se calculan con `.quantile([0.25, 0.5, 0.75])`
- IQR = Q3 - Q1

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd
import numpy as np

# Datos
tiempos = pd.Series([12, 8, 15, 45, 9, 11, 10, 120, 13, 14, 9, 16, 11, 10, 12])

# Estadísticas básicas
media = tiempos.mean()
mediana = tiempos.median()
desv_std = tiempos.std()

print("=== ANÁLISIS DE TIEMPOS DE RESPUESTA ===\n")
print(f"Media: {media:.2f} minutos")
print(f"Mediana: {mediana:.2f} minutos")
print(f"Desviación estándar: {desv_std:.2f} minutos")

# Cuartiles e IQR
Q1 = tiempos.quantile(0.25)
Q2 = tiempos.quantile(0.50)  # Equivalente a la mediana
Q3 = tiempos.quantile(0.75)
IQR = Q3 - Q1

print(f"\nCuartiles:")
print(f"  Q1 (25%): {Q1:.2f} min")
print(f"  Q2 (50%): {Q2:.2f} min (Mediana)")
print(f"  Q3 (75%): {Q3:.2f} min")
print(f"  IQR: {IQR:.2f} min")

# Detección de outliers usando regla IQR
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = tiempos[(tiempos < limite_inferior) | (tiempos > limite_superior)]

print(f"\n=== DETECCIÓN DE OUTLIERS ===")
print(f"Límite inferior: {limite_inferior:.2f} min")
print(f"Límite superior: {limite_superior:.2f} min")
print(f"Outliers detectados: {outliers.values}")

# Análisis comparativo
print(f"\n=== ANÁLISIS ===")
print(f"La diferencia entre media ({media:.2f}) y mediana ({mediana:.2f}) es de {abs(media - mediana):.2f} minutos.")
print(f"\nConclusión: La MEDIANA es más representativa del desempeño típico porque:")
print(f"  1. No se ve afectada por los valores extremos ({outliers.values})")
print(f"  2. El 50% de los tickets se resuelven en {mediana:.0f} minutos o menos")
print(f"  3. La media está inflada por los outliers (45 y 120 minutos)")
```

**Explicación paso a paso:**

1. **Calculamos estadísticas básicas** para tener una visión general
2. **Identificamos cuartiles:**
   - Q1: El 25% de tickets se resuelve en este tiempo o menos
   - Q2: Mediana (50% de los datos)
   - Q3: El 75% de tickets se resuelve en este tiempo o menos
3. **Calculamos IQR (Q3-Q1):** Mide la dispersión de la mitad central de los datos
4. **Detectamos outliers** usando la regla: 
   - Outlier si < Q1 - 1.5×IQR o > Q3 + 1.5×IQR
5. **Comparamos media vs mediana:** La presencia de outliers (45 y 120 min) infla la media, haciendo que la mediana sea más representativa

**Interpretación:** El equipo típicamente responde en ~11-12 minutos, pero casos excepcionales (45 y 120 min) elevan la media a ~19 minutos. La mediana (12 min) es más representativa del desempeño real.

</details>

---

### Ejercicio 4: [Nivel Intermedio-Avanzado] - Dashboard de Métricas de Negocio

**Enunciado:**

Eres analista de datos en una empresa de SaaS. Tienes datos de 50 clientes del último mes:

```python
np.random.seed(42)
datos_clientes = {
    'ingresos_mensuales': np.random.normal(5000, 1500, 50),
    'usuarios_activos': np.random.poisson(25, 50),
    'tasa_retencion': np.random.uniform(70, 98, 50),
    'tickets_soporte': np.random.poisson(8, 50)
}
```

Crea un dashboard estadístico completo que incluya:

1. Resumen estadístico de todas las variables (`.describe()`)
2. Identificación del "cliente promedio" (media de cada métrica)
3. Segmentación de clientes por ingresos: Bajo (<$3500), Medio ($3500-$6500), Alto (>$6500)
4. Análisis de correlación: ¿Los clientes con más usuarios activos generan más ingresos?
5. Distribución por percentiles (10%, 25%, 50%, 75%, 90%)

**Pistas:**
- Usa `pd.cut()` para crear segmentos
- `.corr()` calcula correlaciones entre variables
- `.quantile([0.10, 0.25, 0.50, 0.75, 0.90])` para percentiles

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd
import numpy as np

# Generar datos
np.random.seed(42)
datos_clientes = {
    'ingresos_mensuales': np.random.normal(5000, 1500, 50),
    'usuarios_activos': np.random.poisson(25, 50),
    'tasa_retencion': np.random.uniform(70, 98, 50),
    'tickets_soporte': np.random.poisson(8, 50)
}

df = pd.DataFrame(datos_clientes)

# Asegurar valores positivos en ingresos
df['ingresos_mensuales'] = df['ingresos_mensuales'].clip(lower=1000)

print("="*60)
print("DASHBOARD DE MÉTRICAS DE CLIENTES SaaS")
print("="*60)

# 1. Resumen estadístico completo
print("\n1. RESUMEN ESTADÍSTICO GENERAL")
print("-"*60)
print(df.describe().round(2))

# 2. Perfil del cliente promedio
print("\n2. PERFIL DEL CLIENTE PROMEDIO")
print("-"*60)
print(f"Ingresos mensuales: ${df['ingresos_mensuales'].mean():.2f}")
print(f"Usuarios activos: {df['usuarios_activos'].mean():.1f}")
print(f"Tasa de retención: {df['tasa_retencion'].mean():.2f}%")
print(f"Tickets de soporte: {df['tickets_soporte'].mean():.1f}")

# 3. Segmentación por ingresos
df['segmento'] = pd.cut(
    df['ingresos_mensuales'],
    bins=[0, 3500, 6500, float('inf')],
    labels=['Bajo', 'Medio', 'Alto']
)

print("\n3. SEGMENTACIÓN POR INGRESOS")
print("-"*60)
segmentacion = df.groupby('segmento').agg({
    'ingresos_mensuales': ['count', 'mean'],
    'usuarios_activos': 'mean',
    'tasa_retencion': 'mean',
    'tickets_soporte': 'mean'
}).round(2)
print(segmentacion)

# 4. Análisis de correlación
print("\n4. MATRIZ DE CORRELACIÓN")
print("-"*60)
correlaciones = df[['ingresos_mensuales', 'usuarios_activos', 'tasa_retencion', 'tickets_soporte']].corr()
print(correlaciones.round(3))

print("\n   Interpretación:")
corr_ingresos_usuarios = df['ingresos_mensuales'].corr(df['usuarios_activos'])
if abs(corr_ingresos_usuarios) > 0.7:
    relacion = "fuerte"
elif abs(corr_ingresos_usuarios) > 0.4:
    relacion = "moderada"
else:
    relacion = "débil"
print(f"   - Correlación ingresos-usuarios activos: {corr_ingresos_usuarios:.3f} ({relacion})")

# 5. Distribución por percentiles
print("\n5. DISTRIBUCIÓN POR PERCENTILES")
print("-"*60)
percentiles = df[['ingresos_mensuales', 'usuarios_activos']].quantile([0.10, 0.25, 0.50, 0.75, 0.90])
percentiles.index = ['P10', 'P25', 'P50 (Mediana)', 'P75', 'P90']
print(percentiles.round(2))

print("\n   Interpretación:")
print(f"   - El 10% de clientes genera menos de ${percentiles.loc['P10', 'ingresos_mensuales']:.2f}")
print(f"   - El 50% de clientes genera menos de ${percentiles.loc['P50 (Mediana)', 'ingresos_mensuales']:.2f}")
print(f"   - El 90% de clientes genera menos de ${percentiles.loc['P90', 'ingresos_mensuales']:.2f}")

# Insights adicionales
print("\n6. INSIGHTS CLAVE")
print("-"*60)
print(f"✓ Clientes en segmento Alto: {(df['segmento'] == 'Alto').sum()} ({(df['segmento'] == 'Alto').sum()/len(df)*100:.1f}%)")
print(f"✓ Rango de ingresos: ${df['ingresos_mensuales'].min():.2f} - ${df['ingresos_mensuales'].max():.2f}")
print(f"✓ Desviación estándar de ingresos: ${df['ingresos_mensuales'].std():.2f} (variabilidad)")
print(f"✓ Cliente con más usuarios activos: {df['usuarios_activos'].max()} usuarios")
```

**Explicación paso a paso:**

1. **Resumen estadístico (`.describe()`):**
   - Count, mean, std, min, cuartiles, max de todas las variables
   - Visión panorámica de la distribución de datos

2. **Perfil del cliente promedio:**
   - Calcula medias de todas las métricas
   - Representa al "cliente típico" de la empresa

3. **Segmentación:**
   - Divide clientes en grupos basados en ingresos
   - Usa `.groupby()` para calcular estadísticas por segmento
   - Permite estrategias diferenciadas por segmento

4. **Correlación:**
   - Mide relación lineal entre variables (-1 a 1)
   - |r| > 0.7: correlación fuerte
   - |r| 0.4-0.7: correlación moderada
   - |r| < 0.4: correlación débil

5. **Percentiles:**
   - Dividen los datos en proporciones
   - P50 = mediana (50% de clientes por debajo)
   - Útil para identificar outliers y distribución

**Interpretación:** Este dashboard proporciona una visión 360° de la base de clientes usando solo estadística descriptiva. Permite identificar patrones, segmentar clientes y tomar decisiones basadas en datos.

</details>

---

### Ejercicio 5: [Nivel Desafío] - Análisis Comparativo Multidimensional

**Enunciado:**

Eres el data analyst de una cadena de restaurantes con 4 sucursales. Tienes datos de ventas diarias durante una semana (7 días) para cada sucursal:

```python
np.random.seed(100)
sucursal_norte = np.random.normal(8500, 1200, 7)
sucursal_sur = np.random.normal(7200, 1800, 7)
sucursal_este = np.random.normal(9100, 900, 7)
sucursal_oeste = np.random.normal(6800, 2100, 7)
```

**Tu misión:** Crear un informe ejecutivo completo que responda:

1. ¿Cuál sucursal tiene el mejor desempeño promedio?
2. ¿Cuál sucursal es la más consistente (menor variabilidad)?
3. ¿Qué sucursal tiene el día de mayores ventas?
4. Calcula el coeficiente de variación (CV = std/mean × 100) para cada sucursal
5. Crea una tabla comparativa con todas las métricas
6. **Desafío adicional:** Si cada sucursal tiene costos operativos de $6000/día, ¿cuál es la más rentable?

**Pistas:**
- El CV permite comparar variabilidad entre sucursales con diferentes medias
- La rentabilidad es: (Ventas promedio - Costos) × 7 días
- Usa `.clip(lower=0)` para evitar ventas negativas
- Un CV < 15% indica baja variabilidad; > 30% indica alta variabilidad

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd
import numpy as np

# Generar datos
np.random.seed(100)
datos_semana = {
    'Norte': np.random.normal(8500, 1200, 7).clip(lower=0),
    'Sur': np.random.normal(7200, 1800, 7).clip(lower=0),
    'Este': np.random.normal(9100, 900, 7).clip(lower=0),
    'Oeste': np.random.normal(6800, 2100, 7).clip(lower=0)
}

df_ventas = pd.DataFrame(datos_semana)
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
df_ventas.index = dias

print("="*70)
print("INFORME EJECUTIVO: ANÁLISIS COMPARATIVO DE SUCURSALES")
print("="*70)

# Mostrar datos crudos
print("\n1. VENTAS DIARIAS POR SUCURSAL (USD)")
print("-"*70)
print(df_ventas.round(0))

# 2. Análisis estadístico por sucursal
print("\n2. ESTADÍSTICAS DESCRIPTIVAS")
print("-"*70)

estadisticas = pd.DataFrame({
    'Promedio': df_ventas.mean(),
    'Mediana': df_ventas.median(),
    'Desv. Std': df_ventas.std(),
    'Min': df_ventas.min(),
    'Max': df_ventas.max(),
    'Rango': df_ventas.max() - df_ventas.min()
})

print(estadisticas.round(2))

# 3. Mejor desempeño promedio
mejor_promedio = df_ventas.mean().idxmax()
valor_mejor = df_ventas.mean().max()
print(f"\n3. MEJOR DESEMPEÑO PROMEDIO")
print("-"*70)
print(f"🏆 Sucursal {mejor_promedio}: ${valor_mejor:,.2f}/día")

# 4. Sucursal más consistente (menor variabilidad)
mas_consistente = df_ventas.std().idxmin()
std_consistente = df_ventas.std().min()
print(f"\n4. SUCURSAL MÁS CONSISTENTE")
print("-"*70)
print(f"🎯 Sucursal {mas_consistente}: σ = ${std_consistente:,.2f}")
print(f"   (Menor variación día a día)")

# 5. Día de mayores ventas por sucursal
print(f"\n5. DÍA DE MAYORES VENTAS POR SUCURSAL")
print("-"*70)
for sucursal in df_ventas.columns:
    dia_max = df_ventas[sucursal].idxmax()
    venta_max = df_ventas[sucursal].max()
    print(f"   {sucursal:6s}: {dia_max:10s} - ${venta_max:,.2f}")

# 6. Coeficiente de Variación (CV)
print(f"\n6. COEFICIENTE DE VARIACIÓN (CV %)")
print("-"*70)
cv = (df_ventas.std() / df_ventas.mean() * 100).round(2)
cv_df = pd.DataFrame({
    'CV (%)': cv,
    'Interpretación': cv.apply(lambda x: 'Baja variabilidad' if x < 15 
                                else 'Variabilidad moderada' if x < 30 
                                else 'Alta variabilidad')
})
print(cv_df)

print("\n   Nota: CV bajo = ventas más predecibles")

# 7. Análisis de rentabilidad
COSTO_OPERATIVO_DIA = 6000
print(f"\n7. ANÁLISIS DE RENTABILIDAD (Costo operativo: ${COSTO_OPERATIVO_DIA:,}/día)")
print("-"*70)

rentabilidad = pd.DataFrame({
    'Ventas Totales Semana': df_ventas.sum(),
    'Costos Totales Semana': COSTO_OPERATIVO_DIA * 7,
    'Utilidad Neta Semana': df_ventas.sum() - (COSTO_OPERATIVO_DIA * 7),
    'Margen Utilidad %': ((df_ventas.sum() - (COSTO_OPERATIVO_DIA * 7)) / df_ventas.sum() * 100)
})

print(rentabilidad.round(2))

mas_rentable = rentabilidad['Utilidad Neta Semana'].idxmax()
utilidad_max = rentabilidad['Utilidad Neta Semana'].max()
print(f"\n🏆 SUCURSAL MÁS RENTABLE: {mas_rentable} (${utilidad_max:,.2f} de utilidad semanal)")

# 8. Ranking final
print(f"\n8. RANKING GENERAL (PONDERADO)")
print("-"*70)

# Normalizar métricas (0-100)
ranking = pd.DataFrame({
    'Ventas Promedio': (df_ventas.mean() / df_ventas.mean().max() * 100),
    'Consistencia': (1 - cv/100) * 100,  # Invertir: menos CV = mejor
    'Rentabilidad': (rentabilidad['Margen Utilidad %'] / rentabilidad['Margen Utilidad %'].max() * 100)
})

# Calcular score total (ponderado)
ranking['Score Total'] = (
    ranking['Ventas Promedio'] * 0.4 +
    ranking['Consistencia'] * 0.3 +
    ranking['Rentabilidad'] * 0.3
)

ranking = ranking.sort_values('Score Total', ascending=False)
print(ranking.round(2))

print(f"\n🥇 GANADOR GENERAL: Sucursal {ranking.index[0]} (Score: {ranking['Score Total'].iloc[0]:.2f})")

# 9. Recomendaciones ejecutivas
print(f"\n9. RECOMENDACIONES EJECUTIVAS")
print("-"*70)
print(f"✓ Sucursal {mejor_promedio}: Mantener estrategia actual (mejores ventas)")
print(f"✓ Sucursal {mas_consistente}: Modelo a replicar (más consistente)")
print(f"✓ Sucursal {cv.idxmax()}: Investigar causa de alta variabilidad (CV = {cv.max():.1f}%)")

sucursal_problematica = rentabilidad['Margen Utilidad %'].idxmin()
if rentabilidad.loc[sucursal_problematica, 'Margen Utilidad %'] < 20:
    print(f"⚠️ Sucursal {sucursal_problematica}: Revisar costos operativos (margen bajo: {rentabilidad.loc[sucursal_problematica, 'Margen Utilidad %']:.1f}%)")
```

**Explicación paso a paso:**

1. **Datos crudos:** Mostramos tabla de ventas diarias para contexto

2. **Estadísticas descriptivas:** Calculamos 6 métricas clave por sucursal
   - Media y mediana: Tendencia central
   - Desviación estándar: Dispersión
   - Min/Max/Rango: Amplitud de variación

3. **Mejor desempeño:** Identificamos sucursal con mayor promedio de ventas
   - Usa `.mean().idxmax()` para encontrar el máximo

4. **Consistencia:** Menor desviación estándar = ventas más predecibles
   - Importante para planificación de inventario y personal

5. **Picos de venta:** Identificamos mejores días por sucursal
   - Útil para estrategias promocionales específicas

6. **Coeficiente de Variación (CV):**
   - CV = (std / mean) × 100
   - Permite comparar variabilidad entre sucursales con diferentes escalas
   - CV bajo = operación estable

7. **Rentabilidad:**
   - Ventas totales - costos operativos = utilidad
   - Margen = (utilidad / ventas) × 100
   - Identifica sucursales que generan más valor

8. **Ranking ponderado:**
   - Normaliza métricas a escala 0-100
   - Aplica pesos: Ventas (40%), Consistencia (30%), Rentabilidad (30%)
   - Score integrado para decisiones ejecutivas

9. **Recomendaciones:** Insights accionables basados en el análisis

**Interpretación:** Este análisis combina múltiples dimensiones de la estadística descriptiva para crear un informe ejecutivo completo. Demuestra cómo transformar datos crudos en insights estratégicos usando solo medidas descriptivas (sin inferencia ni predicción).

**Habilidades demostradas:**
- Análisis multivariable
- Normalización y comparación de métricas
- Coeficientes estadísticos (CV)
- Análisis de rentabilidad
- Síntesis de información para decisiones

</details>

---

## Recursos Adicionales

### 📚 Lecturas Recomendadas

- **"Naked Statistics" de Charles Wheelan** - Desmitifica conceptos estadísticos de manera accesible
- **Documentación de pandas:** [pandas.pydata.org](https://pandas.pydata.org/docs/)
- **Documentación de NumPy:** [numpy.org/doc](https://numpy.org/doc/)

### 🔗 Enlaces Útiles

- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Visualización con Matplotlib](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn para gráficos estadísticos](https://seaborn.pydata.org/examples/index.html)

### 📂 Archivos Relacionados del Proyecto

- `notas/`: Documentación de cursos anteriores
- `notebooks/`: Jupyter notebooks de práctica
- `data/`: Datasets para ejercicios

### 📖 Próximos Temas

- Medidas de tendencia central (media, mediana, moda)
- Medidas de dispersión (varianza, desviación estándar)
- Visualización de datos con Python
- Distribuciones de probabilidad

---

**Actualizado:** Noviembre 2025  
**Progreso de la ruta:** 68% completado (13/19 cursos)