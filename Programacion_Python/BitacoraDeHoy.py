# IPython log file

get_ipython().system('pwd')
get_ipython().system('ls')
get_ipython().run_line_magic('pinfo', 'who')
get_ipython().run_line_magic('pinfo2', 'range')
get_ipython().run_line_magic('logstart', 'BitacoraDeHoy.py')
from fractions import Fraction
from math import *
from scipy import stats
import pandas as pd
3 + 2
3 * (-7.1 + 10**2)
1/2
3/2
1/2.
a = 2 ** 2 ** 2 ** 2 ** 2
1 + 3j
1j * 1j
j # sólito, da un error
# Esto es un "comentario" (no se lee, por lo que no cuenta) que se extiende hasta el final de la línea.
e
pi
a
a = 3
b = 17.5
c = 1 + 3j

print(a + b / c)
a = 3
a = -5.5
a = float(3)

pi_short = float('3.1416')
Mypi = int(pi_short)

b = int(17.)

edad = int("19")

year = str(1998)
a
pi_short
Mypi
type(Mypi)
edad
type(edad)
year
type(year)
len(year)
"hola"
'mi edad es: '
cadena = "hola " + 'mi edad es: '
cadena
len(cadena)
from mpmath import *
l = [3, 4, 6]
l2 = [3.5, -1, "hola", [1.0, [3, 17]]]
l3 = [1, 2, 3]
print(l3[0], l3[1])
l[0] = 5
l
ls = [1, 2, 3, 6, 7]
ls[1:3]
ls[:3]
ls[3:]
len(ls)
l = [] # lista vacía
l.append(17)
l.append(3)
print(l, len(l))
get_ipython().run_line_magic('pinfo2', 'range')
range(10)
range(4)
range(3,10)
range(3,17,2)
range(3,17,3)
range(3,17,5)
range(3.,10.)
from numpy import *
from numpy import *
a = array( [1, 2, -1, 100] )
a
a.dtype
b = zeros(10)
print(b)
b = ones(10)
print(b)
a = arange(0., 10., 0.1)
a
l = linspace(0., 10., 11)
l
a = r_[1,2,10,-1.]
a
r_[3:7]
r_[3:7:0.5]
r_[3:7:10j]
v1 = array( [1., 4., 7. ])
v2 = array( [1., 2., -2. ])

print(v1, v2)
v1+v2
v1-v2
v1*v2
v1/v2
v1**v2
dot(v1,v2)
cross(v1,v2)
def gauss(x):
    return 1./(sqrt(2.)) * exp(-x*x / 2.)
gauss( r_[0:10] )
a = array([0, 1, 2, 3])
print(a[0], a[2])
b = a[1:3]
b
b[1] = 10
l=[1,2,3]; k=l; k[1] = 10
l
k
M = array( [ [1, 2], [3, 4] ] )
M
M.shape
M.shape = (4, 1)
print(M)
M.reshape( 2, 2 )
M = r_[0:4].reshape(2,2)
def f(i, j):
    return i+j

M = fromfunction(f, (3, 3))

M
print(M[0])
M[0][1]
M[0, 1]
M.item(1)
M = identity(10)
M[3:5]
M[:, 3:5]
M[3:9, 3:5]     #matriz identidad de 10x10
tile( M, (2,2) )
diagonal(M)
diagonal(M, 1)
diag([1,2,3])
diag([1,2,3], 2)
from random import *   #'random' ya esta cargado!
get_ipython().run_line_magic('pinfo', 'random')
random()
for i in range(10):
    print(random())
