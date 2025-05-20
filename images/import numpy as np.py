import numpy as np

# Given matrices
coeff = np.array([
    [1, 1],
    [0.0, 0.4]
])

constant = np.array([1000, 150])

# Solving linear equations
solution = np.linalg.solve(coeff, constant)

x = solution[0]
y = solution[1]

# Output
print("x is the kg/hr of water evaporated =", x)
print("y is the kg/hr of thick liquor =", y)
print("Name: Sneha Deshpande")
print("PRN No: 202401050016")