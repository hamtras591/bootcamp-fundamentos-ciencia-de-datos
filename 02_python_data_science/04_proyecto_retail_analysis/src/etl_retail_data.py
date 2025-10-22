# online_retail_manager_v2.py
import pandas as pd
import numpy as np
from pathlib import Path
import shutil
import os

class OnlineRetailManager:
    """Gestor mejorado para el dataset Online Retail (CSV)"""

    def __init__(self, working_dir='.'):
        self.working_dir = Path(working_dir)
        self.csv_path = None
        self.df = None
        self.df_clean = None

    def download_with_kagglehub(self):
        """Descarga el dataset usando kagglehub y lo copia a la carpeta actual"""
        try:
            import kagglehub

            print("📥 Descargando dataset con kagglehub...")

            # Descargar dataset
            path = kagglehub.dataset_download("tunguz/online-retail")
            print(f"✅ Descargado en caché: {path}")

            # Convertir a Path object
            cache_path = Path(path)

            # Buscar archivos CSV en la carpeta descargada
            csv_files = list(cache_path.glob('*.csv'))
            xlsx_files = list(cache_path.glob('*.xlsx'))

            print(f"\n📁 Archivos encontrados en caché:")
            for csv in csv_files:
                size = csv.stat().st_size / (1024*1024)
                print(f"  • CSV: {csv.name} ({size:.2f} MB)")
            for xlsx in xlsx_files:
                size = xlsx.stat().st_size / (1024*1024)
                print(f"  • Excel: {xlsx.name} ({size:.2f} MB)")

            # Buscar el archivo principal
            target_file = None

            # Prioridad: Online Retail.csv > Online_Retail.csv > cualquier .csv > cualquier .xlsx
            possible_names = [
                'Online Retail.csv',
                'Online_Retail.csv',
                'online-retail.csv',
                'online_retail.csv',
                'Online Retail.xlsx',
                'Online_Retail.xlsx'
            ]

            for name in possible_names:
                file_path = cache_path / name
                if file_path.exists():
                    target_file = file_path
                    break

            # Si no encontramos con nombres específicos, tomar el primer CSV o XLSX
            if not target_file:
                if csv_files:
                    target_file = csv_files[0]
                elif xlsx_files:
                    target_file = xlsx_files[0]

            if target_file:
                # Copiar a la carpeta de trabajo
                local_filename = f"online_retail.{target_file.suffix[1:]}"  # .csv o .xlsx
                local_path = self.working_dir / local_filename

                print(f"\n📋 Copiando archivo a carpeta actual...")
                print(f"  Desde: {target_file}")
                print(f"  Hacia: {local_path}")

                shutil.copy2(target_file, local_path)

                self.csv_path = local_path
                print(f"✅ Archivo copiado como: {local_filename}")

                return True
            else:
                print("❌ No se encontró el archivo del dataset")
                return False

        except ImportError:
            print("❌ kagglehub no está instalado")
            print("   Instálalo con: pip install kagglehub")
            return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

    def find_local_file(self):
        """Busca archivos del dataset en la carpeta local"""

        # Buscar CSV primero, luego XLSX
        patterns = ['*retail*.csv', '*retail*.xlsx', '*.csv', '*.xlsx']

        for pattern in patterns:
            files = list(self.working_dir.glob(pattern))
            # Excluir archivos sintéticos y limpios
            files = [f for f in files if 'synthetic' not in f.name.lower()
                    and 'clean' not in f.name.lower()]

            if files:
                self.csv_path = files[0]
                print(f"📁 Archivo local encontrado: {self.csv_path.name}")
                return True

        return False

    def load_data(self, force_download=False):
        """Carga el dataset (descarga si es necesario)"""

        # 1. Buscar archivo local primero
        if not force_download and self.find_local_file():
            print(f"📂 Usando archivo local: {self.csv_path.name}")
        else:
            # 2. Descargar con kagglehub
            if not self.download_with_kagglehub():
                print("⚠️ Creando dataset sintético para práctica...")
                self.df = self.create_synthetic_data()
                return self.df

        # 3. Cargar el archivo
        print(f"\n⏳ Cargando dataset...")

        try:
            # Detectar el tipo de archivo y cargar apropiadamente
            if self.csv_path.suffix.lower() == '.csv':
                # Intentar diferentes encodings para CSV
                encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']

                for encoding in encodings:
                    try:
                        self.df = pd.read_csv(self.csv_path, encoding=encoding)
                        print(f"✅ CSV cargado con encoding: {encoding}")
                        break
                    except UnicodeDecodeError:
                        continue
                    except Exception as e:
                        print(f"Error con encoding {encoding}: {e}")

            else:  # Excel
                self.df = pd.read_excel(self.csv_path)
                print("✅ Excel cargado exitosamente")

            # Verificar y convertir tipos de datos
            self.optimize_dtypes()

            # Mostrar información
            self.print_info()

            return self.df

        except Exception as e:
            print(f"❌ Error al cargar archivo: {e}")
            print("⚠️ Creando dataset sintético...")
            self.df = self.create_synthetic_data()
            return self.df

    def optimize_dtypes(self):
        """Optimiza los tipos de datos del DataFrame"""
        if self.df is None:
            return

        print("\n🔧 Optimizando tipos de datos...")

        # Convertir InvoiceDate a datetime si existe y no lo es
        if 'InvoiceDate' in self.df.columns:
            if self.df['InvoiceDate'].dtype == 'object':
                self.df['InvoiceDate'] = pd.to_datetime(self.df['InvoiceDate'], errors='coerce')
                print("  • InvoiceDate convertido a datetime")

        # Convertir CustomerID a string si existe (para evitar problemas con NaN)
        if 'CustomerID' in self.df.columns:
            self.df['CustomerID'] = self.df['CustomerID'].astype('Int64').astype(str)
            self.df.loc[self.df['CustomerID'] == '<NA>', 'CustomerID'] = np.nan
            print("  • CustomerID convertido a string")

        # Asegurar que Quantity y UnitPrice sean numéricos
        for col in ['Quantity', 'UnitPrice']:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

    def create_synthetic_data(self):
        """Crea un dataset sintético similar al Online Retail"""
        np.random.seed(42)
        n_rows = 10000

        print("🔨 Generando dataset sintético...")

        # Generar datos más realistas
        dates = pd.date_range('2010-12-01', '2011-12-09', periods=n_rows)

        # Productos con descripciones reales
        products = [
            ('85123A', 'WHITE HANGING HEART T-LIGHT HOLDER', 2.55),
            ('71053', 'WHITE METAL LANTERN', 3.39),
            ('84406B', 'CREAM CUPID HEARTS COAT HANGER', 2.75),
            ('84029G', 'KNITTED UNION FLAG HOT WATER BOTTLE', 3.39),
            ('84029E', 'RED WOOLLY HOTTIE WHITE HEART', 3.39),
            ('22752', 'SET 7 BABUSHKA NESTING BOXES', 7.65),
            ('21730', 'GLASS STAR FROSTED T-LIGHT HOLDER', 4.25),
            ('22633', 'HAND WARMER UNION JACK', 1.85),
            ('22632', 'HAND WARMER RED POLKA DOT', 1.85),
            ('84879', 'ASSORTED COLOUR BIRD ORNAMENT', 1.69)
        ]

        # Generar datos
        data = []
        invoice_no = 536365

        for i in range(n_rows):
            if i % 20 == 0:  # Nueva factura cada 20 items
                invoice_no += 1

            product = np.random.choice(products)

            data.append({
                'InvoiceNo': str(invoice_no),
                'StockCode': product[0],
                'Description': product[1],
                'Quantity': np.random.randint(1, 12),
                'InvoiceDate': dates[i],
                'UnitPrice': product[2] * np.random.uniform(0.8, 1.2),  # Variación de precio
                'CustomerID': np.random.choice([np.nan] + list(range(12346, 12500)), p=[0.05] + [0.95/154]*154),
                'Country': np.random.choice(
                    ['United Kingdom', 'France', 'Germany', 'EIRE', 'Spain', 'Netherlands', 'Belgium'],
                    p=[0.45, 0.15, 0.15, 0.08, 0.07, 0.05, 0.05]
                )
            })

        df = pd.DataFrame(data)

        # Guardar como CSV
        synthetic_path = self.working_dir / 'online_retail_synthetic.csv'
        df.to_csv(synthetic_path, index=False)
        print(f"💾 Dataset sintético guardado: {synthetic_path.name}")

        return df

    def print_info(self):
        """Imprime información detallada del dataset"""
        if self.df is None:
            return

        print("\n" + "="*70)
        print("📊 INFORMACIÓN DEL DATASET")
        print("="*70)

        print(f"\n📁 Archivo: {self.csv_path.name if self.csv_path else 'Sintético'}")
        print(f"📏 Dimensiones: {self.df.shape[0]:,} filas × {self.df.shape[1]} columnas")
        print(f"💾 Memoria: {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

        print(f"\n📋 Información de columnas:")
        print("-"*50)
        for col in self.df.columns:
            null_count = self.df[col].isnull().sum()
            null_pct = (null_count / len(self.df)) * 100
            unique = self.df[col].nunique()
            print(f"  • {col:<20} {str(self.df[col].dtype):<15} "
                  f"Nulls: {null_count:>6} ({null_pct:>5.1f}%)  "
                  f"Únicos: {unique:>6}")

        print(f"\n🔍 Muestra de datos:")
        print(self.df.head(3).to_string())

        print(f"\n📈 Estadísticas rápidas:")
        if 'InvoiceDate' in self.df.columns:
            print(f"  • Rango de fechas: {self.df['InvoiceDate'].min()} a {self.df['InvoiceDate'].max()}")
        if 'Country' in self.df.columns:
            top_country = self.df['Country'].value_counts().iloc[0]
            print(f"  • País principal: {self.df['Country'].value_counts().index[0]} ({top_country:,} transacciones)")
        if 'CustomerID' in self.df.columns:
            print(f"  • Clientes únicos: {self.df['CustomerID'].nunique():,}")

        print("="*70)

    def clean_data(self, verbose=True):
        """Limpia el dataset con opciones de verbosidad"""
        if self.df is None:
            print("❌ Primero carga el dataset con load_data()")
            return None

        if verbose:
            print("\n🧹 PROCESO DE LIMPIEZA DETALLADO")
            print("-"*50)

        self.df_clean = self.df.copy()
        initial_rows = len(self.df_clean)
        initial_memory = self.df_clean.memory_usage(deep=True).sum() / 1024**2

        # 1. Eliminar duplicados completos
        duplicates = self.df_clean.duplicated().sum()
        self.df_clean = self.df_clean.drop_duplicates()
        if verbose and duplicates > 0:
            print(f"1. Duplicados eliminados: {duplicates:,} filas")

        # 2. Eliminar filas sin CustomerID
        nulls = self.df_clean['CustomerID'].isnull().sum()
        self.df_clean = self.df_clean.dropna(subset=['CustomerID'])
        if verbose and nulls > 0:
            print(f"2. Sin CustomerID eliminados: {nulls:,} filas")

        # 3. Eliminar transacciones canceladas
        if self.df_clean['InvoiceNo'].dtype == 'object':
            cancelled = self.df_clean['InvoiceNo'].str.startswith('C').sum()
            self.df_clean = self.df_clean[~self.df_clean['InvoiceNo'].str.startswith('C')]
            if verbose and cancelled > 0:
                print(f"3. Cancelaciones eliminadas: {cancelled:,} filas")

        # 4. Filtrar cantidades y precios válidos
        invalid = ((self.df_clean['Quantity'] <= 0) | (self.df_clean['UnitPrice'] <= 0)).sum()
        self.df_clean = self.df_clean[(self.df_clean['Quantity'] > 0) &
                                       (self.df_clean['UnitPrice'] > 0)]
        if verbose and invalid > 0:
            print(f"4. Valores inválidos eliminados: {invalid:,} filas")

        # 5. Crear columnas adicionales útiles
        self.df_clean['Revenue'] = self.df_clean['Quantity'] * self.df_clean['UnitPrice']

        # Si tenemos InvoiceDate como datetime, crear columnas de tiempo
        if 'InvoiceDate' in self.df_clean.columns and pd.api.types.is_datetime64_any_dtype(self.df_clean['InvoiceDate']):
            self.df_clean['Year'] = self.df_clean['InvoiceDate'].dt.year
            self.df_clean['Month'] = self.df_clean['InvoiceDate'].dt.month
            self.df_clean['Day'] = self.df_clean['InvoiceDate'].dt.day
            self.df_clean['Weekday'] = self.df_clean['InvoiceDate'].dt.day_name()
            self.df_clean['Hour'] = self.df_clean['InvoiceDate'].dt.hour

        # Resumen
        final_rows = len(self.df_clean)
        final_memory = self.df_clean.memory_usage(deep=True).sum() / 1024**2

        if verbose:
            print(f"\n✅ RESUMEN DE LIMPIEZA:")
            print(f"  • Filas: {initial_rows:,} → {final_rows:,} (-{initial_rows-final_rows:,}, -{(1-final_rows/initial_rows)*100:.1f}%)")
            print(f"  • Memoria: {initial_memory:.1f} MB → {final_memory:.1f} MB (-{initial_memory-final_memory:.1f} MB)")
            print(f"  • Nuevas columnas: Revenue" +
                  (", Year, Month, Day, Weekday, Hour" if 'Year' in self.df_clean.columns else ""))

        return self.df_clean

# SCRIPT PRINCIPAL - Uso del Manager
if __name__ == "__main__":
    print("🚀 ONLINE RETAIL DATA MANAGER v2.0")
    print("="*70)

    # Crear instancia
    manager = OnlineRetailManager()

    # Cargar datos (intentará local primero, luego descarga)
    df = manager.load_data()

    if df is not None:
        # Limpiar datos
        df_clean = manager.clean_data()

        # Guardar versión limpia
        if df_clean is not None:
            output_file = 'online_retail_clean.csv'
            df_clean.to_csv(output_file, index=False)
            print(f"\n💾 Dataset limpio guardado como: {output_file}")

            # Análisis inicial con Pandas
            print("\n" + "="*70)
            print("🎯 ANÁLISIS INICIAL CON PANDAS")
            print("="*70)

            # Top 5 productos por ingresos
            top_products = (df_clean.groupby('Description')['Revenue']
                          .sum()
                          .sort_values(ascending=False)
                          .head(5))

            print("\n💰 Top 5 Productos por Ingresos:")
            for i, (product, revenue) in enumerate(top_products.items(), 1):
                print(f"  {i}. {product[:40]:<40} ${revenue:>12,.2f}")

            # Ventas por país
            country_sales = df_clean.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(5)

            print("\n🌍 Top 5 Países por Ventas:")
            for i, (country, revenue) in enumerate(country_sales.items(), 1):
                print(f"  {i}. {country:<20} ${revenue:>12,.2f}")

            print("\n✅ ¡Dataset listo para análisis con Pandas!")