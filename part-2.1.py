empleados = int(input("Cuantos empleados hay en la empresa?: "))

acum = 1  # variable de control
cont1 = 0  # contador para los que ganan < 3000000
cont2 = 0  # contador para los que ganan > 3000000
gastos = 0  # total de gastos de la empresa

while acum <= empleados:
    sueldo = float(input(f"Ingrese el sueldo del empleado No. {acum}: "))

    if sueldo > 3000000:
        cont2 += 1
    elif sueldo >= 1000000 and sueldo <= 3000000:
        cont1 += 1
    else:
        print("Sueldo fuera de rango, intente nuevamente")
        continue

    gastos += sueldo  # sumamos cada sueldo los gastos de la empresa
    acum += 1  # aumentamos la variable de control en 1

print("######################### RESULTADOS #############################")
print(f"Empleados que ganan entre 1 y 3 millones: {cont1}")
print(f"Empleados que ganan mas de 3 millones: {cont2}")
print(f"Gastos totales de la empresa: {gastos}")
