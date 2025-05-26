from utils.conexsupabase import init_supabase
from datetime import datetime

def obtener_categorias(usuario_id, tipo):
    supabase = init_supabase()
    filtro = f"(is_custom.eq.false,usuario_id.eq.{usuario_id})"
    resp = supabase.table("Categorias").select("id, category_name").eq("category_type", tipo).or_(filtro).execute()
    if resp.status_code == 200:
        return resp.data
    return []

def agregar_transaccion(usuario_id, monto, categoria_id, descripcion, tipo):
    supabase = init_supabase()
    # Agregar una nueva transacción
    
    data = {
        "monto": monto,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "description": descripcion,
        "transaction_type": tipo,
        "category_id": categoria_id,
        "user_id": usuario_id
    }
    resp = supabase.table("transaction").insert(data).execute()
    return resp

def obtener_transacciones(usuario_id, limite=10):
    supabase = init_supabase()
    # Obtener las últimas transacciones del usuario
    resp = supabase.table("transaction").select("*").eq("user_id", usuario_id).order("created_at", desc=True).limit(limite).execute()
    if resp.status_code == 200:
        return resp.data
    return []

def calcular_totales(transacciones):
    ingresos = sum(t['monto'] for t in transacciones if t['transaction_type'] == 'Ingreso')
    gastos = sum(t['monto'] for t in transacciones if t['transaction_type'] == 'Gasto')
    return ingresos, gastos, ingresos - gastos
