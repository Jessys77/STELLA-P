import streamlit as st
from dotenv import load_dotenv

# Importaciones desde la raíz 'ui'
from estudiantes.portal_estudiante import mostrar_modulo_estudiante
from control_escolar.portal_control import mostrar_modulo_control
from profesores.portal_profesor import mostrar_modulo_profesor
from aspirantes.portal_aspirante import mostrar_modulo_aspirante

load_dotenv()

st.set_page_config(
    page_title="Plataforma Escolar Inteligente - STELLA",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==========================================
# ESTILOS VISUALES - PALETA CLARA STELLA
# ==========================================
st.markdown("""
<style>
    * {
        transition: none !important;
        animation: none !important;
    }

    /* Fondo general claro */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stHeader"] {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
        font-family: "Segoe UI", Inter, Arial, sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(248, 250, 252, 0.95) !important;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    /* Contenedor principal */
    .block-container {
        padding-top: 2.5rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1300px;
    }

    /* Textos generales */
    h1 {
        color: #2563EB !important;
        font-size: 2.7rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
        margin-bottom: 0.2rem !important;
    }

    h2, h3, h4, h5, h6, p, span, label, div {
        font-family: "Segoe UI", Inter, Arial, sans-serif;
    }

    h2, h3, h4, h5, h6, p, label {
        color: #0F172A !important;
    }

    .stella-subtitle {
        font-size: 1.15rem;
        font-weight: 500;
        color: #64748B !important;
        margin-top: -0.2rem;
        margin-bottom: 2rem;
    }

    .stella-text {
        font-size: 1.2rem;
        font-weight: 600;
        color: #334155 !important;
        margin-bottom: 1.2rem;
    }

    hr {
        border: none;
        border-top: 1px solid #E5E7EB;
        margin-top: 1rem;
        margin-bottom: 2rem;
    }

    /* Tarjetas de perfil */
    .profile-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 1.5rem;
        min-height: 165px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        margin-bottom: 1rem;
    }

    .profile-card:hover {
        border-color: #2563EB;
        box-shadow: 0 10px 28px rgba(37, 99, 235, 0.14);
    }

    .profile-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }

    .profile-desc {
        color: #64748B !important;
        font-size: 0.95rem;
        line-height: 1.5;
    }

  /* Colores por perfil - todos en azul */
.student-title,
.control-title,
.teacher-title,
.candidate-title {
    color: #2563EB !important;
}

.student-card,
.control-card,
.teacher-card,
.candidate-card {
    border-top: 4px solid #2563EB;
}
/* Botones en azul */
.stButton > button,
.stFormSubmitButton > button {
    width: 100%;
    border-radius: 10px;
    padding: 0.7rem 1rem;
    font-weight: 600;
    font-size: 0.95rem;
    color: #2563EB !important;
    background-color: #FFFFFF !important;
    border: 1px solid #2563EB !important;
    box-shadow: none !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #2563EB !important;
    color: #FFFFFF !important;
    border-color: #2563EB !important;
}.profile-card:hover {
    border-color: #2563EB;
    box-shadow: 0 10px 28px rgba(37, 99, 235, 0.14);
}


    /* Inputs del login en blanco */
    .stTextInput > div {
        background-color: transparent !important;
    }

    .stTextInput div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }

    .stTextInput div[data-baseweb="input"] > div {
        background-color: #FFFFFF !important;
    }

    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
        caret-color: #2563EB !important;
        border: none !important;
        box-shadow: none !important;
    }

    .stTextInput input:focus {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
        outline: none !important;
        box-shadow: none !important;
    }

    .stTextInput div[data-baseweb="input"]:focus-within {
        border: 1px solid #2563EB !important;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.12) !important;
    }

    .stTextInput svg {
        color: #64748B !important;
        fill: #64748B !important;
    }

    .stTextInput button {
        background-color: #FFFFFF !important;
        color: #64748B !important;
        border: none !important;
    }
/* Forzar menú lateral visible */
section[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    min-width: 280px !important;
    width: 280px !important;
    background-color: #FFFFFF !important;
    border-right: 1px solid #E5E7EB !important;
}

section[data-testid="stSidebar"] > div {
    display: block !important;
    visibility: visible !important;
    background-color: #FFFFFF !important;
}

button[kind="header"],
[data-testid="collapsedControl"] {
    display: block !important;
    visibility: visible !important;
}
    /* Mensajes */
    [data-testid="stAlert"] {
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# VARIABLES DE ESTADO GLOBAL
# ==========================================
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
    st.title("STELLA")

    st.markdown(
        '<div class="stella-subtitle">Sistema de Organización Escolar</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="stella-text">Selecciona tu perfil de ingreso institucional:</div>',
        unsafe_allow_html=True
    )

    st.write("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="profile-card student-card">
            <div class="profile-title student-title"> Estudiante</div>
            <div class="profile-desc">
                Portal de reinscripciones, kardex y auditoría.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ingresar como Estudiante", key="btn_estudiante"):
            st.session_state.rol_seleccionado = "Estudiante"
            st.session_state.autenticado = False
            st.rerun()

    with col2:
        st.markdown("""
        <div class="profile-card control-card">
            <div class="profile-title control-title"> Control Escolar</div>
            <div class="profile-desc">
                Área administrativa y migración de bases de datos.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ingresar como Administración / TI", key="btn_control"):
            st.session_state.rol_seleccionado = "Control Escolar"
            st.session_state.autenticado = False
            st.rerun()

    with col3:
        st.markdown("""
        <div class="profile-card teacher-card">
            <div class="profile-title teacher-title"> Docente</div>
            <div class="profile-desc">
                Gestión de actas, grupos y cargas académicas.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ingresar como Docente", key="btn_docente"):
            st.session_state.rol_seleccionado = "Docente"
            st.session_state.autenticado = False
            st.rerun()

    with col4:
        st.markdown("""
        <div class="profile-card candidate-card">
            <div class="profile-title candidate-title"> Aspirante</div>
            <div class="profile-desc">
                Seguimiento de fichas y proceso de nuevo ingreso.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ingresar como Aspirante", key="btn_aspirante"):
            st.session_state.rol_seleccionado = "Aspirante"
            st.session_state.autenticado = False
            st.rerun()


# ==========================================
# SUB-FLUJO DE LOGIN REQUERIDO
# ==========================================
elif not st.session_state.autenticado:
    st.title(f"Acceso - {st.session_state.rol_seleccionado}")
    st.write("Introduce tu matrícula y contraseña de STELLA configurada en el sistema para validar el acceso.")
    st.write("---")

    with st.form("Formulario de Autenticación Escolar"):
        if st.session_state.rol_seleccionado == "Estudiante":
            usuario_label = "Número de Matrícula"
            usuario_default = "202213140"

        elif st.session_state.rol_seleccionado == "Control Escolar":
            usuario_label = "Clave de Usuario Root / TI"
            usuario_default = "admin_control_stella"

        elif st.session_state.rol_seleccionado == "Docente":
            usuario_label = "Número de Clave de Empleado"
            usuario_default = "DOC-TESH-455"

        else:
            usuario_label = "Número de Folio / Ficha de Aspirante"
            usuario_default = "ASP-2026-987"

        txt_user = st.text_input(usuario_label, value=usuario_default)
        txt_pass = st.text_input("Contraseña de Seguridad", type="password", value="12345")

        col_btn1, col_btn2 = st.columns([1, 3])

        with col_btn1:
            btn_login = st.form_submit_button("Entrar")

        with col_btn2:
            btn_regresar = st.form_submit_button("Cancelar / Regresar")

        if btn_regresar:
            st.session_state.rol_seleccionado = None
            st.session_state.autenticado = False
            st.rerun()

        if btn_login:
            # Validación simulada para demo
            if txt_user.strip() != "" and txt_pass.strip() != "":
                st.session_state.autenticado = True
                st.success("Autenticación exitosa.")
                st.rerun()
            else:
                st.error("El usuario y la contraseña no pueden estar vacíos.")


# ==========================================
# ACTIVACIÓN FORMAL DE LOS PORTALES
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
