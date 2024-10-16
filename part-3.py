datos = [
    {
        "name": "Jose",
        "calificacion": 4.5
    },
    {
        "name": "Juliana",
        "calificacion": 5
    },
    {
        "name": "Miguel",
        "calificacion": 7
    }
]

max_calificacion = max(datos, key=lambda x: x["calificacion"])

print(max_calificacion)

print(f"El estudiante con la calificación más alta es {max_calificacion["name"]} con una calificación de {max_calificacion["calificacion"]}.")

# datos = {
#     "names": ["Juliana", "Miguel", "Maria"],
#     "grades": [7, 2, 9]
# }

# max_grade = max(datos["grades"])
# # recuperamos el indice de la lista de grades
# index = datos["grades"].index(max_grade)

# estudiante = datos["names"][index]

# print(f"El estudiante con la calificación más alta es {estudiante} con una calificación de {max_grade}.")

