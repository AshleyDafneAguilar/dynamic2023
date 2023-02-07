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
X0 = np.arange(1,50,1)

for x0 in X0:
	a = -1.0
	b = 2.0
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

#plt.yscale("log")
plt.show()

