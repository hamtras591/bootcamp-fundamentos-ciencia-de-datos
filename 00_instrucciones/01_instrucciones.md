# Guía para Montar tu Proyecto de Ciencia de Datos con una IA

Este documento es una guía paso a paso para estructurar y desarrollar tu proyecto "Optimización de la Experiencia del Cliente" colaborando con un asistente de inteligencia artificial. El objetivo es que tú dirijas el proyecto y utilices a la IA como una herramienta de programación y consulta.

---

### Fase 0: Preparación y Definición

Antes de escribir una sola línea de código, define claramente el alcance con tu IA.

**Tu Acción:** Inicia la conversación con la IA.
**Prompt sugerido para la IA:**
> "Vamos a empezar mi proyecto de portafolio 'Optimización de la Experiencia del Cliente'. El objetivo es crear una aplicación de línea de comandos en Python que cargue datos de encuestas desde un archivo CSV, los limpie, calcule el puntaje CSAT promedio por departamento y exporte un resumen en JSON. Usaremos POO (Programación Orientada a Objetos) y seguiremos las mejores prácticas de desarrollo. ¿Estás listo para ayudarme a estructurarlo?"

---

### Fase 1: Configuración del Entorno Profesional

Aquí establecerás las bases del proyecto, asegurando que sea limpio, profesional y versionado desde el inicio.

**1.1. Crear el Repositorio en GitHub:**
* Ve a [GitHub](https://github.com) y crea un nuevo repositorio.
* Nómbralo algo descriptivo, como `customer-experience-analyzer`.
* Inicialízalo con un `README` y una licencia (ej. MIT).
* **Importante:** Agrega una plantilla de `.gitignore` para Python.

**1.2. Clonar el Repositorio y Crear Estructura de Carpetas:**
* Abre tu terminal (WSL2/Ubuntu).
* Clona el repositorio en tu máquina local:
    ```bash
    git clone git@github.com:tu-usuario/customer-experience-analyzer.git
    cd customer-experience-analyzer
    ```
* Pídele a la IA que te genere los comandos para crear la estructura de carpetas.

**Prompt sugerido para la IA:**
> "Dentro de mi proyecto `customer-experience-analyzer`, necesito crear la estructura de carpetas estándar. Por favor, dame los comandos de terminal para crear las siguientes carpetas: `src` (para el código fuente), `data` (para los archivos CSV), `notebooks` (para exploración), `tests` (para pruebas) y `reports` (para los resultados)."

**Tu Acción:** Ejecuta los comandos que te proporcione la IA. El resultado debería ser algo así:

.
├── data/
├── notebooks/
├── reports/
├── src/
├── tests/
├── .gitignore
└── README.md


---

### Fase 2: Creación del Esqueleto del Código con POO

Ahora, le pedirás a la IA que genere la estructura básica de tus clases en Python.

**Tu Acción:** Pide a la IA que cree los archivos y el código base para cada clase.

**Prompt sugerido para la IA (puedes hacerlo en una o varias peticiones):**
> "Dentro de la carpeta `src`, crea los siguientes archivos de Python con sus clases básicas. Cada clase debe tener un constructor `__init__` y `docstrings` explicando su propósito:
> 1.  `data_loader.py`: Una clase `DataLoader` que se encargará de cargar datos.
> 2.  `data_cleaner.py`: Una clase `DataCleaner` para la limpieza de datos.
> 3.  `analysis_engine.py`: Una clase `AnalysisEngine` para realizar los cálculos.
> 4.  `report_generator.py`: Una clase `ReportGenerator` para exportar los resultados.
> 5.  `main.py`: Un script principal que usará el bloque `if __name__ == '__main__':`."

---

### Fase 3: Desarrollo Iterativo y Pruebas

En esta fase, construirás la funcionalidad de cada clase, método por método, colaborando con la IA.

**Ejemplo de flujo de trabajo para la clase `DataLoader`:**

1.  **Tu Acción:** Enfócate en una sola tarea.
    **Prompt sugerido para la IA:**
    > "En la clase `DataLoader` del archivo `src/data_loader.py`, necesito un método llamado `load_csv`. Debe recibir una ruta de archivo (`filepath`) como parámetro. Dentro del método, usa un bloque `try-except` para manejar `FileNotFoundError` y `pd.errors.EmptyDataError` (asumiendo que usaremos pandas). El método debe leer el CSV y retornarlo como un DataFrame de pandas. No olvides agregar `docstrings` al método."

2.  **Tu Acción:** Probar el método. Crea un pequeño script de prueba o usa un notebook en la carpeta `notebooks/`.
    * Crea un archivo CSV de ejemplo en la carpeta `data/`.
    * Escribe el código para importar tu clase, instanciarla y llamar al nuevo método.
    * Verifica que funciona como esperas.

3.  **Tu Acción:** Refinar y repetir. Continúa este proceso para todos los métodos de todas las clases. Por ejemplo:
    * **Para `DataCleaner`:** Pide métodos para manejar valores nulos (`remove_nulls`) o eliminar duplicados (`drop_duplicates`).
    * **Para `AnalysisEngine`:** Pide un método para calcular el promedio agrupando por una columna (`calculate_average_by_group`).
    * **Para `ReportGenerator`:** Pide un método para guardar un diccionario en un archivo JSON (`save_to_json`).

---

### Fase 4: Integración, Documentación y Finalización

Ahora que todas las piezas funcionan por separado, las unirás en el script principal.

**4.1. Orquestar el Flujo en `main.py`:**
**Prompt sugerido para la IA:**
> "Ahora vamos a completar `src/main.py`. Necesito que el script haga lo siguiente:
> 1. Importe todas las clases que creamos (`DataLoader`, `DataCleaner`, etc.).
> 2. Defina la ruta al archivo CSV de entrada en `data/` y la ruta del reporte de salida en `reports/`.
> 3. Dentro del bloque `if __name__ == '__main__':`, cree instancias de cada clase.
> 4. Orqueste el flujo: `load_csv` -> `clean_data` -> `analyze` -> `save_report`.
> 5. Imprima mensajes en la consola para indicar el progreso, como 'Datos cargados exitosamente' o 'Reporte generado en reports/...'."

**4.2. Documentar el Proyecto en `README.md`:**
**Prompt sugerido para la IA:**
> "Ayúdame a escribir el contenido para mi `README.md`. Necesito las siguientes secciones:
> - **Título del Proyecto:** Customer Experience Analyzer
> - **Descripción:** Una breve descripción de lo que hace el proyecto.
> - **Instalación:** Cómo un usuario puede clonar el repositorio y (si aplica) instalar dependencias.
> - **Uso:** Cómo ejecutar el script principal desde la terminal."

**4.3. Control de Versiones:**
**Tu Acción:** No olvides hacer commits regularmente después de cada cambio significativo.
```bash
# Después de añadir un método y probarlo
git add .
git commit -m "feat: Implementa el método load_csv en DataLoader"
git push origin main