# Ejercicio: Análisis de Ventas Mensuales con NumPy

## 📊 Resumen
El objetivo de este ejercicio es trabajar con arrays de NumPy para analizar y manipular datos de ventas de tres productos a lo largo de un año. A través de diversas operaciones, explorarás cómo usar NumPy para obtener estadísticas, realizar manipulaciones avanzadas y aplicar técnicas de indexación para extraer información clave.

## 🎯 Objetivos de Aprendizaje
- Dominar la creación y manipulación de arrays en NumPy
- Aplicar funciones estadísticas básicas
- Realizar transformaciones de datos (reshape, transpose, flatten)
- Implementar técnicas de indexación y slicing
- Analizar datos para obtener insights significativos

## 📝 Instrucciones

### Paso 1: Crear Arrays con Datos de Ventas
Usa la librería numpy para crear los siguientes arrays:
- **`meses`**: un array con los nombres de los meses del año
- **`ventas_A`**, **`ventas_B`**, **`ventas_C`**: arrays que representan las ventas mensuales de tres productos diferentes

```python
# Estructura sugerida
import numpy as np

meses = np.array(['Enero', 'Febrero', 'Marzo', ...])
ventas_A = np.array([150, 200, 250, ...])  # Valores de ejemplo
ventas_B = np.array([180, 210, 230, ...])  # Valores de ejemplo
ventas_C = np.array([200, 220, 240, ...])  # Valores de ejemplo
```

### Paso 2: Estadísticas Básicas
Calcula la media y la suma de ventas para los productos A, B y C usando las funciones de NumPy.

**Formato de salida esperado:**
- `Media de ventas Producto A: [valor]`
- `Suma de ventas Producto A: [valor]`
- `Media de ventas Producto B: [valor]`
- `Suma de ventas Producto B: [valor]`
- `Media de ventas Producto C: [valor]`
- `Suma de ventas Producto C: [valor]`

### Paso 3: Manipulación y Análisis de Datos

#### 3.1 Total de ventas por mes
Suma las ventas de los tres productos para cada mes.

#### 3.2 Promedio de ventas por producto
Calcula el promedio de ventas por producto.

#### 3.3 Mes con mayor y menor ventas
Identifica qué mes tuvo el total de ventas más alto y cuál el más bajo usando las funciones `np.argmax` y `np.argmin`.

### Paso 4: Operaciones Avanzadas con NumPy

#### 4.1 Reshape y Transposición
- Crea una matriz 2D con las ventas de los tres productos
- Transforma su forma (reshape) a un array tridimensional con dimensiones (3, 4, 3)
- Transpone la matriz de ventas para que las filas se conviertan en columnas

#### 4.2 Invertir arrays
Invierte las ventas de cada producto en orden de meses.

#### 4.3 Aplanar la matriz
Convierte la matriz de ventas a un array unidimensional.

```python
# Ejemplo de estructura
ventas_matrix = np.array([ventas_A, ventas_B, ventas_C])
ventas_reshaped = ventas_matrix.reshape(3, 4, 3)
ventas_transposed = ventas_matrix.T
ventas_flattened = ventas_matrix.flatten()
```

### Paso 5: Análisis de Elementos Únicos
Utiliza `np.unique` para:
- Encontrar los elementos únicos en los datos de ventas
- Contar cuántas veces aparece cada valor único

### Paso 6: Indexación y Slicing

#### 6.1 Ventas del primer trimestre
Extrae las ventas de los tres primeros meses del año.

#### 6.2 Indexación booleana
Selecciona los meses donde el total de ventas de los tres productos supere los 800.

#### 6.3 Selección avanzada
Usa una lista de índices para seleccionar las ventas de los meses pares (o selecciona los meses a tu elección) y muestra esas ventas en una nueva matriz.

```python
# Ejemplo de indexación
indices = [0, 2, 4, 6, 8, 10]  # Meses impares (índices pares)
ventas_seleccionadas = ventas_matrix[:, indices]
```

## 💡 Tips y Recomendaciones
- Usa `print()` statements claros para mostrar los resultados de cada paso
- Comenta tu código para explicar qué hace cada sección
- Verifica las dimensiones de tus arrays con `.shape`
- Usa `.dtype` para verificar el tipo de datos de tus arrays

## 📊 Datos de Ejemplo (Opcional)
Si necesitas datos para empezar, puedes usar estos valores:

```python
ventas_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
ventas_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
ventas_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])
```

## ✅ Criterios de Evaluación
- [ ] Creación correcta de arrays con NumPy
- [ ] Aplicación apropiada de funciones estadísticas (mean, sum)
- [ ] Uso correcto de argmax y argmin
- [ ] Manipulación exitosa de arrays (reshape, transpose, flatten)
- [ ] Implementación correcta de indexación booleana
- [ ] Código limpio y bien documentado

## 🚀 Extensiones Opcionales
Si terminas antes, puedes intentar:
1. Calcular la desviación estándar de las ventas
2. Encontrar la mediana de ventas por producto
3. Crear una función que identifique tendencias (crecimiento/decrecimiento)
4. Visualizar los datos usando matplotlib (si conoces la librería)

## 📤 Entregable
Un notebook de Jupyter (.ipynb) o archivo Python (.py) con:
- Todo el código implementado y ejecutado
- Comentarios explicativos
- Resultados claramente mostrados
- (Opcional) Conclusiones sobre los patrones encontrados en los datos

---
**Nota**: Este ejercicio es parte del curso de NumPy y está diseñado para reforzar los conceptos fundamentales de manipulación de arrays y análisis de datos con NumPy.