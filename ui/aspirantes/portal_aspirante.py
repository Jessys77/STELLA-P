import streamlit as st

def mostrar_modulo_aspirante():
    st.title("👤 Portal de Aspirantes (En construcción)")
    st.info("Módulo disponible en la siguiente fase de actualización.")
    if st.button(" Volver al Menú Principal"):
        st.session_state.rol_seleccionado = None
        st.rerun()