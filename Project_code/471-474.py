import sympy as sp
import numpy as np

x = sp.Symbol('x')
m = sp.Symbol('m', integer=True)
n = sp.Symbol('n', integer=True)

res_471 = sp.limit(sp.sin(5*x) / x, x, 0)
res_472 = sp.limit(sp.sin(x) / x, x, sp.oo)
res_473 = sp.limit(sp.sin(m*x) / sp.sin(n*x) , x, sp.pi)
res_474= sp.limit((1- sp.cos(x))/ x**2, x, 0)


print('471: ', res_471)
print('472: ', res_472)
print('473: ', res_473)
print('474: ', res_474)

