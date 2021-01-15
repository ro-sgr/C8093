import numpy as np

from os import system, name, path, kill, getppid

dir_path = path.dirname(path.realpath(__file__))

# x_f = float(input("\nIntroduzca un valor de 'x_f': "))
# x_i = float(input("\nIntroduzca un valor de 'x_i': "))
# t_f = float(input("\nIntroduzca un valor de 't_f': "))
# t_i = float(input("\nIntroduzca un valor de 't_i': "))

x_f = 10
x_i = 2
t_f = 9
t_i = 3

delta_x = x_f-x_i
t = np.linspace(t_f,t_i,50)

# for i in t:
#         v = (x_f-x_i)/i
#         texto = "La velocidad en t=" + str(i) + " es " + str(v)
#         print(texto)

datos_mru = path.join(dir_path, "datos_mru.txt")

with open(datos_mru, "w") as handle:
        for i in t:
                v = (x_f-x_i)/i
                texto = "La velocidad en t=" + str(i) + " es " + str(v)
                print(texto, file=handle)