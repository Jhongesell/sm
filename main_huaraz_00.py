# Importar librerías
import rasterio
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os


def read_tif(file_name):
    with rasterio.open(file_name) as src:
        data = src.read(1)  # Leemos solo la primera banda para simplificar
    return data

def plot_raster(data, title="Visualización del Raster"):
    plt.imshow(data, cmap='viridis')  # Puedes cambiar 'viridis' a otras paletas de colores
    plt.colorbar(label='Altitud')  # Etiqueta para la barra de colores
    plt.title(title)
    plt.show()

def convert_data(data):
    # Ejemplo de conversión: puedes ajustar esto según tus necesidades
    converted_data = data * 2 # Esta operación es más compleja
    return converted_data

def write_cio(data, file_name):
    # Ejemplo de escritura en un archivo .cio: ajusta según tus necesidades
    with open(file_name, 'w') as cio_file:
        for row in data:
            cio_file.write(','.join(map(str, row)) + '\n')

def main():
    # Rutas de archivos .tif
    ruta01 = r"C:\Users\jhonv\Mi unidad (jhvillanueva91@gmail.com)\PP00890-JhonGesell\01_Productos\GD_S45\img\DEM"
    ruta02 = r"C:\Users\jhonv\Mi unidad (jhvillanueva91@gmail.com)\PP00890-JhonGesell\01_Productos\GD_S45\img\LANDUSE"
    ruta03 = r"C:\Users\jhonv\Mi unidad (jhvillanueva91@gmail.com)\PP00890-JhonGesell\01_Productos\GD_S45\img\TYPESOIL"

    # Carpeta de salida
    directorio_salida = "ruta_de_salida"

    # Verificar si el directorio de salida existe, y si no, crearlo
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Lectura de archivos .tif desde las carpetas proporcionadas
    files_folder1 = [os.path.join(ruta01, file) for file in os.listdir(ruta01) if file.endswith(".tif")]
    files_folder2 = [os.path.join(ruta02, file) for file in os.listdir(ruta02) if file.endswith(".tif")]
    files_folder3 = [os.path.join(ruta03, file) for file in os.listdir(ruta03) if file.endswith(".tif")]

    # Procesamiento de archivos .tif y visualización
    for file in files_folder1 + files_folder2 + files_folder3:
        data = read_tif(file)
        converted_data = convert_data(data)
        output_file = os.path.join(directorio_salida, os.path.basename(file).replace(".tif", ".cio"))
        write_cio(converted_data, output_file)

        # Plotear el raster original
        plot_raster(data, title=f'Visualización del Raster - {os.path.basename(file)}')

        # Plotear el raster convertido (ajusta según tu lógica de conversión)
        plot_raster(converted_data, title=f'Raster Convertido - {os.path.basename(file)}')

if __name__ == "__main__":
    main()