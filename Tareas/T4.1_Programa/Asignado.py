print("Bienvenidx. Este script te permitirá calcular las raíces de una función cuadrática.")

while True:
    print("Si deseas calcular las raíces introduce [1] si deseas salir introduce [2]")
    option = input("> ")

    if option == str(1):
        while True:
            try:
                a = float(input("Valor de a: "))
                while True:
                    try:
                        b = float(input("Valor de b: "))
                        while True:
                            try:
                                c = float(input("Valor de c: "))
                                break
                            except:
                                print("Por favor, introduce un número válido para 'c'.")
                        break
                    except:
                        print("Por favor introduce un número válido para 'b'.")
                break
            except ValueError:
                print("Por favor introduce un número válido para 'a'.")
        
        x_1 = (-b + (b**2-4*a*c)**(1/2) )/(2*a)
        x_2 = (-b - (b**2-4*a*c)**(1/2) )/(2*a)

        valor_a = "x²" if a==1 else "-x²" if a==-1 else str(a) + "x²"

        valor_b = "x" if b==1 else "-x" if b==-1 else "+" + str(b) + "x" if b>0 else str(b) + "x"

        valor_c = "" if c==0 else "+" + str(c) if c>0 else str(c)

        print("Las soluciones a la ecuación " + valor_a + valor_b + valor_c + " son: " + str(x_1) + " y " + str(x_2))

    elif option == str(2):
        break

    else:
        print("Por favor introduce una opción válida")
