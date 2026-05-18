import os
import sys
import streamlit as st

# MÁGIA DE RUTA SEVERA: Le dice a Python exactamente dónde está parado este archivo
# y agrega su propia carpeta ('estudiantes') al buscador global de módulos.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
if directorio_actual not in sys.path:
    sys.path.append(directorio_actual)

# Al hacer lo de arriba, ya podemos importar los archivos DIRECTO por su nombre
# ¡Sin importar si Streamlit corre desde ui, desde la raíz o desde otra carpeta!
from datos_generales import mostrar_datos_generales
from kardex import mostrar_kardex
from pagos_servicios import mostrar_pago_servicios
from horario import mostrar_horario
from calificaciones import mostrar_calificaciones
from cursos_extracurriculares import mostrar_cursos_extracurriculares
from evaluacion_docente import mostrar_evaluacion_docente


def mostrar_modulo_estudiante():
    st.sidebar.markdown("## 🎓 Menú SIE Estudiante")
    st.sidebar.write("👤 **Matrícula:** 202213140")
    st.sidebar.write("🏫 **Plantel:** TESH")
    st.sidebar.write("---")

    # MENÚ COMPLETO BASADO EN TU NUEVA PROPUESTA DE ARQUITECTURA
    apartado = st.sidebar.radio(
        "Navegación:",
        [
            "👤 Datos Generales",
            "📜 Kardex",
            "💳 Pago de Servicios",
            "🗓️ Horario",
            "📊 Calificaciones",
            "🏆 Cursos Extracurriculares",
            "✍️ Evaluación Docente",
            "💬 Asistente IA STELLA"
        ]
    )

    st.sidebar.write("---")
    if st.sidebar.button("🔒 Cerrar Sesión Estudiante"):
        st.session_state.rol_seleccionado = None
        st.session_state.autenticado = False
        st.rerun()

    # ENRUTAMIENTO DINÁMICO
    if apartado == "👤 Datos Generales":
        mostrar_datos_generales()

    elif apartado == "📜 Kardex":
        mostrar_kardex()

    elif apartado == "💳 Pago de Servicios":
        mostrar_pago_servicios()

    elif apartado == "🗓️ Horario":
        mostrar_horario()

    elif apartado == "📊 Calificaciones":
        mostrar_calificaciones()

    elif apartado == "🏆 Cursos Extracurriculares":
        mostrar_cursos_extracurriculares()

    elif apartado == "✍️ Evaluación Docente":
        mostrar_evaluacion_docente()

    elif apartado == "💬 Asistente IA STELLA":
        st.title("💬 Asistente de Auditoría IA")
        st.caption("Capa de conocimiento analítico del estudiante.")
        st.chat_message("assistant").markdown(
            "Hola Jessica. Estoy lista para responder cualquier duda sobre tu avance de créditos, calificaciones en Kardex o tu tira de materias.")