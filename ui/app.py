import os
import streamlit as st
import time
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


# ==========================================
# FUNCIONES DE SIMULACIÓN DE DATOS (EX-AI_CHAIN)
# ==========================================
def obtener_datos_agenda():
    return pd.DataFrame([
        {"Grupo": "ISC-0601", "Materia": "Álgebra Lineal", "Profesor": "Ing. J. Hernández",
         "Horario": "Lunes 14:00-16:00", "Prioridad": "Alta"},
        {"Grupo": "ISC-0601", "Materia": "Programación", "Profesor": "M. en C. R. Téllez",
         "Horario": "Martes 15:00-17:00", "Prioridad": "Media"},
        {"Grupo": "ISC-0602", "Materia": "Física Mecánica", "Profesor": "Dr. A. Gómez",
         "Horario": "Miércoles 14:00-16:00", "Prioridad": "Alta"},
        {"Grupo": "ISC-0601", "Materia": "Álgebra Lineal", "Profesor": "Ing. J. Hernández",
         "Horario": "Jueves 16:00-18:00", "Prioridad": "Baja"},
        {"Grupo": "ISC-0602", "Materia": "Química General", "Profesor": "Dra. N. Domínguez",
         "Horario": "Viernes 13:00-15:00", "Prioridad": "Media"}
    ])


def obtener_datos_kardex_migrado():
    return pd.DataFrame([
        {"Materia": "Cálculo Diferencial", "Estatus": "Aprobada", "Calificación": 85},
        {"Materia": "Álgebra Lineal", "Estatus": "Cursando", "Calificación": 0},
        {"Materia": "Programación Orientada a Objetos", "Estatus": "Aprobada", "Calificación": 90},
        {"Materia": "Estructura de Datos", "Estatus": "Reprobada", "Calificación": 65},
        {"Materia": "Fundamentos de Redes", "Estatus": "Aprobada", "Calificación": 80}
    ])


def obtener_respuestas_faq(pregunta):
    faq = {
        "sistema": "**Respuesta de STELLA:** La migración inteligente mapeó con éxito 12 profesores, 8 grupos y 24 asignaturas del sistema legacy a nuestra base de datos relacional sin pérdida de datos.",
        "horarios": "**Respuesta de STELLA:** El motor de optimización OR-Tools ha diseñado 3 escenarios de horarios posibles para el grupo ISC-0601, eliminando al 100% los cruces de profesores en aulas asignadas."
    }
    return faq.get(pregunta, "La IA está optimizando los datos migrados. Selecciona una consulta válida.")


def obtener_grafica_kardex():
    return {"Aprobadas": 3, "Reprobadas": 1, "Cursando": 1}


# ==========================================
# INTERFAZ DE USUARIO - STELLA
# ==========================================
st.set_page_config(page_title="STELLA - Sistema de Migración Inteligente", page_icon="✨", layout="wide")

# DESACTIVAR ANIMACIONES (Exigencia para la Demo)
st.markdown("<style>* { transition: none !important; animation: none !important; }</style>", unsafe_allow_html=True)

# Inicializar estados globales de la aplicación si no existen
if "migrado" not in st.session_state:
    st.session_state.migrado = False
if "usuario_autenticado" not in st.session_state:
    st.session_state.usuario_autenticado = False

# VISTA 1: LOGIN DEL SISTEMA STELLA
if not st.session_state.usuario_autenticado:
    st.title("✨ STELLA Core System")
    st.subheader("Plataforma de Adaptación de Datos Educativos con IA")

    with st.form("Login de Root Técnico"):
        st.write("### 🔐 Acceso de Administrador Técnico")
        user = st.text_input("Usuario Root", value="admin_stella")
        password = st.text_input("Contraseña", type="password", value="••••••••")

        if st.form_submit_button("Ingresar al Sistema"):
            st.session_state.usuario_autenticado = True
            st.rerun()
else:
    # Si ya se logueó, mostramos el Dashboard de STELLA
    st.title("✨ Sistema STELLA (Ecosistema Adaptado)")
    st.sidebar.write("👤 **Rol:** Administrador Técnico / Root")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.usuario_autenticado = False
        st.session_state.migrado = False
        st.rerun()

    # NAVEGACIÓN EN 4 PESTAÑAS EXIGIDAS
    tab1, tab2, tab3, tab4 = st.tabs([
        "📥 Traspaso & Ingesta DB",
        "🗓️ Adecuación de Horarios Óptimos",
        "💬 Consultas de Control IA",
        "📊 Estadísticas de Calificaciones"
    ])

    # ==========================================
    # PESTAÑA 1: TRASPASO CON BARRA DE CARGA
    # ==========================================
    with tab1:
        st.header("📥 Ingesta y Transformación de la Base de Datos Existente")
        st.caption(
            "Carga el esquema de la base de datos SQL del sistema viejo para adaptarlo al motor inteligente de STELLA.")

        archivo_db = st.file_uploader("Sube el respaldo de la base de datos (.sql, .json, .csv)",
                                      type=["sql", "json", "csv"])

        if archivo_db is not None:
            if st.button("Iniciar Traspaso y Transformación de Datos"):
                barra_progreso = st.progress(0)
                estado_texto = st.empty()

                estado_texto.text("⚡ Leyendo tablas del sistema viejo (Profesores, Grupos, Calificaciones)...")
                time.sleep(1.0)
                barra_progreso.progress(30)

                estado_texto.text("🧠 Adaptando registros con IA: Mapeando competencias y asignaturas...")
                time.sleep(1.2)
                barra_progreso.progress(65)

                estado_texto.text("💾 Normalizando base de datos en PostgreSQL de STELLA y eliminando colisiones...")
                time.sleep(1.0)
                barra_progreso.progress(100)

                estado_texto.text("✅ ¡Traspaso completado! Estructuras heredadas mapeadas con éxito.")
                st.session_state.migrado = True
                st.success("¡Base de datos vieja adaptada al 100% al nuevo ecosistema inteligente!")

    # ==========================================
    # PESTAÑA 2: HORARIOS ADAPTADOS
    # ==========================================
    with tab2:
        st.header("🗓️ Distribución y Posibles Horarios Calculados")
        st.caption("Estructura adaptada matemáticamente por el motor CP-SAT libre de choques de profesores o aulas.")

        if not st.session_state.migrado:
            st.warning("⚠️ Esperando datos. Por favor, realiza el traspaso de la base de datos en la Pestaña 1.")
        else:
            st.success("🤖 ¡Estructura de Horarios Generada automáticamente post-migración!")
            df_agenda = obtener_datos_agenda()
            st.table(df_agenda)

            st.download_button(
                label="📥 Descargar Reporte de Horarios y Grupos (CSV)",
                data=df_agenda.to_csv(index=False).encode('utf-8'),
                file_name='horarios_stella_ISC.csv',
                mime='text/csv'
            )

    # ==========================================
    # PESTAÑA 3: CHAT DE CONTROL IA
    # ==========================================
    with tab3:
        st.header("💬 Chat de Control y Consulta de Datos Migrados")
        st.caption(
            "Pregúntale a STELLA sobre la adecuación de profesores, asignaturas libres o auditorías de la base de datos.")

        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant",
                                          "content": "¡Hola Técnico! Los datos viejos ya están en mi red de conocimiento. Selecciona una auditoría de control rápido:"}]

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        st.write("---")
        col_faq1, col_faq2 = st.columns(2)
        with col_faq1:
            if st.button("❓ ¿Cómo quedó la equivalencia del sistema viejo al nuevo?"):
                st.session_state.messages.append(
                    {"role": "user", "content": "¿Cómo quedó la equivalencia del sistema viejo al nuevo?"})
                st.session_state.messages.append({"role": "assistant", "content": obtener_respuestas_faq("sistema")})
                st.rerun()

        with col_faq2:
            if st.button("❓ ¿Cuántos escenarios de horarios se calcularon para los profesores?"):
                st.session_state.messages.append(
                    {"role": "user", "content": "¿Cuántos escenarios de horarios se calcularon para los profesores?"})
                st.session_state.messages.append({"role": "assistant", "content": obtener_respuestas_faq("horarios")})
                st.rerun()

    # ==========================================
    # PESTAÑA 4: ESTADÍSTICAS Y GRÁFICAS
    # ==========================================
    with tab4:
        st.header("📊 Analíticas e Historial Analizado (Kardex)")
        st.caption("Estadísticas automáticas de materias aprobadas, reprobadas y desempeño general.")

        if not st.session_state.migrado:
            st.warning("⚠️ No hay estadísticas disponibles. Primero migra la base de datos vieja en la Pestaña 1.")
        else:
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.write("### Auditoría de Calificaciones Migradas")
                st.dataframe(obtener_datos_kardex_migrado())

            with col_m2:
                st.write("### Estatus de Materias Totales (3 Gráficas Requeridas)")

                # Gráfica 1: Barras
                st.caption("1. Conteo de Materias por Estatus")
                st.bar_chart(obtener_grafica_kardex())

                # Gráfica 2: Líneas
                st.caption("2. Promedio de Desempeño por Periodo")
                st.line_chart([82, 85, 78, 88, 83])

                # Gráfica 3: Área
                st.caption("3. Carga de Materias Críticas Detectadas por la IA")
                st.area_chart([1, 2, 0, 1, 3])
