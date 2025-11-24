# Flujo de Trabajo en Ciencia de Datos

**Curso:** Matemáticas para Data Science: Estadística Descriptiva  
**Fecha:** Noviembre 2025  
**Ruta:** Fundamentos de Data Science e IA  
**Repositorio:** `bootcamp-fundamentos-ciencia-de-datos`

---

## 📋 Índice

1. [Concepto](#concepto)
2. [Etapas del Flujo de Trabajo](#etapas-del-flujo-de-trabajo)
3. [Ingesta y Preprocesamiento de Datos](#ingesta-y-preprocesamiento-de-datos)
4. [Preparación y Entrenamiento de Modelos](#preparación-y-entrenamiento-de-modelos)
5. [Evaluación y Producción del Modelo](#evaluación-y-producción-del-modelo)
6. [Roles Profesionales en Data Science](#roles-profesionales-en-data-science)
7. [El Papel de la Estadística](#el-papel-de-la-estadística)
8. [Visualización del Flujo](#visualización-del-flujo)
9. [Recursos Adicionales](#recursos-adicionales)

---

## Concepto

El **flujo de trabajo en ciencia de datos** es un viaje esencial que comienza desde la ingesta de datos hasta la interacción final con el usuario. Este camino **no es lineal ni estático**, sino una serie dinámica de pasos donde varias profesiones convergen.

### Características principales:

- **Iterativo:** Se vuelve atrás cuando es necesario ajustar
- **Colaborativo:** Múltiples profesionales trabajan en diferentes etapas
- **Basado en estadística:** La estadística (descriptiva e inferencial) es fundamental en cada paso
- **Orientado a valor:** El objetivo final es transformar datos en conocimientos prácticos

---

## Etapas del Flujo de Trabajo

```
┌─────────────────┐
│  INGESTA DE     │
│     DATOS       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PREPROCESAMIENTO│
│   Y LIMPIEZA    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   ANÁLISIS      │
│  EXPLORATORIO   │
│     (EDA)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PREPARACIÓN    │
│   DEL MODELO    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ENTRENAMIENTO  │
│   DEL MODELO    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   EVALUACIÓN    │
│   DEL MODELO    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   PRODUCCIÓN    │
│ E IMPLEMENTACIÓN│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  INTERACCIÓN    │
│  CON USUARIO    │
└─────────────────┘
```

---

## Ingesta y Preprocesamiento de Datos

La fase de **ingesta y preprocesamiento** es el primer gran paso donde los datos crudos son recolectados y transformados.

### Tareas principales:

#### 1. Identificación de tipos de datos
- Variables numéricas (continuas, discretas)
- Cadenas de texto (categóricas, texto libre)
- Datos estructurados (tablas, bases de datos)
- Datos no estructurados (imágenes, audio, texto)

#### 2. Definición del pipeline de procesamiento
- Determinar qué transformaciones son necesarias
- Establecer el orden de operaciones
- Definir reglas de limpieza

#### 3. Transformación y limpieza de datos
- Manejo de valores nulos
- Eliminación de duplicados
- Corrección de formatos
- Normalización de datos

### Conceptos clave: ETL

**ETL (Extract, Transform, Load)** se vuelve fundamental en esta fase:

- **Extract (Extraer):** Obtener datos de diversas fuentes
- **Transform (Transformar):** Limpiar, normalizar y estructurar
- **Load (Cargar):** Almacenar datos procesados para análisis

---

## Preparación y Entrenamiento de Modelos

Una vez preprocesados los datos, entramos en una fase crítica de preparación y entrenamiento del modelo.

### Análisis Exploratorio de Datos (EDA)

El **EDA** desempeña un rol central, utilizando **estadísticas descriptivas** para:

- **Revelar patrones:** Identificar tendencias y comportamientos en los datos
- **Descubrir correlaciones:** Encontrar relaciones entre variables
- **Realizar reducción de datos:** Simplificar datasets complejos
- **Detectar anomalías:** Identificar valores atípicos (outliers)

### Preparación del modelo

- Asegurar que los datos estén listos para la construcción del modelo
- Selección de features (características) relevantes
- División de datos (train/test/validation)
- Escalamiento y normalización

Esta preparación meticulosa es clave para construir un **modelo robusto** que pueda entregar resultados precisos.

---

## Evaluación y Producción del Modelo

La parte final del flujo de trabajo se centra en evaluar el modelo, enviarlo a producción y gestionar su interacción con el usuario final.

### 1. Evaluación del modelo

- **Pruebas y validación:** Medir el desempeño con métricas apropiadas
- **Test de hipótesis:** Probar suposiciones estadísticas
- **Validación cruzada:** Asegurar que el modelo generaliza bien

Aquí, la **estadística inferencial** cobra protagonismo a través de:
- Probabilidad
- Inferencia estadística
- Test de hipótesis

### 2. Implementación en producción

- **Integración:** Conectar el modelo con sistemas existentes
- **Optimización:** Mejorar velocidad y eficiencia
- **Monitoreo:** Supervisar el rendimiento en tiempo real
- **Mantenimiento:** Actualizar el modelo cuando sea necesario

### 3. Interacción con el usuario

- Asegurar que el modelo cumpla con las expectativas de negocio
- Aportar valor tangible al usuario final
- Facilitar la interpretación de resultados
- Proporcionar dashboards y reportes

---

## Roles Profesionales en Data Science

En el campo de la ciencia de datos, **no existe un solo perfil** que domine todo el flujo de trabajo. Diversas disciplinas y profesiones convergen para facilitar cada paso del proceso:

### 1. Analista de Datos
- **Especialización:** Manipulación y análisis de conjuntos de datos
- **Foco:** Estadística descriptiva, visualización, reportes
- **Herramientas:** SQL, Excel, Tableau, Power BI

### 2. Ingeniero de Datos
- **Especialización:** Construir y mantener la arquitectura de datos
- **Foco:** Pipelines ETL, bases de datos, infraestructura
- **Herramientas:** Apache Spark, Airflow, SQL, cloud services

### 3. Científico de Datos
- **Especialización:** Análisis complejo y construcción de modelos
- **Foco:** Machine Learning, estadística avanzada, predicción
- **Herramientas:** Python, R, scikit-learn, TensorFlow

### 4. Machine Learning Engineer
- **Especialización:** Optimizar modelos para producción
- **Foco:** Escalabilidad, eficiencia, deployment
- **Herramientas:** MLOps, Kubernetes, Docker, cloud ML platforms

### 5. Científico Investigador
- **Especialización:** Innovación y avance de técnicas estadísticas
- **Foco:** Investigación, nuevos algoritmos, publicaciones
- **Herramientas:** Matemáticas avanzadas, frameworks de investigación

### Colaboración entre roles

```
┌────────────────────────────────────────────────┐
│           FLUJO DE TRABAJO COMPLETO            │
└────────────────────────────────────────────────┘

  Ingeniero        Analista         Científico      ML Engineer
  de Datos        de Datos         de Datos

    ████            ░░░░              ░░░░            ░░░░
    ████            ████              ░░░░            ░░░░
    ░░░░            ████              ████            ░░░░
    ░░░░            ████              ████            ░░░░
    ░░░░            ░░░░              ████            ████
    ░░░░            ░░░░              ░░░░            ████

  Ingesta/       Limpieza/        Modelado/      Producción/
   ETL          Exploración      Entrenamiento   Deployment
```

Cada uno de estos roles tiene un momento en el flujo de trabajo donde su experiencia es vital. La **interacción de estas especialidades** asegura que el proceso sea eficiente y efectivo.

---

## El Papel de la Estadística

La estadística, tanto **descriptiva** como **inferencial**, es un componente esencial que guía y mejora este viaje:

### Estadística Descriptiva (Fases iniciales)

| Fase | Aplicación de Estadística Descriptiva |
|------|--------------------------------------|
| **Ingesta** | Identificación de tipos de datos, detección de anomalías |
| **Preprocesamiento** | Normalización, escalamiento, transformaciones |
| **EDA** | Medidas de tendencia central, dispersión, correlaciones |
| **Preparación** | Reducción de dimensionalidad, selección de features |

### Estadística Inferencial (Fases finales)

| Fase | Aplicación de Estadística Inferencial |
|------|---------------------------------------|
| **Evaluación** | Test de hipótesis, intervalos de confianza |
| **Validación** | Pruebas de significancia estadística |
| **Producción** | A/B testing, monitoreo de performance |
| **Optimización** | Análisis de varianza, pruebas comparativas |

---

## Visualización del Flujo

### Flujo completo con componentes estadísticos

```python
import pandas as pd

# Representación conceptual del flujo
flujo_trabajo = {
    'Fase': ['Ingesta', 'Preprocesamiento', 'EDA', 'Modelado', 'Evaluación', 'Producción'],
    'Estadística_Descriptiva': ['Alta', 'Alta', 'Muy Alta', 'Media', 'Baja', 'Baja'],
    'Estadística_Inferencial': ['Baja', 'Baja', 'Media', 'Alta', 'Muy Alta', 'Alta'],
    'Rol_Principal': [
        'Ingeniero de Datos',
        'Analista de Datos',
        'Analista/Científico de Datos',
        'Científico de Datos',
        'Científico de Datos',
        'ML Engineer'
    ]
}

df_flujo = pd.DataFrame(flujo_trabajo)
print(df_flujo)
```

**Output esperado:**

```
            Fase Estadística_Descriptiva Estadística_Inferencial              Rol_Principal
0        Ingesta                    Alta                    Baja      Ingeniero de Datos
1  Preprocesamiento                    Alta                    Baja       Analista de Datos
2            EDA                Muy Alta                   Media  Analista/Científico de Datos
3       Modelado                   Media                    Alta      Científico de Datos
4     Evaluación                    Baja                Muy Alta      Científico de Datos
5     Producción                    Baja                    Alta              ML Engineer
```

---

## Recursos Adicionales

### 📚 Conceptos clave para profundizar

- **ETL (Extract, Transform, Load):** Proceso de extracción, transformación y carga de datos
- **EDA (Exploratory Data Analysis):** Análisis exploratorio de datos
- **Feature Engineering:** Creación y selección de características para modelos
- **Model Deployment:** Puesta en producción de modelos de ML

### 🔗 Enlaces útiles

- [Documentación de pandas para análisis exploratorio](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)
- [Scikit-learn: Machine Learning en Python](https://scikit-learn.org/)
- [MLOps: Machine Learning Operations](https://ml-ops.org/)

### 📂 Archivos relacionados

- `01_que_es_estadistica_descriptiva.md` - Fundamentos de estadística descriptiva
- Siguiente: Estructura del curso y tipos de datos

### 🎯 Puntos clave para recordar

1. El flujo de trabajo en data science es **iterativo y dinámico**
2. La **estadística descriptiva** domina las fases iniciales (ingesta, limpieza, EDA)
3. La **estadística inferencial** es crucial en fases finales (evaluación, producción)
4. **Múltiples roles profesionales** colaboran en diferentes etapas
5. El objetivo final es **transformar datos en conocimientos prácticos y valiosos**

---

**Actualizado:** Noviembre 2025  
**Progreso de la ruta:** 68% completado (13/19 cursos)