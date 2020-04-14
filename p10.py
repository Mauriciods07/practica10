def obtenerMayor(param1, param2):
	if param1 < param2:
		print("{} es mayor que {}".format(param2, param1))

obtenerMayor(5, 7)
obtenerMayor(7, 5)

x = y = z = 3
if x == y ==z:
	print(True)

def obtenerMayorv2(param1, param2):
	if param1 < param2:
		return param2
	else:
		return param1

print("El mayor es {}".format(obtenerMayorv2(4, 20)))
print("El mayor es {}".format(obtenerMayorv2(11, 6)))

def obtenerMayor_idiom(param1, param2):
	valor = param2 if (param1 < param2) else param1
	return valor

print("El mayor es {}".format(obtenerMayor_idiom(11, 6)))

def numeros(num):
	if num == 1:
		print("tu número es 1")
	elif num == 2:
		print("tu número es 2")
	elif num == 3:
		print("tu número es 3")
	elif num == 4:
		print("tu numero es 4")
	else:
		pass

numeros(2)
numeros(4)
numeros(5)

def numeros_idiom(num):
	if num in (1, 2, 3, 4):
		print("tu número es {}".format(num))
	else:
		print("{} no es una opción".format(num))

def obtenerMasGrande(a, b, c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

print("El mas grande es {}".format(obtenerMasGrande(7, 13, 1)))

def cuenta(limite);
	i = limite
	while True:
		print(i)
		i = i - 1
		if i == 0:
			break

cuenta(10)

def factorial(n):
	i = 2
	tmp = 1
	while i  < n+1:
		tmp = tmp + i
		i = i + 1
	return tmp

print(factorial(4))
print(factorial(6))

for x in [1, 2, 3, 4, 5]:
	print(x)

for x in range(5):
	print(x)

for x in range(-5, 2):
	print(x)

for num in ["uno", "dos", "tres", "cuatro"]:
	print(num)

elementos = {'hidrogeno': 1, 'helio': 2, 'carbon': 6}
for llave, valor in elementos.items():
	print(llave, " = ", valor)

for llave in elementos.keys():
	print(llave)

for valor in elementos.values():
	print(valor)

for idx, x in enumerate(elementos):
	print("El indice es: {} y el elemento: {}".format(idx, x))

def cuenta_idiom(limite):
	for i in range(limite, 0, -1):
		print(i)
	else:
		print("Cuenta finalizada")

def cuenta_idiomv2(limite):
	for i in range(llimite, 0, -1):
		print(i)
		if i == 3:
			break
	else:
		print("Cuenta finalizada")

from math import *
x = cos(pi)
print(x)

print(dir(math))
help(math.log)

import math as ma
x = ma.cos(ma.pi)
print(x)

%pylab inline

import mathplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = linspace(0, 5, 20)

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, sin(x), marker='o', color='r', linestyle='None')

ax.grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.legend(["y = x**2"])

plt.title('Puntos')
plt.show()

fig.savefig("gráfica.png")