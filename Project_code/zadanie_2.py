import copy
from sympy import pprint, Matrix

def L(A, xc, j):

    res = 0
    for i in range(len(xc)):
        res += A[j][i] * xc[i]
    return res

def error_calc(x, xn):
    
    max_error = 0
    for i in range(len(x)):
        max_error = max(max_error, abs(xn[i] - x[i]))
    return max_error

def zeid(A, B, eps, start=0):
    n = len(A)
    det_A = Matrix(A).det() 
    if det_A == 0: # Проверка на невырожденность 
        raise ValueError
    if start == 0 or len(start) != n:
        start = [0] * n # Задаем начальный вектор
    X = []
    X.append(start)
    error = float('inf')
    xn = [0] * n
    k = 0
    while error > eps:
        k += 1
        x = X[-1]
        xc = copy.copy(x) # Создаем переменную для сохранения вектора для следующего шага

        for j in range(n):
            xn[j] = round((1 / float(A[j][j])) * (B[j] - (L(A, xc, j) - A[j][j] * xc[j])), 6)  # Находим вектор xn
            xc[j] = xn[j]
        
        X.append(copy.copy(xn))
        error = error_calc(x, xn)  # Вычисление ошибки
        if error > 10000 or k == 1000:
            raise(RuntimeError('Итерация не сходиться!'))
    return X

def prt(X):
    k = 1
    sz = len(X)
    for i in range(sz):
        if i == sz-1:
            print('Ответ: \n')
        else:
            print(f'{i} Итерация: \n')

        for j in range(len(X[i])):
            print(f'x{k} =',X[i][j])
            k += 1
        k = 1
        print('\n')

if __name__ == '__main__':

    try:
        f = open('z_2_file.txt', 'r')
        rows, cols = map(int, f.readline().split())
        eps = float(f.readline())

        # Заполняем матрицы A и B
        A = [[float(i) for i in f.readline().split()] for j in range(rows)]
        B = [float(i) for i in f.readline().split()]

        M = Matrix(A)
        M1  = []
        
        # Проверяем ранги основой и расширенной матрицы
        for i in range(rows):
            M1.append(A[i])
            M1[i].append(B[i])

        M1 = Matrix(M1)

        # Если они совпали, то пытаемся найти решение
        if M1.rref()[0].rank() == M.rref()[0].rank():

            A1 = []
            B1 = []

            for i in range(M1.rref()[0].rank()):
                A1.append(A[i][:-1])
                B1.append(B[i])

            print('A = ', M)
            print('B = ', B)
            print('Точность: ', eps)
            X = zeid(A1, B1,eps)
            prt(X)

        # Иначе система не имеет решений
        else:
            print('Система не имеет решений!')

    # Обработки ошибок
    except RuntimeError as er:
        print(er)

    except ZeroDivisionError:
        print('На ноль делить нельзя! Поменяйте местами уравнения ')

    except ValueError:
        print('В файле данные введены некорректно!')
        
    except IndexError:
        print('Введите систему полностью!')

