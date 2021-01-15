import signal
import math
import matplotlib.pyplot as plt
import numpy as np

from os import system, name, path, kill, getppid
from time import sleep
from random import randint

dir_path = path.dirname(path.realpath(__file__))

def texto_pausado(texto,tiempo):
    for i in range(len(texto)):
        print(texto[i], sep='', end='', flush=True); sleep(tiempo)

nada = '   \n'
def espacio(tiempo):
    texto_pausado(nada,tiempo)

def clear(): 
    # windows 
    if name == 'nt': 
        _ = system('cls') 
    # mac and linux
    else: 
        _ = system('clear')

clear()

texto = '\n¡Bienvenidx!\n'
texto_pausado(texto,0.05)

espacio(0.07)

texto = 'Este script te permitirá calcular promedios, aproximaciones para ciertas constantes, suma de vectores, matrices y mucho más.\n'
texto_pausado(texto,0.05)

espacio(0.2)

_run = True
while _run:
    # 'n' real
    def real(numero):
        try:
            n = float(numero)
        except:
            texto_pausado("\nParece ser que no introdujo un número real.\n",0.01)
        else:
            texto_pausado("'" + str(numero) + "', es válido.\n",0.01)
        return n
    # 'n' natural
    def natural(numero):
        try:
            n = int(numero)
        except:
            texto_pausado("\nParece ser que no introdujo un número natural.\n",0.01)
        else:
            texto_pausado("'" + str(numero) + "', es válido.\n",0.01)
        return n
    # factorial
    def factorial(numero):
        fact = 1
        for i in range(1,int(numero)+1):
            fact *= i
        return fact
    # generador de vectores
    def generador_vectores(no_vect,no_entr):
        vectores = []
        for i in range(int(no_vect)):
            print("---Vector " + str(i+1) + " ---")
            vector = [input("Entrada " + str(k+1) + ": ") for k in range(int(no_entr))]
            espacio(0.01)
            vectores.append(vector)
        return vectores
    # generador de matrices
    def generador_matrices(no_matrices):
        matrices = []
        for i in range(int(no_matrices)):
            print("------- MATRIZ " + str(i+1) + " -------")
            filas = int(input("Filas de matriz: "))
            columnas = int(input("Columnas de matriz: "))
            vectores_temp = generador_vectores(filas,columnas)    
            matrices.append(vectores_temp)
            print('\n')
        return matrices
    # convertidor de entradas
    def convertir_entradas(lista):
        try:
            vector = [real((lista[i])) for i in range(len(lista))]
        except:
            pass
        else:
            texto_pausado("Las entradas son reales.\n",0.01)
            espacio(0.005)
        return vector
    # separar vector
    def separar_vector(vector_inicial):
        vector = []
        if type(vector_inicial) == list:
            vector = convertir_entradas(vector_inicial)
            return vector
        elif type(vector_inicial) == str:
            vec_temp = vector_inicial.split(',')
            vector = convertir_entradas(vec_temp)
            return vector
        else:
            print("El vector introducido es inválido.")
    # separar matriz
    def separar_matriz(matriz_inicial):
        if type(matriz_inicial) == list:
            matriz = [separar_vector(matriz_inicial[i]) for i in range(len(matriz_inicial))]
            return matriz
        elif type(matriz_inicial) == str:
            vectores_temp = matriz_inicial.split(':')
            matriz = [separar_vector(vectores_temp[i]) for i in range(len(vectores_temp))]
            return matriz
        else:
            print("El string o lista de vectores introducido es inválido.")
    # separar matrices
    def separar_matrices(matrices_inicial):
        if type(matrices_inicial) == list:
            matrices = [separar_matriz(matrices_inicial[i]) for i in range(len(matrices_inicial))]        
            return matrices
        elif type(matrices_inicial) == str:
            matrices_temp = matrices_inicial.split(';')
            matrices = [separar_matriz(matrices_temp[i]) for i in range(len(matrices_temp))]        
            return matrices
        else:
            print("El string o lista de matrices introducido es inválido.")
    # tamaño vector
    def tamano_vectores(lista):
        try:
            for i in range(len(lista)):
                len(lista[0]) == len(lista[i])
        except:
            print("Los vectores no tienen el mismo número de entradas. Por favor, revise su documento.")
        else:
            print("Todos los vectores tienen el mismo número de entradas. Por favor, continue.")
    # tamaño matriz
    def tamano_matriz(lista):
        try:
            for k in range(len(lista)):
                print("--- Matriz " + str(k+1) + " ---")
                len(lista[0]) == len(lista[k])
                tamano_vectores(lista[k])
        except:
            print("Las matrices no tienen el mismo número de entradas. Por favor, revise su documento.")
        else:
            print("\n¡Excelente! Todos las matrices tienen el mismo número de vectores.")
    # suma vectores
    def suma_vect(lista):
        suma_vect = []
        for i in range(1):
            a = lista[i]
            b = lista[i+1]
            for k in range(len(a)):
                suma_vect.append(a[k]+b[k])
        return suma_vect
    # suma matrices
    def suma_matrices(lista):
        suma_mat = []
        for i in range(1):
            a = lista[i]
            b = lista[i+1]
            for k in range(len(a)):
                v_temp = []
                v_temp.append(a[k])
                v_temp.append(b[k])
                v = suma_vect(v_temp)
                suma_mat.append(v)
        return suma_mat
    # producto punto
    def prod_int(lista):
        c = 0
        for i in range(1):
            a = lista[i]
            b = lista[i+1]
            for k in range(len(a)):
                c = c + (a[k] * b[k])
        return c
    # multiplicación matrices
    def mult_matrices(lista):
        matriz_1 = lista[0]
        matriz_2 = lista[1]
        for i in matriz_1:
            try:
                len(matriz_2) == len(i)
            except:
                print("El número de columnas de la primer matriz no coincide con el número de filas de la segunda matriz")
        # columnas segunda matriz
        columnas_m2 = []
        for k in range(len(matriz_2[0])):
            columna_temp = []
            for i in range(len(matriz_2)):
                columna_temp.append(matriz_2[i][k])
            columnas_m2.append(columna_temp)
        matriz = []
        for k in range(len(matriz_1)):
            fila = []
            for i in range(len(columnas_m2)):
                mult = []
                mult.append(matriz_1[k])
                mult.append(columnas_m2[i])
                fila.append(prod_int(mult))
            matriz.append(fila)
        return matriz
    # lectura de archivo
    def leer_archivo(documento):
        txt_archivo = ''
        with open(documento) as archivo_temp:
            for renglon in archivo_temp:
                a = renglon.strip()
                txt_archivo += a
        return txt_archivo

    clear()
    texto_pausado('\n--- MENU PRINCIPAL ---\n',0.05)
    espacio(0.1)
    texto_pausado('[1] Calculadora de promedio \n',0.01)
    texto_pausado("[2] Suma de 0 a 'n' \n",0.01)
    texto_pausado('[3] Calculadora de factorial \n',0.01)
    texto_pausado('[4] Calculadora de potencias \n',0.01)
    texto_pausado('[5] Combinatoria \n',0.01)
    texto_pausado('[6] Aproximaciones de π y de ℯ \n',0.01)
    texto_pausado('[7] Ecuación cuadrática \n',0.01)
    texto_pausado('[8] Producto cruz \n',0.01)
    texto_pausado('[9] Suma de vectores \n',0.01)
    texto_pausado('[10] Producto punto de vectores \n',0.01)
    texto_pausado('[11] Suma de matrices \n',0.01)
    texto_pausado('[12] Multiplicación de matrices \n',0.01)
    texto_pausado('[13] Graficadora \n',0.01)
    texto_pausado('[14] MRU, MRUA y Tiro Parabólico \n',0.01)
    texto_pausado('\n[Q] Cerrar script\n',0.025)

    option = input("\n> ")

    # Promedio
    if option == str(1):
        clear()
        texto_pausado("\n--- Calculadora de promedio ---\n",0.01)
        texto = "Calcula el promedio de cualesquiera dos números reales 'a' y 'b'.\n"
        texto_pausado(texto,0.01)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                try:
                    var_a = input("\nIntroduzca un valor de 'a': ")
                    a = real(var_a)
                    var_b = input("Introduzca un valor de 'b': ")
                    b = real(var_b)
                except:
                    z = 0
                else:
                    p = (a+b)/2
                    texto = "El promedio de " + str(a) + " y de " + str(b) + " es " + str(p) + "\n\n"
                    texto_pausado(texto,0.05)
                    z = 1
            else:
                texto_pausado("\n[1] Calcular otro promedio",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
    
    # Suma de 0 a n
    elif option == str(2):
        clear()
        texto_pausado("\n--- Sumatoria de 0 a n ---\n",0.01)
        texto_pausado("Suma todos los números naturales desde 0 hasta n.\n",0.01)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                try:
                    var_n = input("\nIntroduzca un valor de 'n': ")
                    n = natural(var_n)
                except:
                    z = 0
                else:
                    suma = 0
                    for i in range(n+1):
                        suma += i
                    texto = "La suma desde 0 hasta " + str(n) + " es " + str(suma) + "\n"
                    texto_pausado(texto,0.05)
                    z = 1
            else:
                texto_pausado("\n[1] Calcular otra suma de 0 a n",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Factorial
    elif option == str(3):
        clear()
        texto_pausado("\n--- Factorial de n ---\n",0.01)
        texto_pausado("Calcula el valor factorial de n.\n",0.01)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                try:
                    var_n = input("\nIntroduzca un valor de 'n': ")
                    n = natural(var_n)
                except:
                    z = 0
                else:
                    fact = factorial(n)
                    texto = "\n" + str(n) + "! = " + str(fact) + "\n"
                    texto_pausado(texto,0.05)
                    z = 1
            else:
                texto_pausado("\n[1] Calcular otro factorial",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Potencia
    elif option == str(4):
        clear()
        texto_pausado("\n--- 'a' a la potencia 'b' ---\n",0.01)
        texto_pausado("Calcula el valor de 'a' elevado a la 'b'.\n",0.01)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                try:
                    var_a = input("\nIntroduzca un valor de 'a': ")
                    a = natural(var_a)
                    var_b = input("\nIntroduzca un valor de 'b': ")
                    b = natural(var_b)
                except:
                    z = 0
                else:
                    e = a**b
                    texto = str(a) + "^" + str(b) + " = " + str(e)
                    texto_pausado(texto,0.05)
                    z = 1
            else:
                texto_pausado("\n[1] Calcular otra potencia",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Combinatoria
    elif option == str(5):
        clear()
        texto_pausado("\n--- Combinatoria de 'n' en 'r' ---\n",0.01)
        texto_pausado("Calcular el valor de la combinatoria de 'n' en 'r'.\n",0.01)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                try:
                    var_n = input("\nIntroduzca un valor de 'n': ")
                    n = natural(var_n)
                    var_r = input("\nIntroduzca un valor de 'r': ")
                    r = natural(var_r)
                except:
                    z = 0
                else:
                    comb = factorial(n)/(factorial(n-r)*factorial(r))
                    texto = str(n) + "C" + str(r) + " = " + str(comb) + "\n"
                    texto_pausado(texto,0.05)
                    z = 1
            else:
                texto_pausado("\n[1] Calcular otra combinatoria",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Aproximaciones de π y de ℯ
    elif option == str(6):
        clear()
        texto_pausado("\n--- Aproximación de π y de ℯ ---\n",0.01)
        z_1 = 0
        _subrun = True
        while _subrun:
            if z_1 == 0:
                texto_pausado('[1] Aproximación de π',0.025)
                texto_pausado('\n[2] Aproximación de ℯ',0.025)
                texto_pausado('\n[Q] Menu principal\n',0.025)
                suboption = input("> ")
                z_2 = 0
                if z_2 == 0:
                    # Aproximación de π
                    if suboption == str(1):
                        clear()
                        print('--- Aproximación de π ---')
                        z_3 = 0
                        _ssubrun = True
                        while _ssubrun:
                            if z_3 == 0:
                                try:
                                    var_n = input("\nIntroduzca un valor de 'n': ")
                                    n = natural(var_n)
                                except:
                                    z_3 = 0
                                else:
                                    suma = 0
                                    for i in range(0,n+1):
                                        num = (-1)**i
                                        den = (2*i)+1
                                        suma += num/den
                                    pi = 4*suma
                                    texto = "\nDada n=" + str(n) + "... π ≈ " + str(pi) + "\n"
                                    texto_pausado(texto,0.05)
                                    z_3 = 1
                            else:
                                texto_pausado("\n[1] Calcular para otro valor de 'n'",0.01)
                                texto_pausado("\n[Q] Subir un nivel\n",0.01)
                                subopcion = input("> ")
                                if subopcion == str(1):
                                    z_3 = 0
                                    _ssubrun = True
                                elif subopcion == 'Q' or subopcion == 'q':
                                    _ssubrun = False
                                else:
                                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                    # Aproximación de ℯ
                    elif suboption == str(2):
                        clear()
                        print('--- Aproximación de ℯ ---')
                        z_3 = 0
                        _ssubrun = True
                        while _ssubrun:
                            if z_3 == 0:
                                try:
                                    var_n = input("\nIntroduzca un valor de 'n': ")
                                    n = natural(var_n)
                                except:
                                    z_3 = 0
                                else:
                                    suma = 0
                                    den=1
                                    for i in range(0,n): # se toma desde
                                        fact = factorial(i)
                                        suma += 1/fact
                                    e = suma
                                    texto = "\nDada n=" + str(n) + "... ℯ ≈ " + str(e) + "\n"
                                    texto_pausado(texto,0.05)
                                    z_3 = 1
                            else:
                                texto_pausado("\n[1] Calcular para otro valor de 'n'",0.01)
                                texto_pausado("\n[Q] Subir un nivel\n",0.01)
                                subopcion = input("> ")
                                if subopcion == str(1):
                                    z_3 = 0
                                    _ssubrun = True
                                elif subopcion == 'Q' or subopcion == 'q':
                                    _ssubrun = False
                                else:
                                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                    # Salir
                    elif suboption == 'Q' or suboption == 'q':
                        _subrun = False
                    # Error
                    else:
                        texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                else:
                    pass  
            else:
                texto = "\n[1] Calcular otra aproximación de π o de ℯ."
                texto_pausado(texto,0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z_1 = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
    
    # Ecuación cuadrática
    elif option == str(7):
        clear()
        texto_pausado("\n----- ax²+bx+c=0 -----\n",0.05)
        texto_pausado("Calcular las raíces de una ecuación de segundo grado.\n",0.01)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                try:
                    a = real(input("\nIntroduzca un valor de 'a': "))
                    b = real(input("\nIntroduzca un valor de 'b': "))
                    c = real(input("\nIntroduzca un valor de 'c': "))
                except:
                    z = 0
                else:
                    x_1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
                    x_2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
                    val_x1 = "x_1 = " + str(x_1) + "\n"
                    val_x2 = "x_2 = " + str(x_2) + "\n"
                    if a != 0:
                        valor_as = str(a) + 'x²'
                        if b > 0:
                            valor_bs = '+' + str(a) + 'x'
                            if c > 0:
                                valor_cs = '+' + str(c)
                            elif c < 0:
                                valor_cs = str(c)
                            else:
                                valor_cs = ''
                        elif b < 0:
                            valor_bs = str(b) + 'x'
                            if c > 0:
                                valor_cs = '+' + str(c)
                            elif c < 0:
                                valor_cs = str(c)
                            else:
                                valor_cs = ''
                        else:
                            valor_bs = ''
                            if c > 0:
                                valor_cs = '+' + str(c)
                            elif c < 0:
                                valor_cs = str(c)
                            else:
                                valor_cs = ''
                    else:
                        valor_as = ''
                        if b != 0:
                            valor_bs = str(b) + 'x'
                            if c > 0:
                                valor_cs = '+' + str(c)
                            elif c < 0:
                                valor_cs = str(c)
                            else:
                                valor_cs = ''
                        else:
                            valor_bs = ''
                            if c != 0:
                                valor_cs = str(c)
                            else:
                                valor_cs = '0'
                    tipo = "\nLas soluciones a la ecuación " + valor_as + valor_bs + valor_cs + " son "
                    if b**2-4*a*c > 0:
                        texto_pausado(tipo + "reales.\n",0.05)
                        texto_pausado(val_x1,0.01)
                        texto_pausado(val_x2,0.01)
                    elif b**2-4*a*c == 0:
                        texto_pausado(tipo + "iguales.\n",0.05)
                        texto_pausado(val_x1,0.01)
                        texto_pausado(val_x2,0.01)
                    else:
                        texto_pausado(tipo + "complejas.\n",0.05)
                        texto_pausado(val_x1,0.01)
                        texto_pausado(val_x2,0.01)
                    z = 1
            else:
                texto_pausado("\n[1] Calcular las raíces de otra cuadrática.",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Producto cruz dos de vectores en R³
    elif option == str(8):
        clear()
        texto_pausado("\n--- Producto cruz de dos vectores en R³ ---\n",0.05)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                try:
                    vectores = generador_vectores(2,3)
                except:
                    z = 0
                else:
                    vectores = separar_matriz(vectores)
                    i = vectores[0][1]*vectores[1][2]-vectores[0][2]*vectores[1][1]
                    j = vectores[0][2]*vectores[1][0]-vectores[0][0]*vectores[1][2]
                    k = vectores[0][0]*vectores[1][1]-vectores[0][1]*vectores[1][0]
                    vec_pd = [i,j,k]
                    texto = '\n' + str(vectores[0]) + " x " + str(vectores[1]) + " = " + str(vec_pd) + '\n'
                    texto_pausado(texto,0.03)
                    z = 1
            else:
                texto = "\n[1] Calcular producto cruz de otros dos vectores."
                texto_pausado(texto,0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Suma dos vectores en R³
    elif option == str(9):
        clear()
        texto_pausado("\n----- Suma de dos vectores en R³ -----\n",0.05)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                texto_pausado('[1] Escribir entradas',0.025)
                texto_pausado('\n[2] Leer archivo\n',0.025)
                texto_pausado('\n[Q] Salir\n',0.025)
                suboption = input("\n> ")
                y = 0
                if y == 0:
                    if suboption == str(1):
                        clear()
                        print("\n----- Suma de dos vectores en R³ -----\n\n")
                        texto = "--- Introducir entradas de vectores ---\n\n"
                        texto_pausado(texto,0.025)
                        try:
                            vectores = generador_vectores(2,3)
                        except:
                            y = 0
                        else:
                            vectores = separar_matriz(vectores)
                            vec_suma = [vectores[0][0]+vectores[1][0],vectores[0][1]+vectores[1][1],vectores[0][2]+vectores[1][2]]
                            texto = '\n' + str(vectores[0]) + ' + ' + str(vectores[1]) + ' = ' + str(vec_suma) + '\n'
                            texto_pausado(texto,0.01)
                            y = 1
                            z = 1
                    elif suboption == str(2):
                        clear()
                        print("\n----- Suma de dos vectores en R³ -----\n\n")
                        texto_pausado("--- Leer archivo ---\n\n",0.01)
                        texto_pausado("Las entradas de cada vector deben estar separadas por comas:\n",0.02)
                        texto_pausado("entrada_1, entrada_2, entrada_3, ..., entrada_n\n\n",0.01)
                        texto_pausado("Cada vector deberá estar separado por dos puntos:\n",0.02)
                        texto_pausado("vector_1: vector_2: vector_3: ...: vector_n\n\n",0.01)
                        texto_pausado("Por favor, introduzca el nombre del archivo con su extensión:\n",0.01)
                        archivo = input('> ')
                        try:
                            txt_archivo = leer_archivo(dir_path + '/' + archivo)
                        except:
                            texto = "Parece ser que hubo un error. Verifique su archivo y/o que haya tecleado bien su nombre.\n"
                            texto_pausado(texto,0.05)
                        else:
                            vectores = separar_matriz(txt_archivo)
                            try:
                                espacio(0.02)
                                tamano_vectores(vectores)
                                espacio(0.02)
                            except:
                                y = 0
                            else:
                                suma_vectores = suma_vect(vectores)
                                texto = str(vectores[0]) + ' + ' + str(vectores[1]) + ' = ' + str(suma_vectores) + '\n\n'
                                texto_pausado(texto,0.05)
                                y = 1
                                z = 1
                    elif suboption == 'Q' or suboption == 'q':
                        _subrun = False
                    else:
                        texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                else:
                    pass
            else:
                texto_pausado("\n[1] Calcular suma de otros dos vectores en R³.",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Producto punto dos vectores en R³
    elif option == str(10):
        clear()
        texto = "\n----- Producto punto de dos vectores en R³ -----\n"
        texto_pausado(texto,0.05)
        z = 0
        _subrun = True
        while _subrun:
            if z == 0:
                texto = '[1] Escribir entradas'
                texto_pausado(texto,0.025)
                texto = '\n[2] Leer archivo'
                texto_pausado(texto,0.025)
                texto = '\n[Q] Salir\n'
                texto_pausado(texto,0.025)
                suboption = input("> ")
                y = 0
                if y == 0:
                    if suboption == str(1):
                        clear()
                        print("\n----- Producto punto de dos vectores en R³ -----\n")
                        texto = "\n--- Introducir entradas de vectores ---\n"
                        texto_pausado(texto,0.025)
                        try:
                            vectores = generador_vectores(2,3)
                        except:
                            y = 0
                        else:
                            vectores = separar_matriz(vectores)
                            vec_prod = prod_int(vectores)
                            texto = '\n' + str(vectores[0]) + ' • ' + str(vectores[1]) + ' = ' + str(vec_prod) + '\n'
                            texto_pausado(texto,0.01)
                            y = 1
                            z = 1
                    elif suboption == str(2):
                        clear()
                        print("\n----- Producto punto de dos vectores en R³ -----\n")
                        texto = "\n--- Leer archivo ---\n\n"
                        texto_pausado(texto,0.01)
                        texto = "Las entradas de cada vector deben estar separadas por comas:\n"
                        texto_pausado(texto,0.02)
                        texto = "entrada_1, entrada_2, entrada_3, ..., entrada_n\n\n"
                        texto_pausado(texto,0.01)
                        texto = "Cada vector deberá estar separado por dos puntos:\n"
                        texto_pausado(texto,0.02)
                        texto = "vector_1: vector_2: vector_3: ...: vector_n\n\n"
                        texto_pausado(texto,0.01)
                        texto = "Por favor, introduzca el nombre del archivo con su extensión:\n"
                        texto_pausado(texto,0.01)
                        archivo = input('> ')
                        try:
                            txt_archivo = leer_archivo(dir_path + '/' + archivo)
                        except:
                            texto = "Parece ser que hubo un error. Verifique su archivo y/o que haya tecleado bien su nombre.\n"
                            texto_pausado(texto,0.05)
                        else:
                            vectores = separar_matriz(txt_archivo)
                            try:
                                espacio(0.02)
                                tamano_vectores(vectores)
                                espacio(0.02)
                            except:
                                y = 0
                            else:
                                vec_prod = prod_int(vectores)
                                texto = '\n' + str(vectores[0]) + ' • ' + str(vectores[1]) + ' = ' + str(vec_prod) + '\n'
                                texto_pausado(texto,0.05)
                                y = 1
                                z = 1
                    elif suboption == 'Q' or suboption == 'q':
                        _subrun = False
                    else:
                        texto = "\nPor favor, introduzca una opción válida\n"
                        texto_pausado(texto,0.02)
                else:
                    pass
            else:
                texto = "\n[1] Calcular el producto punto de otros dos vectores en R³."
                texto_pausado(texto,0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Suma de matrices en R^n×n
    elif option == str(11):
        clear()
        texto = "\n----- Suma de dos matrices en R^n×n -----\n"
        texto_pausado(texto,0.05)
        z_1 = 0
        _subrun = True
        while _subrun:
            if z_1 == 0:
                texto = '[1] Escribir entradas'
                texto_pausado(texto,0.025)
                texto = '\n[2] Leer archivo'
                texto_pausado(texto,0.025)
                texto = '\n[Q] Salir\n'
                texto_pausado(texto,0.025)
                suboption = input("> ")
                z_2 = 0
                if z_2 == 0:
                    if suboption == str(1):
                        clear()
                        print("\n----- Suma de dos matrices en R^n×n -----\n")
                        texto = "\n--- Introducir entradas de vectores ---\n"
                        texto_pausado(texto,0.025)
                        try:
                            matrices = generador_matrices(2)
                        except:
                            z_2 = 0
                        else:
                            matrices = separar_matrices(matrices)
                            try:
                                espacio(0.02)
                                tamano_matriz(matrices)
                                espacio(0.02)
                            except:
                                z_2 = 0
                            else:
                                matriz = suma_matrices(matrices)
                                texto = '\nLa suma de las dos matrices es \n' + str(matriz)
                                texto_pausado(texto,0.05)
                                z_2 = 1
                                z_1 = 1
                    elif suboption == str(2):
                        clear()
                        print("\n----- Suma de dos matrices en R^n×n -----\n")
                        texto_pausado("\n--- Leer archivo ---\n\n",0.01)
                        texto_pausado("Las entradas de cada vector deben estar separadas por comas:\n",0.02)
                        texto_pausado("entrada_1, entrada_2, entrada_3, ..., entrada_n\n\n",0.01)
                        texto_pausado("Cada vector deberá estar separado por dos puntos:\n",0.02)
                        texto_pausado("vector_1: vector_2: vector_3: ...: vector_n\n\n",0.01)
                        texto_pausado("Cada matriz deberá estar separada por punto y coma:\n",0.02)
                        texto_pausado("matriz_1; matriz_2; matriz_3; ...; matriz_4\n\n",0.01)
                        texto_pausado("Por favor, introduzca el nombre del archivo con su extensión:\n",0.01)
                        archivo = input('> ')
                        try:
                            txt_archivo = leer_archivo(dir_path + '/' + archivo)
                        except:
                            texto = "Parece ser que hubo un error. Verifique su archivo y/o que haya tecleado bien su nombre.\n"
                            texto_pausado(texto,0.05)
                        else:
                            matrices = separar_matrices(txt_archivo)
                            try:
                                espacio(0.02)
                                tamano_matriz(matrices)
                                espacio(0.02)
                            except:
                                z_2 = 0
                            else:
                                matriz = suma_matrices(matrices)
                                texto_pausado('\nLa suma de las dos matrices es \n' + str(matriz),0.05)
                                z_2 = 1
                                z_1 = 1
                    elif suboption == 'Q' or suboption == 'q':
                        _subrun = False
                    else:
                        texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                else:
                    pass
            else:
                texto_pausado("\n[1] Calcular la suma de otras dos matrices en en R^n×n.",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z_1 = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Mutiplicación de dos matrices en R^m×n
    elif option == str(12):
        clear()
        texto_pausado("\n----- Multiplicar dos matrices en R^m×n -----\n",0.05)
        z_1 = 0
        _subrun = True
        while _subrun:
            if z_1 == 0:
                texto_pausado('[1] Escribir entradas',0.025)
                texto_pausado('\n[2] Leer archivo',0.025)
                texto_pausado('\n[Q] Salir\n',0.025)
                suboption = input("> ")
                z_2 = 0
                if z_2 == 0:
                    if suboption == str(1):
                        clear()
                        print("\n----- Multiplicar dos matrices en R^m×n -----\n")
                        texto_pausado("\n--- Introducir entradas de vectores ---\n",0.025)
                        try:
                            matrices = generador_matrices(2)
                        except:
                            z_2 = 0
                        else:
                            matrices = separar_matrices(matrices)
                            try:
                                espacio(0.02)
                                tamano_matriz(matrices)
                                espacio(0.02)
                            except:
                                z_2 = 0
                            else:
                                matriz = mult_matrices(matrices)
                                texto_pausado('\nLa multiplicación de las dos matrices es \n' + str(matriz) + "\n",0.05)
                                z_2 = 1
                                z_1 = 1
                    elif suboption == str(2):
                        clear()
                        print("\n----- Multiplicar dos matrices en R^m×n -----\n")
                        texto_pausado("\n--- Leer archivo ---\n\n",0.01)
                        texto_pausado("Las entradas de cada vector deben estar separadas por comas:\n",0.02)
                        texto_pausado("entrada_1, entrada_2, entrada_3, ..., entrada_n\n\n",0.01)
                        texto_pausado("Cada vector deberá estar separado por dos puntos:\n",0.02)
                        texto_pausado("vector_1: vector_2: vector_3: ...: vector_n\n\n",0.01)
                        texto_pausado("Cada matriz deberá estar separada por punto y coma:\n",0.02)
                        texto_pausado("matriz_1; matriz_2; matriz_3; ...; matriz_4\n\n",0.01)
                        texto_pausado("Por favor, introduzca el nombre del archivo con su extensión:\n",0.01)
                        archivo = input('> ')
                        try:
                            txt_archivo = leer_archivo(dir_path + '/' + archivo)
                        except:
                            texto = "Parece ser que hubo un error. Verifique su archivo y/o que haya tecleado bien su nombre.\n"
                            texto_pausado(texto,0.05)
                        else:
                            matrices = separar_matrices(txt_archivo)
                            try:
                                espacio(0.02)
                                tamano_matriz(matrices)
                                espacio(0.02)
                            except:
                                z_2 = 0
                            else:
                                matriz = mult_matrices(matrices)
                                texto_pausado('\nLa multiplicación de las dos matrices es \n' + str(matriz) + "\n",0.05)
                                z_2 = 1
                                z_1 = 1
                    elif suboption == 'Q' or suboption == 'q':
                        _subrun = False
                    else:
                        texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                else:
                    pass
            else:
                texto_pausado("\n[1] Calcular la multiplicación de otras dos matrices en R^n×m.",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z_1 = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)

    # Graficadora
    elif option == str(13):
        clear()
        texto_pausado("\n----- Graficadora -----\n",0.01)
        z_1 = 0
        _subrun = True
        while _subrun:
            if z_1 == 0:
                texto_pausado('[1] Recta',0.025)
                texto_pausado('\n[2] Parábola',0.025)
                texto_pausado('\n[Q] Menu principal\n',0.025)
                suboption = input("> ")
                z_2 = 0
                if z_2 == 0:
                    # recta
                    if suboption == str(1):
                        clear()
                        texto_pausado('---- Graficar una recta ----\n',0.025)
                        texto_pausado('La ecuación de la recta es y=mx+b\n',0.025)
                        z_3 = 0
                        _ssubrun = True
                        while _ssubrun:
                            if z_3 == 0:
                                try:
                                    valor_m = real(input("\nIntroduzca un valor de 'm': "))
                                    valor_b = real(input("\nIntroduzca un valor de 'b': "))
                                except:
                                    z_3 = 0
                                else:
                                    rango_x1 = real(input('\nEl rango de x irá de: '))
                                    rango_x2 = real(input('hasta: '))

                                    # recta
                                    x = np.linspace(rango_x1,rango_x2,100)
                                    y = valor_m*x + valor_b

                                    # ejes
                                    plt.vlines(0, min(y), max(y), colors='k', linestyles='solid', label='')
                                    plt.hlines(0, rango_x1-1, rango_x2+1, colors='k', linestyles='solid', label='')

                                    label = 'y=' + str(valor_m) + 'x' + '+' + str(valor_b)

                                    plt.plot(x, y, '-r', label=label) # recta
                                    plt.title('Gráfica de ' + label)

                                    plt.xlabel('x', color='#1C2833')
                                    plt.ylabel('y', color='#1C2833')

                                    plt.legend(loc='upper left')
                                    plt.grid()

                                    plt.show()

                                    z_3 = 1
                            else:
                                texto_pausado("\n[1] Graficar otra recta",0.01)
                                texto_pausado("\n[Q] Subir un nivel\n",0.01)
                                subopcion = input("> ")
                                if subopcion == str(1):
                                    z_3 = 0
                                    _ssubrun = True
                                elif subopcion == 'Q' or subopcion == 'q':
                                    _ssubrun = False
                                else:
                                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                    # parábola
                    elif suboption == str(2):
                        clear()
                        texto_pausado('--- Graficar una parábola ---\n',0.025)
                        texto_pausado('La ecuación de la parábola es ax²+bx+c=0\n',0.025)
                        z_3 = 0
                        _ssubrun = True
                        while _ssubrun:
                            if z_3 == 0:
                                try:
                                    valor_a = real(input("\nIntroduzca un valor de 'a': "))
                                    valor_b = real(input("\nIntroduzca un valor de 'b': "))
                                    valor_c = real(input("\nIntroduzca un valor de 'c': "))
                                except:
                                    z_3 = 0
                                else:
                                    rango_x1 = real(input('\nEl rango de x irá de: '))
                                    rango_x2 = real(input('hasta: '))

                                    # parábola
                                    x = np.linspace(rango_x1,rango_x2,100)
                                    y = valor_a*(x**2) + valor_b*x + valor_c

                                    if valor_a != 0:
                                        vertice = (-valor_b**2 - 4*valor_a*valor_c)/(4*valor_a)
                                    else:
                                        pass

                                    # ejes
                                    if valor_a < 0:
                                        min_y1 = valor_a*(rango_x1**2) + valor_b*rango_x1 + valor_c
                                        min_y2 = valor_a*(rango_x2**2) + valor_b*rango_x2 + valor_c
                                        min = min([min_y1,min_y2])
                                        plt.vlines(0, min, max(y)+1, colors='k', linestyles='solid', label='')
                                    elif valor_a > 0:
                                        plt.vlines(0, vertice-1, max(y), colors='k', linestyles='solid', label='')
                                    else:
                                        plt.vlines(0, min(y), max(y), colors='k', linestyles='solid', label='')
                                    
                                    plt.hlines(0, rango_x1-1, rango_x2+1, colors='k', linestyles='solid', label='')

                                    if valor_a != 0:
                                        valor_as = str(valor_a) + 'x²'
                                        if valor_b > 0:
                                            valor_bs = '+' + str(valor_b) + 'x'
                                            if valor_c > 0:
                                                valor_cs = '+' + str(valor_c)
                                            elif valor_c < 0:
                                                valor_cs = str(valor_c)
                                            else:
                                                valor_cs = ''
                                        elif valor_b < 0:
                                            valor_bs = str(valor_b) + 'x'
                                            if valor_c > 0:
                                                valor_cs = '+' + str(valor_c)
                                            elif valor_c < 0:
                                                valor_cs = str(valor_c)
                                            else:
                                                valor_cs = ''
                                        else:
                                            valor_bs = ''
                                            if valor_c > 0:
                                                valor_cs = '+' + str(valor_c)
                                            elif valor_c < 0:
                                                valor_cs = str(valor_c)
                                            else:
                                                valor_cs = ''
                                    else:
                                        valor_as = ''
                                        if valor_b != 0:
                                            valor_bs = str(valor_b) + 'x'
                                            if valor_c > 0:
                                                valor_cs = '+' + str(valor_c)
                                            elif valor_c < 0:
                                                valor_cs = str(valor_c)
                                            else:
                                                valor_cs = ''
                                        else:
                                            valor_bs = ''
                                            if valor_c != 0:
                                                valor_cs = str(valor_c)
                                            else:
                                                valor_cs = '0'

                                    label = 'y=' + valor_as + valor_bs + valor_cs

                                    plt.plot(x, y, '-r', label=label) # recta
                                    plt.title('Gráfica de ' + label)

                                    plt.xlabel('x', color='#1C2833')
                                    plt.ylabel('y', color='#1C2833')

                                    plt.legend(loc='upper left')
                                    plt.grid()

                                    plt.show()

                                    z_3 = 1
                            else:
                                texto_pausado("\n[1] Graficar otra cuadrática",0.01)
                                texto_pausado("\n[Q] Subir un nivel\n",0.01)
                                subopcion = input("> ")
                                if subopcion == str(1):
                                    z_3 = 0
                                    _ssubrun = True
                                elif subopcion == 'Q' or subopcion == 'q':
                                    _ssubrun = False
                                else:
                                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                    # Salir
                    elif suboption == 'Q' or suboption == 'q':
                        _subrun = False
                    # Error
                    else:
                        texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                else:
                    pass  
            else:
                texto_pausado("\n[1] Calcular otra recta o parábola.",0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z_1 = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
    
    # MRU, MRUA y Tiro Parabólico
    elif option == str(14):
        clear()
        texto = "\n----- Cinemática -----\n"
        texto_pausado(texto,0.01)
        z_1 = 0
        _subrun = True
        while _subrun:
            if z_1 == 0:
                texto_pausado('\n[1] Movimiento rectilíneo uniforme',0.025)
                texto_pausado('\n[2] Movimiento rectilíneo uniformemente acelerado',0.025)
                texto_pausado('\n[3] Tiro Parabólico\n',0.025)
                texto_pausado('\n[Q] Salir\n',0.025)
                suboption = input("> ")
                z_2 = 0
                if z_2 == 0:
                    # MRU
                    if suboption == str(1):
                        clear()
                        texto_pausado('---- Movimiento Rectilíneo Uniforme ----\n',0.025)
                        texto = 'Se arroja como resultado un archivo con los datos de un MRU, en un intervalo de tiempo.\n'
                        texto_pausado(texto,0.025)
                        texto_pausado('[1] Encontrar posición final',0.025)
                        texto_pausado('\n[2] Encontrar velocidad',0.025)
                        texto_pausado('\n[Q] Subir un nivel\n',0.025)
                        ssuboption = input("> ")
                        z_3 = 0
                        _ssubrun = True
                        while _ssubrun:
                            if z_3 == 0:
                                # posición final
                                if ssuboption == str(1):
                                    clear()
                                    texto_pausado('--- MRU - posición final ---\n',0.025)
                                    texto_pausado('Recuerde que la posición final en un MRU está dada por\n\n',0.01)
                                    texto_pausado('x_f = x_i + v * (t_f-t_i)\n\n',0.02)
                                    try:
                                        x_i = real(input("\nIntroduzca un valor de 'x_i': "))
                                        t_f = real(input("\nIntroduzca un valor de 't_f': "))
                                        t_i = real(input("\nIntroduzca un valor de 't_i': "))
                                        v = real(input("\nIntroduzca un valor de 'v': "))
                                    except:
                                        z_3 = 0
                                    t = np.linspace(t_f,t_i,50)
                                    datos_mru = path.join(dir_path, "mru_posicion.txt")
                                    with open(datos_mru, "w") as handle:
                                            for i in t:
                                                    x_f = x_i+v*(i)
                                                    texto = "La posición en t=" + str(i) + " es " + str(x_f)
                                                    print(texto, file=handle)
                                    texto_pausado("\nSe ha generado correctamente un archivo en el directorio.\n",0.05)
                                    _ssubrun = False
                                # velocidad
                                elif ssuboption == str(2):
                                    clear()
                                    texto_pausado('--- MRU - velocidad ---\n',0.025)
                                    texto_pausado('Recuerde que la velocidad un MRU está dada por\n\n',0.01)
                                    texto_pausado('v = (x_f-x_i)/(t_f-t_i) \n\n',0.02)
                                    try:
                                        x_f = real(input("\nIntroduzca un valor de 'x_f': "))
                                        x_i = real(input("\nIntroduzca un valor de 'x_i': "))
                                        t_f = real(input("\nIntroduzca un valor de 't_f': "))
                                        t_i = real(input("\nIntroduzca un valor de 't_i': "))
                                    except:
                                        z_3 = 0
                                    t = np.linspace(t_f,t_i,50)
                                    datos_mru = path.join(dir_path, "mru_posicion.txt")
                                    with open(datos_mru, "w") as handle:
                                            for i in t:
                                                    v = (x_f-x_i)/(i)
                                                    texto = "La velocidad en t=" + str(i) + " es " + str(v)
                                                    print(texto, file=handle)
                                    texto_pausado("\nSe ha generado correctamente un archivo en el directorio.\n",0.05)
                                    _ssubrun = False
                                # salir
                                elif ssuboption == 'Q' or ssuboption == 'q':
                                    _ssubrun = False
                                # error
                                else:
                                    texto = "\nPor favor, introduzca una opción válida\n"
                                    texto_pausado(texto,0.02)
                            else:
                                texto_pausado('\n[1] Calcular para valores diferentes',0.01)
                                texto_pausado("\n[Q] Subir un nivel\n",0.01)
                                subopcion = input("> ")
                                if subopcion == str(1):
                                    z_3 = 0
                                    _ssubrun = True
                                elif subopcion == 'Q' or subopcion == 'q':
                                    _ssubrun = False
                                else:
                                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
                    # MRUA
                    elif suboption == str(2):
                        clear()
                        texto_pausado('---- Movimiento Rectilíneo Uniformemente Acelerado  ----\n',0.025)
                        texto = 'Se arroja como resultado un archivo con los datos de un MRUA, en un intervalo de tiempo.\n'
                        texto_pausado(texto,0.025)
                        texto_pausado('[1] Encontrar posición final',0.025)
                        texto_pausado('\n[2] Encontrar velocidad (dado tiempo)',0.025)
                        texto_pausado('\n[3] Encontrar aceleración',0.025)
                        texto_pausado('\n[Q] Subir un nivel\n',0.025)
                        ssuboption = input("> ")
                        z_3 = 0
                        _sssubrun = True
                        while _sssubrun:
                            if z_3 == 0:
                                # posición final
                                if ssuboption == str(1):
                                    clear()
                                    texto_pausado('--- MRUA - posición final ---\n',0.025)
                                    texto_pausado('Recuerde que la posición final en un MRUA está dada por\n\n',0.01)
                                    texto_pausado('x_f = x_i + v_0 • (t_f - t_i) + (1/2) • a (t_f - t_i)²\n\n',0.02)
                                    try:
                                        x_i = real(input("\nIntroduzca un valor de 'x_i': "))
                                        t_f = real(input("\nIntroduzca un valor de 't_f': "))
                                        t_i = real(input("\nIntroduzca un valor de 't_i': "))
                                        v_0 = real(input("\nIntroduzca un valor de 'v_0': "))
                                        a = real(input("\nIntroduzca un valor de 'a': "))
                                    except:
                                        z_3 = 0
                                    t = np.linspace(t_f,t_i,50)
                                    datos_mru = path.join(dir_path, "mrua_posicion.txt")
                                    with open(datos_mru, "w") as handle:
                                            for i in t:
                                                    x_f=x_i+v_0*(t_f-t_i)+(1/2)*a*((t_f-t_i)**2)
                                                    texto = "La posición en t=" + str(i) + " es " + str(x_f)
                                                    print(texto, file=handle)
                                    texto_pausado("Se ha generado correctamente un archivo en el directorio.",0.05)
                                    _sssubrun = False
                                # velocidad
                                elif ssuboption == str(2):
                                    clear()
                                    texto_pausado('--- MRUA - velocidad ---\n',0.025)
                                    texto_pausado('Recuerde que la velocidad final en MRUA dado el tiempo es\n\n',0.01)
                                    texto_pausado('v_f = v_i + a • (t_f - t_i) \n\n',0.02)
                                    try:
                                        v_i = real(input("\nIntroduzca un valor de 'v_i': "))
                                        a = real(input("\nIntroduzca un valor de 'a': "))
                                        t_f = real(input("\nIntroduzca un valor de 't_f': "))
                                        t_i = real(input("\nIntroduzca un valor de 't_i': "))
                                    except:
                                        z_3 = 0
                                    t = np.linspace(t_f,t_i,50)
                                    datos_mru = path.join(dir_path, "mrua_velocidad-t.txt")
                                    with open(datos_mru, "w") as handle:
                                            for i in t:
                                                    v_f=v_i+a*(t_f-t_i)
                                                    texto = "La velocidad en t=" + str(i) + " es " + str(v_f)
                                                    print(texto, file=handle)
                                    texto_pausado("Se ha generado correctamente un archivo en el directorio.",0.05)
                                    _sssubrun = False
                                # aceleración
                                elif ssuboption == str(3):
                                    clear()
                                    texto_pausado('--- MRUA - aceleración ---\n',0.025)
                                    texto_pausado('Recuerde que la aceleración en un MRUA está dada por\n\n',0.01)
                                    texto_pausado('a = (v_f - v_i) / (t_f - t_i) \n\n',0.02)
                                    try:
                                        v_f = real(input("\nIntroduzca un valor de 'v_f': "))
                                        v_i = real(input("\nIntroduzca un valor de 'v_i': "))
                                        t_f = real(input("\nIntroduzca un valor de 't_f': "))
                                        t_i = real(input("\nIntroduzca un valor de 't_i': "))
                                    except:
                                        z_3 = 0
                                    t = np.linspace(t_f,t_i,50)
                                    datos_mru = path.join(dir_path, "mrua_aceleracion.txt")
                                    with open(datos_mru, "w") as handle:
                                        for i in t:
                                            a=(v_f-v_i)/(t_f-t_i)
                                            texto = "La aceleración en t=" + str(i) + " es " + str(a)
                                            print(texto, file=handle)
                                    texto_pausado("Se ha generado correctamente un archivo en el directorio.",0.05)
                                    _sssubrun = False
                                # salir
                                elif ssuboption == str(4):
                                    _sssubrun = False
                                # error
                                else:
                                    texto = "\nPor favor, introduzca una opción válida\n"
                                    texto_pausado(texto,0.02)                                
                            else:
                                texto = "\n[1] Calcular para valores diferentes"
                                texto_pausado(texto,0.01)
                                texto = "\n[Q] Subir un nivel\n"
                                texto_pausado(texto,0.01)
                                subopcion = input("> ")
                                if subopcion == str(1):
                                    z_3 = 0
                                    _ssubrun = True
                                elif subopcion == 'Q' or subopcion == 'q':
                                    _ssubrun = False
                                else:
                                    texto = "\nPor favor, introduzca una opción válida\n"
                                    texto_pausado(texto,0.02)
                    # Tiro parabólico
                    elif suboption == str(3):
                        clear()
                        texto_pausado('---- Tiro parabólico  ----\n',0.025)
                        texto = 'Se arroja como resultado un archivo con los datos de un tiro parabólico, en un intervalo de tiempo.\n'
                        texto_pausado(texto,0.025)
                        texto_pausado("[1] Alcance",0.025)
                        texto_pausado("\n[2] Altura máxima",0.025)
                        texto_pausado("\n[Q] Subir un nivel\n",0.025)
                        ssuboption = input("> ")
                        z_3 = 0
                        _sssubrun = True
                        while _sssubrun:
                            if z_3 == 0:
                                g = 9.80665
                                # alcance
                                if ssuboption == str(1):
                                    clear()
                                    texto_pausado('--- Tiro parabólico - alcance ---\n',0.025)
                                    texto_pausado('Recuerde que el alcance horizontal en un tiro parabólico está dada por\n\n',0.01)
                                    texto_pausado('x_max = (v_i²•sin(2θ))/ℊ\n\n',0.02)
                                    try:
                                        v_0 = real(input("\nIntroduzca un valor de 'v_0': "))
                                        theta = real(input("\nIntroduzca un valor de 'θ' (en radianes): "))
                                    except:
                                        z_3 = 0
                                    datos_mru = path.join(dir_path, "tp_alcance.txt")
                                    with open(datos_mru, "w") as handle:
                                        x_max = (((v_0)**2)*math.sin(2*theta))/g
                                        texto = "El alcance máximo del proyectil es " + str(x_max)
                                        print(texto, file=handle)
                                    texto_pausado("Se ha generado correctamente un archivo en el directorio.",0.05)
                                    _sssubrun = False
                                # altura máxima
                                elif ssuboption == str(2):
                                    clear()
                                    texto_pausado('--- MRUA - altura máxima ---\n',0.025)
                                    texto_pausado('La altura máxima en un tiro parabólico está dada por\n',0.01)
                                    texto_pausado('y_max = (v_i²•sin²θ)/(2ℊ) \n\n',0.02)
                                    try:
                                        v_i = real(input("\nIntroduzca un valor de 'v_i': "))
                                        theta = real(input("\nIntroduzca un valor de 'θ': "))
                                    except:
                                        z_3 = 0
                                    datos_mru = path.join(dir_path, "tp_alturamax.txt")
                                    with open(datos_mru, "w") as handle:
                                        y_max = (((v_i)**2)*(math.sin(theta)**2))/(2*g)
                                        texto = "La altura máxima que alcanza el proyectil es " + str(y_max)
                                        print(texto, file=handle)
                                    texto_pausado("Se ha generado correctamente un archivo en el directorio.",0.05)
                                    _sssubrun = False
                                elif ssuboption == 'Q' or ssuboption == 'q':
                                    z_3 = 1
                                    _sssubrun = False
                                else:
                                    texto = "\nPor favor, introduzca una opción válida\n"
                                    texto_pausado(texto,0.02)                                
                            else:
                                texto = "\n[1] Calcular para valores diferentes"
                                texto_pausado(texto,0.01)
                                texto = "\n[Q] Subir un nivel\n"
                                texto_pausado(texto,0.01)
                                subopcion = input("> ")
                                if subopcion == str(1):
                                    z_3 = 0
                                    _ssubrun = True
                                elif subopcion == 'Q' or subopcion == 'q':
                                    _ssubrun = False
                                else:
                                    texto = "\nPor favor, introduzca una opción válida\n"
                                    texto_pausado(texto,0.02)
                    # Salir
                    elif suboption == 'Q' or suboption == 'q':
                        _subrun = False
                    # Error
                    else:
                        texto = "\nPor favor, introduzca una opción válida\n"
                        texto_pausado(texto,0.02)
                else:
                    pass                
            else:
                texto = "\n[1] Realizar otro cálculo."
                texto_pausado(texto,0.01)
                texto_pausado("\n[Q] Menu principal\n",0.01)
                subopcion = input("> ")
                if subopcion == str(1):
                    z_1 = 0
                    _subrun = True
                elif subopcion == 'Q' or subopcion == 'q':
                    _subrun = False
                else:
                    texto_pausado("\nPor favor, introduzca una opción válida\n",0.02)
    
    elif option == 'Q' or option == 'q':
        clear()
        value = randint(0, 4)
        if value == 1:
            texto_pausado("Hasta la vista,",0.05)
            texto_pausado(" baby\n\n",0.15)
        elif value == 2:
            texto_pausado("Que la fuerza te acompañe\n\n",0.05)
        elif value == 3:
            texto_pausado("Adiós, vaquero\n\n",0.05)
        else:
            texto_pausado("Autodestrucción inicializada\n\n",0.1)
            texto_pausado("3\n\n",0.3)
            texto_pausado("2\n\n",0.3)
            texto_pausado("1\n\n",0.3)
            texto_pausado("Adiós\n\n",0.4)
        _run = False
        break

    else:
        texto_pausado("\nParece ser que no introdujiste una opción válida. Por favor, vuelve a intentarlo.\n",0.02)
        _run = True

kill(getppid(), signal.SIGHUP)
