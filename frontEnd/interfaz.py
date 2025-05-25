import streamlit as st
import pandas as pd
from datetime import datetime
from logica.gastosingresos import main

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
    
    if st.button("Iniciar sesión"):
        st.title("Iniciar sesión 😊 ")
        username = st.text_input("Nombre de usuario").lower()
        password = st.text_input("Contraseña", type="password")
        # Aquí iría la lógica para verificar las credenciales del usuario
        if username == 'jose' and password == '1234' or username == 'mily' and password == '1234':
            st.success("Inicio de sesión exitoso 😃😃")
            #mantener la sesion activa
            st.session_state.username = username
            # Llamar a la función principal de la aplicación sin perder el estado de la sesión
            main()
            return username
        else:
            st.error("Nombre de usuario o contraseña incorrectos 😞😞")
    elif st.button("Registrarse"):
        st.title("Registrarse")
        new_username = st.text_input("Nombre de usuario").lower()
        new_password = st.text_input("Contraseña", type="password")
        if new_username and new_password:
            # Aquí iría la lógica para registrar al nuevo usuario
            #Guardar el usuario en el supabase registrado
            # supabase.table('usuarios').insert({"username": new_username, "password": new_password}).execute()
            # Simulación de registro exitoso
            st.success("Registro exitoso. Ahora puedes iniciar sesión.")
        else:
            st.warning("Por favor, completa todos los campos")
    else:
        st.warning("Por favor, ingresa tus credenciales")