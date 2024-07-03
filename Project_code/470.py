import sympy as sp
import numpy as np

x = sp.Symbol('x')
a_1 = sp.Symbol('a_1')
b_1 = sp.Symbol('b_1')
a_2 = sp.Symbol('a_2')
b_2 = sp.Symbol('b_2')

l_1 = sp.limit(sp.sqrt(x**2 - x + 1) - a_1 * x - b_1, x,sp.oo ,'-')
l_2 = sp.limit(sp.sqrt(x**2 - x + 1) - a_2 * x - b_2, x,sp.oo ,'+')

print(l_1)
print(l_2)


