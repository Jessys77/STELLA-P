import streamlit as st


def mostrar_datos_generales():
    st.title("👤 Datos Generales del Estudiante")
    st.success("🟢 Estatus de Control Escolar: Sincronizado correctamente con STELLA Core.")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📋 Información Personal")
        st.info(
            "**Nombre:** Jessica Esquivel Téllez\n\n**Matrícula:** 202213140\n\n**Fecha de Nacimiento:** 21 de Julio de 2005")
    with col2:
        st.write("### 🏫 Información Académica")
        st.warning(
            "**Carrera:** Ingeniería en Sistemas Computacionales\n\n**Institución:** TESH (Huixquilucan)\n\n**Semestre:** Sexto Semestre (601-M)")