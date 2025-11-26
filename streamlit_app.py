import Definitions
import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Polygon
from streamlit_folium import st_folium
from src.back.ModelController import ModelController
from sklearn.metrics import confusion_matrix, classification_report, RocCurveDisplay
from PIL import Image
from io import BytesIO


st.set_page_config(layout="wide", page_title="Segmentación semantica", page_icon="Sitios Búsquedaﾠ")


##Logo Maestria
logo = Image.open("resources/img/logo.png")
st.image(logo, width=500, use_container_width=False)

st.title(":gray[Aplicación de una red de segmentación semántica para la identificación de áreas arqueológicas en Modelos Digitales de Terreno.​​]")

##Imagen Ciudad Perdida
ciudad_perdida = Image.open("resources/img/ciudad_perdida.png")
st.image(ciudad_perdida, width=1500, use_container_width=False)
# Fuente
st.caption("Ciudad Perdida- maravilla arqueológica de América del Sur. Restos de la civilización Tayrona.")


# Subtítulo contextual
st.subheader(":gray[Proyecto de segmentacion de semantica para la identificación de áreas de interés arqueológico]")

st.subheader(":gray[Introducción:]", divider=True)
# Texto descriptivo
st.markdown("""
Este aplicativo facilita el análisis de datos geoespaciales mediante la ingesta de imágenes de un canal (DTM, PTI) y de tres canales (RGB). Su objetivo es realizar una segmentación semántica para estimar la probabilidad de presencia arqueológica a nivel de píxel, con un enfoque orientado a la topografía de Teyuna - Ciudad Perdida, Colombia.

El sistema estima la probabilidad de cada pixel de pertenecer a cualquiera de las siguientes clases:

- **Clase 1:** Templo
- **Clase 2:** Monticulo
- **Clase 3:** Hidrología
- **Clase 4:** Fondo

A través de un mapa de segmentación , tablas de resumen y exportación de resultados, esta herramienta facilita la toma de decisiones arqueológicas basada en evidencia geoespacial.
""")

# Nota aclaratoria
st.caption("Los resultados de este aplicativo son de carácter exploratorio y aunque se implementan técnicas de aprendizaje automático —herramientas computacionales diseñadas para reconocer patrones y clasificar datos a partir de ejemplos—, se ha optado por no usar el término “predicción” de forma directa. Esto se debe a que esta propuesta no busca ni pretende reemplazar la profunda labor investigativa y arqueológica, sino que propone una aproximación técnica complementaria, desde el campo de los análisis geoespaciales y el análisis supervisado de datos, para aportar insights que acoten esa labor.")

# Construccion Dataset

with st.expander(":violet[Clic acá para ver información sobre las imagenes de entrada]"):
    st.markdown("""
    Se requiere la carga de los archivos RGB, DTM y PTI, asegurando la consistencia con los canales de entrada utilizados durante el entrenamiento de la red de segmentación semántica.

    - **Imagen de Color Real (RGB):** Representa la cobertura superficial de la zona. Se compone de tres canales (Rojo, Verde y Azul).
        
    - **Modelo Digital de Terreno (DTM):** Una representación digital del relieve terrestre sin la influencia de vegetación o estructuras. Corresponde a un solo canal de datos de elevación.
    
    - **Índice de Posición Topográfica (PTI):** Derivado del DTM, este índice de un solo canal describe la posición morfológica relativa de cada píxel en el terreno (por ejemplo, si está en una cumbre, ladera o valle).  
    
    Al completar la carga, se obtendra el mapa de probabilidades, listo para su análisis externo en software especializado como 'QGIS'.
    """)


# ---------------carga de datos
st.subheader(":gray[Carga de datos:]", divider=True)
# -------------------------------
#  IMAGENES
# -------------------------------

st.write(":gray[Selecciona tus archivos]")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(":gray[**RGB**]")
    uploaded_rgb = st.file_uploader("RGB", type=["gpkg"], key="col_rgb")

with col2:
    st.markdown(":gray[**Modelo Digital de terreno**]")
    uploaded_dtm = st.file_uploader("DTM", type=["tif", "gpkg"], key="col_dtm")

with col3:
    st.markdown(":gray[**Índice de posición topográfica**]")
    uploaded_pti = st.file_uploader("PTI", type=["tif", "gpkg"], key="col_pti")

# -------------------------------
#  PREDICCIÓN DESDE GPKG - TRES MODELOS
# -------------------------------
st.markdown("---")
st.subheader(":gray[Estimación de probabilidad]", divider=True)

ctrl = ModelController()















