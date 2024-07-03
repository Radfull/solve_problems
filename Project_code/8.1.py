from sympy import Matrix, pprint
from sympy.solvers.solveset import linsolve
import sympy as sp

x1, x2, x3, x4, x5 = sp.symbols('x1, x2, x3, x4, x5')

augmented_matrix = Matrix([
    [6, 4, 5, 2, 3, 1],
    [3, 2, -2, 1,0, -7],
    [9, 6, 1, 3, 2, 2],
    [3, 2, 4, 1, 2, 3]
])

row_reduced_matrix, _ = augmented_matrix.rref()

pprint(sp.linsolve(row_reduced_matrix, (x1, x2, x3, x4, x5 )))
