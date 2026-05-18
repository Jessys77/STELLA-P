import streamlit as st
import pandas as pd


def mostrar_horario():
    st.title(" Propuesta de Horarios Óptimos")
    st.caption("Distribución de carga calculada mediante el optimizador matemático OR-Tools sin choques de grupo.")

    df_horario = pd.DataFrame([
        {"Grupo": "ISC-0601", "Asignatura": "Álgebra Lineal", "Profesor": "Ing. J. Hernández",
         "Horario": "Lunes 14:00-16:00", "Aula": "Lab C-3"},
        {"Grupo": "ISC-0601", "Asignatura": "Programación Angular", "Profesor": "M. en C. R. Téllez",
         "Horario": "Martes 15:00-17:00", "Aula": "Aula 12"},
        {"Grupo": "ISC-0602", "Asignatura": "Física Mecánica", "Profesor": "Dr. A. Gómez",
         "Horario": "Miércoles 14:00-16:00", "Aula": "Lab Física"}
    ])
    st.table(df_horario)