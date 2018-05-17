from numpy import *

# Односторонняя производная (y(i+1)-y(i))/(x(i+1)-x(i)) или y(i+1)-y(i)/H
def one_sided(table, h):

    for i in range(len(table[0]) - 1):
        table[2].append((table[1][i+1] - table[1][i])/h)

    table[2].append(None)

    return table

# Центральная производная Y'n = (Y(n+1) - Y(n-1))/2h
def central(table, h):

    table[3].append(None)

    for i in range(1,len(table[0]) - 1):
        table[3].append((table[1][i+1] - table[1][i-1])/(2*h))

    table[3].append(None)

    return table

# Повышенная точность в граничных точках y0 = (-3*y0 + 4 * y1 - y2)/(2*h)
# yn = (3*y(n-1) - 4 * y(n-2) + y(n-3))/(2*h)
def increased_accuracy(table, h):

    table[4].append((-3*table[1][0] + 4 * table[1][1] - table[1][2])/(2*h))

    for i in range(1, len(table[0])-1):
        table[4].append(None)

    table[4].append((3*table[1][len(table[0])-1] - 4 * table[1][len(table[0])-2] + table[1][len(table[0])-3])/(2*h))

    return table

# Рунге
def runge(table, h):
    h2 = h * 2
    p = 1 # степень
    vec1 = []
    vec2 = []

    for i in range(len(table[0]) - 2):
        vec1.append((table[1][i+1] - table[1][i])/h)
        vec2.append((table[1][i+2] - table[1][i])/h2)
        table[5].append(vec1[i] + (vec1[i] - vec2[i]) / (2**p - 1))

    table[5].append(None)
    table[5].append(None)

    return table

# Выравнивающие переменные (экспонента)
def alig(table, h):

    n_tab = [[],[],[],[]]

    for i in range(len(table[0])):
        n_tab[0].append(table[0][i])
        n_tab[1].append(log(table[1][i]))

    n_tab = central(n_tab, h)
    table[6].append(None)
    for i in range(1, len(table[0]) - 1):
        if table[0][i] != 0:
            table[6].append(n_tab[3][i] * table[1][i])
        else:
            table[6].append(None)
    table[6].append(None)

    return table

