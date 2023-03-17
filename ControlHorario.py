"""
##ControlHorario.py## 
Programa que simula el control horario de un trabajador, contando hora de entrada, de salida, de comida (si la hay)
y cuantas horas extras se tienen acumuladas  
"""
import datetime

# Definimos los horarios de trabajo
horarios = {
    "Lunes": {
        "entrada": "8:00",
        "salida": "17:30",
        "entrada-comida": "14:30",
        "salida-comida":"15:30"
    },
    "Martes": {
        "entrada": "8:00",
        "salida": "17:30",
        "entrada-comida": "14:30",
        "salida-comida":"15:30"
    },
    "Miércoles": {
        "entrada": "8:00",
        "salida": "17:30",
        "entrada-comida": "14:30",
        "salida-comida":"15:30"
    },
    "Jueves": {
        "entrada": "8:00",
        "salida": "17:30",
        "entrada-comida": "14:30",
        "salida-comida":"15:30"
    },
    "Viernes": {
        "entrada": "8:00",
        "salida": "14:00",
        "entrada-comida": None,
        "salida-comida": None
    }
}

# Definimos las horas reales del usuario
horarios_real = horarios.copy()  # copiamos los horarios de trabajo por defecto
horarios_real["Lunes"]["entrada"] = "8:05"
horarios_real["Lunes"]["salida"] = "18:00"
horarios_real["Martes"]["entrada"] = "7:50"
horarios_real["Martes"]["salida"] = "17:45"
horarios_real["Miércoles"]["entrada"] = "8:10"
horarios_real["Miércoles"]["salida"] = "18:20"
horarios_real["Jueves"]["entrada"] = "8:15"
horarios_real["Jueves"]["salida"] = "17:30"
horarios_real["Viernes"]["entrada"] = "8:00"
horarios_real["Viernes"]["salida"] = "14:30"

# Convertimos los horarios de entrada y salida en objetos datetime.time
for dia in horarios_real:
    horarios_real[dia]["entrada"] = datetime.datetime.strptime(horarios_real[dia]["entrada"], "%H:%M").time()
    horarios_real[dia]["salida"] = datetime.datetime.strptime(horarios_real[dia]["salida"], "%H:%M").time()
    if horarios_real[dia]["entrada-comida"] is not None:
        horarios_real[dia]["entrada-comida"] = datetime.datetime.strptime(horarios_real[dia]["entrada-comida"], "%H:%M").time()
    if horarios_real[dia]["salida-comida"] is not None:
        horarios_real[dia]["salida-comida"] = datetime.datetime.strptime(horarios_real[dia]["salida-comida"], "%H:%M").time()

# Calculamos el exceso de horas por día y en total para la semana
exceso_total = datetime.timedelta()  # inicializamos en cero
for dia in horarios_real:
    horas_trabajadas = horarios_real[dia]["salida"] - horarios_real[dia]["entrada"]
    if horarios_real[dia]["entrada-comida"] is not None and horarios_real[dia]["salida-comida"] is not None:
        horas_trabajadas -= horarios_real[dia]["salida-comida"] - horarios_real[dia]["entrada-comida"]
    horas_establecidas = datetime.datetime.strptime(horarios[dia]["salida"], "%H:%M") - datetime.datetime.strptime(horarios[dia]["entrada"], "%H:%M")
    if horarios[dia]["entrada-comida"] is not None and horarios[dia]["salida-comida"] is not None:
        horas_establecidas -= datetime.datetime.strptime(horarios[dia]["salida-comida"], "%H:%M") - datetime.datetime.strptime(horarios[dia]["entrada-comida"], "%H:%M")
    exceso = horas_trabajadas - horas_establecidas
    if exceso > datetime.timedelta():
        print(f"Exceso de {exceso} horas en {dia}")
    exceso_total += max(exceso, datetime.timedelta())

print(f"Exceso total de {exceso_total} horas en la semana")


