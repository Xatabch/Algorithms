from legendre import *
from math import *
from bisection import *

def f(x):
    '''Функция'''
    return (1 / sqrt(2 * pi)) * (e ** (- (x ** 2) / 2))

def gauss(m):
    '''Метод Гаусса'''
    # Приводим к треугольному виду
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    # Вычисление ответов
    ans = []
    m.reverse() #переворачиваю так как идет с конца в начало
    for sol in range(len(m)):
            if sol == 0:
                ans.append(m[sol][-1] / m[sol][-2])
            else:
                inner = 0
                for x in range(sol):
                    inner += (ans[x]*m[sol][-2-x])
                # уравнение теперь преобразовано в ax + b = c
                # решаем уравнение при помощи (c - b) / a
                ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans

def legendre(n):
    '''Полином Лежандра'''
    roots = []
    roots_inter = []
    h = 2 / n
    a = -1
    b = a + h
    l = get_legendge_polynomial(n)

    while len(roots_inter) != n:
        roots_inter = []

        while b <= 1:
            if l.get(a) * l.get(b) < 0:
                roots_inter.append([a, b])
            a = b
            b += h

        h /= 2
        a = -1
        b = a + h

    for i in roots_inter:
        roots.append(bisection_x(i[0], i[1], 1e-5, l.get))
    return roots

def system_of_equations(N, leg):
    '''Составляет (3) систему уравнений'''

    system = [] # матрица коэффициентов при неизвестных

    for i in range(N):
        system.append([])
        for j in range(N):
            system[i].append(leg[j]**i)

        if(i%2 != 0):
            system[i].append(0)
        else:
            system[i].append(2/(i+1))

    return system



def integral(N, b):
    '''Алгоритм интеграла'''

    #1. Задаем количество узлов N

    #2. Находим корни полнома N-й степени

    leg = legendre(N)

    #3. Из 1-х N ур-й системы (3) находим Ai N-шт(Решаем СЛАУ методом Гаусса)

    syst = system_of_equations(N, leg)
    Ai = gauss(syst)

    #4. Определить переход от [-1 1] к [a b] по ф-ле x = (b-a)/2*t + (a+b)/2 (замена)

    a = 0

    return (b - a) / 2 * sum(Ai[i] * f((b - a) / 2 * leg[i] + (a + b) / 2) for i in range(N))

def F(N, x, α):
    ''''''
    return integral(N, x) - α

def bisection_xy(N, a, b, k, f):

    c = (a + b) / 2
    while abs(b - a) > 0.001 * abs(c) + 0.001:
        c = (a + b) / 2
        if f(N, b, k) * f(N, c, k) < 0:
            a = c
        else:
            b = c
    return (a + b)/2

if __name__ == "__main__":
    a = 0
    b = 5
    alpha = float(input("Альфа: "))
    n = int(input("Введите степень полинома Лежандра: "))

    print("Alpha = ",alpha ," N = ",n ," X= ", bisection_xy(n, a, b, alpha, F))





