import sympy as sp
import numpy as np

n = sp.Symbol('n')

res = sp.summation((-1)**n/(n**2 + n - 2),(n,2,sp.oo))

print(res)
