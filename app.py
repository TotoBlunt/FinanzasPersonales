import streamlit as st
from frontEnd.interfaz import welcome, inicio_sesion, registrar
from logica.gastosingresos import main

# Inicializa estado
if 'page' not in st.session_state:
    st.session_state['page'] = 'inicio'

# Renderiza según el estado
if 'username' in st.session_state and st.session_state['page'] == 'app':
    main()

    # Botón de cerrar sesión
    if st.button("Cerrar sesión"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
else:
    if st.session_state['page'] == 'inicio':
        welcome()
    elif st.session_state['page'] == 'login':
        inicio_sesion()
    elif st.session_state['page'] == 'registro':
        registrar()

