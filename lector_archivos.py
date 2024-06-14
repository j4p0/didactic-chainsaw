espacios = 0
letras = 0
with open('nuevo_archivo.txt', 'r') as archivo:
    lector = archivo.read()
    for i in lector:
        for x in i:
            if x == " ":
                espacios +=1
            elif x != " ":
                letras +=1

with open('resumenvalores.txt', 'w') as archivo:
    archivo.write(f"La cantidad de espacios son: {espacios} y la cantidad de letras son: {letras}")

print(lector)
