
import streamlit as st
from utils.conexsupabase import init_supabase

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
    supabase = init_supabase()
    try:
        response = supabase.table("usuarios").insert({
            "name": username,
            "password": password
        }).execute()

        if response.data:
            st.success("Usuario registrado exitosamente.")
            return True

        # Supabase SDK moderno lanza errores como objetos o diccionarios, así que los atrapamos abajo
        st.error(f"Error al registrar usuario: {response.status_code}")
        return False

    except Exception as e:
        error_str = str(e)
        if "duplicate key" in error_str or '23505' in error_str:
            st.error("Ese nombre de usuario ya está registrado. Por favor, elige otro.")
        else:
            st.error(f"Ocurrió un error inesperado al registrar: {e}")
        return False

#Funcion para verificar  Inicio de sesión
def verificar_usuario(username, password):
    supabase = init_supabase()
    try:
        response = supabase.table("usuarios")\
            .select("*")\
            .eq("name", username)\
            .eq("password", password)\
            .execute()
        
        # Si encuentra al menos un registro, el usuario y pass son correctos
        if response.data and len(response.data) > 0:
            return True
        else:
            return False
    except Exception as e:
        st.error(f"Error al conectar con la base de datos: {e}")
        return False
