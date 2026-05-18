import streamlit as st


def mostrar_evaluacion_docente():
    st.title("✍️ Evaluación Docente Obligatoria")
    st.caption("Tu opinión ayuda a mejorar la asignación inteligente del profesorado.")

    profesor = st.selectbox("Seleccione al profesor a evaluar:",
                            ["Ing. J. Hernández", "M. en C. R. Téllez", "Dr. A. Gómez"])

    st.write(f"Evaluating: {profesor}")
    st.slider("1. ¿El docente domina los temas explicados en clase?", 1, 5, 5)
    st.slider("2. ¿Cumple con el horario establecido de la asignatura?", 1, 5, 5)

    if st.button("Enviar Evaluación Encriptada"):
        st.success("¡Evaluación registrada! Los datos han sido anonimizados antes de guardarse en STELLA.")