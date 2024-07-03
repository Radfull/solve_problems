import sympy as sp
import numpy as np

a1 = sp.Matrix([2, 1, -3])
a2 = sp.Matrix([3, 1, -5])
a3 = sp.Matrix([4, 2, -1])
a4 = sp.Matrix([1, 0, -7])

A = sp.Matrix.hstack(a1, a2, a3, a4)
A_reduced = A.rref()

pivot_columns = A_reduced[1]

basis_vectors = [A.col(i) for i in pivot_columns]

print("Базис системы:")
for vector in basis_vectors:
    print(vector)

A = sp.Matrix.hstack(a1, a2, a3)

coeffs = sp.linsolve((A, a4)).args[0]

print(f"a4 = {coeffs[0]} * a1 + {coeffs[1]} * a2  {coeffs[2]} * a3")
