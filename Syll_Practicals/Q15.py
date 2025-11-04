# Write a python program to create a Numpy array and perform the basic matrix operation.

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Transpose of A:\n", a.T)
