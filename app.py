from frontEnd.interfaz import welcome,inicio_sesion, registrar
import streamlit as st

if 'page' not in st.session_state:
    st.session_state['page'] = 'inicio'

if st.session_state['page'] == 'inicio':
    welcome()
elif st.session_state['page'] == 'login':
    inicio_sesion()
elif st.session_state['page'] == 'registro':
    registrar()
    
