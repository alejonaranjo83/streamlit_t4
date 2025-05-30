import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import os



#LEER DATOS (cambiando el directorio de trabajo... genera error luego para leer directorio de 'pages')

# base_dir = os.path.dirname(__file__)

# sub_dir = "data" # subdirectory name

# path = os.path.join(base_dir, sub_dir)

# os.listdir(path)
# os.chdir(path)




st.set_page_config(
    page_title="Habitar Macondo", layout='wide',
    # page_icon="👋",  
    initial_sidebar_state='expanded'
)



# Use 'openpyxl' library to read the Excel file
# df = pd.read_excel("df_total_e3.xlsx", engine='openpyxl')

# st.write(df)
# st.write(path)


st.title("Habitar Macondo")



with st.sidebar.container(height=470, border=0):
    st.write('En el corazón de la zona bananera del Caribe colombiano, donde el tiempo parece detenerse y la magia se entrelaza con la realidad, se encuentra Guacamayal. Te invitamos a repensar el destino de un lugar que, en la versión de Gabo, desapareció en medio de la desdicha y el olvido. Tú, junto con otros, tendrás la oportunidad de escribir un nuevo relato para este pueblo encantado, donde los sueños de sus habitantes florecerán en cada rincón, transformando la desdicha en esperanza y el olvido en memoria viva.  \n \n Tu misión consiste en transformar a Guacamayal en un paraíso regenerativo, donde su hábitat, coherente con los retos actuales, mitiga el impacto de la humanidad sobre el medio ambiente y se adapta al Cambio Climático. En conjunto con tu equipo, adoptarás roles inspirados en icónicos personajes de "Cien Años de Soledad", explorando alternativas para colaborar, aprovechando los recursos naturales de manera sabia y fomentando propuestas económicas basadas en la cooperatividad y el diálogo entre diversas partes interesadas en el territorio.  \n \n En el camino, generarás posibilidades para fortalecer los lazos familiares que sostienen la comunidad y fomentarás la interacción entre los habitantes a escala local. Además, reinterpretarás las ricas tradiciones culturales de gaiteros, tejidos y comidas típicas, infundiendo nueva vida a las costumbres ancestrales y atrayendo un turismo responsable movido por el tren.  \n \n Cada equipo, compuesto por estrategas, tácticos y activadores, deberá enfrentar desafíos y tomar decisiones que definirán el futuro de Guacamayal. A través de la creación gráfica, tridimensional y textual, los debates, el análisis y la activación consciente de tu atención, te sumergirás en una experiencia que combina la magia del realismo mágico con la urgencia de un mundo en constante cambio. Así, Guacamayal renacerá, no como un recuerdo de soledad, sino como un faro de esperanza y renovación.')




#CONTENIDO PRINCIPAL


# st.image('ImagenCentral.png', width=100, use_column_width=True)


st.image('ImagenCentral.png', width=850, use_container_width='always')


col = st.columns((0.33, 0.33, 0.33), gap='small')

with col[0]:
    st.image('Miniatura1_roles.png', use_container_width='always')

with col[1]:
    st.image('Miniatura2_equipos.png', use_container_width='always')

with col[2]:
    st.image('Miniatura3_entornos.png', use_container_width='always')

st.image('Formulac_desafioB.png', use_container_width='always')