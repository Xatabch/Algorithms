import algorithms
from math import *
from prettytable import PrettyTable

def f(x):
    return exp(x)

def table_x_y(begin, end, step):

    table = [[], [], [], [], [], [], []]
    sz = int((end - begin + step)/step)

    for i in range(int(sz)):
        table[0].append(begin)
        table[1].append(f(begin))
        begin += step

    return table


if __name__ == "__main__":
    # begin = float(input("Введите начало отрезка x: "))
    # end = float(input("Введите конец отрезка x: "))
    # step = float(input("Введите шаг: "))
    begin = 0
    end = 5
    step = 0.001

    tb = table_x_y(begin, end, step)
    tb = algorithms.one_sided(tb, step)
    tb = algorithms.central(tb, step)
    tb = algorithms.increased_accuracy(tb, step)
    tb = algorithms.runge(tb, step)
    tb = algorithms.alig(tb, step)

    table = PrettyTable()
    table.add_column("X", tb[0])
    table.add_column("Y", tb[1])
    table.add_column("Односторонняя", tb[2])
    table.add_column("Центральная", tb[3])
    table.add_column("Повышенная точность", tb[4])
    table.add_column("Рунге", tb[5])
    table.add_column("Выравнивающее", tb[6])

    print(table)