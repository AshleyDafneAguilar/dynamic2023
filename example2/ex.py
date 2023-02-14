#!/usr/bin/env python3
# by Ashley Aguilar
# UNAM
# ashaguilar06@gmail.com
# x = x + r + x**2


import matplotlib.pyplot as plt
import numpy as np

def  f(x, r):
	return x + r - (x**2)

X0 = np.arange(0.1, 0.2, 0.1)

for x0 in X0:
	r = 0.99999
	N = 20
	
	print("r="+ str(r))

	i = np.arange(0, N, 1)
	x = x0
	X = []

	for _ in i:
		print(x)
		X.append(x)
		x = f(x, r)

	plt.plot(X) 
plt.show()
