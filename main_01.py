# -*- coding: utf-8 -*-
# Agrega un mensaje para verificar que el script se ejecutó
print("El script main_01.py se está ejecutando.")

# Importa el módulo para lectura de datos
from convertFromArc import ConvertFromArc

def main():
    # Directorio donde se encuentran los archivos .adf y .tif
    data_directory = "data"

    # Crea una instancia del convertidor
    convertor = ConvertFromArc(data_directory)

    # Ejecuta la conversión
    convertor.run()

if __name__ == "__main__":
    main()

