import os
import httpx
import requests
import streamlit as st
from dotenv import load_dotenv

# 1. CARGA DE CONFIGURACIÓN Y DETECCIÓN AUTOMÁTICA DEL BACKEND
load_dotenv()

# Intentar detectar la URL del backend según los candidatos de tu equipo
backend_candidates = [
    os.getenv("BACKEND_URL", "http://backend:8000").rstrip("/"),
    "http://localhost:8000",
]

# Por defecto tomamos el primero, pero tu botón de test puede validar la sintonía
BACKEND_URL = backend_candidates[0]

# REQUERIMIENTO CRÍTICO: Cambia a True para asegurar que la demo funcione con datos estáticos
MODO_DEMO = True

st.set_page_config(page_title="Mi Copiloto de Estudio IA",
                   #page_icon="🎓",
                   layout="wide")
st.title(" Mi Copiloto de Estudio IA")
st.subheader("Optimiza tu tiempo, organiza tus materias y destruye el estrés académico")

# 2. PROTOCOLO REQUERIDO: DESACTIVAR ANIMACIONES DE STREAMLIT
st.markdown(
    """
    <style>
    /* Desactivar transiciones y animaciones visuales pesadas para acelerar la demo */
    * {
        transition: none !important;
        animation: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Herramienta de diagnóstico heredada del Scaffold de tu equipo
with st.sidebar:
    st.header(" Diagnóstico Técnico")
    if st.button("Probar Conexión Backend"):
        errors: list[str] = []
        for base_url in dict.fromkeys(backend_candidates):
            try:
                response = httpx.get(f"{base_url}/health", timeout=3.0)
                response.raise_for_status()
                st.success(f"Conectado a: {base_url}")
                st.json(response.json())
                BACKEND_URL = base_url
                break
            except Exception as exc:
                errors.append(f"{base_url}: {exc}")
        else:
            st.error("Backend desconectado. Usando MODO_DEMO local.")

# 3. NAVEGACIÓN REQUERIDA: LAYOUT DE 4 PESTAÑAS
tab1, tab2, tab3, tab4 = st.tabs([
    " Ingesta IA (Mapeo de Temarios)",
    " Agenda Semanal Optimizada",
    " Consulta al Copiloto IA",
    " Mis Estadísticas de Rendimiento"
])

# ==========================================
# PESTAÑA 1: INGESTA IA (MIGRACIÓN DE TEMARIOS)
# ==========================================
with tab1:
    st.header(" Carga Inteligente de Temarios y Evaluaciones")
    st.caption("Sube el PDF desordenado de tu materia. La IA extraerá las fechas límite automáticamente.")

    uploaded_file = st.file_uploader("Arrastra aquí el archivo de tu asignatura", type=["pdf", "txt", "png", "jpg"])

    if uploaded_file is not None:
        if st.button("Procesar Temario con IA", key="btn_ingesta"):
            with st.spinner("La IA está leyendo el archivo y extrayendo las fechas límite..."):
                if MODO_DEMO:
                    st.success("¡Datos extraídos con éxito (Modo Demo - Datos Estáticos)!")
                    st.json({
                        "asignatura": "Cálculo Integral",
                        "evaluaciones": [
                            {"nombre": "Examen Parcial 1", "ponderacion": "30%", "fecha_limite": "2026-06-05"},
                            {"nombre": "Problemario Derivadas", "ponderacion": "20%", "fecha_limite": "2026-05-30"},
                            {"nombre": "Proyecto Final", "ponderacion": "50%", "fecha_limite": "2026-06-20"}
                        ]
                    })
                else:
                    try:
                        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                        response = requests.post(f"{BACKEND_URL}/api/migracion", files=files)
                        if response.status_code == 200:
                            st.success("¡Temario estructurado e insertado en la base de datos SQL!")
                            st.json(response.json())
                        else:
                            st.error(f"Error en el servidor backend: {response.status_code}")
                    except Exception as e:
                        st.error(f"Error crítico de conexión: {e}. Considera activar MODO_DEMO = True.")

# ==========================================
# PESTAÑA 2: AGENDA SEMANAL OPTIMIZADA
# ==========================================
with tab2:
    st.header(" Tu Horario de Estudio Óptimo")
    st.caption("Distribución generada matemáticamente por el motor CP-SAT de OR-Tools en tus horas libres.")

    if st.button("Calcular Distribución de Estudio Ideal", key="btn_optimizar"):
        with st.spinner("El motor matemático está buscando la combinación de horas libre de colisiones..."):
            if MODO_DEMO:
                st.success("¡Calendario optimizado generado de forma instantánea!")
                agenda_mock = [
                    {"Día": "Lunes", "Hora": "14:00 - 16:00", "Actividad": "Estudio: Álgebra Lineal (Dificultad Alta)"},
                    {"Día": "Martes", "Hora": "15:00 - 17:00", "Actividad": "Estudio: Programación (Proyecto Próximo)"},
                    {"Día": "Miércoles", "Hora": "14:00 - 16:00", "Actividad": "Estudio: Física Mecánica"},
                    {"Día": "Jueves", "Hora": "16:00 - 18:00", "Actividad": "Estudio: Álgebra Lineal (Repaso)"},
                    {"Día": "Viernes", "Hora": "13:00 - 15:00", "Actividad": "Estudio: Química General"}
                ]
                st.table(agenda_mock)
            else:
                try:
                    response = requests.get(f"{BACKEND_URL}/api/agenda/optimizar")
                    if response.status_code == 200:
                        st.success("¡Horario calculado exitosamente!")
                        st.table(response.json())
                    else:
                        st.error("El motor de optimización devolvió un error.")
                except Exception as e:
                    st.error(f"No se pudo conectar con el motor matemático: {e}")

# ==========================================
# PESTAÑA 3: CONSULTA AL COPILOTO IA
# ==========================================
with tab3:
    st.header(" Pregúntale a tu Copiloto Académico")
    st.caption("Consulta sobre tu disponibilidad de tiempo y la probabilidad de cubrir tus temas.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("¿Voy a alcanzar a cubrir los temas de Álgebra para el examen?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Analizando tus métricas y calendario de estudio..."):
                if MODO_DEMO:
                    respuesta_mock = "¡Hola! Analizando tu agenda actual con el modelo OR-Tools, tienes asignados 2 bloques de estudio para Álgebra antes del examen del viernes. Si mantienes el ritmo actual, cubrirás el 95% del temario mapeado por la IA. ¡Vas por muy buen camino!"
                    st.markdown(respuesta_mock)
                    st.session_state.messages.append({"role": "assistant", "content": respuesta_mock})
                else:
                    try:
                        response = requests.post(f"{BACKEND_URL}/api/chat", json={"prompt": prompt})
                        if response.status_code == 200:
                            answer = response.json().get("response", "Sin respuesta.")
                            st.markdown(answer)
                            st.session_state.messages.append({"role": "assistant", "content": answer})
                        else:
                            st.error("Error al obtener respuesta de la IA del backend.")
                    except Exception as e:
                        st.error(f"Fallo en comunicación de chat: {e}")

# ==========================================
# PESTAÑA 4: MIS ESTADÍSTICAS DE RENDIMIENTO
# ==========================================
with tab4:
    st.header(" Analíticas de Gestión del Tiempo")
    st.caption("Visualiza cómo la IA y la optimización matemática impactan tus horas de estudio.")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Tiempo Administrativo Ahorrado", value="14.5 horas/mes", delta="⚡ Eficiencia IA")
    with col2:
        st.metric(label="Nivel de Cobertura de Temarios", value="92%", delta=" +15% de control")

    st.write("### Distribución de Horas de Estudio Recomendadas por Materia")

    data_grafica = {
        "Álgebra Lineal": 6,
        "Programación": 8,
        "Física Mecánica": 4,
        "Química General": 3
    }
    st.bar_chart(data_grafica)
