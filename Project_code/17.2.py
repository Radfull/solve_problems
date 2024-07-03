import sympy as sp
from sympy import pprint

A = sp.Matrix([
    [3, 0, 2],
    [0, 1, 3],
    [2, 2, 0],
    [0, 1, 0]
])

B = sp.Matrix([
    [1, 2, -1, 2],
    [-2,-1, 1, 2],
    [2, 1, 1, 2]
])

C = sp.Matrix([
    [0, -4, 6, 1],
    [2, 2, -5, -2],
    [2, -2, 6, 4],
    [1, 3, 0, 1]
])
res = A * B + C

pprint(res)
