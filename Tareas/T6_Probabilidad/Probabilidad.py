from os import system, name

import matplotlib.pyplot as plt
import random as rnd

def clear(): 
    # windows 
    if name == 'nt': 
        _ = system('cls') 
    # mac and linux
    else: 
        _ = system('clear')

_run = True
while _run:
    clear()
    print("--- PROBABILIDAD ---\n")
    print("[1] Águila o sol")
    print("[2] Sacar un 3 en un dado")
    print("[3] Sumar 8 dados dos dados")

    print("\n[Q] Salir\n")

    opcion = input("> ")

    dado = [1,2,3,4,5,6]

    # águila o sol
    if opcion == '1':
        print("\nProbabilidad de sacar águila o sol\n")
        print("¿Cuántas veces deseas tirar la moneda?\n")
        moneda = ['águila','sol']
        n = int(input("> "))
        x = []
        aguila = [] # Lista de probabilidad para águila
        sol = [] # Lista de probabilidad para sol
        a = 0 # Conteo de águila
        s = 0 # Conteo de sol

        for i in range(1,n+1):
            tiro = rnd.choice(moneda)
            if tiro == 'águila':
                a += 1
            else:
                s += 1
            x.append(i) # Valores en x
            pa = a/i # Probabilidad de sacar águila
            aguila.append(pa)
            ps = s/i #Probabilidad de sacar sol
            sol.append(ps)

        plt.style.use('seaborn-whitegrid')
        plt.scatter(x, aguila, s=5, color='red')
        plt.scatter(x, sol, s=5, color='blue')
        plt.title('\nConvergencia de tirar una moneda\n')
        plt.xlabel('\nNúmero de tiros\n')
        plt.ylabel('Probabilidad\n')
        plt.show()
    # sacar 3
    elif opcion == '2':
        print("\nProbabilidad de sacar 3 al tirar un dado\n")
        print("¿Cuántas veces deseas hacer rodar el dado?\n")
        n = int(input("> "))
        x = []
        tres = [] # Lista de probabilidad de sacar 3
        t = 0 # Conteo de tres

        for i in range(1,n+1):
            tiro = rnd.choice(dado)
            if tiro == 3:
                t += 1
            else:
                pass
            x.append(i) # Valores en x 
            pt = t/i # Probabilidad de sacar tres
            tres.append(pt)

        plt.style.use('seaborn-whitegrid')
        plt.scatter(x, tres, s=5, color='green')
        plt.title('\nProbabilidad de sacar un 3 al rodar un dado\n')
        plt.xlabel('\nNúmero de tiros\n')
        plt.ylabel('Probabilidad\n')
        plt.show()
    # sumar 8
    elif opcion == '3':
        print("\nProbabilidad de que la suma de dos dados sea 8\n")
        print("¿Cuántas veces deseas hacer rodar la pareja de dados?\n")
        dado1 = dado
        dado2 = dado
        n = int(input("n: "))
        x = []
        suma_ocho = [] # Lista de probabilidad de sacar 3
        so = 0 # Conteo de suma ocho

        for i in range(1,n+1):
            tiro1 = rnd.choice(dado1)
            tiro2 = rnd.choice(dado2)
            if tiro1+tiro2 == 8:
                so += 1
            else:
                pass
            x.append(i) # Valores en x
            pso = so/i # Probabilidad de sumar ocho
            suma_ocho.append(pso)

        plt.style.use('seaborn-whitegrid')
        plt.scatter(x, suma_ocho, s=5, color='purple')
        plt.title('\nSuma de dos dados es igual a 8\n')
        plt.xlabel('\nNúmero de tiros\n')
        plt.ylabel('Probabilidad\n')
        plt.show()
    # salir
    elif opcion == 'Q' or opcion == 'q':
        break
    # error
    else:
        print("Por favor, introduzca una opción válida.")

clear()