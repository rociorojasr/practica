import gdown
import streamlit as st
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
from streamlit_echarts import st_echarts

#id = 1Gu65mnJ_lxE0BdbkL1nTq5qaFJ1dJ9tq
@st.experimental_memo
def download_data():
     url = "https://docs.google.com/spreadsheets/d/13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM/edit#gid=46563781"
     output = 'data.csv'
     gdown.download(url,output,quiet=False)
download_data()
#df = pd.read_csv(r'C:\Users\51952\Downloads\PositivosCovid\positivos_covid.csv',sep=";", skip_blank_lines=True, parse_dates=['id_centro_vacunacion', 'id_eess'])

df = pd.read_csv('data.csv',sep = ";",  skip_blank_lines=True, nrows=1000000,parse_dates=['id_centro_vacunacion', 'id_eess'])

st.title("      CASOS POSITIVOS: COVID-19", anchor = None )
from PIL import Image
image = Image.open('covid.jpg')
st.subheader('Equipo 04:')
st.markdown("*S")

#####CONTEXTO
st.subheader("Contexto:")
st.markdown("La enfermedad por coronavirus (COVID-19) es una enfermedad infecciosa causada por el virus SARS-CoV-2. Esta enfermedad  se convirtió en una  pandemia  gracias a su forma de transmisión la cual es por vía aérea.  Causando la propagación exponencial por todo el mundo,afectando  a muchos países, originando  miles de muertes, cierre de actividades, impactos económicos, ambientales. Es por ello que  fue indispensable generar un sistema de datos para contabilizar el número de infectados, así como los departamentos del Perú con mayor incidencia de positivos , con el objetivo de tomar medidas para frenar  la propagación de este virus y evitar muertes. También fue necesario registrar  el tipo de prueba y sexo. Con todo ello los sistemas de información fueron puntos claves durante la pandemia ya que gracias  a estos datos  se pudo  tomar decisiones lo más informadas posibles y adecuar políticas que permitan una mejor inteligencia en acciones de salud.")
st.image(image)
st.subheader("Dashboard")
st.dataframe(df.head(20))
