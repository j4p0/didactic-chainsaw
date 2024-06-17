import random
#Definiciones
def valor_fila():
    return int(input("Ingresa la fila, entre 0-2: "))
def valor_columna():
    return int(input("Ingresa la columna, entre 0-2: "))
def modo_versus():
    jugador = "X"
    movimientos = 1
    #Movimientos totales = 9
    while movimientos <= 9:
        F=valor_fila()
        C= valor_columna()
        #Si la lista en la posicion dada es igual a vacio entonces reemplaza por la variable jugador en esa posiciòn. Luego muestra el tablero
        if matriz[F][C] == "":
            matriz[F][C] = jugador
            tablero()
            #Cambia el valor de la variable jugador si jugador es igual al valor original "X", si no es igual, mantiene el valor original.
            if comprobar_ganador(jugador) == True:
                print("Gana el jugador", jugador)
                return
            movimientos += 1
            jugador = "O" if jugador == "X" else "X"
        else:
            print("El espacio esta ocupado. Ingresa una nueva ubicación.")
    print("Empate!")
def tablero():
    print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
def comprobar_ganador(jugador):
    #Filas
    if matriz[0][0] == matriz[0][1] == matriz[0][2] == jugador:
        return True
    if matriz[1][0] == matriz[1][1] == matriz[1][2] == jugador:
        return True
    if matriz[2][0] == matriz[2][1] == matriz[2][2] == jugador:
        return True
    #Columnas
    if matriz[0][0] == matriz[1][0] == matriz[2][0] == jugador:
        return True
    if matriz[1][0] == matriz[1][1] == matriz[2][1] == jugador:
        return True
    if matriz[2][0] == matriz[2][1] == matriz[2][2] == jugador:
        return True
    #Diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == jugador:
        return True
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] == jugador:
        return True
def vsmaquina():
    jugador = "X"
    PC = "O"
    movimientos = 1
    #Movimientos totales = 9
    while movimientos <= 9:
        F = valor_fila()
        C= valor_columna()
        #Si la lista en la posicion dada es igual a vacio, entonces reemplaza por la variable de la maquina en esa posiciòn. Luego muestra el tablero.
        if matriz[F][C] == "":
            matriz[F][C] = jugador
            tablero()
            if comprobar_ganador(jugador) == True:
                print("Gana el jugador.")
                return
            movimientos += 1

            while True:
                move_fila = random.randint(0,2)
                move_columna = random.randint(0,2)
                print(f"El movimiento de la maquina es: [{move_fila}][{move_columna}]")
                if matriz[move_fila][move_columna] == "":
                    matriz[move_fila][move_columna] = PC
                    tablero()
                    if comprobar_ganador(PC) == True:
                        print("Gana la maquina.")
                        return
                movimientos +=1
                break
        else:
            print("El espacio está ocupado. Ingresa una nueva ubicación.")
    print("Empate!")

matriz = [["","",""],["","",""],["","",""]]
opcion = 0

#Saludo de bienvenida al programa.
print(("Bienvenido.")) 

#Menú de opciones y ejecucion del juego.
while opcion == 0:
    print("1. Nueva partida (VS Computadora).","\n2. Versus local.","\n3. Salir")
    opcion = int(input("Ingresa un numero 1-3: "))
    if opcion == 1:
        print("Partida nueva iniciada.")
        tablero()
        vsmaquina()
    elif opcion == 2:
        print("Modo versus iniciado.")
        tablero()
        modo_versus()
    elif opcion == 3:
        print("Saliendo del programa")
        break
    else:
        print("El valor ingreasado no corresponde a un número definido.")
        opcion = 0
print("")
