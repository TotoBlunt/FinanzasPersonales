from frontEnd.interfaz import welcome, inicio_sesion, registrar
import streamlit as st
from logica.gastosingresos import main  

# Inicializa página si no está
if 'page' not in st.session_state:
    st.session_state['page'] = 'inicio'

# Redirección si ya hay sesión activa
if 'username' in st.session_state and st.session_state['page'] != 'app':
    st.session_state['page'] = 'app'

# Control de navegación
if st.session_state['page'] == 'app':
    main()
elif st.session_state['page'] == 'inicio':
    welcome()
elif st.session_state['page'] == 'login':
    inicio_sesion()
elif st.session_state['page'] == 'registro':
    registrar()
