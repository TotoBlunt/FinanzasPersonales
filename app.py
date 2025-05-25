from frontEnd.interfaz import welcome, login_form
import streamlit as st
# Configuración de la página
st.set_page_config(
    page_title="Finanzas Personales",
    page_icon="💵",
    layout="centered",
    initial_sidebar_state="expanded"
)
    
welcome()
login_form()