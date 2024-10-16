datos = {}

numero = int(input("Ingrese cantidad de estudiantes: "))

for i in range(numero):
    name = input("Ingrese nombre del estudiante: ")
    nota = input(f"Ingrese nota del estudiante {name}: ")

    # {"juan": 3.4}
    # si la clave no existe crea la clave y le asigna el valor, caso contrario solo reemplaza el valor
    datos[name] = nota

print(datos)
