numero = int(input("Ingrese numero positivo: "))

msg = f"El número {numero} tiene "

if numero > 0 and numero <= 9:
    msg += "1 dígito"
elif numero >= 10 and numero <= 99:
    msg += "2 dígitos"
elif numero >= 100 and numero <= 999:
    msg += "3 dígitos"
else:
    print("Numero fuera de rango")
    exit() # Terminamos el codigo si no esta en el rango

print(msg)