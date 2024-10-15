c1=0
c2=0
c3=0
c4=0

puntos=int(input("Ingrese la cantidad de puntos a procesar: "))

for punto in range(puntos):
    x = int(input("Coordenada X: "))
    y = int(input("Coordenada Y: "))

    if x < 0 and y > 0:
        c1 += 1
    elif x > 0 and y > 0:
        c2 += 1
    elif x < 0 and y < 0:
        c3 += 1
    elif x > 0 and y < 0:
        c4 += 1
    else:
        print("0")

print(f"Puntos en cuadrante 1: {c1}")
print(f"Puntos en cuadrante 2: {c2}")
print(f"Puntos en cuadrante 3: {c3}")
print(f"Puntos en cuadrante 4: {c4}")

    

