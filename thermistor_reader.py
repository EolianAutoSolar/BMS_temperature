import pandas as pd
import time
import os
import numpy as np

# Definir la asignación de termistores a módulos
module_mapping = {
    1: [41], 2: [43], 3: [46], 4: [47, 48], 5: [49, 50], 6: [51], 7: [54, 55],
    8: [56], 9: [57, 58], 10: [22], 11: [21, 25], 12: [23, 24], 13: [27, 28],
    14: [29, 30], 15: [31, 32], 16: [33, 34], 17: [35], 18: [39], 19: [37, 38],
    20: [13, 14], 21: [11, 12], 22: [7, 8], 23: [10], 24: [6], 25: [4], 26: [1],
    27: [36], 28: [np.nan]
}

# Invertir el mapeo para facilitar la asignación
termistor_to_module = {}
for module, termistors in module_mapping.items():
    for termistor in termistors:
        termistor_to_module[termistor] = module

# Cargar el archivo CSV
file_path = 'thermistor_log.csv'
data = pd.read_csv(file_path)

# Extraer las columnas de termistores (asumiendo que están en las columnas 5 a 65)
termistor_columns = data.columns[5:65]

# Función para renombrar las columnas con el formato "Thermistor n-m"
def rename_columns(columns):
    new_columns = []
    for col in columns:
        termistor_number = int(col.split(' ')[-1])
        module_number = termistor_to_module.get(termistor_number, 'NaN')
        new_columns.append(f"Thermistor {termistor_number}-{module_number}")
    return new_columns

# Renombrar las columnas de termistores
new_termistor_columns = rename_columns(termistor_columns)
data.rename(columns=dict(zip(termistor_columns, new_termistor_columns)), inplace=True)

# Función para mostrar las filas reemplazando el contenido cada segundo
def display_rows(data):
    for index, row in data.iterrows():
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        # Mostrar solo las primeras 65 columnas
        print(row.iloc[:65].to_string())
        time.sleep(1)

# Ejecutar la función
display_rows(data)
