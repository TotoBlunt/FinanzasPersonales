import streamlit as st
from logica.transaction import obtener_categorias, agregar_transaccion, obtener_transacciones, calcular_totales

def mostrar_formulario(usuario_id):
    st.sidebar.header("Agregar Transacción")
    tipo = st.sidebar.radio("Tipo:", ("Ingreso", "Gasto"))
    monto = st.sidebar.number_input("Monto:", min_value=0.0, step=0.01)
    
    categorias = obtener_categorias(usuario_id, tipo)
    opciones = {c['category_name']: c['id'] for c in categorias}
    categoria_sel = st.sidebar.selectbox("Categoría:", list(opciones.keys()))
    
    descripcion = st.sidebar.text_area("Descripción (opcional):")
    
    if st.sidebar.button("Agregar"):
        if monto > 0 and categoria_sel:
            cat_id = opciones[categoria_sel]
            resp = agregar_transaccion(usuario_id, monto, cat_id, descripcion, tipo)
            if resp.status_code == 201:
                st.sidebar.success("Transacción agregada!")
                st.experimental_rerun()
            else:
                st.sidebar.error("Error al agregar transacción.")
        else:
            st.sidebar.warning("Debe ingresar monto y categoría.")

def mostrar_resumen(usuario_id):
    st.title(f"💰 Finanzas Personales de {st.session_state['username']})")
    transacciones = obtener_transacciones(usuario_id, 100)
    ingresos, gastos, balance = calcular_totales(transacciones)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Ingresos", f"${ingresos:,.2f}")
    with col2:
        st.metric("Total Gastos", f"${gastos:,.2f}")
    st.subheader(f"Balance: ${balance:,.2f}")

    st.subheader("Últimas transacciones")
    ultimas = transacciones[:10]
    if ultimas:
        for t in ultimas:
            color = "green" if t['tipo'] == 'Ingreso' else "red"
            st.markdown(
                f"<div style='border-left: 5px solid {color}; padding: 10px; margin: 5px 0;'>"
                f"<b>{t['tipo']}</b> - ${t['monto']:,.2f}<br>"
                f"{t['descripcion']}<br>"
                f"<small>{t['fecha']}</small>"
                "</div>", unsafe_allow_html=True
            )
    else:
        st.info("No hay transacciones aún.")
