import streamlit as st


def mostrar_pago_servicios():
    st.title(" Pago de Servicios Institucionales")
    st.caption("Validación de referencias bancarias y estado financiero.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Concepto", "Reinscripción Semestral")
    col2.metric("Monto", "$2,850.00 MXN")
    col3.metric("Estado", "Pagado ")

    st.write("###  Generar Nueva Referencia")
    opcion = st.selectbox("Seleccione el servicio a tramitar:",
                          ["Constancia de Estudios", "Examen Extraordinario", "Curso de Inglés"])
    if st.button("Generar Línea de Captura Inteligente"):
        st.success(f"Línea de captura para '{opcion}' emitida con éxito: STELLA-PAY-2026-9831")