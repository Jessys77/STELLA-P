import streamlit as st

def mostrar_modulo_profesor():
    st.title(" Panel Docente (En construcción)")
    st.warning("Módulo en desarrollo por el equipo técnico.")
    if st.button(" Volver al Menú Principal"):
        st.session_state.rol_seleccionado = None
        st.rerun()