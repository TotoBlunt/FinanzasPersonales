from frontEnd.interfaz import welcome, login_form
import streamlit as st
# Inicializar lista de transacciones en session_state
if 'transacciones' not in st.session_state:
    st.session_state.transacciones = []
    
    welcome()
    login_form()