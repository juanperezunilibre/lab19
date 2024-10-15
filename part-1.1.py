numero = int(input("Ingrese un numero: "))

# f-string
msg = f"El número {numero} es "

if numero % 2 == 0:
    msg += "par"
else:
    msg += "impar"

print(msg)
