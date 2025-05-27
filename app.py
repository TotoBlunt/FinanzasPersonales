from frontEnd.interfaz import welcome, inicio_sesion, registrar
import streamlit as st
from logica.gastosingresos import main

if 'page' not in st.session_state:
    st.session_state['page'] = 'inicio'

# Si ya hay sesión iniciada, mostrar la app
if 'username' in st.session_state and st.session_state['page'] != 'app':
    st.session_state['page'] = 'app'

# Controlador de navegación
if st.session_state['page'] == 'app':
    main()
elif st.session_state['page'] == 'inicio':
    welcome()
elif st.session_state['page'] == 'login':
    inicio_sesion()
elif st.session_state['page'] == 'registro':
    registrar()
