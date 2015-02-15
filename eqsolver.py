#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the expression whose roots we want to find


T = 1
C = 1

n1 = 1000
Kd1 = 2

n2 = 1000
Kd2 = 1


func = lambda F : n1*C/(1+Kd1/F) + n2*C/(1+Kd2/F) - T


# Use the numerical solver to find the roots

F_initial_guess = 0.5
F_solution = fsolve(func, F_initial_guess)

print "The solution is F = %f" % F_solution
print "at which the value of the expression is %f" % func(F_solution)

n1_range = np.linspace(0, 100, 200)

F_initial_guess = F_solution
for n1 in n1_range:
	func = lambda F : n1*C/(1+Kd1/F) + n2*C/(1+Kd2/F) - T
	F_solution = fsolve(func, F_solution)
	print('n1: %20.8f \t\tF: %20.8f' % (n1, F_solution))
# # Plot it
	
# F = np.linspace(0, 1.5, 201)

# plt.plot(F, func(F))
# plt.xlabel("F")
# plt.ylabel("expression value")
# plt.grid()
# plt.show()
