#!/usr/bin/env python3
# by Ashley Aguilar
# UNAM
# ashaguilar06@gmail.com
# x = x + r + x**2


import matplotlib.pyplot as plt
import numpy as np

def  f(x, r):
	return x + r - (x**2)

x0 = 0.1
R = [0.1, 0.5, 1.0, 1.1, 1.5, 1.6]

for r in R:
	N = 30
	print("r = "+ str(r))
	x = x0
	X = []

	for _ in i:
		print(x)
		X.append(x)
		x = f(x, r)

	plt.plot(X)
	plt.ylim(0.0, 2.0) 
plt.show()
