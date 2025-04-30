import pandas as pd
import streamlit as st
import os

from pathlib import Path
 

# Using pathlib, create a path for a directory that is two directories up from the current file's location. Don´t do any other process (i.e. st.set_page_config) before setting the path. 


path = Path(__file__).resolve().parent.parent.parent / "data/processed"

st.write(path)



os.listdir(path)
os.chdir(path)





st.title("Prueba de rutas en Streamlit")

st.write("Prueba para manipular rutas en una app de Streamlit")


st.image('ImagenCentral.png', width=850, use_container_width='always')

df = pd.read_excel('df_total_e3.xlsx')

st.write(df)