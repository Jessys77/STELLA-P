import streamlit as st
from dotenv import load_dotenv

# IMPORTACIONES DE TUS CARPETAS INDEPENDIENTES
from estudiantes.portal_estudiante import mostrar_modulo_estudiante
from control_escolar.portal_control import mostrar_modulo_control
from profesores.portal_profesor import mostrar_modulo_profesor
from aspirantes.portal_aspirante import mostrar_modulo_aspirante

load_dotenv()

st.set_page_config(page_title="Plataforma Escolar Inteligente - STELLA", page_icon="✨", layout="wide")
st.markdown("<style>* { transition: none !important; animation: none !important; }</style>", unsafe_allow_html=True)

if "rol_seleccionado" not in st.session_state:
    st.session_state.rol_seleccionado = None
if "traspaso_completado" not in st.session_state:
    st.session_state.traspaso_completado = False

# ORQUESTADOR CENTRAL
if st.session_state.rol_seleccionado is None:
    st.title("✨ Plataforma Escolar Inteligente")
    st.subheader("Tecnológico de Estudios Superiores de Huixquilucan")
    st.write("### Selecciona tu perfil de ingreso:")
    st.write("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.info("### 👥 Estudiante")
        if st.button("Ingresar como Estudiante"):
            st.session_state.rol_seleccionado = "Estudiante"
            st.rerun()

    with col2:
        st.error("### ⚙️ Control Escolar")
        if st.button("Ingresar como Administración / TI"):
            st.session_state.rol_seleccionado = "Control Escolar"
            st.rerun()

    with col3:
        st.warning("### 👨‍🏫 Docente")
        if st.button("Ingresar como Docente"):
            st.session_state.rol_seleccionado = "Docente"
            st.rerun()

    with col4:
        st.success("### 👤 Aspirante")
        if st.button("Ingresar como Aspirante"):
            st.session_state.rol_seleccionado = "Aspirante"
            st.rerun()

# ACTIVACIÓN DE CADA MÓDULO INDEPENDIENTE
elif st.session_state.rol_seleccionado == "Estudiante":
    mostrar_modulo_estudiante()

elif st.session_state.rol_seleccionado == "Control Escolar":
    mostrar_modulo_control()

elif st.session_state.rol_seleccionado == "Docente":
    mostrar_modulo_profesor()

elif st.session_state.rol_seleccionado == "Aspirante":
    mostrar_modulo_aspirante()
