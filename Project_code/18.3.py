import sympy as sp
from sympy import pprint

# Пусть n = 4

A = sp.Matrix([
    [1,1,1, 1],
    [0,1,1, 1],
    [0,0,1, 1],
    [0,0,0, 1]
])

B = sp.Matrix([
    [1,2,3,4],
    [0,1,2,3],
    [0,0,1,2],
    [0,0,0,1]
])

res = B * A**(-1)
pprint(res)

