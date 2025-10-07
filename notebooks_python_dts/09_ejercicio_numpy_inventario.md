# Ejercicio: Análisis de Inventario de Tienda de Tecnología con NumPy

## 📱 Contexto
Eres el analista de datos de una cadena de tiendas de tecnología con 4 sucursales. Necesitas analizar el inventario mensual de diferentes categorías de productos durante un año para optimizar las compras y detectar patrones de demanda.

## 🎯 Objetivo
Trabajar con arrays de NumPy para analizar y manipular datos de inventario de cuatro categorías de productos a lo largo de un año, aplicando operaciones estadísticas, transformaciones avanzadas y técnicas de indexación.

## 📝 Instrucciones:

### Paso 1: Crear Arrays con Datos de Inventario
Crea los siguientes arrays usando NumPy:
- `meses`: array con los nombres de los meses del año
- `laptops`: inventario mensual de laptops (valores sugeridos entre 30-80 unidades)
- `smartphones`: inventario mensual de smartphones (valores sugeridos entre 50-120 unidades)  
- `tablets`: inventario mensual de tablets (valores sugeridos entre 20-60 unidades)
- `accesorios`: inventario mensual de accesorios (valores sugeridos entre 100-250 unidades)

**Datos sugeridos para que uses:**
```python
# Puedes usar estos datos o crear los tuyos propios
laptops = [45, 52, 48, 55, 60, 58, 62, 65, 70, 68, 72, 75]
smartphones = [80, 85, 92, 95, 88, 102, 110, 108, 115, 112, 118, 120]
tablets = [35, 38, 40, 42, 45, 48, 44, 46, 50, 52, 55, 58]
accesorios = [150, 165, 180, 175, 190, 200, 210, 205, 220, 225, 230, 240]
```

### Paso 2: Estadísticas Básicas
Calcula y muestra:
- La **mediana** y la **desviación estándar** del inventario para cada categoría
- El **valor máximo** y **mínimo** de inventario para cada categoría
- El **inventario total anual** por categoría

Formato de salida esperado:
- "Mediana de inventario Laptops: X unidades"
- "Desviación estándar Laptops: X"
- "Inventario máximo/mínimo Laptops: X/X unidades"

### Paso 3: Análisis Comparativo de Inventarios
- **Inventario total por mes**: Suma el inventario de todas las categorías para cada mes
- **Promedio trimestral**: Calcula el promedio de inventario por trimestre (Q1, Q2, Q3, Q4) para cada categoría
- **Mes crítico**: Identifica el mes con el inventario total más bajo (posible desabastecimiento)
- **Mes peak**: Identifica el mes con el inventario total más alto

### Paso 4: Operaciones de Transformación
**Matrices y Reorganización:**
- Crea una matriz 2D `inventario_matriz` con las 4 categorías como filas
- Transforma la matriz a un array 3D con dimensiones (2, 6, 4) representando (semestres, meses, categorías)
- Crea una versión normalizada del inventario (valores entre 0 y 1) usando min-max scaling

**Operaciones adicionales:**
- Ordena los valores de inventario de cada categoría de menor a mayor
- Crea un array que contenga la diferencia mes a mes (variación) del inventario total

### Paso 5: Análisis Estadístico Avanzado
- **Percentiles**: Calcula los percentiles 25, 50 y 75 del inventario total
- **Correlación**: Calcula qué tan relacionados están los inventarios de laptops y tablets
- **Valores atípicos**: Identifica si hay meses con inventarios anormalmente altos o bajos (fuera de 1.5 veces el rango intercuartil)

### Paso 6: Indexación y Filtrado Avanzado
- **Inventario segundo semestre**: Extrae solo los datos de julio a diciembre
- **Meses de alto inventario**: Selecciona los meses donde el inventario total supere las 400 unidades
- **Categorías críticas**: Identifica las categorías que en algún mes tuvieron menos del 80% de su promedio anual
- **Patrón estacional**: Extrae los datos de los meses de temporada alta (marzo, junio, septiembre, diciembre)
- **Comparación cruzada**: Crea una matriz que muestre solo los meses donde los smartphones superaron las 100 unidades Y las laptops superaron las 60 unidades

### Paso 7: Visualización de Resumen (Bonus)
Crea un reporte final que muestre:
- Una matriz de resumen con: [Categoría, Promedio Anual, Total Anual, Mes Peak, Valor Peak]
- Un ranking de categorías por volumen total anual
- El porcentaje que representa cada categoría del inventario total anual

## ✅ Criterios de Evaluación
- Uso correcto de funciones NumPy (mean, std, median, sum, etc.)
- Manipulación apropiada de arrays (reshape, transpose, flatten)
- Aplicación correcta de indexación booleana y fancy indexing
- Cálculos estadísticos precisos
- Código limpio y bien comentado

## 💡 Tips
- Recuerda usar `np.array()` para crear los arrays iniciales
- Para la normalización min-max: `(array - array.min()) / (array.max() - array.min())`
- Usa `np.where()` para encontrar índices que cumplan condiciones
- La función `np.diff()` es útil para calcular diferencias entre elementos consecutivos
- Para el rango intercuartil: IQR = Q3 - Q1, donde Q1 = percentil 25 y Q3 = percentil 75

## 📤 Entregable
Un notebook de Jupyter (.ipynb) con:
1. El código completo y ejecutado
2. Comentarios explicando cada paso
3. Interpretación breve de los resultados más relevantes
4. Al menos una conclusión o insight del análisis

---
**Nota**: Este ejercicio está diseñado para profundizar en las capacidades de NumPy, incluyendo análisis estadístico avanzado y manipulación compleja de datos.

¡Buena suerte con el ejercicio! 🚀