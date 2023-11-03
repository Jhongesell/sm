# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# main.py

# Importa el módulo para lectura de datos
from lectura_de_datos import leer_datos_adf_tif

def main():
    # Directorio donde se encuentran los archivos .adf y .tif
    data_directory = "data"
    
    # Llama a la función para leer los datos
    datos = leer_datos_adf_tif(data_directory)
    
    # Ahora puedes procesar o alimentar estos datos en el modelo SWAT+
    # Ejemplo: Imprimir la lista de archivos leídos
    print("Archivos encontrados:")
    for archivo in datos:
        print(archivo)

if __name__ == "__main__":
    main()
