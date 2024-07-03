import sympy as sp
import numpy as np

x = sp.Symbol('x')

n = input('Введите n: ')

y = sp.sin(x)**3

res = sp.diff(y,x,n)

print(res)
