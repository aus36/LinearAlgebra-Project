#Authors: Austin Hale, Zenon Nowakowksi
#Linear Algebra Final Project
#Topic 1: Perform transformations on vectors using numpy and matplotlib in Python

#imports
from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt

#test plotting
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

#rotation of vectors
theta = np.deg2rad(30)
rotation = np.array([cos(theta), -sin(theta)],[sin(theta), cos(theta)])
v1 = np.array([1, 2])

#scaling of vectors using scalar values