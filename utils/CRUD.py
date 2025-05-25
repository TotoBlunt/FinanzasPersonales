#Modulos para CRUD en supabase
from supabase import Client
from typing import List, Dict, Any
from utils.conexsupabase import create_supabase_client
import pandas as pd
from datetime import datetime

# Crear el cliente de Supabase
supabase: Client = create_supabase_client()

#Funcion para insertar un usuario
def insert_transaction(user_id: str, date: str, type_: str, amount: float, category: str, description: str):
    data = {
        "user_id": user_id,
        "date": date,
        "type": type_,
        "amount": amount,
        "category": category,
        "description": description
    }
    return supabase.table("transactions").insert(data).execute()

#Funcion para ver la transacción del usuario
def get_transactions(user_id: str):
    response = supabase.table("transactions").select("*").eq("user_id", user_id).execute()
    return pd.DataFrame(response.data)


