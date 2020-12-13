print("Bienvenidx. Este script te permitirá calcular el volumen de tres polígonos platónicos.")

while True:
    print("""Teclea el número del sólido que deseas calcular el volumen: Tetraedro [1], Octaedro  [2], Icosaedro [3]
    
    O bien, teclea [4] para salir del programa.""")

    option = input("> ")

    # Tetraedro
    if option == str(1):
        while True:
            try:
                l = float(input("Valor de la arista: "))
                break
            except ValueError:
                print("Por favor introduce una longitud válida para el arista.")
        v = ((2**(1/2))*(l)**3)/(12)
        print("El volumen de un tetraedro regular con aristas de longitud " + str(l) + " es " + str(v) + " u³" + """
        
        """)

    # Octaedro
    elif option == str(2):
        while True:
            try:
                l = float(input("Valor de la arista: "))
                break
            except ValueError:
                print("Por favor introduce una longitud válida para el arista.")
        v = ((2**(1/2))*(l)**3)/(3)
        print("El volumen de un octaedro regular con aristas de longitud " + str(l) + " es " + str(v) + " u³" + """
        
        """)

    # Icosaedro
    elif option == str(3):
        while True:
            try:
                l = float(input("Valor de la arista: "))
                break
            except ValueError:
                print("Por favor introduce una longitud válida para el arista.")
        v = ((5)/(12))*(3+(5)**(1/2))*(l**3)
        print("El volumen de un icosaedro regular con aristas de longitud " + str(l) + " es " + str(v) + " u³" + """ 
        
        """)

    elif option == str(4):
        break

    else:
        print("Por favor introduce una opción válida")
