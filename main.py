# Rock-Paper-Scissors Game
# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

#Modules
import os
from colorama import Fore, init
import random

#To allow changing the text color in the cmd
init()

#To clean the screen
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

n = 0
while n!=2:
    #Welcome
    print(Fore.GREEN + "\n-----------------------")
    print("¡PIEDRA!¡PAPEL!¡TIJERA!")
    print("-----------------------\n\n")

    opcion_maquina = random.choice(['piedra', 'papel', 'tijera']) #Random machine option

    verificado = 0 #Verify that the user has not typed another option
    while verificado!=1:
        opcion_usuario = input("¿Piedra, Papel o tijera?: ")
        opcion_usuario = opcion_usuario.lower()

        if opcion_usuario == 'piedra':
            verificado = 1
        elif opcion_usuario == 'papel':
            verificado = 1
        elif opcion_usuario == 'tijera':
            verificado = 1
        else:
            print("\nEsa opciòn no existe") 
            print(input())

    print("")
    print(opcion_usuario + " VS " + opcion_maquina)

    if opcion_usuario == opcion_maquina:
        print("\n¡ EMPATE !")
    else:
        if opcion_usuario == 'piedra' and opcion_maquina == 'tijera':
            print("\n¡ GANASTE :) !") 
        elif opcion_usuario == 'tijera' and opcion_maquina == 'papel':
            print("\n¡ GANASTE :) !")  
        elif opcion_usuario == 'papel' and opcion_maquina == 'piedra':
            print("\n¡ GANASTE :) !") 
        else:
            print("\n¡ PERDISTE :) !")

    print("\n1. SI")
    print("2. NO")
    n = int(input("¿Desea seguir jugando?: "))

    clearConsole()

