#Librerias para la conexión a Supabase
import os
from supabase import create_client, Client
from dotenv import load_dotenv
# Cargar las variables de entorno desde el archivo .env
load_dotenv()
# Obtener las variables de entorno  
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

#funcion para crear el cliente de supabase
def create_supabase_client() -> Client:
    """
    Crea un cliente de Supabase utilizando las credenciales de entorno.
    
    Returns:
        Client: Un cliente de Supabase.
    """
    # Crear el cliente de Supabase
    supabase: Client = create_client(url, key)
    return supabase
