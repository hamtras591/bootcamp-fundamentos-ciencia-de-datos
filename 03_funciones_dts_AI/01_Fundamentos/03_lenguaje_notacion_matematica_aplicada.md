# Lenguaje y Notación Matemática para Data Science

**Curso:** Lenguaje y Notación Matemática  
**Fecha:** 30 de octubre de 2025  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [Símbolos de Relación e Igualdad](#símbolos-de-relación-e-igualdad)
3. [Símbolos de Operaciones Acumulativas](#símbolos-de-operaciones-acumulativas)
4. [Teoría de Conjuntos](#teoría-de-conjuntos)
5. [Conjuntos de Números](#conjuntos-de-números)
6. [Notación de Funciones](#notación-de-funciones)
7. [Casos de Uso en Data Science](#casos-de-uso-en-data-science)
8. [Ejercicios Prácticos](#ejercicios-prácticos)
9. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

La **notación matemática** es un lenguaje universal que permite expresar ideas complejas de forma concisa y precisa. En Data Science, necesitas entender esta notación para:

- Leer papers científicos y documentación técnica
- Implementar fórmulas en código
- Comunicarte con otros profesionales
- Entender documentación de librerías (NumPy, Pandas, SciKit-learn)

**Analogía:** Si el español es para hablar con personas, la notación matemática es para hablar con máquinas y científicos.

---

## Símbolos de Relación e Igualdad

Estos símbolos se usan para comparar valores y expresar relaciones.

### Símbolos Básicos

| Símbolo | Nombre | Significado | Ejemplo | Python |
|---------|--------|-------------|---------|--------|
| `=` | Igualdad | Es exactamente igual a | `2 = 1 + 1` | `2 == 1 + 1` |
| `>` | Mayor que | Es más grande que | `5 > 3` | `5 > 3` |
| `<` | Menor que | Es más pequeño que | `4 < 7` | `4 < 7` |
| `≥` | Mayor o igual | Es más grande O igual | `x ≥ 0` | `x >= 0` |
| `≤` | Menor o igual | Es más pequeño O igual | `y ≤ 10` | `y <= 10` |
| `≠` | Diferente | NO es igual a | `a ≠ b` | `a != b` |

### Símbolos Avanzados

| Símbolo | Nombre | Significado | Ejemplo |
|---------|--------|-------------|---------|
| `≈` | Aproximadamente | Casi igual a (redondeado) | `π ≈ 3.14159...` |
| `≡` | Idénticamente igual | Igual en TODOS los casos | `(x+1)² ≡ x² + 2x + 1` |
| `>>` | Mucho mayor que | SIGNIFICATIVAMENTE mayor | `1000 >> 1` |
| `<<` | Mucho menor que | SIGNIFICATIVAMENTE menor | `0.001 << 1000` |
| `∞` | Infinito | Sin límite, ilimitado | `lim_{x→∞} 1/x = 0` |

### Ejemplos Prácticos en Code

```python
# Símbolo = (en Python es ==)
edad = 25
if edad == 25:
    print("Cumpleaños!")

# Símbolo >
puntuacion = 8
if puntuacion > 7:
    print("Cliente satisfecho")

# Símbolo ≠ (en Python es !=)
estado = "activo"
if estado != "inactivo":
    print("Usuario puede comprar")

# Símbolo ≈ (aproximadamente)
import math
print(f"π ≈ {math.pi:.2f}")  # π ≈ 3.14

# Símbolo >> y <<
if beneficios >> costos:
    print("Proyecto muy rentable")

valor_pequeño = 0.0001
valor_grande = 1e10
if valor_pequeño << valor_grande:
    print("Diferencia enorme")
```

---

## Símbolos de Operaciones Acumulativas

Estos símbolos representan operaciones repetidas.

### Sigma (Σ) - Sumatoria

**Símbolo:** `Σ`

**Significado:** Suma todos los valores

**Notación formal:**
```
    n
   Σ f(i)  =  f(1) + f(2) + f(3) + ... + f(n)
   i=1
```

**En español:** "Sumatoria desde i=1 hasta n de f(i)"

**Ejemplo matemático:**
```
    5
   Σ i  =  1 + 2 + 3 + 4 + 5 = 15
   i=1
```

**En Python:**

```python
# Sumatoria de 1 a 5
resultado = sum(range(1, 6))  # 1 + 2 + 3 + 4 + 5
print(resultado)  # 15

# Sumatoria con condiciones
numeros = [1, 2, 3, 4, 5]
suma = sum(n for n in numeros if n > 2)  # 3 + 4 + 5
print(suma)  # 12

# Sumatoria de cuadrados
suma_cuadrados = sum(i**2 for i in range(1, 6))  # 1² + 2² + 3² + 4² + 5²
print(suma_cuadrados)  # 55
```

### Pi (Π) - Productoria

**Símbolo:** `Π`

**Significado:** Multiplica todos los valores

**Notación formal:**
```
    n
   Π f(i)  =  f(1) × f(2) × f(3) × ... × f(n)
   i=1
```

**Ejemplo matemático:**
```
    4
   Π i  =  1 × 2 × 3 × 4 = 24
   i=1
```

**En Python:**

```python
import math

# Productoria de 1 a 4 (factorial)
resultado = math.factorial(4)  # 1 × 2 × 3 × 4
print(resultado)  # 24

# Productoria manual
producto = 1
for i in range(1, 5):
    producto *= i
print(producto)  # 24

# Productoria con NumPy
import numpy as np
numeros = [1, 2, 3, 4]
producto_np = np.prod(numeros)
print(producto_np)  # 24
```

---

## Teoría de Conjuntos

Un **conjunto** es una colección de elementos distintos.

### Símbolos de Conjunto

| Símbolo | Nombre | Significado | Ejemplo |
|---------|--------|-------------|---------|
| `∈` | Pertenece | El elemento está EN el conjunto | `3 ∈ {1,2,3,4}` → Verdadero |
| `∉` | No pertenece | El elemento NO está en el conjunto | `5 ∉ {1,2,3,4}` → Verdadero |
| `∪` | Unión | Todos los elementos de ambos conjuntos | `{1,2} ∪ {2,3} = {1,2,3}` |
| `∩` | Intersección | Elementos que están en AMBOS | `{1,2} ∩ {2,3} = {2}` |
| `∅` | Vacío | Conjunto sin elementos | `{} = ∅` |
| `⊂` | Subconjunto | Todos los elementos de A están en B | `{1,2} ⊂ {1,2,3}` |
| `⊃` | Superconjunto | B contiene todos los elementos de A | `{1,2,3} ⊃ {1,2}` |
| `\` | Diferencia | Elementos en A pero NO en B | `{1,2,3} \ {2,3} = {1}` |
| `|Ω|` | Cardinalidad | Cantidad de elementos en el conjunto | `|{1,2,3}| = 3` |

### Ejemplos Prácticos en Python

```python
# Conjuntos en Python
conjunto_A = {1, 2, 3, 4}
conjunto_B = {3, 4, 5, 6}

# ∈ (Pertenencia)
print(3 in conjunto_A)  # True (3 ∈ A)
print(7 in conjunto_A)  # False (7 ∉ A)

# ∪ (Unión)
union = conjunto_A | conjunto_B
print(union)  # {1, 2, 3, 4, 5, 6}

# ∩ (Intersección)
interseccion = conjunto_A & conjunto_B
print(interseccion)  # {3, 4}

# \ (Diferencia)
diferencia = conjunto_A - conjunto_B
print(diferencia)  # {1, 2}

# ∅ (Conjunto vacío)
vacio = set()
print(len(vacio) == 0)  # True

# ⊂ (Subconjunto)
sub = {1, 2}
print(sub <= conjunto_A)  # True ({1,2} ⊂ {1,2,3,4})

# |A| (Cardinalidad)
print(len(conjunto_A))  # 4
```

### Con Pandas (Data Science Real)

```python
import pandas as pd

# Dataset de encuestas
df = pd.DataFrame({
    'cliente_id': [1, 2, 3, 4, 5],
    'departamento': ['Ventas', 'Soporte', 'Ventas', 'Producto', 'Soporte'],
    'compra_hecha': [True, False, True, True, False]
})

# Conjuntos de departamentos
departamentos_totales = set(df['departamento'])  # {Ventas, Soporte, Producto}
departamentos_ventas = set(df[df['departamento'] == 'Ventas']['departamento'])

# Clientes que compraron
clientes_compradores = set(df[df['compra_hecha']]['cliente_id'])  # {1, 3, 4}

# Clientes que NO compraron
clientes_no_compradores = set(df[~df['compra_hecha']]['cliente_id'])  # {2, 5}

# Diferencia: clientes totales - que compraron
total_clientes = set(df['cliente_id'])
clientes_para_seguimiento = total_clientes - clientes_compradores

print(f"Departamentos: {departamentos_totales}")
print(f"Clientes a seguimiento: {clientes_para_seguimiento}")
```

---

## Conjuntos de Números

Existen conjuntos especiales para diferentes tipos de números.

### Conjuntos Numéricos Principales

| Símbolo | Nombre | Definición | Ejemplos |
|---------|--------|-----------|----------|
| `ℕ` | Naturales | Números positivos sin decimales | `{1, 2, 3, 4, ...}` |
| `ℤ` | Enteros | Naturales + negativos + cero | `{..., -2, -1, 0, 1, 2, ...}` |
| `ℚ` | Racionales | Números que se expresan como fracción a/b | `{1/2, 0.75, -3/4, ...}` |
| `𝕀` | Irracionales | NO se pueden expresar como fracción | `{π, e, √2, ...}` |
| `ℝ` | Reales | Todos los números (Q ∪ I) | Cualquier número de la recta real |
| `ℝ⁺` | Reales positivos | Reales mayores que cero | `{x ∈ ℝ \| x > 0}` |
| `ℝ⁻` | Reales negativos | Reales menores que cero | `{x ∈ ℝ \| x < 0}` |
| `ℂ` | Complejos | Números con parte real e imaginaria | `{3 + 4i, 2 - i, ...}` |

### Jerarquía de Conjuntos

```
ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
           ⊃ 𝕀
           
Es decir:
- Todos los Naturales están en Enteros
- Todos los Enteros están en Racionales
- Todos los Racionales están en Reales
- Los Irracionales también están en Reales
```

### Ejemplos en Python

```python
import numpy as np
from fractions import Fraction

# ℕ Naturales (números positivos enteros)
naturales = [1, 2, 3, 4, 5]
print(f"Naturales: {naturales}")

# ℤ Enteros (incluyen negativos y cero)
enteros = [-3, -2, -1, 0, 1, 2, 3]
print(f"Enteros: {enteros}")

# ℚ Racionales (fracciones)
racional_1 = Fraction(1, 2)  # 0.5
racional_2 = Fraction(3, 4)  # 0.75
print(f"Racionales: {racional_1}, {racional_2}")

# 𝕀 Irracionales (π, e, √2)
import math
pi = math.pi  # 3.14159...
e = math.e    # 2.71828...
raiz_2 = math.sqrt(2)  # 1.41421...
print(f"Irracionales: π={pi}, e={e}, √2={raiz_2}")

# ℝ Reales (todos)
reales = [-5.5, -3, 0, 3.14, math.pi, 100]
print(f"Reales: {reales}")

# ℝ⁺ Reales positivos
reales_positivos = [x for x in reales if x > 0]
print(f"Reales positivos: {reales_positivos}")
```

---

## Notación de Funciones

Una **función** se denota así:

```
f: X → Y

Se lee: "f es una función de X a Y"
```

Significa que:
- `f` es el nombre de la función
- `X` es el **dominio** (conjunto de entrada)
- `Y` es el **codominio** (conjunto de salida)
- `→` significa "mapea a" o "transforma a"

### Ejemplos

```
f: ℕ → ℝ        (una función de naturales a reales)
f: ℝ → ℝ⁺       (una función de reales a reales positivos)
f(x) = x²       (especificar qué hace)
f(x) = abs(x)   (valor absoluto)
```

### En Python

```python
# Ejemplo 1: Función simple
def f(x):
    """
    f: ℝ → ℝ
    Mapea cualquier real a su valor absoluto
    """
    return abs(x)

print(f(-5))  # 5
print(f(3.5))  # 3.5

# Ejemplo 2: Función de ℕ → ℝ
def factorial(n):
    """
    f: ℕ → ℝ
    Calcula el factorial de un número natural
    """
    if n < 0:
        raise ValueError("n debe ser natural")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# Ejemplo 3: Función de ℝ → ℝ⁺ (CSAT normalizado)
def normalizar_csat(puntuacion):
    """
    f: ℝ → ℝ⁺
    Transforma CSAT (1-10) a rango (0-1)
    
    Dominio: ℝ (cualquier número real)
    Rango real: (0, 1) (salida solo positivos)
    """
    if puntuacion < 1 or puntuacion > 10:
        raise ValueError("CSAT debe estar entre 1 y 10")
    return (puntuacion - 1) / 9

print(normalizar_csat(5))  # 0.4444...
```

---

## Casos de Uso en Data Science

### Caso de Uso 1: Sumatoria en Estadística (Cálculo de Promedio)

**Contexto:** Necesitas calcular el CSAT promedio de todas las encuestas.

**Fórmula matemática:**
```
        n
       Σ x_i
       i=1
promedio = --------
            n
```

**Interpretación:**
- `Σ x_i` = suma de todos los valores CSAT
- `i=1 hasta n` = desde la primera hasta la última encuesta
- Dividir entre `n` = dividir por cantidad de encuestas

**En código:**

```python
import pandas as pd
import numpy as np

# Dataset CSAT
encuestas = [5, 7, 8, 6, 9, 4, 7, 8]

# Usando sumatoria manual
suma = sum(encuestas)
n = len(encuestas)
promedio_manual = suma / n
print(f"Promedio (manual): {promedio_manual:.2f}")

# Usando NumPy (más eficiente)
promedio_numpy = np.mean(encuestas)
print(f"Promedio (NumPy): {promedio_numpy:.2f}")

# Con Pandas
df = pd.DataFrame({'csat': encuestas})
promedio_pandas = df['csat'].mean()
print(f"Promedio (Pandas): {promedio_pandas:.2f}")

# Escribir en notación matemática
print(f"\nΣ x_i = {suma}")
print(f"n = {n}")
print(f"promedio = {suma}/{n} = {promedio_manual:.2f}")
```

### Caso de Uso 2: Conjuntos en Segmentación de Clientes

**Contexto:** Necesitas identificar:
- Clientes que compraron Y dejaron reseña
- Clientes que NO hicieron compra
- Clientes únicos en múltiples departamentos

**Matemática:**
```
Compradores = {x ∈ clientes | compra_hecha = True}
Reseñadores = {x ∈ clientes | reseña ≠ ∅}
Leales = Compradores ∩ Reseñadores (compra AND reseña)
```

**En código:**

```python
import pandas as pd

df = pd.DataFrame({
    'cliente_id': [1, 2, 3, 4, 5, 6],
    'compra_hecha': [True, False, True, True, False, True],
    'reseña': ['Excelente', None, 'Bueno', 'Excelente', None, 'Malo']
})

# Compradores: {x ∈ clientes | compra = True}
compradores = set(df[df['compra_hecha'] == True]['cliente_id'])
print(f"Compradores (∈ con condición): {compradores}")

# Reseñadores: {x ∈ clientes | reseña ≠ None}
reseñadores = set(df[df['reseña'].notna()]['cliente_id'])
print(f"Reseñadores (≠ None): {reseñadores}")

# Leales = Compradores ∩ Reseñadores
leales = compradores & reseñadores
print(f"Clientes leales (∩): {leales}")

# No compradores = Clientes totales - Compradores
todos = set(df['cliente_id'])
no_compradores = todos - compradores
print(f"No compradores (diferencia): {no_compradores}")

# Clientes problemáticos: compraron pero no reseñaron
problematicos = compradores - reseñadores
print(f"Compradores sin reseña (- diferencia): {problematicos}")
```

### Caso de Uso 3: Notación de Función en Regresión

**Contexto:** Necesitas entender la fórmula de regresión lineal.

**Fórmula matemática:**
```
f: ℝ → ℝ
f(x) = mx + b

Donde:
- x ∈ ℝ (cualquier número real)
- f(x) ∈ ℝ (resultado es número real)
- m = pendiente
- b = intercepto
```

**En código:**

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset: Tiempo de respuesta vs CSAT
datos = pd.DataFrame({
    'tiempo_respuesta': [1, 2, 4, 8, 12, 24],
    'csat_score': [9, 8, 7, 5, 3, 2]
})

# Entrenar modelo
X = datos[['tiempo_respuesta']].values
y = datos['csat_score'].values

modelo = LinearRegression()
modelo.fit(X, y)

# Obtener parámetros
m = modelo.coef_[0]  # pendiente
b = modelo.intercept_  # intercepto

print(f"Función: f(x) = {m:.4f}x + {b:.4f}")
print(f"Dominio: x ∈ ℝ (cualquier tiempo)")
print(f"Rango: f(x) ∈ ℝ (cualquier satisfacción predicha)")

# Predicción (aplicar la función)
tiempo_nuevo = 6
prediccion = modelo.predict([[tiempo_nuevo]])
print(f"\nf({tiempo_nuevo}) = {prediccion[0]:.2f}")

# Visualizar
plt.scatter(X, y, label='Datos reales')
x_line = np.linspace(0, 25, 100)
y_line = m * x_line + b
plt.plot(x_line, y_line, 'r-', label=f'f(x) = {m:.4f}x + {b:.4f}')
plt.xlabel('Tiempo de respuesta (horas)')
plt.ylabel('CSAT Score')
plt.legend()
plt.title('Función de Regresión')
plt.show()
```

---

## Ejercicios Prácticos

### Ejercicio 1: Traducir Notación Matemática a Python [Nivel Básico]

**Enunciado:** Traduce las siguientes expresiones matemáticas a código Python:

1. `a > b ∧ c ≤ 5` (a mayor que b Y c menor o igual a 5)
2. `x ∈ {1,2,3,4,5}` (x pertenece al conjunto)
3. `Σ(i=1 a 10) i²` (sumatoria de cuadrados del 1 al 10)
4. `|A| = 5` (cardinalidad del conjunto A es 5)
5. `A ∩ B ≠ ∅` (intersección de A y B no es vacía)

**Pistas:**
- Para `∧` usa `and` en Python
- Para `∈` usa `in`
- Para `Σ` usa `sum()`
- Para `|A|` usa `len()`
- Para `≠` usa `!=`

<details>
<summary>💡 Ver solución</summary>

```python
# 1. a > b ∧ c ≤ 5
a, b, c = 10, 5, 3
if a > b and c <= 5:
    print("1. Condición verdadera")

# 2. x ∈ {1,2,3,4,5}
x = 3
conjunto = {1, 2, 3, 4, 5}
if x in conjunto:
    print("2. x pertenece al conjunto")

# 3. Σ(i=1 a 10) i²
sumatoria = sum(i**2 for i in range(1, 11))
print(f"3. Sumatoria: {sumatoria}")

# 4. |A| = 5
A = {1, 2, 3, 4, 5}
print(f"4. Cardinalidad de A: {len(A)}")

# 5. A ∩ B ≠ ∅
A = {1, 2, 3}
B = {3, 4, 5}
interseccion = A & B
if interseccion != set():
    print(f"5. Intersección no es vacía: {interseccion}")
```

</details>

---

### Ejercicio 2: Trabajar con Conjuntos [Nivel Básico-Intermedio]

**Enunciado:** Dado dos departamentos con sus clientes satisfechos, realiza operaciones de conjunto:

1. Clientes que están en AMBOS departamentos (∩)
2. Todos los clientes únicos (∪)
3. Clientes solo en Ventas (-)
4. Verificar si uno es subconjunto del otro (⊂)

**Pistas:**
- Usa `&` para ∩
- Usa `|` para ∪
- Usa `-` para diferencia
- Usa `<=` para subconjunto

<details>
<summary>💡 Ver solución</summary>

```python
# Clientes satisfechos por departamento
ventas = {101, 102, 103, 104}
soporte = {103, 104, 105, 106}

print(f"Clientes Ventas: {ventas}")
print(f"Clientes Soporte: {soporte}\n")

# 1. Intersección ∩ (ambos departamentos)
comunes = ventas & soporte
print(f"1. Intersección (∩): {comunes}")

# 2. Unión ∪ (todos únicos)
todos = ventas | soporte
print(f"2. Unión (∪): {todos}")

# 3. Diferencia - (solo Ventas)
solo_ventas = ventas - soporte
print(f"3. Solo Ventas (-): {solo_ventas}")

# 4. Subconjunto ⊂
sub = {101, 102}
es_subconjunto = sub <= ventas
print(f"4. ¿{sub} ⊂ {ventas}? {es_subconjunto}")
```

</details>

---

### Ejercicio 3: Sumatoria y Productoria [Nivel Intermedio]

**Enunciado:** Calcula:
1. Σ(i=1 a 100) i (suma de 1 a 100)
2. Σ(i=1 a 10) 2i (suma de pares hasta 20)
3. Π(i=1 a 5) i (factorial de 5)
4. Σ de CSAT en un dataset

**Pistas:**
- `range(1, 101)` genera del 1 al 100
- `2*i` multiplica por 2
- `math.factorial()` o multiplicar manualmente
- Usar `.sum()` de Pandas

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd
import math

# 1. Σ(i=1 a 100) i
suma_1_a_100 = sum(range(1, 101))
print(f"1. Σ(i=1 a 100) i = {suma_1_a_100}")

# 2. Σ(i=1 a 10) 2i (pares)
suma_pares = sum(2*i for i in range(1, 11))
print(f"2. Σ(i=1 a 10) 2i = {suma_pares}")

# 3. Π(i=1 a 5) i (factorial)
factorial_5 = math.factorial(5)
print(f"3. Π(i=1 a 5) i = {factorial_5}")

# 4. Σ CSAT dataset
df_csat = pd.DataFrame({
    'departamento': ['Ventas', 'Soporte', 'Producto'],
    'csat': [8, 7, 9]
})
suma_csat = df_csat['csat'].sum()
print(f"4. Σ CSAT = {suma_csat}")
```

</details>

---

### Ejercicio 4: Notación de Funciones [Nivel Intermedio-Avanzado]

**Enunciado:** Define una función en notación matemática y luego implementa en Python:

1. `f: ℝ → ℝ` donde `f(x) = 2x + 3`
2. `g: ℝ → ℝ⁺` donde `g(x) = x²`
3. `h: ℕ → ℝ` donde `h(n) = suma de 1 a n`
4. Valida dominios y lanza errores si es necesario

**Pistas:**
- Escribe la notación en docstring
- Validar entrada según el dominio
- Raise ValueError si está fuera de dominio
- Usar type hints

<details>
<summary>💡 Ver solución</summary>

```python
def f(x: float) -> float:
    """
    f: ℝ → ℝ
    f(x) = 2x + 3
    
    Dominio: Cualquier número real
    Rango: Cualquier número real
    """
    return 2*x + 3

def g(x: float) -> float:
    """
    g: ℝ → ℝ⁺ (casi)
    g(x) = x²
    
    Dominio: Cualquier número real
    Rango: Números reales ≥ 0
    """
    return x**2

def h(n: int) -> float:
    """
    h: ℕ → ℝ
    h(n) = 1 + 2 + 3 + ... + n
    
    Dominio: Números naturales (≥ 1)
    Rango: Números reales positivos
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError(f"n debe ser natural (≥ 1), recibido: {n}")
    
    return sum(range(1, n + 1))

# Pruebas
print(f"f(5) = {f(5)}")  # 2*5 + 3 = 13
print(f"g(-3) = {g(-3)}")  # (-3)² = 9
print(f"h(5) = {h(5)}")  # 1+2+3+4+5 = 15

# Validación de dominio
try:
    print(h(-2))  # Fuera de dominio ℕ
except ValueError as e:
    print(f"Error: {e}")
```

</details>

---

### Ejercicio 5: Integración Completa - Análisis de CSAT [Nivel Desafío]

**Enunciado:** Realiza un análisis completo usando notación matemática:

1. Define el conjunto de clientes satisfechos: `C_s = {x ∈ clientes | CSAT(x) > 7}`
2. Define el conjunto de clientes VIP: `C_v = {x ∈ clientes | es_vip = True}`
3. Calcula: Clientes VIP satisfechos: `C_v ∩ C_s`
4. Calcula: Promedio CSAT usando Σ
5. Define una función `f: ℝ → ℝ⁺` que normalice CSAT
6. Documenta todo con notación matemática en los docstrings

**Pistas:**
- Usa set comprehensions para definir conjuntos
- Usa `sum()` para sumatoria
- Define funciones con validación de dominio
- Documenta con notación matemática en docstrings

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd

# Dataset
df = pd.DataFrame({
    'cliente_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'csat': [8, 5, 9, 6, 10, 4, 7, 8],
    'es_vip': [1, 0, 1, 0, 1, 0, 0, 1]
})

print("=" * 70)
print("ANÁLISIS DE CSAT CON NOTACIÓN MATEMÁTICA")
print("=" * 70)

# 1. Conjunto de satisfechos: C_s = {x ∈ clientes | CSAT(x) > 7}
C_s = set(df[df['csat'] > 7]['cliente_id'])
print(f"\n1. Clientes Satisfechos (CSAT > 7):")
print(f"   C_s = {{x ∈ clientes | CSAT(x) > 7}}")
print(f"   C_s = {C_s}")

# 2. Conjunto de VIPs: C_v = {x ∈ clientes | es_vip = 1}
C_v = set(df[df['es_vip'] == 1]['cliente_id'])
print(f"\n2. Clientes VIP:")
print(f"   C_v = {{x ∈ clientes | es_vip = True}}")
print(f"   C_v = {C_v}")

# 3. Intersección: Clientes VIP y Satisfechos
C_vip_satisfechos = C_v & C_s
print(f"\n3. Clientes VIP Satisfechos (C_v ∩ C_s):")
print(f"   C_v ∩ C_s = {C_vip_satisfechos}")

# 4. Promedio CSAT: promedio = Σ(i=1 a n) CSAT_i / n
csat_scores = df['csat'].values
suma_csat = sum(csat_scores)
n_clientes = len(csat_scores)
promedio = suma_csat / n_clientes

print(f"\n4. Promedio CSAT:")
print(f"   promedio = Σ(i=1 a {n_clientes}) CSAT_i / {n_clientes}")
print(f"   promedio = {suma_csat} / {n_clientes}")
print(f"   promedio = {promedio:.2f}")

# 5. Función de normalización: f: ℝ → ℝ⁺
def normalizar_csat(x):
    """
    Función de normalización CSAT
    f: [1, 10] ⊂ ℝ → [0, 1] ⊂ ℝ⁺
    f(x) = (x - 1) / 9
    
    Dominio: Números reales en rango [1, 10]
    Rango: Números reales positivos en [0, 1]
    """
    if x < 1 or x > 10:
        raise ValueError(f"CSAT debe estar en [1, 10], recibido: {x}")
    return (x - 1) / 9

df['csat_normalizado'] = df['csat'].apply(normalizar_csat)

print(f"\n5. Función de Normalización CSAT:")
print(f"   f: [1, 10] ⊂ ℝ → [0, 1] ⊂ ℝ⁺")
print(f"   f(x) = (x - 1) / 9")
print(f"\n   Valores normalizados:")
print(df[['cliente_id', 'csat', 'csat_normalizado']])

print("\n" + "=" * 70)
print("RESUMEN")
print("=" * 70)
print(f"Total clientes: {len(df)}")
print(f"|C_s| = {len(C_s)} (satisfechos)")
print(f"|C_v| = {len(C_v)} (VIPs)")
print(f"|C_v ∩ C_s| = {len(C_vip_satisfechos)} (VIPs satisfechos)")
print(f"Promedio CSAT global: {promedio:.2f}")
```

**Salida esperada:**
```
=======================================================================
ANÁLISIS DE CSAT CON NOTACIÓN MATEMÁTICA
=======================================================================

1. Clientes Satisfechos (CSAT > 7):
   C_s = {x ∈ clientes | CSAT(x) > 7}
   C_s = {1, 3, 4, 7, 8}

2. Clientes VIP:
   C_v = {x ∈ clientes | es_vip = True}
   C_v = {1, 3, 5, 8}

3. Clientes VIP Satisfechos (C_v ∩ C_s):
   C_v ∩ C_s = {1, 3, 8}

4. Promedio CSAT:
   promedio = Σ(i=1 a 8) CSAT_i / 8
   promedio = 57 / 8
   promedio = 7.12

5. Función de Normalización CSAT:
   f: [1, 10] ⊂ ℝ → [0, 1] ⊂ ℝ⁺
   f(x) = (x - 1) / 9
   ...
```

</details>

---

## Recursos Adicionales

- **PDF de Símbolos Matemáticos**: Archivo adjunto en el proyecto
- **Documentación oficial**:
  - [Python set operations](https://docs.python.org/3/tutorial/datastructures.html#sets)
  - [NumPy Sum/Product](https://numpy.org/doc/stable/reference/routines.math.html)
- **Archivos relacionados**:
  - `02_tipos_variables_datasciense.md`
  - `10_funciones_matematicas_ds_ia.md`
- **Próximos temas**:
  - Estadística (uso intensivo de Σ)
  - Probabilidad (uso de conjuntos)
  - Cálculo (notación de límites)

---

**Actualizado:** 30 de octubre de 2025  
**Progreso de la ruta:** 42% completado (8/19 cursos)  
**Estado:** Completado ✅