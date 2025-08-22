secciones = []
votos = []

opcion = input("queres agregar una nueva seccion, ¿y o n?")

while (opcion == "y"):
    nuevas = input("cual es la nueva seccion que vas a meter???????????????")
    secciones.append(nuevas)
    nuevav = input("cual es la cantidad de votos")
    votos.append(nuevav)
    opcion = input("queres agregar una nueva seccion, ¿y o n?")

#A
longitud = len(secciones)
print("a continuacion, la cantidad de secciones")
print(longitud)

#B
for p in range(0, len(votos)):
    total = total + votos[p]

#c
valor = 0
for i in range(0, len(votos)):
    if (valor < votos[i]):
        m = listas[i]
        posicion = i