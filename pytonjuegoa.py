import random
#Definiciones
def valor_fila():
    return int(input("Ingresa la fila, entre 0-2: "))
def valor_columna():
    return int(input("Ingresa la columna, entre 0-2: "))
def cambio():
    jugador = "X"
    while True:
        F=valor_fila()
        C= valor_columna()
        #Si la lista en la posicion dada es igual a vacio entonces reemplaza por la variable jugador en esa posiciòn. Luego muestra el tablero
        if (matriz[F][C] == ""):
            matriz[F][C] = jugador
            tablero()
            jugador = "O" if jugador == "X" else "X"
        else:
            print("El espacio esta ocupado. Ingresa una nueva ubicación.")
def tablero():
    print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
def tablero_lleno():
    for i in range (matriz()):
        for x in matriz:
            if x != "":
                return False
    return True
# def jugadores():
#     a = [input("Primer jugador: "), "X", input ("Segundo jugador: "), "O"]
#     maquina = random.randint(0,1)

matriz = [["","",""],["","",""],["","",""]]
opcion = 0
# matriz[0][0] = matriz[0][1] = matriz[0][2]
# matriz[0][0] = 'X'
# else gana computadora

#diagonal
# matriz[0][0] = matriz[1][1] = matriz[2][2]

#Saludo de bienvenida al programa.
print(("Bienvenido.")) 

#Menú de opciones y ejecucion del juego.
while opcion == 0:
    print("1. Nueva partida (VS Computadora).","\n2. Versus local.","\n3. Salir")
    opcion = int(input("Ingresa un numero 1-3: "))
    if opcion == 1:
        print("Partida nueva iniciada.")
        print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
        #matriz[valor_fila()][valor_columna()] = "X"
        while True:
            cambio()
            if tablero_lleno() == True:
                tablero_lleno()
            break   
            
        
    elif opcion == 2:
        print("Modo versus iniciado.")
        print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
        #Iniciar modo local con inputs para la asignacion de los valores del juego.
    elif opcion == 3:
        print("Saliendo del programa")
        break
    else:
        print("El valor ingreasado no corresponde a un número definido.")
        opcion = 0
print("")