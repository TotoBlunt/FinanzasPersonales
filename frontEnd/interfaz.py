import streamlit as st
import pandas as pd
from datetime import datetime
from logica.gastosingresos import main
from utils.conexsupabase import init_supabase, get_users, insert_user

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
        if st.button("Ingresar"):
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
        if st.button("Registrar"):
            # Ingresar el nuevo usuario en la base de datos
            if new_username and new_password:
                # Aquí iría la lógica para registrar al nuevo usuario
                # Por ejemplo, verificar si el nombre de usuario ya existe
                existing_users = get_users()
                if any(user['name'] == new_username for user in existing_users):
                    st.error("El nombre de usuario ya existe. Por favor, elige otro.")
                else:
                    # Insertar el nuevo usuario en la base de datos
                    insert_user(new_username, new_password)
                    st.success("Registro exitoso. Ahora puedes iniciar sesión.")
            else:
                st.warning("Por favor, completa todos los campos")
        else:
            st.warning("Por favor, completa todos los campos")
    #Boton para regresar a la pantalla de inicio
    elif st.button("Regresar"):
        st.session_state.username = None
            
    else:
        st.warning("Por favor, ingresa tus credenciales")
        
# Para ejecutar esta pagina directamente,util para desarrollo individual
if __name__ == "__main__":
    login_form()