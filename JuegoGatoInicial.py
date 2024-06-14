import random
#Necesito definir !Variables?. Definir el juego o por su parte, programar una variable que ejecute junto con la lista.
def valor_fila():
    return int(input("Ingresa la fila, entre 0-2: "))
def valor_columna():
    return int(input("Ingresa la columna, entre 0-2: "))
def cambio():
    jugador = "X"
    while True:
        valor_fila(), valor_columna()

        if (matriz[F][C] == ""):
            matriz[F][C] = jugador
            print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
            if (matriz[F][C] != ""):
                valor_fila(), valor_columna()
            else:
                jugador = "O" if jugador == "X" else "X"
        else:
            print("El espacio esta ocupado. Ingresa una nueva ubicación.")

matriz = [["","",""],["","",""],["","",""]]
opcion = 0
a = 1

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
            F = valor_fila()
            C = valor_columna()
            cambio()
            
        
            
        

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
