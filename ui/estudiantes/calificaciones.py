import streamlit as st


def mostrar_calificaciones():
    st.title("📊 Calificaciones del Parcial Activo")
    st.caption("Consulta rápida del rendimiento en el periodo en curso.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("💻 **Programación**\n\n* Parcial 1: 95\n* Parcial 2: 90\n* **Promedio: 92.5**")
    with col2:
        st.info("📐 **Álgebra Lineal**\n\n* Parcial 1: 85\n* Parcial 2: 80\n* **Promedio: 82.5**")
    with col3:
        st.info("⚛️ **Física Mecánica**\n\n* Parcial 1: 75\n* Parcial 2: 88\n* **Promedio: 81.5**")