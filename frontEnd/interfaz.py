import streamlit as st
import pandas as pd
from datetime import datetime
from logica.gastosingresos import main
from utils.conexsupabase import init_supabase
from utils.registrosInicio import get_users, insert_user,verificar_usuario

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
        if verificar_usuario(username, password):
            st.success("Inicio de sesión exitoso 😃")
            st.session_state['username'] = username
            st.session_state['page'] = 'app'  # Redireccionamos a la página principal
            #st.query_params(page="app")  # Opcional para control de navegación
            st.stop()  # Detiene la ejecución para que en el próximo ciclo se cargue `main()`
        else:
            st.error("Usuario o contraseña incorrectos 😞")

        
#Funcion para registro de usuario nuevo
def registrar():
    """
    Muestra un formulario de registro para nuevos usuarios.
    """
    st.title("Registrarse")
    new_username = st.text_input("Nombre de usuario").strip().lower()
    new_password = st.text_input("Contraseña", type="password")

    if st.button("Registrar"):
        if not new_username or not new_password:
            st.warning("Por favor, completa todos los campos.")
        else:
            success = insert_user(new_username, new_password)
            if success:
                st.success("Registro exitoso. Ahora puedes iniciar sesión.")

    if st.button("Regresar"):
        st.session_state['page'] = 'inicio'

