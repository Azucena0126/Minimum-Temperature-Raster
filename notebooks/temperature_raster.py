import geopandas as gpd
import rasterio
import rioxarray 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from unidecode import unidecode
from rasterio.plot import show
import os


ruta = r'../POAAR_DATA_V2/test/2025-Gasto-Diario.zip'

import rasterio

# Ruta al archivo
archivo = "Prec_raster.tif"

archivo = r'C:\Users\USUARIO\Documents\GitHub\Minimum-Temperature-Raster\data\raw\tmin_raster.tif'

# Abrir el archivo
with rasterio.open(archivo) as src:
    print("Ancho:", src.width)
    print("Alto:", src.height)
    print("Número de bandas:", src.count)
    print("Sistema de coordenadas:", src.crs)
    print("Transformación (afín):", src.transform)

    # Leer los datos de la primera banda
    banda1 = src.read(1)
    banda2 = src.read(2)
    banda3 = src.read(3)
    banda4 = src.read(4)
    banda5 = src.read(5)