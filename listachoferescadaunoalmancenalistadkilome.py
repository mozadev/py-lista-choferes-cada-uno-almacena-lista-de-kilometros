nombresCond=[]
listatotalkilosemana=[]

cant=int(input("ingrese canti choferes: "))
for i in range(cant):
    nombre=input("ingrese nombre chofer: ")
    nombresCond.append(nombre)
    listkilometrosdias = []

    for j in range(7):
        kilometros = input("ingrese kilometros : ")
        listkilometrosdias.append(kilometros)
    suma=0

    for k in range(7):
        suma=suma+listkilometrosdias[i]
    listatotalkilosemana.append(suma)


print(nombresCond)
print(" ")
print(listatotalkilosemana)
