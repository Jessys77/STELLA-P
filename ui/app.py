import streamlit as st
from dotenv import load_dotenv

# Importaciones desde la raíz 'ui'
from estudiantes.portal_estudiante import mostrar_modulo_estudiante
from control_escolar.portal_control import mostrar_modulo_control
from profesores.portal_profesor import mostrar_modulo_profesor
from aspirantes.portal_aspirante import mostrar_modulo_aspirante

load_dotenv()

st.set_page_config(page_title="Plataforma Escolar Inteligente - STELLA", page_icon="✨", layout="wide")
st.markdown("<style>* { transition: none !important; animation: none !important; }</style>", unsafe_allow_html=True)

# Variables de estado global para controlar la sesión y autenticación
if "rol_seleccionado" not in st.session_state:
    st.session_state.rol_seleccionado = None
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "traspaso_completado" not in st.session_state:
    st.session_state.traspaso_completado = False

# ==========================================
# MENÚ PRINCIPAL: SELECCIÓN DE PERFIL
# ==========================================
if st.session_state.rol_seleccionado is None:
    st.title("✨ Plataforma Escolar Inteligente")
    st.subheader("Sistema de Organizacíon Stella")
    st.write("### Selecciona tu perfil de ingreso institucional:")
    st.write("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("### 👥 Estudiante")
        st.write("Portal de reinscripciones, kardex y auditoría.")
        if st.button("Ingresar como Estudiante"):
            st.session_state.rol_seleccionado = "Estudiante"
            st.session_state.autenticado = False
            st.rerun()

    with col2:
        st.error("### ⚙️ Control Escolar")
        st.write("Área administrativa y migración de bases de datos.")
        if st.button("Ingresar como Administración / TI"):
            st.session_state.rol_seleccionado = "Control Escolar"
            st.session_state.autenticado = False
            st.rerun()

    with col3:
        st.warning("### 👨‍🏫 Docente")
        st.write("Gestión de actas, grupos y cargas académicas.")
        if st.button("Ingresar como Docente"):
            st.session_state.rol_seleccionado = "Docente"
            st.session_state.autenticado = False
            st.rerun()

    with col4:
        st.success("### 👤 Aspirante")
        st.write("Seguimiento de fichas y proceso de nuevo ingreso.")
        if st.button("Ingresar como Aspirante"):
            st.session_state.rol_seleccionado = "Aspirante"
            st.session_state.autenticado = False
            st.rerun()

# ==========================================
# SUB-FLUJO DE LOGIN REQUERIDO (SI NO ESTÁ AUTENTICADO)
# ==========================================
elif not st.session_state.autenticado:
    st.title(f"🔐 Acceso Restringido - Módulo {st.session_state.rol_seleccionado}")
    st.write("Introduce tu matricula y contraseña de Stella  configurada en el sistema para validar el acceso.")
    st.write("---")

    # Crear un contenedor visual tipo tarjeta para el Login
    with st.form("Formulario de Autenticación Escolar"):
        if st.session_state.rol_seleccionado == "Estudiante":
            usuario_label = "Número de Matrícula"
            usuario_default = "202213140"
        elif st.session_state.rol_seleccionado == "Control Escolar":
            usuario_label = "Clave de Usuario Root (TI)"
            usuario_default = "admin_control_stella"
        elif st.session_state.rol_seleccionado == "Docente":
            usuario_label = "Número de Clave de Empleado"
            usuario_default = "DOC-TESH-455"
        else:
            usuario_label = "Número de Folio / Ficha de Aspirante"
            usuario_default = "ASP-2026-987"

        txt_user = st.text_input(usuario_label, value=usuario_default)
        txt_pass = st.text_input("Contraseña de Seguridad", type="password", value="12345")

        col_btn1, col_btn2 = st.columns([1, 5])
        with col_btn1:
            btn_login = st.form_submit_button("🔑 Entrar")
        with col_btn2:
            # Botón por si se equivocaron de perfil y quieren regresar al menú principal
            if st.form_submit_button("❌ Cancelar / Regresar"):
                st.session_state.rol_seleccionado = None
                st.rerun()

        if btn_login:
            # Validación simulada (Acepta cualquier credencial en la demo para no trabarse)
            if txt_user != "" and txt_pass != "":
                st.session_state.autenticado = True
                st.success("¡Autenticación exitosa!")
                st.rerun()
            else:
                st.error("Error: El usuario o la contraseña no pueden estar vacíos.")

# ==========================================
# ACTIVACIÓN FORMAL DE LOS PORTALES (YA AUTENTICADOS)
# ==========================================
else:
    if st.session_state.rol_seleccionado == "Estudiante":
        mostrar_modulo_estudiante()

    elif st.session_state.rol_seleccionado == "Control Escolar":
        mostrar_modulo_control()

    elif st.session_state.rol_seleccionado == "Docente":
        mostrar_modulo_profesor()

    elif st.session_state.rol_seleccionado == "Aspirante":
        mostrar_modulo_aspirante()
