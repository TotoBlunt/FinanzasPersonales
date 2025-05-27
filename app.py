from frontEnd.interfaz import welcome, inicio_sesion, registrar
import streamlit as st
from logica.gastosingresos import main  

if 'username' in st.session_state:
    main()
else:
    if st.session_state['page'] == 'inicio':
        welcome()
    elif st.session_state['page'] == 'login':
        inicio_sesion()
    elif st.session_state['page'] == 'registro':
        registrar()

