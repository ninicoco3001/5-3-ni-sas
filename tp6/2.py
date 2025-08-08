lista = ["manolo",
         "mica",
         "Pedro",
         "manuel",
         "paco",]
print(".1 agregar persona al final de la cola ")
print(".2 que se vaya la primera persona de la lista")
print(".3 que pase la persona discapacitada")
print(".4 fin del dia")

gente = input("inserte la opcion que va a elegir")

while (gente != "4"):
    if (gente == "1"):
        print(lista)
        nuevagente = input("¿como se llama el wachin?")
        lista.append(nuevagente)
        print(lista)
    if (gente == "2"):
        lista.pop(0)
        print(lista)
    if (gente == "3"):
        discapacitado = input("¿como se llama la persona?") 
        lista.insert(0, discapacitado)
        print(lista)

    gente = input("inserte la opcion que va a elegir")

if (gente == "4"):
 print("chau weon")
 print(lista)    