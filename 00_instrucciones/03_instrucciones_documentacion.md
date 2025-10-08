# Instrucciones para Documentación de Sesiones de Estudio

**Propósito:** Guía estandarizada para generar documentación de cada clase del bootcamp  
**Ubicación:** `00_instrucciones/03_instrucciones_documentacion_sesiones.md`  
**Fecha de creación:** 08 de octubre de 2025  
**Proyecto:** Bootcamp Fundamentos de Ciencia de Datos

---

## 📋 Flujo de Trabajo por Sesión

### Paso 1: Contexto inicial (OBLIGATORIO)
Al inicio de cada nueva conversación para documentar un tema, SIEMPRE ejecutar:

```
Por favor lee las conversaciones del proyecto:
1. Jupyter notebook file reading
2. Python for data science bootcamp
3. [Nombre de conversación adicional si aplica]
```

**Razón:** Mantener coherencia en estilo, estructura y nivel técnico de la documentación.

---

## 📝 Formato de Documentación

### Estructura base de cada archivo markdown

```markdown
# [Título del Tema]

**Curso:** Python para Ciencia de Datos  
**Fecha:** [Fecha de estudio]  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [Sintaxis](#sintaxis)
3. [Ejemplos Básicos](#ejemplos-básicos)
4. [Casos de Uso en Data Science](#casos-de-uso-en-data-science)
5. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

[Explicación clara del tema]

---

## Sintaxis

```python
# Código de ejemplo de sintaxis base
```

---

## Ejemplos Básicos

### Ejemplo 1: [Nombre descriptivo]

```python
# Código del ejemplo 1
```

### Ejemplo 2: [Nombre descriptivo]

```python
# Código del ejemplo 2
```

---

## Casos de Uso en Data Science

### Caso de Uso 1: [Título del caso]

**Contexto:** [Descripción del problema real en data science]

**Solución:**

```python
# Código de la solución
```

**Explicación:** [Por qué este enfoque es útil]

---

### Caso de Uso 2: [Título del caso]

**Contexto:** [Descripción del problema real en data science]

**Solución:**

```python
# Código de la solución
```

**Explicación:** [Por qué este enfoque es útil]

---

## Ejercicios Prácticos

### Ejercicio 1: [Nivel Básico]

**Enunciado:** [Descripción clara del ejercicio]

**Pistas:**
- Pista 1
- Pista 2

<details>
<summary>💡 Ver solución</summary>

```python
# Solución del ejercicio 1
```

**Explicación:** [Paso a paso de la solución]

</details>

---

### Ejercicio 2: [Nivel Básico-Intermedio]

**Enunciado:** [Descripción clara del ejercicio]

**Pistas:**
- Pista 1
- Pista 2

<details>
<summary>💡 Ver solución</summary>

```python
# Solución del ejercicio 2
```

**Explicación:** [Paso a paso de la solución]

</details>

---

### Ejercicio 3: [Nivel Intermedio]

**Enunciado:** [Descripción clara del ejercicio]

**Pistas:**
- Pista 1
- Pista 2

<details>
<summary>💡 Ver solución</summary>

```python
# Solución del ejercicio 3
```

**Explicación:** [Paso a paso de la solución]

</details>

---

### Ejercicio 4: [Nivel Intermedio-Avanzado]

**Enunciado:** [Descripción clara del ejercicio]

**Pistas:**
- Pista 1
- Pista 2

<details>
<summary>💡 Ver solución</summary>

```python
# Solución del ejercicio 4
```

**Explicación:** [Paso a paso de la solución]

</details>

---

### Ejercicio 5: [Nivel Desafío]

**Enunciado:** [Descripción clara del ejercicio - combina múltiples conceptos]

**Pistas:**
- Pista 1
- Pista 2
- Pista 3

<details>
<summary>💡 Ver solución</summary>

```python
# Solución del ejercicio 5
```

**Explicación:** [Paso a paso de la solución]

</details>

---

## Recursos Adicionales

- Documentación oficial: [link]
- Archivos relacionados: [lista]
- Próximos temas: [lista]

---

**Actualizado:** [Fecha]  
**Progreso de la ruta:** [X]% completado ([N]/19 cursos)
```

---

## ✅ Checklist de Requisitos OBLIGATORIOS

Cada documentación DEBE cumplir con:

### ✓ Formato celda por celda
- [ ] Todo código debe estar en bloques separados de markdown
- [ ] Cada bloque de código debe ser **copiable** directamente a un `.ipynb`
- [ ] Los bloques de markdown deben ser independientes
- [ ] Facilitar la creación de notebooks desde el markdown

### ✓ Casos de uso (MÍNIMO 2)
- [ ] Caso de uso 1: Problema real en data science
- [ ] Caso de uso 2: Problema real en data science
- [ ] Cada caso debe tener: Contexto + Código + Explicación
- [ ] Los casos deben ser diferentes entre sí
- [ ] Deben relacionarse con análisis de datos, limpieza, visualización o ML

### ✓ Ejercicios (OMITIDOS TEMPORALMENTE)
- [ ] **NO generar ejercicios durante el estudio de temas individuales**
- [ ] Los ejercicios se acumularán para una sesión práctica al final del módulo
- [ ] Enfoque: Teoría + Sintaxis + Casos de Uso únicamente

### ✓ Estructura general
- [ ] Título y metadatos del curso
- [ ] Índice con enlaces internos
- [ ] Sección de conceptos
- [ ] Sección de sintaxis
- [ ] Sección de ejemplos básicos
- [ ] Sección de casos de uso
- [ ] Sección de ejercicios
- [ ] Sección de recursos adicionales

---

## 🎯 Criterios de Calidad

### Para los casos de uso:

1. **Relevancia:** Deben ser problemas que un data scientist enfrentaría
2. **Realismo:** Usar datasets o situaciones comunes (CSV, análisis de ventas, limpieza de datos)
3. **Progresión:** Caso 1 más simple que Caso 2
4. **Aplicabilidad:** Conectar con el proyecto final (Customer Experience Analyzer)

**Ejemplos de buenos contextos:**
- Análisis de ventas de e-commerce
- Limpieza de datos de encuestas
- Filtrado de información de clientes
- Preparación de datos para visualización
- Cálculo de métricas de negocio (CSAT, NPS, etc.)

---

### Para los ejercicios:

1. **Progresión gradual:** Cada ejercicio debe ser un poco más complejo que el anterior
2. **Variedad:** No repetir el mismo tipo de problema 5 veces
3. **Pistas útiles:** Guiar sin dar la respuesta completa
4. **Explicaciones detalladas:** En la solución, explicar el "por qué" no solo el "cómo"
5. **Código funcional:** Todas las soluciones deben ser ejecutables

**Distribución de dificultad sugerida:**
- Ejercicio 1: Aplicación directa de sintaxis básica
- Ejercicio 2: Requiere pensar un paso adicional
- Ejercicio 3: Combina 2 conceptos del tema
- Ejercicio 4: Requiere lógica o manipulación más compleja
- Ejercicio 5: Integra múltiples conceptos + pensamiento crítico

---

## 📂 Convenciones de Nombres

### Para archivos markdown:
```
[número]_[tema_descriptivo].md

Ejemplos:
- 12_seleccion_datos_iloc_loc.md
- 13_filtrado_datos_pandas.md
- 14_groupby_agregaciones.md
```

### Para notebooks:
```
[número]_pd_[tema_corto].ipynb

Ejemplos:
- 12_pd_seleccion_datos_loc_iloc.ipynb
- 13_pd_filtrado_condicional.ipynb
- 14_pd_groupby.ipynb
```

---

## 🔄 Proceso de Generación

### Cuando inicies una nueva sesión de documentación:

1. **Cargar contexto:**
   ```
   "Lee las conversaciones del proyecto y el archivo 
   03_instrucciones_documentacion_sesiones.md"
   ```

2. **Proporcionar material:**
   ```
   "Aquí está el resumen de Platzi sobre [tema]. 
   Por favor genera la documentación siguiendo las instrucciones."
   ```

3. **Verificar requisitos:**
   - ✅ ¿Tiene 2 casos de uso?
   - ✅ ¿Tiene 5 ejercicios?
   - ✅ ¿El código es copiable celda por celda?
   - ✅ ¿Sigue el formato estándar?

4. **Guardar y versionar:**
   ```bash
   git add notas/[número]_[tema].md
   git commit -m "docs: Añade documentación de [tema]"
   git push origin main
   ```

---

## 🚫 Errores Comunes a Evitar

### ❌ NO hacer:

1. **Generar código que no sea copiable directamente**
   - Evitar: Código incompleto con "..." o "# código aquí"
   - Hacer: Código completo y ejecutable

2. **Casos de uso genéricos sin contexto**
   - Evitar: "Ejemplo de uso de iloc"
   - Hacer: "Análisis de ventas top 10 productos por región"

3. **Ejercicios demasiado fáciles o repetitivos**
   - Evitar: 5 ejercicios de "selecciona la columna X"
   - Hacer: Progresión de dificultad con variedad

4. **Explicaciones superficiales**
   - Evitar: "Aquí está el código"
   - Hacer: "Este código funciona porque... paso a paso..."

5. **Olvidar la conexión con el proyecto final**
   - Evitar: Ejemplos abstractos sin contexto
   - Hacer: "Esta técnica la usarás para filtrar encuestas CSAT en el proyecto"

---

## 📊 Ejemplo de Prompt Ideal

```
Hola, por favor lee las conversaciones del proyecto:
1. Jupyter notebook file reading
2. Python for data science bootcamp

Y lee también el archivo 03_instrucciones_documentacion_sesiones.md

Necesito documentar el tema de [TEMA]. Aquí está el resumen de Platzi:

[PEGAR RESUMEN]

Por favor genera la documentación completa siguiendo TODOS los requisitos:
- Formato celda por celda para .ipynb
- 2 casos de uso en data science
- SIN ejercicios (se harán al final del módulo)

Asegúrate de incluir todo el checklist obligatorio.
```

---

## 🎓 Referencia Rápida

### Cada archivo debe tener:

| Elemento | Cantidad | Obligatorio |
|----------|----------|-------------|
| Casos de uso en data science | 2 | ✅ Sí |
| Ejercicios prácticos | 0 | ❌ No (al final del módulo) |
| Bloques de código copiables | Variable | ✅ Sí |
| Sección de conceptos | 1 | ✅ Sí |
| Sección de sintaxis | 1 | ✅ Sí |
| Ejemplos básicos | 2-3 | ✅ Sí |
| Recursos adicionales | 1 | ✅ Sí |

---

## 📝 Notas Finales

- Este documento se debe actualizar si cambian los requisitos
- Cada sesión debe seguir exactamente estas instrucciones
- La consistencia es clave para mantener calidad en la documentación
- Si algo no está claro, preguntar antes de generar la documentación

---

**Versión:** 1.0  
**Última actualización:** 08 de octubre de 2025  
**Autor:** Sistema de documentación del bootcamp