import pandas as pd

# 1. ESQUEMA DE DATOS ESTÁTICOS DE LA AGENDA
def obtener_datos_agenda():
    return pd.DataFrame([
        {"Día": "Lunes", "Hora": "14:00 - 16:00", "Actividad": "Estudio: Álgebra Lineal", "Prioridad": "Alta"},
        {"Día": "Martes", "Hora": "15:00 - 17:00", "Actividad": "Estudio: Programación", "Prioridad": "Media"},
        {"Día": "Miércoles", "Hora": "14:00 - 16:00", "Actividad": "Estudio: Física Mecánica", "Prioridad": "Alta"},
        {"Día": "Jueves", "Hora": "16:00 - 18:00", "Actividad": "Estudio: Álgebra Lineal", "Prioridad": "Baja"},
        {"Día": "Viernes", "Hora": "13:00 - 15:00", "Actividad": "Estudio: Química General", "Prioridad": "Media"}
    ])

# 2. RESPUESTAS PREDEFINIDAS DEL FAQ (SIMULANDO LA IA DESACTIVADA)
def obtener_respuestas_faq(pregunta):
    faq = {
        "álgebra": "**Respuesta del Copiloto:** Sí. Basado en el mapeo de tu temario y las 4 horas asignadas por el motor matemático esta semana, tu probabilidad de cobertura es del 94%.",
        "reprobación": "**Respuesta del Copiloto:** Programación. Tienes un proyecto final que equivale al 50% de tu nota con fecha límite para el 20 de junio. Se te sugiere añadir un bloque extra de estudio."
    }
    return faq.get(pregunta, "Lo siento, la IA en tiempo real está en mantenimiento. Por favor selecciona una pregunta válida.")

# 3. COMPONENTES DE LAS 3 GRÁFICAS REQUERIDAS
def obtener_grafica_horas():
    return {"Álgebra Lineal": 6, "Programación": 8, "Física Mecánica": 4, "Química General": 3}

def obtener_grafica_cobertura():
    return pd.DataFrame({
        "Semana": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        "Progreso Real (%)": [20, 45, 70, 92]
    }).set_index("Semana")

def obtener_grafica_prioridades():
    return pd.DataFrame({
        "Alta": [3, 2, 4, 1],
        "Media": [2, 5, 3, 4],
        "Baja": [5, 3, 2, 6]
    })