import streamlit as st


def mostrar_datos_generales():
    st.markdown("""
    <style>
        .datos-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .datos-icon {
            font-size: 3rem;
        }

        .datos-title {
            font-size: 2.7rem;
            font-weight: 800;
            color: #2563EB;
            margin: 0;
            letter-spacing: -0.5px;
        }

        .status-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-left: 5px solid #2563EB;
            border-radius: 14px;
            padding: 1rem 1.2rem;
            margin-bottom: 2rem;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
            color: #0F172A;
            font-size: 1rem;
        }

        .section-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: #0F172A;
            margin-bottom: 1rem;
        }

        .info-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-top: 4px solid #2563EB;
            border-radius: 16px;
            padding: 1.5rem;
            min-height: 180px;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        }

        .info-row {
            margin-bottom: 1rem;
            color: #0F172A;
            font-size: 1rem;
            line-height: 1.5;
        }

        .info-label {
            font-weight: 700;
            color: #0F172A;
        }

        .info-value {
            color: #334155;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="datos-header">
        <div class="datos-icon"></div>
        <h1 class="datos-title">Datos Generales del Estudiante</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="status-card">
        🟢 <strong>Estatus de Control Escolar:</strong>
        Sincronizado correctamente con STELLA Core.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Información Personal</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
            <div class="info-row">
                <span class="info-label">Nombre:</span>
                <span class="info-value">Jessica Esquivel Téllez</span>
            </div>
            <div class="info-row">
                <span class="info-label">Matrícula:</span>
                <span class="info-value">202213140</span>
            </div>
            <div class="info-row">
                <span class="info-label">Fecha de Nacimiento:</span>
                <span class="info-value">21 de Julio de 2005</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-title"> Información Académica</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
            <div class="info-row">
                <span class="info-label">Carrera:</span>
                <span class="info-value">Ingeniería en Sistemas Computacionales</span>
            </div>
            <div class="info-row">
                <span class="info-label">Institución:</span>
                <span class="info-value">TESH (Huixquilucan)</span>
            </div>
            <div class="info-row">
                <span class="info-label">Semestre:</span>
                <span class="info-value">Sexto Semestre (601-M)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)