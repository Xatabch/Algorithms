from math import *
import numpy as np


class nolin_eq:

    def __init__(self, p, T):
        self._p = p
        self._T = T
        self._G = 0
        self._k = 1.38 * 10**(-23)
        self._Ei = [12.13, 20.96, 31.05, 42.2]
        self._Zi = [0, 1, 2, 3, 4]
        self._Qi = [1, 4.30, 5.98, 4, 5]
        self._Values = [0]*6

        self.initial_value() #set initial values

    def print_values(self):
        print(self._Values)

    def Ki(self, Qi1, Qi, Ei, deltaEi):
        '''Ki'''

        return (2 * 2.415 * 10**(-3) * Qi1/Qi * self._T**(3/2) * exp(-(Ei - deltaEi) * 11603/self._T))

    def deltaEi(self, Zi1, Zi, G):
        '''deltaEi'''

        return (8.61 * 10**(-5) * self._T * log(((1+Zi1**2 * G/2)*(1+G/2))/(1 + Zi**2 * G/2)))

    def initial_value(self):
        '''Find initial approximations'''

        z1 = self._Zi[0]
        z2 = self._Zi[1]

        Q1 = self._Qi[0]
        Q2 = self._Qi[1]

        E1 = self._Ei[0]

        T = self._T
        p = self._p
        k = self._k

        G = self._G

        deltaEi = self.deltaEi(z2, z1, G)
        Ki = self.Ki(Q2, Q1, E1, deltaEi)
        b = 2*Ki
        d = (b)**2 - 4 * (-(Ki*(p /(k * T))))

        x1 = (-b + sqrt(d))/2
        x2 = (-b - sqrt(d))/2

        if x1 > 0:
            ne = x1
        else:
            ne = x2

        n1 = p /(k * T) - 2 * ne
        n2 = ne

        self._Values[0] = -2#log1p(ne)
        self._Values[1] = log1p(n1)
        self._Values[2] = -2#log1p(n2)
        self._Values[3] = -100
        self._Values[4] = -120
        self._Values[5] = -170

    def find_scalars(self):
        '''Find members for Gauss'''

        Ve = self._Values[0]
        x1 = self._Values[1]
        x2 = self._Values[2]
        x3 = self._Values[3]
        x4 = self._Values[4]
        x5 = self._Values[5]

        Q1 = self._Qi[0]
        Q2 = self._Qi[1]
        Q3 = self._Qi[2]
        Q4 = self._Qi[3]
        Q5 = self._Qi[4]

        z1 = self._Zi[0]
        z2 = self._Zi[1]
        z3 = self._Zi[2]
        z4 = self._Zi[3]
        z5 = self._Zi[4]

        E1 = self._Ei[0]
        E2 = self._Ei[1]
        E3 = self._Ei[2]
        E4 = self._Ei[3]

        G = self._G

        alpha = 0.285 * 10**(-11) * (G * self._T)**3

        scalarMatrix = [[1, -1, 1, 0, 0, 0],
                        [1, 0, -1, 1, 0, 0],
                        [1, 0, 0, -1, 1, 0],
                        [1, 0, 0, 0, -1, 1],
                        [np.exp(Ve), np.exp(x1), np.exp(x2), np.exp(x3), np.exp(x4), np.exp(x5)],
                        [np.exp(Ve), 0, -z2 * np.exp(x2), -z3 * np.exp(x3), -z4 * np.exp(x4), -z5 * np.exp(x5)]]

        membersMatrix = [-(Ve + x2 - x1 - log1p(self.Ki(Q2, Q1, E1, self.deltaEi(z2, z1, G)))),
                         -(Ve + x3 - x2 - log1p(self.Ki(Q3, Q2, E2, self.deltaEi(z3, z2, G)))),
                         -(Ve + x4 - x3 - log1p(self.Ki(Q4, Q3, E3, self.deltaEi(z3, z2, G)))),
                         -(Ve + x5 - x4 - log1p(self.Ki(Q5, Q4, E4, self.deltaEi(z4, z3, G)))),
                         -(np.exp(Ve) + np.exp(x1) + np.exp(x2) + np.exp(x3) + np.exp(x4) + np.exp(x5) - alpha -
                           ((self._p * 7.242 * 10 **3)/self._T)),
                         -(np.exp(Ve) - z2 * np.exp(x2) + z3 * np.exp(x3) + z4 * np.exp(x4) + z5 * np.exp(x5))]

        return scalarMatrix, membersMatrix

    def find_coefs(self):
        '''Gauss'''

        a, b = self.find_scalars()

        x = [0] * 6

        for k in range(len(a)):
            for j in range(k+1,len(a[k])):
                d = a[j][k] / a[k][k]
                for i in range(k, len(a[k])):
                    a[j][i] = a[j][i] - d * a[k][i]
                b[j] = b[j] - d * b[k]

        for k in range(len(a)-1, -1, -1):
            d = 0
            for j in range(k + 1, len(a[k])):
                s = a[k][j] * x[j]
                d = d + s
            x[k] = (b[k] - d) / a[k][k]

        return x

    def func(self, G):
        '''G**2 - f(G) = 0'''

        Ve = self._Values[0]
        x2 = self._Values[2]
        x3 = self._Values[3]
        x4 = self._Values[4]
        x5 = self._Values[5]
        t = self._T

        z2 = self._Zi[1]
        z3 = self._Zi[2]
        z4 = self._Zi[3]
        z5 = self._Zi[4]

        summ = (np.exp(x2) * z2**2)/(1 + z2**2 * G/2) + (np.exp(x3) * z3**2)/(1 + z3**2 * G/2) + \
               (np.exp(x4) * z4**2)/(1 + z4**2 * G/2) + (np.exp(x5) * z5**2)/(1 + z5**2 * G/2)

        return G**2 - 5.85 * 10**10 * 1/t**3 * (np.exp(Ve)/(1 + G/2) + summ)

    def half_division(self):
        '''Method of half devision'''

        a = 0
        b = 1

        while (b - a)/b > 0.00001:
            c = (a+b)/2
            d = self.func(c) * self.func(a)
            if d > 0:
                a = c
            if d < 0:
                b = c

        return c


    def increment(self, values_array):
        """Increment roots"""

        self._Values[0] += values_array[0]
        self._Values[1] += values_array[1]
        self._Values[2] += values_array[2]
        self._Values[3] += values_array[3]
        self._Values[4] += values_array[4]
        self._Values[5] += values_array[5]


    def refinement(self):
        '''refinement itteration'''

        self.initial_value()

        Ve = self._Values[0]
        x1 = self._Values[1]
        x2 = self._Values[2]
        x3 = self._Values[3]
        x4 = self._Values[4]
        x5 = self._Values[5]

        values_array = self.find_coefs()

        while(abs(max((values_array[0]/Ve), (values_array[1]/x1), (values_array[2]/x2), (values_array[3]/x3), \
                  (values_array[4]/x4), (values_array[5]/x5)))) > 0.00001:

            self.increment(values_array)
            self._G = self.half_division()
            values_array = self.find_coefs()

        print(self._Values)



