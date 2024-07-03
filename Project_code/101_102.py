import numpy as np
import sympy as sp

n = sp.Symbol('n', integer=True, positive=True)
xn = 1 - 1/n

sup_xn = sp.limit(xn, n, sp.oo)
inf_xn = sp.limit(xn, n, 1)

print(f"Верхняя граница (sup xn): {sup_xn}")
print(f"Нижняя граница (inf xn): {inf_xn}")


upper_limit = sp.limit(xn, n,sp.oo, '+')
lower_limit = sp.limit(xn, n,sp.oo ,'-')  

print(f"Верхний предел: {upper_limit}")
print(f"Нижний предел: {lower_limit}\n")

xn1 = (1/n + 1)
xn2 = (-1/n)

sup_xn = sp.limit(xn1, n, 2)
inf_xn = sp.limit(xn2, n, 1)
print(f"Верхняя граница (sup xn): {sup_xn}")
print(f"Нижняя граница (inf xn): {inf_xn}")


upper_limit = sp.limit(xn1, n,sp.oo, '+')
lower_limit = sp.limit(xn2, n,sp.oo ,'-') 

print(f"Верхний предел: {upper_limit}")
print(f"Нижний предел: {lower_limit}\n")
