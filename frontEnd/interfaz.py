import streamlit as st
import pandas as pd
from datetime import datetime

#Funcion para dar la bienvenida al usuario antes de iniciar sesión
def welcome():
    """
    Muestra un mensaje de bienvenida al usuario.
    """
    st.title("Bienvenido a la aplicación de gestión financiera 💵💵")
    st.write("Esta aplicación te ayudará a gestionar tus finanzas personales de manera eficiente. 💰")
    st.write("Por favor, inicia sesión para continuar.")
    
#Funcion para mostrar el formulario de inicio de sesión
def login_form():
    """
    Muestra un formulario de inicio de sesión.
    """
    st.title("Iniciar sesión 😊 ")
    username = st.text_input("Nombre de usuario").lower()
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar sesión"):
        # Aquí iría la lógica para verificar las credenciales del usuario
        if username == 'jose' and password == '1234' or username == 'mily' and password == '1234':
            st.success("Inicio de sesión exitoso 😃😃")
            return username
        else:
            st.error("Nombre de usuario o contraseña incorrectos 😞😞")
    else:
        st.warning("Por favor, ingresa tus credenciales")