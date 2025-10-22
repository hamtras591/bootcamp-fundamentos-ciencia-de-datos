# data_loader.py
"""
Universal Data Loader Module
============================
Módulo reutilizable para cargar cualquier tipo de datos sin problemas de encoding.
Autor: Anderson Sebastian Rubio Pacheco
Versión: 1.0.0
"""

import pandas as pd
import numpy as np
from pathlib import Path
import chardet
import json
import logging
from typing import Optional, Dict, Any, Union
import warnings

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class UniversalDataLoader:
    """
    Cargador universal de datos que maneja automáticamente:
    - Detección de encoding
    - Múltiples formatos (CSV, Excel, JSON)
    - Validación de integridad
    - Caché de archivos
    """

    def __init__(self, cache_dir: Optional[str] = None, verbose: bool = True):
        """
        Inicializa el cargador universal

        Args:
            cache_dir: Directorio para caché (opcional)
            verbose: Mostrar mensajes detallados
        """
        self.verbose = verbose
        self.logger = logging.getLogger(self.__class__.__name__)
        self.cache_dir = Path(cache_dir) if cache_dir else Path('.cache')
        self._cache = {}

        # Crear directorio de caché si no existe
        if cache_dir:
            self.cache_dir.mkdir(exist_ok=True)

    def load(self,
             filepath: Union[str, Path],
             force_reload: bool = False,
             **kwargs) -> pd.DataFrame:
        """
        Método principal - carga cualquier archivo automáticamente

        Args:
            filepath: Ruta del archivo
            force_reload: Forzar recarga ignorando caché
            **kwargs: Argumentos adicionales para pandas

        Returns:
            DataFrame con los datos cargados
        """
        filepath = Path(filepath)

        # Verificar caché
        cache_key = str(filepath.absolute())
        if not force_reload and cache_key in self._cache:
            self._log("📦 Cargando desde caché")
            return self._cache[cache_key]

        # Detectar tipo de archivo
        file_extension = filepath.suffix.lower()

        if file_extension in ['.csv', '.txt', '.tsv']:
            df = self._load_csv(filepath, **kwargs)
        elif file_extension in ['.xlsx', '.xls']:
            df = self._load_excel(filepath, **kwargs)
        elif file_extension == '.json':
            df = self._load_json(filepath, **kwargs)
        elif file_extension == '.parquet':
            df = self._load_parquet(filepath, **kwargs)
        else:
            raise ValueError(f"Formato no soportado: {file_extension}")

        # Guardar en caché
        self._cache[cache_key] = df

        # Agregar metadata
        df.attrs['source_file'] = str(filepath)
        df.attrs['load_timestamp'] = pd.Timestamp.now()

        return df

    def _load_csv(self, filepath: Path, **kwargs) -> pd.DataFrame:
        """Carga archivos CSV con detección automática de encoding"""

        # Detectar separador si no se especifica
        if 'sep' not in kwargs and 'delimiter' not in kwargs:
            kwargs['sep'] = self._detect_delimiter(filepath)
            self._log(f"📊 Separador detectado: '{kwargs['sep']}'")

        # Detectar encoding si no se especifica
        if 'encoding' not in kwargs:
            encoding, confidence = self._detect_encoding(filepath)
            kwargs['encoding'] = encoding
            self._log(f"🔤 Encoding detectado: {encoding} ({confidence:.1%} confianza)")

        # Intentar cargar
        try:
            df = pd.read_csv(filepath, **kwargs)
            self._log(f"✅ CSV cargado: {df.shape[0]:,} filas × {df.shape[1]} columnas")

        except UnicodeDecodeError:
            self._log("⚠️ Error de encoding, intentando con latin-1")
            kwargs['encoding'] = 'latin-1'
            df = pd.read_csv(filepath, **kwargs)

        except Exception as e:
            self._log(f"⚠️ Error, intentando con configuración robusta")
            df = self._fallback_csv_load(filepath)

        # Validar integridad
        if self._check_corruption(df):
            self._log("⚠️ Posible corrupción de caracteres detectada")

        return df

    def _load_excel(self, filepath: Path, **kwargs) -> pd.DataFrame:
        """Carga archivos Excel"""
        try:
            df = pd.read_excel(filepath, **kwargs)
            self._log(f"✅ Excel cargado: {df.shape[0]:,} filas × {df.shape[1]} columnas")
            return df
        except Exception as e:
            self._log(f"❌ Error cargando Excel: {e}")
            raise

    def _load_json(self, filepath: Path, **kwargs) -> pd.DataFrame:
        """Carga archivos JSON"""
        try:
            df = pd.read_json(filepath, **kwargs)
            self._log(f"✅ JSON cargado: {df.shape[0]:,} filas × {df.shape[1]} columnas")
            return df
        except Exception as e:
            # Intentar con orientaciones diferentes
            for orient in ['records', 'index', 'columns', 'values']:
                try:
                    df = pd.read_json(filepath, orient=orient)
                    self._log(f"✅ JSON cargado con orient='{orient}'")
                    return df
                except:
                    continue
            raise e

    def _load_parquet(self, filepath: Path, **kwargs) -> pd.DataFrame:
        """Carga archivos Parquet (formato eficiente)"""
        try:
            df = pd.read_parquet(filepath, **kwargs)
            self._log(f"✅ Parquet cargado: {df.shape[0]:,} filas × {df.shape[1]} columnas")
            return df
        except ImportError:
            self._log("❌ Instala 'pyarrow' para leer archivos Parquet")
            raise

    def _detect_encoding(self, filepath: Path, sample_size: int = 100000) -> tuple:
        """Detecta el encoding del archivo"""
        try:
            with open(filepath, 'rb') as file:
                raw_data = file.read(sample_size)
                result = chardet.detect(raw_data)
                return result['encoding'], result['confidence']
        except:
            return 'utf-8', 0.5

    def _detect_delimiter(self, filepath: Path) -> str:
        """Detecta el delimitador del CSV"""
        with open(filepath, 'r', encoding='latin-1', errors='ignore') as file:
            first_line = file.readline()

        # Contar ocurrencias de posibles delimitadores
        delimiters = {
            ',': first_line.count(','),
            ';': first_line.count(';'),
            '\t': first_line.count('\t'),
            '|': first_line.count('|')
        }

        return max(delimiters, key=delimiters.get)

    def _check_corruption(self, df: pd.DataFrame) -> bool:
        """Verifica si hay caracteres corruptos en el DataFrame"""
        corruption_patterns = ['Ã', 'Â£', 'Ã±', 'Ã¡', 'Ã©', 'Â']

        for col in df.select_dtypes(include=['object']).columns:
            sample = df[col].astype(str).head(100).str.cat(sep=' ')
            if any(pattern in sample for pattern in corruption_patterns):
                return True
        return False

    def _fallback_csv_load(self, filepath: Path) -> pd.DataFrame:
        """Método de respaldo para CSVs problemáticos"""
        return pd.read_csv(
            filepath,
            encoding='latin-1',
            sep=None,  # Detectar automáticamente
            engine='python',
            on_bad_lines='skip',
            encoding_errors='ignore'
        )

    def _log(self, message: str):
        """Imprime mensaje si verbose está activo"""
        if self.verbose:
            print(message)

    def save_clean(self,
                   df: pd.DataFrame,
                   filepath: Union[str, Path],
                   format: str = 'auto') -> None:
        """
        Guarda el DataFrame en formato limpio y estandarizado

        Args:
            df: DataFrame a guardar
            filepath: Ruta donde guardar
            format: Formato ('csv', 'excel', 'parquet', 'auto')
        """
        filepath = Path(filepath)

        if format == 'auto':
            format = filepath.suffix[1:] if filepath.suffix else 'csv'

        if format == 'csv':
            df.to_csv(filepath, encoding='utf-8', index=False)
            self._log(f"💾 Guardado como CSV UTF-8: {filepath}")
        elif format == 'excel':
            df.to_excel(filepath, index=False)
            self._log(f"💾 Guardado como Excel: {filepath}")
        elif format == 'parquet':
            df.to_parquet(filepath, index=False)
            self._log(f"💾 Guardado como Parquet: {filepath}")
        else:
            raise ValueError(f"Formato no soportado: {format}")

    def get_info(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Obtiene información detallada del DataFrame"""
        info = {
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.to_dict(),
            'memory_mb': df.memory_usage(deep=True).sum() / 1024 ** 2,
            'nulls': df.isnull().sum().to_dict(),
            'source': df.attrs.get('source_file', 'Unknown'),
            'loaded_at': df.attrs.get('load_timestamp', 'Unknown')
        }
        return info


# Funciones de conveniencia (shortcuts)
def load_data(filepath: Union[str, Path], **kwargs) -> pd.DataFrame:
    """
    Función rápida para cargar cualquier archivo

    Uso:
        df = load_data('archivo.csv')
        df = load_data('archivo.xlsx', sheet_name='Hoja1')
    """
    loader = UniversalDataLoader(verbose=True)
    return loader.load(filepath, **kwargs)


def quick_load(filepath: Union[str, Path]) -> pd.DataFrame:
    """
    Carga rápida sin mensajes

    Uso:
        df = quick_load('archivo.csv')
    """
    loader = UniversalDataLoader(verbose=False)
    return loader.load(filepath)


def load_and_clean(filepath: Union[str, Path]) -> pd.DataFrame:
    """
    Carga y limpia automáticamente

    Uso:
        df = load_and_clean('archivo.csv')
    """
    loader = UniversalDataLoader(verbose=True)
    df = loader.load(filepath)

    # Limpieza automática básica
    initial_shape = df.shape

    # Eliminar filas completamente vacías
    df = df.dropna(how='all')

    # Eliminar columnas completamente vacías
    df = df.dropna(axis=1, how='all')

    # Eliminar duplicados
    df = df.drop_duplicates()

    final_shape = df.shape

    if initial_shape != final_shape:
        print(f"🧹 Limpieza: {initial_shape} → {final_shape}")

    return df


# Para importar directamente las funciones más usadas
__all__ = ['UniversalDataLoader', 'load_data', 'quick_load', 'load_and_clean']