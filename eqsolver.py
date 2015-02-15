#!/usr/bin/python

# Import librarys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define parameters

T = 1
C = 1

n1 = 1100
Kd1 = 2

n2 = 1000
Kd2 = 1


# Use the numerical solver to find the roots
n_solutions = 200
x_list = np.linspace(1, 2e4, n_solutions)
F_list = np.zeros(n_solutions)

F_solution = 0.5
for i in range(n_solutions):
	# Redefine n1
	n1 = x_list[i]

	# Define function
	concentration_function = lambda F : n1*C/(1+Kd1/F) + n2*C/(1+Kd2/F) - T

	# Solve numerically with the solution from previous iteration as initial guess
	F_solution = fsolve(func=concentration_function, x0=F_solution, xtol=1e-6)
	F_list[i] = F_solution

	# Print result
	print 'x: %20.8f \t\tF: %20.8f' % (x_list[i], F_solution)




# Plot it

plt.plot(x_list, F_list)
plt.xlabel("x")
plt.ylabel("F")
plt.grid()
plt.show()