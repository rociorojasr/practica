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
st.subheader("DESCRIPCION DEL DATASET:")
st.markdown("Para los presentes graficos se consideraron los siguientes datos: Sexo, Departamento, Metodo de prueba  y  fecha de resultados, estos datos fueron elegidos por su importacia para generar  un informe  oportuno de la situacion del covid y poder tomar la decisiones pertinentes.")
st.markdown("- Sexo: Este dato es muy relevante ya que muestra si durante el intervalo que duro la pandemia fueron mas afectados los hombres o mujeres")
st.markdown("- Departamento: Los datos que representan a los casos positivos por covid en departamentos se realizó una recopilación de los casos positivos por provincias y distritos.")
st.markdown("- Método de prueba: Estos datos son importantes para saber cual de ellos se utilizó más dependiendo el lugar y la cantidad en total .")
st.markdown("- Fecha de resultados: Estos datos son muy relevantes ya que se puede determinar mediante ella en qué periodo del año fue subiendo o bajando los casos de covid.")       
st.subheader("Guia de usuario:")
st.markdown("- Gráfico circular de MÉTODOS: Muestra la cantidad  de pruebas tomadas según el tipo de método aplicado para el diagnóstico de la enfermedad, con esto podemos observar en el en Perú durante este periodo de pandemia las más utilizadas fueron las pruebas antigénicas (AG).")
st.markdown("- Gráfico de barras por SEXO : Este gráfico nos muestra la cantidad infectados por sexo de  COVID-19. Asimismo nos muestra la diferencia, para estimar  que género es el más vulnerable.")
st.markdown("- Gráfico de barras por DEPARTAMENTOS: Este gráfico representa el número de infectados por covid - 19, en los distintos departamentos del Perú. Además de la interpretación de cómo en uno tiene más casos que en otros departamentos pudiendo deducir que el contagio fue más acelerado en algunos de estos departamentos. ")
st.markdown("- Gráfico de dispersión por FECHA DE RESULTADOS: En este gráfico se muestra el número de casos positivos según la fecha de resultados, el cual está dividido en periodos trimestrales del mes de abril del año 2020 hasta el mes de abril del 2022, en donde los picos más altos de infectados se alcanzaron en los meses de julio a octubre del 2020.")
option = st.selectbox(
     'Seleccione el tipo de gráfico',
     ('Gráfico circular de MÉTODOS', 'Gráfico de barras por SEXO ', 'Gráfico de barras por DEPARTAMENTOS', "Gráfico de dispersión por FECHA DE RESULTADOS"))
st.write('Tu seleccionaste:', option)
if option == "Gráfico circular de MÉTODOS":
    tipo1=df["METODODX"].value_counts().PCR
    tipo2=df["METODODX"].value_counts().AG
    tipo3=df["METODODX"].value_counts().PR
    options = {
        "title": {"text": " ", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
        "series": [
            {
                "name": "Tipo de prueba",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": int(tipo1), "name": "PCR"},
                    {"value": int(tipo2), "name": "AG"},
                    {"value": int(tipo3), "name": "PR"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    st_echarts(
        options=options, height="600px",
    )
#Segundo grafico
elif option == "Gráfico de barras por SEXO ":
    st.subheader("Gráfico de barras por SEXO ")
    tipo2=df["SEXO"].value_counts().FEMENINO
    tipo3=df["SEXO"].value_counts().MASCULINO
    b = (
        Bar()
        .add_xaxis(["FEMENINO", "MASCULINO"])
        .add_yaxis(
            "Casos positivos por sexo", [int(tipo2),int(tipo3)]
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=" "
            ),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    st_pyecharts(b)
#Tercer grafico
elif option == "Gráfico de barras por DEPARTAMENTOS":
    st.subheader("Gráfico de barras por DEPARTAMENTOS")
    L = df[['DEPARTAMENTO', 'METODODX']].groupby('DEPARTAMENTO').count()
    st.bar_chart(L)
##Cuarto grafico
elif option == "Gráfico de dispersión por FECHA DE RESULTADOS":
    st.subheader("Gráfico de dispersión por FECHA DE RESULTADOS")
    L = df[['FECHA_RESULTADO', 'METODODX']].groupby('FECHA_RESULTADO').count()
    st.line_chart(L)
