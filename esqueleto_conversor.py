# PROYECTO: Conversión de inputs de entrada que alimentan a SWAT+
# AUTOR: Jhon Gesell Villanueva Portella
# FECHA: 20/11/2023

# Descripción: Los archivos de extensión .tif seran convertidos a .cio y vinculados a la base de datos de SWAT+.
# El archivo .cio contiene la información de los atributos de los polígonos de la cuenca hidrográfica.
# El archivo .tif contiene la información de la elevación de la cuenca hidrográfica.


# Importar librerías
import rasterio
import pandas as pd
import argparse

# Ruta de los archivos de entrada: .tif
# Implementa el código para leer el archivo .tif con las rutas que te he facilitado 'Ruta01 Ruta02, Ruta03', no lo pongas como comentario

# Ruta01: "C:\Users\jhonv\Mi unidad (jhvillanueva91@gmail.com)\PP00890-JhonGesell\01_Productos\GD_S11\Inputs_SWAT_IGP_Kithner\1_Datos\3_Grillados\Data_Procesada\DEM"
# Ruta02: "C:\Users\jhonv\Mi unidad (jhvillanueva91@gmail.com)\PP00890-JhonGesell\01_Productos\GD_S11\Inputs_SWAT_IGP_Kithner\1_Datos\3_Grillados\Data_Procesada\Tipo_de_suelo"
# Ruta03: "C:\Users\jhonv\Mi unidad (jhvillanueva91@gmail.com)\PP00890-JhonGesell\01_Productos\GD_S11\Inputs_SWAT_IGP_Kithner\1_Datos\3_Grillados\Data_Procesada\Uso_de_suelo"





def read_tif(file_name):
    # código para leer el archivo .tif
    def read_tif(file_name):
    with rasterio.open(file_name) as src:
        data = src.read()
    return data
    



def convert_data(data):
    # código para convertir los datos

def write_cio(data, file_name):
    # código para escribir el archivo .cio

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    data = read_tif(args.input_file)
    converted_data = convert_data(data)
    write_cio(converted_data, args.output_file)

if __name__ == "__main__":
    main()