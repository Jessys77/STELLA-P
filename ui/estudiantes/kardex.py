import streamlit as st
import pandas as pd


def mostrar_kardex():
    st.title("📜 Historial Académico / Kardex Completo")
    st.caption("Mapeo relacional de asignaturas cursadas e importadas del sistema legacy.")

    datos = pd.DataFrame([
        {"Clave": "ISC-101", "Asignatura": "Cálculo Diferencial", "Calificación": 85, "Estatus": "Aprobada",
         "Periodo": "2024-1"},
        {"Clave": "ISC-103", "Asignatura": "Programación Orientada a Objetos", "Calificación": 90,
         "Estatus": "Aprobada", "Periodo": "2024-1"},
        {"Clave": "ISC-104", "Asignatura": "Estructura de Datos", "Calificación": 65, "Estatus": "Reprobada",
         "Periodo": "2024-2"},
        {"Clave": "ISC-105", "Asignatura": "Fundamentos de Redes", "Calificación": 80, "Estatus": "Aprobada",
         "Periodo": "2024-2"}
    ])
    st.dataframe(datos, use_container_width=True)
    st.metric(label="Promedio General Mapeado", value="80.0")