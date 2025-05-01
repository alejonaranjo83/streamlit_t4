import streamlit as st
import os
import pandas as pd


#LEER DATOS

base_dir = os.path.dirname(__file__)
# base_dir = "." # what is doing this line of code? 
 
sub_dir = "data_prueba" # subdirectory name

file_name = "df_total_e3.xlsx" # file name

file_path = os.path.join(base_dir, sub_dir, file_name) # join the base directory with the subdirectory and file name


df = pd.read_excel(file_path)



st.write(df)


