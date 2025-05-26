import streamlit as st
from datetime import datetime

def inicializar_datos():
    if 'transacciones' not in st.session_state:
        st.session_state.transacciones = []

def agregar_transaccion(tipo, monto, categoria, descripcion):
    nueva_transaccion = {
        'tipo': tipo,
        'monto': monto,
        'categoria': categoria,
        'descripcion': descripcion,
        'fecha': datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    st.session_state.transacciones.append(nueva_transaccion)

def calcular_totales():
    ingresos = sum(t['monto'] for t in st.session_state.transacciones if t['tipo'] == 'Ingreso')
    gastos = sum(t['monto'] for t in st.session_state.transacciones if t['tipo'] == 'Gasto')
    balance = ingresos - gastos
    return ingresos, gastos, balance

def mostrar_formulario():
    with st.sidebar:
        st.header("Agregar Transacción")
        tipo = st.radio("Tipo:", ("Ingreso", "Gasto"))
        monto = st.number_input("Monto:", min_value=0.0, step=0.01)
        categoria = st.text_input("Categoría:")
        descripcion = st.text_area("Descripción (opcional):")
        
        if st.button("Agregar"):
            if monto > 0 and categoria:
                agregar_transaccion(tipo, monto, categoria, descripcion)
                st.success("Transacción agregada!")
                st.experimental_rerun()  # REFRESCAR para mostrar actualización
            else:
                st.warning("Debes ingresar monto y categoría")

def mostrar_resumen():
    st.title(f"💰 Finanzas Personales de {st.session_state['username']}")
    
    ingresos, gastos, balance = calcular_totales()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Ingresos", f"${ingresos:,.2f}")
    with col2:
        st.metric("Total Gastos", f"${gastos:,.2f}")
    
    st.subheader(f"Balance: ${balance:,.2f}", divider="rainbow")

def mostrar_ultimas_transacciones():
    st.subheader("Últimas Transacciones")
    if st.session_state.transacciones:
        for t in reversed(st.session_state.transacciones[-10:]):
            color = "green" if t['tipo'] == 'Ingreso' else "red"
            st.markdown(
                f"<div style='border-left: 5px solid {color}; padding: 10px; margin: 5px 0;'>"
                f"<b>{t['tipo']}</b> - ${t['monto']:,.2f}<br>"
                f"{t['categoria']} - {t['descripcion']}<br>"
                f"<small>{t['fecha']}</small>"
                "</div>",
                unsafe_allow_html=True
            )
    else:
        st.info("No hay transacciones registradas aún")

def main():
    if 'username' not in st.session_state:
        st.warning("No has iniciado sesión. Por favor, inicia sesión para continuar.")
        # Aquí podrías redirigir al login o detener la app
        return
    
    inicializar_datos()
    mostrar_formulario()
    mostrar_resumen()
    mostrar_ultimas_transacciones()

    if st.button("Cerrar sesión"):
        del st.session_state['username']
        st.experimental_rerun()

if __name__ == "__main__":
    main()