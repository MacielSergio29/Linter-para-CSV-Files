import pandas as pd
import numpy as np

def validar_datos(archivo_entrada, archivo_log):
    # Cargar el archivo CSV
    df = pd.read_csv(archivo_entrada, encoding='utf-8')

    # Inicializar el registro de errores
    errores = []

    # Verificar la cantidad de columnas
    columnas_esperadas = ['Nombre', 'Edad', 'Correo', 'Calificacion']
    if len(df.columns) != len(columnas_esperadas) or list(df.columns) != columnas_esperadas:
        errores.append("Error: El archivo no tiene la cantidad correcta de columnas o las columnas no coinciden.")

    # Verificar que las columnas tengan datos
    if df.isnull().values.any():
        errores.append("Error: El archivo contiene celdas vacías.")

    # Verificar el tipo de datos
    tipos_esperados = {'Nombre': 'alpha', 'Edad': 'numeric', 'Correo': 'correo', 'Calificacion': 'numeric'}
    for columna, tipo_esperado in tipos_esperados.items():
        if columna not in df.columns:
            errores.append(f"Error: La columna {columna} no existe en el archivo CSV.")
            continue

        if tipo_esperado == 'numeric' and not pd.to_numeric(df[columna], errors='coerce').notnull().all():
            errores.append(f"Error: La columna {columna} no es de tipo numérico.")
        elif tipo_esperado == 'alpha' and not df[columna].str.isalpha().all():
            errores.append(f"Error: La columna {columna} no es de tipo alfabético.")
        elif tipo_esperado == 'correo' and not df[columna].str.match(r"[^@]+@[^@]+\.[^@]+").all():
            errores.append(f"Error: La columna {columna} no contiene correos electrónicos válidos.")

    # Guardar errores en el archivo de registro
    with open(archivo_log, 'w') as log_file:
        log_file.write('\n'.join(errores))

if __name__ == "__main__":
    # Cambiar con el nombre de tu archivo CSV y el nombre deseado para el archivo de registro
    archivo_entrada = 'Alumnos.csv'
    archivo_log = 'log_errores.txt'

    # Llamar a la función de validación
    validar_datos(archivo_entrada, archivo_log)
