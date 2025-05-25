#Librerias para la conexión a Supabase
import os
from supabase import create_client, Client
import streamlit as st

# Obtener las variables de entorno  
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
#funcion para crear el cliente de supabase
def init_supabase() -> Client:
    """
    Inicializa el cliente de Supabase y lo almacena en st.session_state.
    Así, la conexión persiste a través de los reruns de Streamlit.
    """
    if "supabase_client" not in st.session_state:
        # Es buena práctica cargar credenciales desde variables de entorno
        # para mayor seguridad y flexibilidad.
        # Puedes definirlas en un archivo .env si usas dotenv,
        # o directamente en la configuración de tu despliegue (ej. en Supabase/Vercel).
        SUPABASE_URL = os.getenv("SUPABASE_URL")
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        if not SUPABASE_URL or not SUPABASE_KEY:
            st.error("Por favor, configura las variables de entorno SUPABASE_URL y SUPABASE_KEY.")
            st.stop()

        try:
            st.session_state.supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
            st.success("Conexión a Supabase establecida.")
        except Exception as e:
            st.error(f"Error al conectar con Supabase: {e}")
            st.stop()
    return st.session_state.supabase_client

#Funcion para obtener los datos de la tabla de usuarios
def get_users():
    """
    Obtiene los datos de la tabla de usuarios desde Supabase.
    """
    supabase = init_supabase()
    try:
        response = supabase.table("usuarios").select("*").execute()
        if response.status_code == 200:
            return response.data
        else:
            st.error(f"Error al obtener los datos de usuarios: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error al conectar con Supabase: {e}")
        return []

#Funcion para ingresar un nuevo usuario
def insert_user(username, password):
    """
    Inserta un nuevo usuario en la tabla de usuarios en Supabase.
    """
    supabase = init_supabase()
    try:
        response = supabase.table("usuarios").insert({"name": username, "password": password}).execute()
        if response.status_code == 201:
            st.success("Usuario registrado exitosamente.")
        else:
            st.error(f"Error al registrar el usuario: {response.status_code}")
    except Exception as e:
        st.error(f"Error al conectar con Supabase: {e}")