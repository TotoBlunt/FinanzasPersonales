import streamlit as st
import pandas as pd
from datetime import datetime
from logica.gastosingresos import main
from utils.conexsupabase import init_supabase, get_users, insert_user,user_exists

#Funcion para dar la bienvenida al usuario antes de iniciar sesión
def welcome():
    """
    Muestra un mensaje de bienvenida al usuario.
    """
    st.title("Bienvenido a la aplicación de gestión financiera 💵💵")
    st.write("Esta aplicación te ayudará a gestionar tus finanzas personales de manera eficiente. 💰")
    st.write("Por favor, inicia sesión para continuar.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iniciar sesión"):
            st.session_state['page'] = 'login'
    with col2:
        if st.button("Registrarse"):
            st.session_state['page'] = 'registro'
#Funcion para mostrar el formulario de inicio de sesión
def inicio_sesion():
    """
    Muestra un formulario de inicio de sesión.
    """
    st.title("Iniciar sesión 😊")
    username = st.text_input("Nombre de usuario").lower()
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if (username == 'jose' and password == '1234') or (username == 'mily' and password == '1234'):
            st.success("Inicio de sesión exitoso 😃😃")
            st.session_state.username = username
            main()
        else:
            st.error("Nombre de usuario o contraseña incorrectos 😞😞")

    if st.button("Regresar"):
        st.session_state['page'] = 'inicio'

        
#Funcion para registro de usuario nuevo
def registrar():
    """
    Muestra un formulario de registro para nuevos usuarios.
    """
    st.title("Registrarse")
    new_username = st.text_input("Nombre de usuario").lower()
    new_password = st.text_input("Contraseña", type="password")

    if st.button("Registrar"):
        if new_username and new_password:
            
            if user_exists(new_username):
                st.error("El nombre de usuario ya existe. Por favor, elige otro.")
            else:
                insert_user(new_username, new_password)
                st.success("Registro exitoso. Ahora puedes iniciar sesión.")
        else:
            st.warning("Por favor, completa todos los campos")

    if st.button("Regresar"):
        st.session_state['page'] = 'inicio'

