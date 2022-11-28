@@ -19,6 +19,8 @@ def download_data():
download_data()

###################################################
st.sidebar.header("sidebar")
st.header("sidebar")
#descripcion inicial
st.title("Centros de vacunación")
st.subheader("Integrantes")
st.write(""" - Aguilar Rojas, Enith""")  
st.write(""" - Fuertes Lizarbe, Mirko""")
st.write(""" - Rojas Rua, Rocio""")
st.subheader("¿Cual es el objetivo:") 
st.write("""Facilitar al usuario la disponibilidad de centros de vacunación, dada por una estrategia para poder promocionar y facilitar la Vacunación en el país""") 
st.subheader("Contexto") 
st.write("""holi""") 
st.subheader("¿Cuáles son los síntomas del Coronavirus?") 
##############################################################################
col1, col2, col3= st.columns(3)
with col1:
    st.subheader("Síntomas habituales") 
    st.write("""- Fiebre""")  
    st.write("""- Cansancio""")
    st.write("""- Tos""")
    st.write("""- Pérdida del gusto o del olfato        
             """)
