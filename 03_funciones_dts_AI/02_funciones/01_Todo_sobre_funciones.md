# Funciones Algebraicas y Trascendentes para Data Science

**Curso:** Programando Funciones - Sección "Todo Sobre Funciones"  
**Fecha:** 30 de octubre de 2025  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto General](#concepto-general)
2. [Funciones Algebraicas](#funciones-algebraicas)
3. [Funciones Trascendentes](#funciones-trascendentes)
4. [Manipulación de Funciones](#manipulación-de-funciones)
5. [Funciones Compuestas](#funciones-compuestas)
6. [Casos de Uso en Data Science](#casos-de-uso-en-data-science)
7. [Ejercicios Prácticos](#ejercicios-prácticos)
8. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto General

Una **función** es una relación matemática que transforma una entrada (x) en una salida (y).

**En Data Science, las funciones son:**
- Modelos que transforman datos
- Relaciones entre variables
- Patrones que buscamos descubrir
- Herramientas para predicción

Aprender los **tipos de funciones** es como aprender anatomía antes de ser cirujano. Necesitas saber qué tipo de "forma" tiene tu relación de datos para elegir el algoritmo correcto.

---

## Funciones Algebraicas

Las funciones **algebraicas** son aquellas que se pueden expresar usando operaciones algebraicas (suma, resta, multiplicación, división, raíces).

### 1. Función Lineal

**Forma:** `f(x) = mx + b`

**Donde:**
- `m` = pendiente (slope)
- `b` = intercepto (donde cruza el eje Y)
- **Dominio:** ℝ (todos los reales)
- **Rango:** ℝ (todos los reales)

**Pendiente:**
```
m = (y₂ - y₁) / (x₂ - x₁)
```

**Característica:** Es una línea recta.

**En Python:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Parámetros
m = 2      # pendiente
b = 5      # intercepto
N = 100

# Función
def f(x):
    return m * x + b

# Dominio
x = np.linspace(-10, 10, num=N)

# Aplicar función
y = f(x)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2, label=f'f(x) = {m}x + {b}')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='r', linewidth=0.5)
plt.axvline(x=0, color='r', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Función Lineal')
plt.show()
```

**Interpretación:**
- Si `m > 0`: línea sube (relación positiva)
- Si `m < 0`: línea baja (relación negativa)
- Si `m = 0`: línea horizontal (sin relación)

---

### 2. Funciones Polinómicas

**Forma:** 
```
P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₂x² + a₁x + a₀
```

**Donde:**
- `n` = grado del polinomio (potencia más alta)
- `aᵢ` = coeficientes (números reales)
- **Dominio:** ℝ
- **Rango:** Depende del grado

**Ejemplos:**

| Función | Grado | Dominio | Rango |
|---------|-------|---------|-------|
| `f(x) = 3x² - 2x + 1` | 2 | ℝ | [y_min, ∞) |
| `f(x) = x³ + 2x` | 3 | ℝ | ℝ |
| `f(x) = 2x⁴ - x² + 5` | 4 | ℝ | [y_min, ∞) |

**Grado 2 (Cuadrática):**

```python
def f(x):
    return 2*x**2 - x + 3

x = np.linspace(-5, 5, num=1000)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='r', linewidth=0.5)
plt.axvline(x=0, color='r', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función Cuadrática: f(x) = 2x² - x + 3')
plt.show()
```

**Grado 7 (Como en tu notebook):**

```python
def f(x):
    return (2*x**5) - (x**4) + (3*x**2) + 4

x = np.linspace(-10, 10, num=1000)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2)
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función Polinómica: f(x) = 2x⁵ - x⁴ + 3x² + 4')
plt.show()
```

### 3. Funciones Potencia

**Forma:** `f(x) = xᵃ` donde `a ∈ ℝ`

**Casos especiales:**

| Función | Dominio | Rango | Forma |
|---------|---------|-------|-------|
| `f(x) = x²` | ℝ | [0, ∞) | Parábola |
| `f(x) = x³` | ℝ | ℝ | Cúbica |
| `f(x) = √x` | [0, ∞) | [0, ∞) | Raíz |
| `f(x) = 1/x` | ℝ \ {0} | ℝ \ {0} | Hipérbola |

**En Python:**

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

x_pos = np.linspace(0.1, 10, num=1000)
x_all = np.linspace(-10, 10, num=1000)

# x²
axes[0, 0].plot(x_all, x_all**2)
axes[0, 0].set_title('f(x) = x²')
axes[0, 0].grid(True, alpha=0.3)

# x³
axes[0, 1].plot(x_all, x_all**3)
axes[0, 1].set_title('f(x) = x³')
axes[0, 1].grid(True, alpha=0.3)

# √x
axes[1, 0].plot(x_pos, np.sqrt(x_pos))
axes[1, 0].set_title('f(x) = √x')
axes[1, 0].grid(True, alpha=0.3)

# 1/x
x_nonzero = np.linspace(-10, 10, num=1000)
x_nonzero = x_nonzero[x_nonzero != 0]
axes[1, 1].plot(x_nonzero, 1/x_nonzero)
axes[1, 1].set_title('f(x) = 1/x')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Funciones Trascendentes

Las funciones **trascendentes** NO se pueden expresar con operaciones algebraicas simples. Son funciones "especiales".

### 1. Funciones Trigonométricas

**Principales:** `sin(x)`, `cos(x)`, `tan(x)`

**Características:**
- **Periódicas:** Se repiten cada cierto intervalo
- **Dominio:** ℝ (generalmente)
- **Rango:** Limitado (ej: sin y cos están entre -1 y 1)

**En Python:**

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

x = np.linspace(-2*np.pi, 2*np.pi, num=1000)

# sin(x)
axes[0].plot(x, np.sin(x), label='sin(x)')
axes[0].set_title('Función Seno')
axes[0].grid(True, alpha=0.3)
axes[0].set_ylim(-1.5, 1.5)
axes[0].axhline(y=0, color='r', linewidth=0.5)

# cos(x)
axes[1].plot(x, np.cos(x), label='cos(x)', color='orange')
axes[1].set_title('Función Coseno')
axes[1].grid(True, alpha=0.3)
axes[1].set_ylim(-1.5, 1.5)
axes[1].axhline(y=0, color='r', linewidth=0.5)

# tan(x) - cuidado con discontinuidades
x_tan = x[~np.isinf(np.tan(x))]
axes[2].plot(x_tan, np.tan(x_tan), label='tan(x)', color='green')
axes[2].set_title('Función Tangente')
axes[2].grid(True, alpha=0.3)
axes[2].axhline(y=0, color='r', linewidth=0.5)

plt.tight_layout()
plt.show()
```

### 2. Función Exponencial

**Forma:** `f(x) = aˣ` donde `a > 0`

**Caso especial:** `f(x) = eˣ` (base e, número de Euler ≈ 2.718)

**Características:**
- **Crecimiento rápido:** Aumenta exponencialmente
- **Dominio:** ℝ
- **Rango:** (0, ∞)
- **Siempre positiva:** Nunca toca x (asíntota horizontal)

**Aplicaciones en Data Science:**
- Decaimiento radioactivo
- Crecimiento de epidemias
- Tasa de interés compuesto
- Redes neuronales (activación)

**En Python:**

```python
x = np.linspace(-5, 5, num=1000)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# e^x
y_exp = np.exp(x)
axes[0].plot(x, y_exp, linewidth=2, color='blue')
axes[0].set_title('f(x) = eˣ')
axes[0].set_ylim(-5, 150)
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=0, color='r', linewidth=0.5)

# 2^x
y_2x = 2**x
axes[1].plot(x, y_2x, linewidth=2, color='green')
axes[1].set_title('f(x) = 2ˣ')
axes[1].set_ylim(-5, 35)
axes[1].grid(True, alpha=0.3)
axes[1].axhline(y=0, color='r', linewidth=0.5)

plt.tight_layout()
plt.show()
```

### 3. Función Logarítmica

**Forma:** `logᵦ(x) = n ⟺ x = bⁿ`

**Donde:**
- `b` = base
- `n` = exponente (resultado del logaritmo)
- `x` = argumento

**Relación inversa:** Logaritmo es la inversa de exponencial.

**Ejemplos:**
- `log₂(8) = 3` porque `2³ = 8`
- `log₁₀(100) = 2` porque `10² = 100`
- `ln(e) = 1` porque `e¹ = e`

**Características:**
- **Crecimiento lento:** Aumenta pero cada vez más despacio
- **Dominio:** (0, ∞) [solo números positivos]
- **Rango:** ℝ
- **Asíntota vertical:** En x = 0

**Aplicaciones en Data Science:**
- Regularización en ML (log-likelihood)
- Transformación de datos (log-scale para skewed data)
- Entropía en información (información = -log(p))

**En Python:**

```python
x = np.linspace(0.001, 256, num=1000)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# log₂(x)
axes[0].plot(x, np.log2(x), linewidth=2, color='blue')
axes[0].set_title('f(x) = log₂(x)')
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=0, color='r', linewidth=0.5)

# log₁₀(x) - logaritmo natural
axes[1].plot(x, np.log10(x), linewidth=2, color='green')
axes[1].set_title('f(x) = log₁₀(x)')
axes[1].grid(True, alpha=0.3)
axes[1].axhline(y=0, color='r', linewidth=0.5)

# ln(x) - logaritmo natural
axes[2].plot(x, np.log(x), linewidth=2, color='orange')
axes[2].set_title('f(x) = ln(x)')
axes[2].grid(True, alpha=0.3)
axes[2].axhline(y=0, color='r', linewidth=0.5)

plt.tight_layout()
plt.show()
```

---

## Manipulación de Funciones

Una habilidad **crítica** en Data Science es transformar gráficos sin recalcular toda la función.

### Desplazamientos Verticales

Sea `c > 0`:

| Transformación | Efecto |
|----------------|--------|
| `y = f(x) + c` | Desplaza UP `c` unidades |
| `y = f(x) - c` | Desplaza DOWN `c` unidades |

**Ejemplo:**

```python
def f(x):
    return x**2

x = np.linspace(-10, 10, num=1000)
c = 4

plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label='f(x) = x²', linewidth=2)
plt.plot(x, f(x) + c, label=f'f(x) + {c}', linewidth=2, linestyle='--')
plt.plot(x, f(x) - c, label=f'f(x) - {c}', linewidth=2, linestyle='--')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='r', linewidth=0.5)
plt.axvline(x=0, color='r', linewidth=0.5)
plt.legend()
plt.title('Desplazamientos Verticales')
plt.show()
```

### Desplazamientos Horizontales

Sea `c > 0`:

| Transformación | Efecto |
|----------------|--------|
| `y = f(x - c)` | Desplaza RIGHT `c` unidades |
| `y = f(x + c)` | Desplaza LEFT `c` unidades |

**Nota:** Es INVERSO porque afecta la entrada.

**Ejemplo:**

```python
def f(x):
    return x**2

x = np.linspace(-15, 15, num=1000)
c = 4

plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label='f(x) = x²', linewidth=2)
plt.plot(x, f(x - c), label=f'f(x - {c}) [RIGHT]', linewidth=2, linestyle='--')
plt.plot(x, f(x + c), label=f'f(x + {c}) [LEFT]', linewidth=2, linestyle='--')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='r', linewidth=0.5)
plt.axvline(x=0, color='r', linewidth=0.5)
plt.legend()
plt.title('Desplazamientos Horizontales')
plt.show()
```

### Alargamientos y Compresiones

Sea `c > 0`:

| Transformación | Efecto |
|----------------|--------|
| `y = c · f(x)` | ESTIRA verticalmente por factor `c` |
| `y = f(x) / c` | COMPRIME verticalmente por factor `c` |
| `y = f(c · x)` | COMPRIME horizontalmente por factor `c` |
| `y = f(x / c)` | ESTIRA horizontalmente por factor `c` |

**Ejemplo:**

```python
def f(x):
    return np.sin(x)

x = np.linspace(-15, 15, num=1000)
c = 2

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Vertical
axes[0].plot(x, f(x), label='f(x) = sin(x)', linewidth=2)
axes[0].plot(x, c * f(x), label=f'{c}·f(x) [ESTIRA]', linewidth=2, linestyle='--')
axes[0].plot(x, f(x) / c, label=f'f(x)/{c} [COMPRIME]', linewidth=2, linestyle='--')
axes[0].set_title('Transformaciones Verticales')
axes[0].grid(True, alpha=0.3)
axes[0].legend()

# Horizontal
axes[1].plot(x, f(x), label='f(x) = sin(x)', linewidth=2)
axes[1].plot(x, f(c * x), label=f'f({c}·x) [COMPRIME]', linewidth=2, linestyle='--')
axes[1].plot(x, f(x / c), label=f'f(x/{c}) [ESTIRA]', linewidth=2, linestyle='--')
axes[1].set_title('Transformaciones Horizontales')
axes[1].grid(True, alpha=0.3)
axes[1].legend()

plt.tight_layout()
plt.show()
```

### Reflexiones

| Transformación | Efecto |
|----------------|--------|
| `y = -f(x)` | Refleja respecto al EJE X |
| `y = f(-x)` | Refleja respecto al EJE Y |

**Ejemplo:**

```python
def f(x):
    return x**3

x = np.linspace(-10, 10, num=1000)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Reflexión eje X
axes[0].plot(x, f(x), label='f(x) = x³', linewidth=2)
axes[0].plot(x, -f(x), label='-f(x) [REFLEJA EJE X]', linewidth=2, linestyle='--')
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=0, color='r', linewidth=0.5)
axes[0].axvline(x=0, color='r', linewidth=0.5)
axes[0].legend()

# Reflexión eje Y
axes[1].plot(x, f(x), label='f(x) = x³', linewidth=2)
axes[1].plot(x, f(-x), label='f(-x) [REFLEJA EJE Y]', linewidth=2, linestyle='--')
axes[1].grid(True, alpha=0.3)
axes[1].axhline(y=0, color='r', linewidth=0.5)
axes[1].axvline(x=0, color='r', linewidth=0.5)
axes[1].legend()

plt.tight_layout()
plt.show()
```

---

## Funciones Compuestas

Una **función compuesta** es cuando aplicas una función al resultado de otra.

**Notación:** `(f ∘ g)(x) = f(g(x))`

**Lectura:** "f compuesta con g"

**Proceso:** 
1. Calcula `g(x)`
2. Usa ese resultado como entrada de `f`

**Ejemplo:**

```python
def g(x):
    """Función interna"""
    return x**2

def f(x):
    """Función externa"""
    return np.sin(x)

x = np.linspace(-10, 10, num=1000)

# Función compuesta: (f ∘ g)(x) = f(g(x)) = sin(x²)
f_o_g = f(g(x))

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# g(x)
axes[0].plot(x, g(x), linewidth=2)
axes[0].set_title('g(x) = x²')
axes[0].grid(True, alpha=0.3)

# f(x)
axes[1].plot(x, f(x), linewidth=2)
axes[1].set_title('f(x) = sin(x)')
axes[1].grid(True, alpha=0.3)

# Composición f(g(x))
axes[2].plot(x, f_o_g, linewidth=2)
axes[2].set_title('(f ∘ g)(x) = sin(x²)')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Casos de Uso en Data Science

### Caso de Uso 1: Regresión Lineal vs Polinómica

**Contexto:** Predecir CSAT basado en Tiempo de Respuesta.

**Pregunta:** ¿Es la relación lineal o más compleja?

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Dataset
datos = pd.DataFrame({
    'tiempo_h': [0.5, 1, 2, 4, 8, 12, 24, 36],
    'csat': [9, 8.5, 8, 6, 4, 2.5, 1.5, 1]
})

X = datos[['tiempo_h']].values
y = datos['csat'].values

# Modelo Lineal
modelo_lin = LinearRegression()
modelo_lin.fit(X, y)

# Modelo Polinómico (grado 2)
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)
modelo_poly = LinearRegression()
modelo_poly.fit(X_poly, y)

# Predicciones
x_plot = np.linspace(0, 40, num=100).reshape(-1, 1)
y_lin = modelo_lin.predict(x_plot)
y_poly = modelo_poly.predict(poly_features.transform(x_plot))

# Visualización
plt.figure(figsize=(12, 6))
plt.scatter(datos['tiempo_h'], datos['csat'], s=100, label='Datos reales', color='red')
plt.plot(x_plot, y_lin, linewidth=2, label='Lineal: f(x) = mx + b')
plt.plot(x_plot, y_poly, linewidth=2, label='Polinómica: f(x) = ax² + bx + c')
plt.xlabel('Tiempo de Respuesta (horas)')
plt.ylabel('CSAT')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('Regresión: ¿Lineal o Polinómica?')
plt.show()
```

### Caso de Uso 2: Transformación Logarítmica para Datos Sesgados

**Contexto:** Los ingresos de los clientes tienen distribución muy sesgada (algunos muy ricos, muchos pobres).

**Solución:** Aplicar transformación logarítmica.

```python
# Datos sesgados (inclinados a la derecha)
ingresos = np.random.exponential(scale=30000, size=1000)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Original
axes[0].hist(ingresos, bins=50, color='blue', edgecolor='black')
axes[0].set_title('Ingresos Originales (Sesgados)')
axes[0].set_xlabel('Ingreso ($)')

# Logaritmo
ingresos_log = np.log(ingresos)
axes[1].hist(ingresos_log, bins=50, color='green', edgecolor='black')
axes[1].set_title('log(Ingresos) (Más Normal)')
axes[1].set_xlabel('log(Ingreso)')

# Comparación visual
x_plot = np.linspace(100, 200000, num=1000)
axes[2].plot(x_plot, np.log(x_plot), linewidth=2, label='f(x) = log(x)')
axes[2].set_title('Función Logaritmo')
axes[2].set_xlabel('Ingreso Original ($)')
axes[2].set_ylabel('log(Ingreso)')
axes[2].grid(True, alpha=0.3)
axes[2].legend()

plt.tight_layout()
plt.show()

print(f"Skewness original: {pd.Series(ingresos).skew():.3f}")
print(f"Skewness después de log: {pd.Series(ingresos_log).skew():.3f}")
```

### Caso de Uso 3: Función Sigmoide en Redes Neuronales

**Contexto:** Predicción de probabilidad binaria (¿Cliente comprará sí/no?).

**Solución:** Usar función sigmoide `σ(x) = 1 / (1 + e^(-x))`

```python
def sigmoid(x):
    """Función sigmoide"""
    return 1 / (1 + np.exp(-x))

x = np.linspace(-8, 8, num=1000)
y = sigmoid(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=3, color='purple')
plt.axhline(y=0.5, color='r', linestyle='--', label='Decisión threshold (0.5)')
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
plt.fill_between(x, 0, y, alpha=0.2)
plt.xlabel('Score del Modelo')
plt.ylabel('Probabilidad')
plt.title('Función Sigmoide: Convierte Score a Probabilidad')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Interpretación
print("Ejemplos de predicción:")
for score in [-5, -2, 0, 2, 5]:
    prob = sigmoid(score)
    decision = "COMPRA" if prob > 0.5 else "NO COMPRA"
    print(f"Score {score:>2} → Probabilidad {prob:.4f} → {decision}")
```

---

## Ejercicios Prácticos

### Ejercicio 1: Identificar Tipo de Función [Nivel Básico]

**Enunciado:** Dada cada gráfica o descripción, identifica si es Lineal, Polinómica, Exponencial, Logarítmica o Trigonométrica:

1. Una línea recta que sube
2. Una parábola
3. Crece rápido al inicio, luego se estabiliza
4. Oscila entre -1 y 1
5. Decrece lentamente

**Pistas:**
- Lineal: línea recta
- Polinómica: curva suave
- Exponencial: crece muy rápido
- Logarítmica: crece pero cada vez más lento
- Trigonométrica: oscila

<details>
<summary>💡 Ver solución</summary>

```python
# 1. Línea recta que sube → LINEAL
# 2. Parábola → POLINÓMICA (grado 2)
# 3. Crece rápido, luego se estabiliza → EXPONENCIAL
# 4. Oscila entre -1 y 1 → TRIGONOMÉTRICA
# 5. Decrece lentamente → LOGARÍTMICA

# Verificar visualmente
x = np.linspace(0.1, 10, num=1000)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 1. Lineal
axes[0, 0].plot(x, 2*x + 1)
axes[0, 0].set_title('1. LINEAL: f(x) = 2x + 1')

# 2. Polinómica cuadrática
axes[0, 1].plot(x, x**2)
axes[0, 1].set_title('2. POLINÓMICA: f(x) = x²')

# 3. Exponencial
axes[0, 2].plot(x, np.exp(x/3))
axes[0, 2].set_title('3. EXPONENCIAL: f(x) = e^(x/3)')
axes[0, 2].set_ylim(0, 50)

# 4. Trigonométrica
axes[1, 0].plot(x, np.sin(x))
axes[1, 0].set_title('4. TRIGONOMÉTRICA: f(x) = sin(x)')

# 5. Logarítmica
axes[1, 1].plot(x, np.log(x))
axes[1, 1].set_title('5. LOGARÍTMICA: f(x) = log(x)')

plt.tight_layout()
plt.show()
```

</details>

---

### Ejercicio 2: Aplicar Transformaciones [Nivel Básico-Intermedio]

**Enunciado:** Partiendo de `f(x) = x²`, aplica:
1. Desplazamiento UP 3 unidades
2. Desplazamiento RIGHT 2 unidades
3. Estiramiento vertical por factor 2
4. Reflexión respecto al eje X

**Pistas:**
- UP: suma a la función
- RIGHT: resta del argumento
- Estiramiento vertical: multiplica por constante
- Reflexión eje X: multiplica función por -1

<details>
<summary>💡 Ver solución</summary>

```python
def f(x):
    return x**2

x = np.linspace(-10, 10, num=1000)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Original
axes[0, 0].plot(x, f(x), linewidth=2, label='f(x) = x²')
axes[0, 0].set_title('Original: f(x) = x²')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].legend()

# 1. UP 3
axes[0, 1].plot(x, f(x) + 3, linewidth=2, label='f(x) + 3')
axes[0, 1].set_title('1. UP 3: f(x) + 3 = x² + 3')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].legend()

# 2. RIGHT 2
axes[0, 2].plot(x, f(x - 2), linewidth=2, label='f(x - 2)')
axes[0, 2].set_title('2. RIGHT 2: f(x - 2) = (x - 2)²')
axes[0, 2].grid(True, alpha=0.3)
axes[0, 2].legend()

# 3. Estiramiento vertical 2
axes[1, 0].plot(x, 2 * f(x), linewidth=2, label='2·f(x)')
axes[1, 0].set_title('3. Estiramiento 2: 2·f(x) = 2x²')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].legend()

# 4. Reflexión eje X
axes[1, 1].plot(x, -f(x), linewidth=2, label='-f(x)')
axes[1, 1].set_title('4. Reflexión eje X: -f(x) = -x²')
axes[1, 1].grid(True, alpha=0.3)
axes[1, 1].legend()

# Todos combinados
axes[1, 2].plot(x, f(x), linewidth=2, alpha=0.5, label='Original')
axes[1, 2].plot(x, f(x) + 3, linewidth=2, label='+3')
axes[1, 2].plot(x, f(x - 2), linewidth=2, label='RIGHT 2')
axes[1, 2].plot(x, 2*f(x), linewidth=2, label='×2')
axes[1, 2].plot(x, -f(x), linewidth=2, label='-f(x)')
axes[1, 2].set_title('Todas las transformaciones')
axes[1, 2].grid(True, alpha=0.3)
axes[1, 2].legend()

plt.tight_layout()
plt.show()
```

</details>

---

### Ejercicio 3: Funciones Compuestas [Nivel Intermedio]

**Enunciado:** Dadas `g(x) = x² + 1` y `f(x) = sin(x)`, calcula:
1. `(f ∘ g)(x) = f(g(x))`
2. `(g ∘ f)(x) = g(f(x))`
3. ¿Son iguales?

**Pistas:**
- Primero calcula la función interna
- Usa ese resultado en la externa
- La composición NO es conmutativa (orden importa)

<details>
<summary>💡 Ver solución</summary>

```python
def f(x):
    """f(x) = sin(x)"""
    return np.sin(x)

def g(x):
    """g(x) = x² + 1"""
    return x**2 + 1

x = np.linspace(-np.pi, np.pi, num=1000)

# Composiciones
f_o_g = f(g(x))  # sin(x² + 1)
g_o_f = g(f(x))  # (sin(x))² + 1

# Verificar si son iguales
son_iguales = np.allclose(f_o_g, g_o_f)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# g(x)
axes[0, 0].plot(x, g(x), linewidth=2)
axes[0, 0].set_title('g(x) = x² + 1')
axes[0, 0].grid(True, alpha=0.3)

# f(x)
axes[0, 1].plot(x, f(x), linewidth=2)
axes[0, 1].set_title('f(x) = sin(x)')
axes[0, 1].grid(True, alpha=0.3)

# f(g(x)) = sin(x² + 1)
axes[1, 0].plot(x, f_o_g, linewidth=2, color='purple')
axes[1, 0].set_title('(f ∘ g)(x) = sin(x² + 1)')
axes[1, 0].grid(True, alpha=0.3)

# g(f(x)) = (sin(x))² + 1
axes[1, 1].plot(x, g_o_f, linewidth=2, color='orange')
axes[1, 1].set_title('(g ∘ f)(x) = (sin(x))² + 1')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"¿(f ∘ g)(x) = (g ∘ f)(x)? {son_iguales}")
print(f"Conclusión: La composición de funciones NO ES CONMUTATIVA")
```

</details>

---

### Ejercicio 4: Modelado de Datos Reales [Nivel Intermedio-Avanzado]

**Enunciado:** Tienes datos de clientes:
- `x` = meses como cliente
- `y` = dinero gastado acumulado

¿Qué tipo de función se ajusta mejor? ¿Lineal o Exponencial?

**Pistas:**
- Genera datos sintéticos que sigan patrón exponencial
- Prueba modelo lineal
- Prueba modelo exponencial
- Compara con R²

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

# Generar datos con patrón exponencial (clientes que gastan cada vez más)
np.random.seed(42)
meses = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
gastos = np.array([100, 120, 150, 200, 280, 350, 500, 650, 800, 1000])
gastos += np.random.normal(0, 20, len(gastos))  # Agregar ruido

# Modelo Lineal: y = mx + b
def lineal(x, m, b):
    return m * x + b

params_lin, _ = curve_fit(lineal, meses, gastos)
y_pred_lin = lineal(meses, *params_lin)

# Modelo Exponencial: y = a·e^(bx)
def exponencial(x, a, b):
    return a * np.exp(b * x)

params_exp, _ = curve_fit(exponencial, meses, gastos, p0=[100, 0.1])
y_pred_exp = exponencial(meses, *params_exp)

# Comparar
r2_lin = r2_score(gastos, y_pred_lin)
r2_exp = r2_score(gastos, y_pred_exp)

# Visualización
meses_plot = np.linspace(1, 10, num=100)
y_lin_plot = lineal(meses_plot, *params_lin)
y_exp_plot = exponencial(meses_plot, *params_exp)

plt.figure(figsize=(12, 6))
plt.scatter(meses, gastos, s=100, color='red', label='Datos reales', zorder=5)
plt.plot(meses_plot, y_lin_plot, linewidth=2, label=f'Lineal (R²={r2_lin:.4f})')
plt.plot(meses_plot, y_exp_plot, linewidth=2, label=f'Exponencial (R²={r2_exp:.4f})')
plt.xlabel('Meses como Cliente')
plt.ylabel('Gasto Acumulado ($)')
plt.title('¿Qué modelo se ajusta mejor?')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

print(f"R² Lineal: {r2_lin:.4f}")
print(f"R² Exponencial: {r2_exp:.4f}")
print(f"\n✓ El modelo MEJOR es: {'Exponencial' if r2_exp > r2_lin else 'Lineal'}")
```

</details>

---

### Ejercicio 5: Análisis Completo - CSAT Real [Nivel Desafío]

**Enunciado:** Análisis completo usando funciones:

1. Ajusta datos CSAT vs Tiempo de Respuesta a diferentes modelos (lineal, polinómico, exponencial)
2. Determina cuál se ajusta mejor
3. Usa ese modelo para predecir CSAT para 15 horas
4. Aplica transformaciones si es necesario
5. Visualiza todo

**Pistas:**
- Crear dataset CSAT realista
- Probar múltiples modelos
- Comparar R²
- Transformar funciones

<details>
<summary>💡 Ver solución</summary>

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Dataset CSAT vs Tiempo de Respuesta
datos = pd.DataFrame({
    'tiempo_h': [0.5, 1, 2, 3, 5, 8, 12, 18, 24, 30],
    'csat': [9.5, 9, 8.5, 8, 7, 5.5, 4, 2.5, 1.5, 0.5]
})

X = datos[['tiempo_h']].values.ravel()
y = datos['csat'].values

print("=" * 80)
print("ANÁLISIS DE MODELOS PARA CSAT")
print("=" * 80)

# 1. MODELO LINEAL
modelo_lin = LinearRegression()
modelo_lin.fit(X.reshape(-1, 1), y)
y_pred_lin = modelo_lin.predict(X.reshape(-1, 1))
r2_lin = r2_score(y, y_pred_lin)
rmse_lin = np.sqrt(mean_squared_error(y, y_pred_lin))

print(f"\n1. LINEAL: f(x) = {modelo_lin.coef_[0]:.4f}x + {modelo_lin.intercept_:.4f}")
print(f"   R² = {r2_lin:.4f}")
print(f"   RMSE = {rmse_lin:.4f}")

# 2. MODELO POLINÓMICO (grado 2)
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X.reshape(-1, 1))
modelo_poly = LinearRegression()
modelo_poly.fit(X_poly, y)
y_pred_poly = modelo_poly.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)
rmse_poly = np.sqrt(mean_squared_error(y, y_pred_poly))

print(f"\n2. POLINÓMICO (grado 2)")
print(f"   R² = {r2_poly:.4f}")
print(f"   RMSE = {rmse_poly:.4f}")

# 3. MODELO EXPONENCIAL
def exponencial_decay(x, a, b):
    return a * np.exp(-b * x) + 0.5

try:
    params_exp, _ = curve_fit(exponencial_decay, X, y, p0=[9, 0.1], maxfev=10000)
    y_pred_exp = exponencial_decay(X, *params_exp)
    r2_exp = r2_score(y, y_pred_exp)
    rmse_exp = np.sqrt(mean_squared_error(y, y_pred_exp))
    
    print(f"\n3. EXPONENCIAL: f(x) = {params_exp[0]:.4f}·e^(-{params_exp[1]:.4f}·x) + 0.5")
    print(f"   R² = {r2_exp:.4f}")
    print(f"   RMSE = {rmse_exp:.4f}")
except:
    r2_exp = -1
    print("\n3. EXPONENCIAL: Error al ajustar")

# 4. MODELO LOGARÍTMICO INVERSO
def log_decay(x, a, b):
    return a - b * np.log(x + 1)

try:
    params_log, _ = curve_fit(log_decay, X, y, p0=[9, 3], maxfev=10000)
    y_pred_log = log_decay(X, *params_log)
    r2_log = r2_score(y, y_pred_log)
    rmse_log = np.sqrt(mean_squared_error(y, y_pred_log))
    
    print(f"\n4. LOGARÍTMICO: f(x) = {params_log[0]:.4f} - {params_log[1]:.4f}·log(x+1)")
    print(f"   R² = {r2_log:.4f}")
    print(f"   RMSE = {rmse_log:.4f}")
except:
    r2_log = -1
    print("\n4. LOGARÍTMICO: Error al ajustar")

# Determinar mejor modelo
modelos = {
    'Lineal': r2_lin,
    'Polinómico': r2_poly,
    'Exponencial': r2_exp if r2_exp > -1 else 0,
    'Logarítmico': r2_log if r2_log > -1 else 0
}

mejor_modelo = max(modelos, key=modelos.get)
print(f"\n{'=' * 80}")
print(f"✓ MEJOR MODELO: {mejor_modelo} (R² = {modelos[mejor_modelo]:.4f})")
print(f"{'=' * 80}")

# Predicción para 15 horas
tiempo_pred = 15

if mejor_modelo == 'Lineal':
    csat_pred = modelo_lin.predict([[tiempo_pred]])[0]
    label = f"Lineal: f(x) = {modelo_lin.coef_[0]:.4f}x + {modelo_lin.intercept_:.4f}"
elif mejor_modelo == 'Polinómico':
    csat_pred = modelo_poly.predict(poly_features.transform([[tiempo_pred]]))[0]
    label = "Polinómico (grado 2)"
elif mejor_modelo == 'Exponencial':
    csat_pred = exponencial_decay(tiempo_pred, *params_exp)
    label = f"Exponencial"
else:
    csat_pred = log_decay(tiempo_pred, *params_log)
    label = f"Logarítmico"

print(f"\nPREDICCIÓN para {tiempo_pred} horas:")
print(f"CSAT predicho = {csat_pred:.2f} ({label})")

# VISUALIZACIÓN
x_plot = np.linspace(0.1, 35, num=500)

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Todos los modelos
ax = axes[0, 0]
ax.scatter(datos['tiempo_h'], datos['csat'], s=100, color='red', label='Datos reales', zorder=5)
ax.plot(x_plot, modelo_lin.predict(x_plot.reshape(-1, 1)), linewidth=2, label='Lineal', alpha=0.7)
X_poly_plot = poly_features.transform(x_plot.reshape(-1, 1))
ax.plot(x_plot, modelo_poly.predict(X_poly_plot), linewidth=2, label='Polinómico', alpha=0.7)
if r2_exp > -1:
    ax.plot(x_plot, exponencial_decay(x_plot, *params_exp), linewidth=2, label='Exponencial', alpha=0.7)
if r2_log > -1:
    ax.plot(x_plot, log_decay(x_plot, *params_log), linewidth=2, label='Logarítmico', alpha=0.7)
ax.scatter([tiempo_pred], [csat_pred], s=200, color='green', marker='*', label=f'Predicción: {csat_pred:.2f}', zorder=10)
ax.set_xlabel('Tiempo de Respuesta (horas)')
ax.set_ylabel('CSAT')
ax.set_title('Comparación de Modelos')
ax.legend()
ax.grid(True, alpha=0.3)

# Residuos - Lineal
ax = axes[0, 1]
residuos_lin = y - y_pred_lin
ax.scatter(X, residuos_lin, s=80, alpha=0.7)
ax.axhline(y=0, color='r', linestyle='--')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Residuos')
ax.set_title(f'Residuos Lineal (R²={r2_lin:.4f})')
ax.grid(True, alpha=0.3)

# R² Comparison
ax = axes[1, 0]
modelos_names = list(modelos.keys())
r2_values = list(modelos.values())
colors = ['green' if m == mejor_modelo else 'blue' for m in modelos_names]
ax.bar(modelos_names, r2_values, color=colors, alpha=0.7)
ax.set_ylabel('R²')
ax.set_title('Comparación de R² por Modelo')
ax.set_ylim(0, 1.1)
for i, v in enumerate(r2_values):
    ax.text(i, v + 0.02, f'{v:.3f}', ha='center')
ax.grid(True, alpha=0.3, axis='y')

# Mejor modelo específico
ax = axes[1, 1]
ax.scatter(datos['tiempo_h'], datos['csat'], s=100, color='red', label='Datos', zorder=5)
if mejor_modelo == 'Lineal':
    ax.plot(x_plot, modelo_lin.predict(x_plot.reshape(-1, 1)), linewidth=3, color='green', label=mejor_modelo)
elif mejor_modelo == 'Polinómico':
    ax.plot(x_plot, modelo_poly.predict(poly_features.transform(x_plot.reshape(-1, 1))), linewidth=3, color='green', label=mejor_modelo)
elif mejor_modelo == 'Exponencial':
    ax.plot(x_plot, exponencial_decay(x_plot, *params_exp), linewidth=3, color='green', label=mejor_modelo)
else:
    ax.plot(x_plot, log_decay(x_plot, *params_log), linewidth=3, color='green', label=mejor_modelo)
ax.scatter([tiempo_pred], [csat_pred], s=200, color='green', marker='*', label=f'Pred: {csat_pred:.2f}', zorder=10)
ax.set_xlabel('Tiempo de Respuesta (horas)')
ax.set_ylabel('CSAT')
ax.set_title(f'Mejor Modelo: {mejor_modelo}')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Salida:**
```
================================================================================
ANÁLISIS DE MODELOS PARA CSAT
================================================================================

1. LINEAL: f(x) = -0.3136x + 9.2159
   R² = 0.9456
   RMSE = 0.4223

2. POLINÓMICO (grado 2)
   R² = 0.9789
   RMSE = 0.2654

3. EXPONENCIAL: f(x) = 9.0000·e^(-0.2000·x) + 0.5
   R² = 0.9567
   RMSE = 0.3889

...

================================================================================
✓ MEJOR MODELO: Polinómico (R² = 0.9789)
================================================================================

PREDICCIÓN para 15 horas:
CSAT predicho = 1.35 (Polinómico (grado 2))
```

</details>

---

## Recursos Adicionales

- **NumPy Documentation**: [Functions](https://numpy.org/doc/stable/reference/)
- **SciPy**: [Optimization - curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
- **Archivos relacionados**:
  - `10_funciones_matematicas_ds_ia.md`
  - `07_lenguaje_notacion_matematica_ampliada.md`
- **Próximos temas**:
  - Derivadas (velocidad de cambio)
  - Integrales (área bajo la curva)
  - Optimización (encontrar máximos/mínimos)

---

**Actualizado:** 30 de octubre de 2025  
**Progreso de la ruta:** 47% completado (9/19 cursos)  
**Estado:** Completado ✅
