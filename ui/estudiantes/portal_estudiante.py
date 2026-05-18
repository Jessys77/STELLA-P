import os
import sys
import streamlit as st

# ==========================================
# CONFIGURACIÓN DE RUTA
# ==========================================
directorio_actual = os.path.dirname(os.path.abspath(__file__))

if directorio_actual not in sys.path:
    sys.path.append(directorio_actual)

# Importaciones de módulos del estudiante
from datos_generales import mostrar_datos_generales
from kardex import mostrar_kardex
from pagos_servicios import mostrar_pago_servicios
from horario import mostrar_horario
from calificaciones import mostrar_calificaciones
from cursos_extracurriculares import mostrar_cursos_extracurriculares
from evaluacion_docente import mostrar_evaluacion_docente


# ==========================================
# ESTILOS DEL MÓDULO ESTUDIANTE
# ==========================================
def aplicar_estilo_modulo_estudiante():
    st.markdown("""
<style>
    /* Ocultar sidebar nativo de Streamlit */
    [data-testid="stSidebar"] {
        display: none !important;
    }

    /* Contenedor general */
    .block-container {
        padding-top: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1500px !important;
    }

    /* Tarjeta principal del menú */
    .menu-panel {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 18px;
        padding: 1.3rem;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        margin-bottom: 1rem;
    }

    .menu-title {
        color: #2563EB;
        font-size: 1.45rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }

    .menu-subtitle {
        color: #64748B;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }

    /* Tarjeta de datos del alumno */
    .menu-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-left: 4px solid #2563EB;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.04);
    }

    .menu-card p {
        color: #0F172A !important;
        margin: 0.35rem 0;
        font-size: 0.92rem;
    }

    /* Texto general */
    label, p, span {
        color: #0F172A !important;
        font-family: "Segoe UI", Inter, Arial, sans-serif;
    }

    /* Opciones del radio */
    div[role="radiogroup"] label {
        background-color: #FFFFFF !important;
        border: 1px solid transparent !important;
        border-radius: 10px !important;
        padding: 0.45rem 0.55rem !important;
        margin-bottom: 0.25rem !important;
    }

    div[role="radiogroup"] label:hover {
        background-color: #EFF6FF !important;
        border-color: #BFDBFE !important;
    }

    /* Botones */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        padding: 0.65rem 1rem;
        font-weight: 600;
        color: #2563EB !important;
        background-color: #FFFFFF !important;
        border: 1px solid #2563EB !important;
        box-shadow: none !important;
    }

    .stButton > button:hover {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border-color: #2563EB !important;
    }

    /* Separador */
    hr {
        border: none;
        border-top: 1px solid #E5E7EB;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# MÓDULO ESTUDIANTE
# ==========================================
def mostrar_modulo_estudiante():
    aplicar_estilo_modulo_estudiante()

    col_menu, col_contenido = st.columns([1.15, 4.85], gap="large")

    # ======================================
    # MENÚ LATERAL PROPIO
    # ======================================
    with col_menu:
        st.markdown("""
<div class="menu-panel">
    <div class="menu-title"> STELLA</div>
    <div class="menu-subtitle">Módulo Estudiante</div>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="menu-card">
    <p><strong> Matrícula:</strong> 202213140</p>
    <p><strong> Stella:</strong> Activo</p>
</div>
""", unsafe_allow_html=True)

        apartado = st.radio(
            "Navegación:",
            [
                " Datos Generales",
                " Kardex",
                " Pago de Servicios",
                " Horario",
                " Calificaciones",
                " Cursos Extracurriculares",
                " Evaluación Docente",
                " Asistente IA STELLA"
            ],
            key="menu_estudiante"
        )

        st.write("---")

        cerrar_sesion = st.button("Cerrar Sesión")

    # ======================================
    # CONTENIDO PRINCIPAL
    # ======================================
    with col_contenido:
        if cerrar_sesion:
            st.session_state.rol_seleccionado = None
            st.session_state.autenticado = False
            st.rerun()

        if apartado == " Datos Generales":
            mostrar_datos_generales()

        elif apartado == " Kardex":
            mostrar_kardex()

        elif apartado == " Pago de Servicios":
            mostrar_pago_servicios()

        elif apartado == " Horario":
            mostrar_horario()

        elif apartado == " Calificaciones":
            mostrar_calificaciones()

        elif apartado == " Cursos Extracurriculares":
            mostrar_cursos_extracurriculares()

        elif apartado == " Evaluación Docente":
            mostrar_evaluacion_docente()

        elif apartado == " Asistente IA STELLA":
            st.title("Asistente de Auditoría IA")
            st.caption("Capa de conocimiento analítico del estudiante.")
            st.chat_message("assistant").markdown(
                "Hola Jessica. Estoy lista para responder cualquier duda sobre tu avance de créditos, "
                "calificaciones en Kardex o tu tira de materias."
            )


