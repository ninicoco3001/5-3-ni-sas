contraseña = ("12345678")
for contador in range (1,5):
    contra = input("ingresa la contraseña")
    if contraseña != contra :
        print("flaco, esta mal")
    if contraseña == contra :
        print("la pusiste")
        break
print("sos un pelotudo, no podes intentar mas")
