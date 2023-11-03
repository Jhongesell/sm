# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:59:10 2023

@author: jhonv
"""

# lectura_de_datos.py

import os

def leer_datos_adf_tif(directory):
    """
    Lee archivos con extensiones .adf o .tif en un directorio.

    Args:
        directory (str): La ruta al directorio que contiene los archivos.

    Returns:
        list: Una lista de nombres de archivos encontrados.
    """
    archivos = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".adf") or file.endswith(".tif"):
                archivos.append(os.path.join(root, file))
    return archivos
