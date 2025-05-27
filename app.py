from frontEnd.interfaz import welcome,inicio_sesion, registrar
import streamlit as st
from logica.gastosingresos import main  

if 'page' not in st.session_state:
    st.session_state['page'] = 'inicio'

if 'username' in st.session_state:
    st.session_state['page'] = 'app'  # Página principal de la app

if st.session_state['page'] == 'app':
    main()
elif st.session_state['page'] == 'inicio':
    welcome()
elif st.session_state['page'] == 'login':
    inicio_sesion()
    main()
elif st.session_state['page'] == 'registro':
    registrar()
