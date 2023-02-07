#!/usr/bin/env python3
# by Ashley Aguilar
# UNAM
# ashaguilar06@gmail.com
# x = ax + b

import matplotlib.pyplot as plt
import numpy as np

def f(x, a, b):
	return a*x + b

print("1st dynamic system\n x = a*x + b")

#initial condition
A = np.arange(0,50,1)

for a in A:
	b = 2.0
	x0 = 0.5
	N = 100

	print("a = "+ str(a))
	print("b = "+ str(b))
	print("x0 = "+ str(x0))
	print("N = "+str(N))

	i = np.arange(0, N, 1)

	x = x0

	#vector
	X = []

	for _ in i:
		print(x)
		X.append(x)
		x = f(x, a, b)

	plt.plot(X)

plt.yscale("log")
plt.show()




#print("Hola mundo")
