import sympy as sp
import numpy as np

x = sp.Symbol('x')

res_1702 = sp.integrate(1/(sp.sin(x)**2 + 2* sp.cos(x)**2), x)
res_1703 = sp.integrate(1/ sp.sin(x), x)
res_1704 = sp.integrate(1/sp.cos(x), x)
res_1705 = sp.integrate(1/sp.sinh(x), x)

print('1702: ', res_1702)
print('1703: ', res_1703)
print('1704: ', res_1704)
print('1705: ', res_1705)
