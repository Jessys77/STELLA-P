import streamlit as st


def mostrar_cursos_extracurriculares():
    st.title("🏆 Créditos y Cursos Extracurriculares")
    st.caption("Validación de actividades complementarias obligatorias para titulación.")

    st.write("### 📜 Cursos Registrados")
    st.info("🥇 **Taller de Desarrollo de Videojuegos (Unity):** 2 Créditos - Completado")
    st.info("♟️ **Torneo de Ajedrez Stella:** 1 Crédito - Completado")
    st.warning("🌐 **Bootcamp Blockchain (Stellar/Sui):** En proceso de validación")

    st.progress(75)
    st.caption("Progreso de liberación: 3 de 4 créditos necesarios.")