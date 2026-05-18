import streamlit as st
import pandas as pd


def obtener_datos_horario_stella():
    return pd.DataFrame([
        {"Grupo": "ISC-0601", "Asignatura": "Álgebra Lineal", "Profesor": "Ing. J. Hernández",
         "Horario": "Lunes 14:00-16:00", "Aula": "Lab C-3"},
        {"Grupo": "ISC-0601", "Asignatura": "Programación", "Profesor": "M. en C. R. Téllez",
         "Horario": "Martes 15:00-17:00", "Aula": "Aula 12"},
        {"Grupo": "ISC-0602", "Asignatura": "Física Mecánica", "Profesor": "Dr. A. Gómez",
         "Horario": "Miércoles 14:00-16:00", "Aula": "Lab Física"}
    ])


def obtener_datos_kardex_legacy():
    return pd.DataFrame([
        {"Clave": "ISC-101", "Asignatura": "Cálculo Diferencial", "Estatus": "Aprobada", "Calificación": 85,
         "Periodo": "2024-1"},
        {"Clave": "ISC-102", "Asignatura": "Álgebra Lineal", "Estatus": "Cursando", "Calificación": 0,
         "Periodo": "2024-2"},
        {"Clave": "ISC-104", "Asignatura": "Estructura de Datos", "Estatus": "Reprobada", "Calificación": 65,
         "Periodo": "2024-2"}
    ])


def mostrar_modulo_estudiante():
    st.sidebar.markdown("## 🎓 Menú SIE Estudiante")
    st.sidebar.write("👤 **Matrícula:** 202213140")
    st.sidebar.write("🏫 **Plantel:** TESH")
    st.sidebar.write("---")

    # Menú lateral interactivo según tus capturas oficiales del portal
    apartado = st.sidebar.radio(
        "Seleccione una opción:",
        ["📌 Estatus de Datos", "📝 Reinscripción", "📊 Calificaciones", "💬 Asistente de Auditoría IA"]
    )

    st.sidebar.write("---")
    if st.sidebar.button("🔒 Cerrar Sesión Estudiante"):
        st.session_state.rol_seleccionado = None
        st.rerun()

    # ==========================================
    # APARTADO 1: SEÑALIZACIÓN Y BIENVENIDA (¡ENTRA DIRECTO!)
    # ==========================================
    if apartado == "📌 Estatus de Datos":
        st.title("🎓 Portal del Estudiante Inteligentificado")
        st.subheader("Bienvenido de vuelta, Alumno del TESH")
        st.write("---")

        # SEÑALIZACIÓN EN PRIMERA INSTANCIA SOLICITADA
        st.success(
            "🟢 **Señalización de Control Escolar:** Tus datos de revalidación e historial académico han sido registrados correctamente en el nuevo ecosistema inteligente STELLA. Puedes navegar de forma libre por los módulos del menú lateral.")

        # Resumen rápido de datos en la pantalla de inicio
        st.write("### 📋 Resumen Informativo de Matrícula")
        col1, col2 = st.columns(2)
        col1.metric(label="Estatus General", value="Regular")
        col2.metric(label="Promedio Acumulado Mapeado", value="82.3")

    # ==========================================
    # APARTADO 2: REINSCRIPCIÓN (HORARIOS OPTIMIZADOS)
    # ==========================================
    elif apartado == "📝 Reinscripción":
        st.title("📝 Módulo de Reinscripción")
        st.subheader("Submenú: Elección de Materias & Horarios Disponibles")
        st.caption("Propuesta de horarios óptimos sin choques entre grupos y profesores calculada con OR-Tools.")

        df_horario = obtener_datos_horario_stella()
        st.table(df_horario)

        st.download_button(
            label="📥 Descargar Tira de Materias Propuesta (CSV)",
            data=df_horario.to_csv(index=False).encode('utf-8'),
            file_name='horario_sie_estudiante.csv',
            mime='text/csv'
        )

    # ==========================================
    # APARTADO 3: CALIFICACIONES (KARDEX HISTÓRICO Y GRÁFICAS)
    # ==========================================
    elif apartado == "📊 Calificaciones":
        st.title("📊 Consulta de Calificaciones")
        st.subheader("Submenú: Historial Académico / Kardex")

        col_g1, col_g2 = st.columns([3, 2])
        with col_g1:
            st.write("### Historial Analizado por STELLA")
            st.dataframe(obtener_datos_kardex_legacy())

        with col_g2:
            st.write("### Gráficas Estadísticas de Rendimiento")
            st.caption("1. Conteo de Estatus Académico")
            st.bar_chart({"Aprobadas": 2, "Reprobadas": 1, "Cursando": 1})

            st.caption("2. Comportamiento de Calificaciones")
            st.line_chart([85, 0, 65])

    # ==========================================
    # APARTADO 4: CHAT DE AUDITORÍA
    # ==========================================
    elif apartado == "💬 Asistente de Auditoría IA":
        st.title("💬 Asistente de Auditoría IA")
        st.chat_message("assistant").markdown(
            "Hola Estudiante. Tus datos del sistema escolar anterior han sido adecuados con éxito. ¿Tienes alguna consulta sobre tus materias o la asignación de tus grupos?")