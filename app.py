import streamlit as st
from frontEnd.interfaz import welcome, inicio_sesion, registrar
from logica.gastosingresos import main

if 'page' not in st.session_state:
    st.session_state['page'] = 'inicio'

if 'username' in st.session_state:
    # Usuario logueado, mostrar app principal
    main()
else:
    # Usuario no logueado, mostrar pantallas de bienvenida, login o registro
    if st.session_state['page'] == 'inicio':
        welcome()
    elif st.session_state['page'] == 'login':
        inicio_sesion()
    elif st.session_state['page'] == 'registro':
        registrar()

