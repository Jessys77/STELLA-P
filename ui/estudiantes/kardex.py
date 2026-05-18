import streamlit as st
import pandas as pd


def mostrar_kardex():
    st.markdown("""
    <style>
        .kardex-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 0.5rem;
        }

        .kardex-icon {
            font-size: 3rem;
        }

        .kardex-title {
            font-size: 2.7rem;
            font-weight: 800;
            color: #2563EB;
            margin: 0;
            letter-spacing: -0.5px;
        }

        .kardex-subtitle {
            color: #64748B;
            font-size: 1rem;
            margin-bottom: 2rem;
        }

        .kardex-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-top: 4px solid #2563EB;
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
            margin-bottom: 1.5rem;
        }

        .section-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #0F172A;
            margin-bottom: 1rem;
        }

        .metric-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-left: 5px solid #2563EB;
            border-radius: 14px;
            padding: 1.2rem 1.5rem;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
            margin-top: 1rem;
        }

        .metric-label {
            color: #64748B;
            font-size: 0.95rem;
            margin-bottom: 0.3rem;
        }

        .metric-value {
            color: #2563EB;
            font-size: 2rem;
            font-weight: 800;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="kardex-header">
        <div class="kardex-icon"></div>
        <h1 class="kardex-title">Historial Académico</h1>
    </div>
    <div class="kardex-subtitle">
        Kardex completo importado desde el sistema legacy.
    </div>
    """, unsafe_allow_html=True)

    datos = pd.DataFrame([
        {
            "Clave": "ISC-101",
            "Asignatura": "Cálculo Diferencial",
            "Calificación": 85,
            "Estatus": "Aprobada",
            "Periodo": "2024-1"
        },
        {
            "Clave": "ISC-103",
            "Asignatura": "Programación Orientada a Objetos",
            "Calificación": 90,
            "Estatus": "Aprobada",
            "Periodo": "2024-1"
        },
        {
            "Clave": "ISC-104",
            "Asignatura": "Estructura de Datos",
            "Calificación": 65,
            "Estatus": "Reprobada",
            "Periodo": "2024-2"
        },
        {
            "Clave": "ISC-105",
            "Asignatura": "Fundamentos de Redes",
            "Calificación": 80,
            "Estatus": "Aprobada",
            "Periodo": "2024-2"
        }
    ])

    st.markdown("""
    <div class="kardex-card">
        <div class="section-title">Asignaturas cursadas</div>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        datos,
        use_container_width=True,
        hide_index=True
    )

    promedio = datos["Calificación"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Promedio General Mapeado</div>
            <div class="metric-value">{promedio:.1f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        aprobadas = datos[datos["Estatus"] == "Aprobada"].shape[0]
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Materias Aprobadas</div>
            <div class="metric-value">{aprobadas}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        reprobadas = datos[datos["Estatus"] == "Reprobada"].shape[0]
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Materias Reprobadas</div>
            <div class="metric-value">{reprobadas}</div>
        </div>
        """, unsafe_allow_html=True)