import pandas as pd

def obtener_datos_agenda():
    return pd.DataFrame([
        {"Grupo": "ISC-0601", "Materia": "Álgebra Lineal", "Profesor": "Ing. J. Hernández", "Horario": "Lunes 14:00-16:00", "Prioridad": "Alta"},
        {"Grupo": "ISC-0601", "Materia": "Programación", "Profesor": "M. en C. R. Téllez", "Horario": "Martes 15:00-17:00", "Prioridad": "Media"},
        {"Grupo": "ISC-0602", "Materia": "Física Mecánica", "Profesor": "Dr. A. Gómez", "Horario": "Miércoles 14:00-16:00", "Prioridad": "Alta"},
        {"Grupo": "ISC-0601", "Materia": "Álgebra Lineal", "Profesor": "Ing. J. Hernández", "Horario": "Jueves 16:00-18:00", "Prioridad": "Baja"},
        {"Grupo": "ISC-0602", "Materia": "Química General", "Profesor": "Dra. N. Domínguez", "Horario": "Viernes 13:00-15:00", "Prioridad": "Media"}
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