import sympy as sp

M = sp.Matrix([
    [1, 5, 3, 5, -4],
    [3, 1, 2, 9, 8],
    [-1, 7, -3, 8, -9],
    [3, 4, 2, 4, 7],
    [1, 8, 3, 3, 5]
])
res = sp.det(M)

print(res)


