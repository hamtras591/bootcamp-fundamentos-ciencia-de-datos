# Medidas de Tendencia Central

**Curso:** Matemáticas para Data Science: Estadística Descriptiva  
**Fecha:** Noviembre 2025  
**Módulo:** Estadística Descriptiva para Analítica  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [¿Para qué sirven?](#para-qué-sirven)
3. [La Media (Promedio)](#la-media-promedio)
4. [La Mediana](#la-mediana)
5. [La Moda](#la-moda)
6. [Tabla de Frecuencias](#tabla-de-frecuencias)
7. [Comparación: Media vs Mediana](#comparación-media-vs-mediana)
8. [La Metáfora de Bill Gates en un Bar](#la-metáfora-de-bill-gates-en-un-bar)
9. [Implementación en Python](#implementación-en-python)
10. [Casos de Uso](#casos-de-uso)
11. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

Las **medidas de tendencia central** son herramientas fundamentales en estadística descriptiva que nos permiten **resumir un conjunto de datos en un solo valor representativo** que indica dónde se "centra" la información.

### Analogía del salón de clase:

Imagina un salón con 30 estudiantes de diferentes edades. Si te digo que:
- **La edad promedio es 7 años** → Entiendes inmediatamente que son niños pequeños
- **La mediana es 7 años** → La mitad tiene 7 años o menos
- **La moda es 7 años** → 7 años es la edad más común

**Ventaja principal:** Condensan información compleja en cifras simples y comprensibles.

---

## ¿Para qué sirven?

Las medidas de tendencia central tienen múltiples aplicaciones:

### 1. Resumir información
- Convertir miles de valores en uno solo
- Facilitar la comunicación de resultados
- Simplificar comparaciones

### 2. Detectar patrones
- Identificar valores "típicos"
- Encontrar comportamientos centrales
- Establecer referencias

### 3. Tomar decisiones
- Establecer metas (ej. ventas promedio)
- Detectar anomalías (alejadas del centro)
- Realizar pronósticos

### 4. Comparar grupos
- Estudiantes de dos escuelas
- Ventas de diferentes sucursales
- Desempeño de equipos

---

## La Media (Promedio)

### Definición

La **media** o **promedio** es la suma de todos los valores dividida por el número total de datos.

**Fórmula:**

```
Media (μ o x̄) = (Suma de todos los valores) / (Número de valores)

μ = (x₁ + x₂ + x₃ + ... + xₙ) / n
```

---

### Características

✅ **Ventajas:**
- Usa todos los datos en su cálculo
- Matemáticamente estable
- Ideal para cálculos posteriores (varianza, desviación estándar)

⚠️ **Desventajas:**
- **MUY sensible a valores atípicos (outliers)**
- Puede no representar ningún valor real del dataset
- No apropiada para datos categóricos

---

### Ejemplo básico

```python
import pandas as pd

# Edades de estudiantes
edades = pd.Series([6, 7, 7, 7, 8, 8, 6, 7, 8, 7])

media = edades.mean()
print(f"Media de edades: {media:.2f} años")  # 7.10 años
```

---

### Interpretación

La media nos dice el "centro de masa" de los datos. Es como el punto de equilibrio de una balanza.

```
Datos: [6, 7, 7, 7, 8, 8, 6, 7, 8, 7]
                    ↓
                  7.10 ← Media (punto de equilibrio)
```

---

### Impacto de valores atípicos

```python
import pandas as pd

# Salarios en una empresa pequeña
salarios = pd.Series([30000, 32000, 31000, 33000, 35000])  # Empleados regulares
salarios_con_ceo = pd.Series([30000, 32000, 31000, 33000, 35000, 500000])  # + CEO

print("SIN OUTLIER:")
print(f"  Media: ${salarios.mean():,.0f}")  # $32,200

print("\nCON OUTLIER (CEO):")
print(f"  Media: ${salarios_con_ceo.mean():,.0f}")  # $110,167

print("\n❌ La media NO es representativa cuando hay outliers")
```

**Resultado:**
- Sin CEO: $32,200 (representativo)
- Con CEO: $110,167 (engañoso, nadie gana cerca de eso excepto el CEO)

---

## La Mediana

### Definición

La **mediana** es el valor que está **exactamente en la mitad** de los datos cuando están ordenados. La mitad de los datos es menor o igual a la mediana, y la otra mitad es mayor o igual.

**Características clave:**
- Divide el dataset en dos partes iguales
- Es el valor del percentil 50 (P50)
- **Robusta ante valores atípicos**

---

### Cálculo de la mediana

Depende de si el número de datos es **par** o **impar**:

#### Caso 1: Número impar de datos

```
Datos ordenados: [6, 7, 7, |7|, 8, 8, 9]
                           ↑
                       Mediana = 7
```

La mediana es el valor central.

#### Caso 2: Número par de datos

```
Datos ordenados: [6, 7, |7, 8|, 8, 9]
                        ↓
              Mediana = (7 + 8) / 2 = 7.5
```

La mediana es el promedio de los dos valores centrales.

---

### Ejemplo en Python

```python
import pandas as pd

# Caso impar
datos_impar = pd.Series([6, 7, 7, 7, 8, 8, 9])
print(f"Datos (impar): {sorted(datos_impar.values)}")
print(f"Mediana: {datos_impar.median()}")  # 7.0

# Caso par
datos_par = pd.Series([6, 7, 7, 8, 8, 9])
print(f"\nDatos (par): {sorted(datos_par.values)}")
print(f"Mediana: {datos_par.median()}")  # 7.5
```

---

### Ventaja principal: Resistencia a outliers

```python
import pandas as pd

# Salarios sin outlier
salarios = pd.Series([30000, 32000, 31000, 33000, 35000])

# Salarios con outlier (CEO)
salarios_con_ceo = pd.Series([30000, 32000, 31000, 33000, 35000, 500000])

print("SIN OUTLIER:")
print(f"  Media:   ${salarios.mean():,.0f}")    # $32,200
print(f"  Mediana: ${salarios.median():,.0f}")  # $32,000

print("\nCON OUTLIER (CEO):")
print(f"  Media:   ${salarios_con_ceo.mean():,.0f}")    # $110,167 ❌ Distorsionada
print(f"  Mediana: ${salarios_con_ceo.median():,.0f}")  # $32,000 ✅ Estable

print("\n✅ La mediana SE MANTIENE representativa incluso con outliers")
```

---

## La Moda

### Definición

La **moda** es el valor que **aparece con mayor frecuencia** en un conjunto de datos.

**Características:**
- Puede haber más de una moda (bimodal, multimodal)
- Puede no existir moda (todos los valores únicos)
- Es la única medida de tendencia central aplicable a **datos categóricos**

---

### Tipos de distribuciones según la moda

```python
# Unimodal: Una sola moda
datos_unimodal = [7, 7, 7, 8, 8, 9, 6, 7]  # Moda: 7

# Bimodal: Dos modas
datos_bimodal = [7, 7, 7, 8, 8, 8, 9, 6]  # Modas: 7 y 8

# Sin moda: Todos los valores son únicos
datos_sin_moda = [1, 2, 3, 4, 5, 6, 7, 8]  # No hay moda
```

---

### Ejemplo en Python

```python
import pandas as pd

# Edades de estudiantes
edades = pd.Series([6, 7, 7, 7, 8, 8, 6, 7, 8, 7, 9, 7])

# Calcular moda
moda = edades.mode()
print(f"Moda: {moda.values}")  # [7]
print(f"Aparece {(edades == 7).sum()} veces")

# Tabla de frecuencias
print("\nTabla de frecuencias:")
print(edades.value_counts().sort_index())
```

**Output:**
```
Moda: [7]
Aparece 6 veces

Tabla de frecuencias:
6    2
7    6  ← Moda (más frecuente)
8    3
9    1
```

---

### Moda con datos categóricos

```python
import pandas as pd

# Método de pago más usado
metodos_pago = pd.Series([
    'Tarjeta', 'PayPal', 'Tarjeta', 'Efectivo', 
    'Tarjeta', 'Tarjeta', 'PayPal', 'Tarjeta'
])

moda = metodos_pago.mode()[0]
print(f"Método de pago más común: {moda}")  # Tarjeta

# Frecuencias
print("\nFrecuencias:")
print(metodos_pago.value_counts())
```

**Output:**
```
Método de pago más común: Tarjeta

Frecuencias:
Tarjeta     5  ← Moda
PayPal      2
Efectivo    1
```

---

## Tabla de Frecuencias

Una **tabla de frecuencias** muestra cuántas veces aparece cada valor en un conjunto de datos.

### Ejemplo: Edades de 20 estudiantes

```python
import pandas as pd

# Edades de 20 estudiantes
edades = pd.Series([15, 16, 15, 17, 16, 15, 18, 16, 19, 15, 
                    16, 17, 15, 16, 18, 16, 15, 17, 16, 15])

# Crear tabla de frecuencias
tabla_frecuencias = pd.DataFrame({
    'Frecuencia': edades.value_counts().sort_index(),
    'Frecuencia Relativa': edades.value_counts(normalize=True).sort_index() * 100
})

print("TABLA DE FRECUENCIAS:")
print(tabla_frecuencias)

# Identificar moda
print(f"\nModa (edad más común): {edades.mode()[0]} años")
print(f"Aparece {edades.value_counts().max()} veces ({edades.value_counts().max()/len(edades)*100:.1f}%)")
```

**Output:**
```
TABLA DE FRECUENCIAS:
    Frecuencia  Frecuencia Relativa
15           8                 40.0
16           7                 35.0
17           3                 15.0
18           2                 10.0
19           1                  5.0

Moda (edad más común): 15 años
Aparece 8 veces (40.0%)
```

---

### Visualización de tabla de frecuencias

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Diagrama de barras
plt.figure(figsize=(10, 6))
edades.value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribución de Edades de Estudiantes', fontsize=14, fontweight='bold')
plt.xlabel('Edad (años)')
plt.ylabel('Frecuencia (número de estudiantes)')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

## Comparación: Media vs Mediana

### ¿Cuándo usar cada una?

| Situación | Usar | Razón |
|-----------|------|-------|
| **Datos simétricos sin outliers** | Media | Usa toda la información, matemáticamente precisa |
| **Datos con outliers** | Mediana | No se ve afectada por valores extremos |
| **Distribución sesgada** | Mediana | Representa mejor el "centro" real |
| **Ingreso de población** | Mediana | Pocas personas con ingresos extremos distorsionan la media |
| **Calificaciones de estudiantes** | Media | Generalmente no hay outliers extremos |
| **Precios de casas** | Mediana | Mansiones caras distorsionan la media |
| **Temperatura promedio** | Media | Datos generalmente bien distribuidos |

---

### Ejemplo comparativo completo

```python
import pandas as pd
import numpy as np

# Dataset 1: Sin outliers (simétrico)
notas_clase = pd.Series([85, 88, 90, 87, 85, 92, 89, 86, 88, 90])

print("DATASET 1: NOTAS DE CLASE (Sin outliers)")
print(f"Media:   {notas_clase.mean():.2f}")    # 88.00
print(f"Mediana: {notas_clase.median():.2f}")  # 88.00
print("Conclusión: Media y mediana similares → Distribución simétrica\n")

# Dataset 2: Con outliers
ingresos = pd.Series([30000, 32000, 31000, 33000, 35000, 500000])  # CEO outlier

print("DATASET 2: INGRESOS (Con outlier)")
print(f"Media:   ${ingresos.mean():,.0f}")    # $110,167 ❌
print(f"Mediana: ${ingresos.median():,.0f}")  # $32,000 ✅
print("Conclusión: Media >> Mediana → Usar MEDIANA para representar ingreso típico\n")

# Dataset 3: Distribución sesgada
tiempo_respuesta = pd.Series([2, 3, 2, 4, 3, 2, 5, 45, 3, 4])  # Un ticket muy lento

print("DATASET 3: TIEMPO DE RESPUESTA (minutos)")
print(f"Media:   {tiempo_respuesta.mean():.2f} min")    # 7.30 min
print(f"Mediana: {tiempo_respuesta.median():.2f} min")  # 3.00 min
print("Conclusión: Mediana más representativa del tiempo típico")
```

---

## La Metáfora de Bill Gates en un Bar

### Concepto

Esta famosa metáfora ilustra perfectamente el impacto de los outliers en la media:

> **"Bill Gates entra a un bar. De repente, en promedio, todos los presentes son millonarios."**

---

### Demostración numérica

```python
import pandas as pd

# Ingresos de 10 personas en un bar (en dólares anuales)
ingresos_bar = pd.Series([
    50000,   # Persona 1
    45000,   # Persona 2
    52000,   # Persona 3
    48000,   # Persona 4
    51000,   # Persona 5
    49000,   # Persona 6
    47000,   # Persona 7
    53000,   # Persona 8
    46000,   # Persona 9
    50000    # Persona 10
])

# Bill Gates entra al bar (patrimonio: ~100 mil millones)
ingresos_con_bill = pd.concat([ingresos_bar, pd.Series([100_000_000_000])])

print("="*60)
print("LA METÁFORA DE BILL GATES EN UN BAR")
print("="*60)

print("\nANTES de que Bill Gates entre:")
print(f"  Media:   ${ingresos_bar.mean():,.0f}")
print(f"  Mediana: ${ingresos_bar.median():,.0f}")
print(f"  Interpretación: Salario típico ~$49,000")

print("\nDESPUÉS de que Bill Gates entre:")
print(f"  Media:   ${ingresos_con_bill.mean():,.0f}")  # ~$9,090 millones
print(f"  Mediana: ${ingresos_con_bill.median():,.0f}")  # $50,000 (sin cambio)

print("\n" + "="*60)
print("CONCLUSIÓN:")
print("="*60)
print("❌ Media:   Se disparó a $9,090 millones (NO representativa)")
print("✅ Mediana: Se mantuvo en $50,000 (SÍ representativa)")
print("\nLa mediana es ROBUSTA ante outliers extremos.")
```

---

### Lección clave

📌 **Cuando hay outliers extremos, la mediana es más representativa que la media.**

Esto aplica a:
- 💰 Ingresos y patrimonio
- 🏠 Precios de inmuebles
- ⏱️ Tiempos de respuesta en servicios
- 📈 Datos de ventas con picos ocasionales

---

## Implementación en Python

### Todas las medidas en un solo análisis

```python
import pandas as pd
import numpy as np

# Cargar dataset
df = pd.read_csv('cars.csv')

# Seleccionar columna numérica
columna = 'Price'

print("="*60)
print(f"ANÁLISIS DE TENDENCIA CENTRAL: {columna}")
print("="*60)

# Calcular medidas
media = df[columna].mean()
mediana = df[columna].median()
moda = df[columna].mode()[0] if not df[columna].mode().empty else "No hay moda"

print(f"\nMedia:   ${media:,.2f}")
print(f"Mediana: ${mediana:,.2f}")
print(f"Moda:    ${moda:,.2f}" if isinstance(moda, (int, float)) else f"Moda:    {moda}")

# Comparación
diferencia = abs(media - mediana)
porcentaje_diferencia = (diferencia / mediana) * 100

print(f"\nDiferencia Media-Mediana: ${diferencia:,.2f} ({porcentaje_diferencia:.1f}%)")

if porcentaje_diferencia < 5:
    print("✅ Distribución relativamente simétrica")
elif porcentaje_diferencia < 15:
    print("⚠️ Distribución con sesgo moderado")
else:
    print("❌ Distribución muy sesgada o con outliers")

# Estadísticas adicionales
print(f"\nValor mínimo: ${df[columna].min():,.2f}")
print(f"Valor máximo: ${df[columna].max():,.2f}")
print(f"Rango: ${df[columna].max() - df[columna].min():,.2f}")
```

---

## Casos de Uso

### Caso de Uso 1: Análisis de Salarios en una Empresa

**Contexto:** RH necesita reportar el "salario típico" de la empresa al CEO.

```python
import pandas as pd
import numpy as np

# Salarios de 100 empleados
np.random.seed(42)
salarios = pd.Series(np.random.normal(50000, 10000, 98).clip(30000, 80000))
salarios = pd.concat([salarios, pd.Series([150000, 200000])])  # 2 ejecutivos

print("ANÁLISIS DE SALARIOS")
print("="*60)

media = salarios.mean()
mediana = salarios.median()
moda = salarios.mode()[0] if not salarios.mode().empty else "No hay moda única"

print(f"Media:   ${media:,.0f}")
print(f"Mediana: ${mediana:,.0f}")
print(f"Moda:    {moda if isinstance(moda, str) else f'${moda:,.0f}'}")

print(f"\n📊 INTERPRETACIÓN:")
print(f"  - Media ({media:,.0f}) inflada por salarios ejecutivos")
print(f"  - Mediana ({mediana:,.0f}) representa mejor el salario típico")
print(f"\n✅ RECOMENDACIÓN: Reportar MEDIANA como 'salario típico'")
```

**Explicación:** En este caso, la mediana es más apropiada porque no se ve afectada por los salarios ejecutivos extremadamente altos.

---

### Caso de Uso 2: Análisis de Tiempos de Atención

**Contexto:** Un call center quiere medir el tiempo típico de atención al cliente.

```python
import pandas as pd
import numpy as np

# Tiempos de atención (en minutos)
np.random.seed(100)
tiempos = pd.Series(np.random.gamma(2, 3, 100))  # Distribución sesgada

print("ANÁLISIS DE TIEMPOS DE ATENCIÓN")
print("="*60)

media = tiempos.mean()
mediana = tiempos.median()

print(f"Media:   {media:.2f} minutos")
print(f"Mediana: {mediana:.2f} minutos")

# Percentiles para contexto
print(f"\nDistribución:")
print(f"  P25: {tiempos.quantile(0.25):.2f} min")
print(f"  P50: {tiempos.quantile(0.50):.2f} min (Mediana)")
print(f"  P75: {tiempos.quantile(0.75):.2f} min")
print(f"  P90: {tiempos.quantile(0.90):.2f} min")

print(f"\n📊 INTERPRETACIÓN:")
print(f"  - El 50% de las llamadas se atiende en {mediana:.1f} min o menos")
print(f"  - El 90% de las llamadas se atiende en {tiempos.quantile(0.90):.1f} min o menos")
print(f"\n✅ META: Mantener la mediana bajo 7 minutos")
```

**Explicación:** La mediana es útil para establecer SLAs (Service Level Agreements) porque representa el tiempo típico sin ser distorsionada por casos excepcionales.

---

## Recursos Adicionales

### 📚 Conceptos clave

- **Media:** Suma de valores / Número de valores (sensible a outliers)
- **Mediana:** Valor central cuando los datos están ordenados (robusta)
- **Moda:** Valor más frecuente (única aplicable a categóricos)

### 🔗 Referencias

- **Libro recomendado:** "Naked Statistics" de Charles Wheelan
- [Pandas describe()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
- [NumPy statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)

### 📂 Archivos relacionados

- `04_tipos_datos_ciencia_datos.md` - Tipos de datos
- Próximo: `06_medidas_dispersion.md` - Variabilidad de los datos
- Notebook de ejercicios: `ejercicios_estadistica_descriptiva.ipynb`

### 🎯 Decisión rápida: ¿Media o Mediana?

```
¿Hay outliers? 
    ├─ Sí → MEDIANA
    └─ No → ¿Distribución simétrica?
            ├─ Sí → MEDIA
            └─ No → MEDIANA
```

---

**Actualizado:** Noviembre 2025  
**Progreso de la ruta:** 68% completado (13/19 cursos)