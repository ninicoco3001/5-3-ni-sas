print("beletin")
nota = 0
for i in range(1 , 11):
    nota2 = int(input("ingrese la nota del examen del alumno"))
    nota = nota + nota2
nota = nota/10
print(f"el alumno se saco un{nota}")