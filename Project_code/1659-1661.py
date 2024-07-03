import sympy as sp

x = sp.Symbol('x')

res_1659 = sp.integrate(1 /(5*x - 2)**(5/2), x)
res_1660 = sp.integrate(sp.simplify('(1-2*x+x**2)**(1/5) / (1-x)'), x)
res_1661 = sp.integrate(1/(2+3*x**2), x)

print('1659: ', res_1659)
print('1660: ', res_1660)
print('1661: ', res_1661)
