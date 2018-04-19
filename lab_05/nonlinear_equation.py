from math import *

class nolin_eq:

    def __init__(self, p, T):
        self._p = p
        self._T = T
        self._G = 0
        self._k = 1.38 * 10**(-23)
        self._Ei = [12.08, 22.21, 32.10, 32.10]
        self._Zi = [0,1,2,3,4]
        self._Qi = [1, 4.30, 5.98, 5.98, 5.98]
        self._Values = [0]*6

    def Ki(self, Qi1, Qi, Ei, deltaEi):
        '''Ki'''

        return (2 * 2.415 * 10**(-3) * Qi1/Qi * self._T**(3/2) * exp(-(Ei - deltaEi) * 11603/self._T))

    def deltaEi(self, Zi1, Zi, G):
        '''deltaEi'''

        return (8.61 * 10**(-5) * self._T * log(((1+Zi1**2 * G/2)*(1+G/2))/(1 + Zi**2 * G/2)))

    def initialValue(self):
        '''Find initial approximations'''
        deltaEi = self.deltaEi(self._Zi[1], self._Zi[0], self._G)
        Ki = self.Ki(self._Qi[1], self._Qi[0], self._Ei[0], deltaEi)
        b = 2*Ki
        d = (b)**2 - 4 * (-(Ki*(self._p /(self._k * self._T))))

        x1 = (-b + sqrt(d))/2
        x2 = (-b - sqrt(d))/2

        if x1 > 0:
            ne = x1
        else:
            ne = x2

        n1 = self._p /(self._k * self._T) - 2 * ne
        n2 = ne

        self._Values[0] = log1p(ne)
        self._Values[1] = log1p(n1)
        self._Values[2] = log1p(n2)
        self._Values[3] = -100
        self._Values[4] = -120
        self._Values[5] = -170

        print(self._Values)

    def findScalars(self):
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
                        [exp(Ve), exp(x1), exp(x2), exp(x3), exp(x4), exp(x5)],
                        [exp(Ve), 0, z2 * exp(x2), z3 * exp(x3), z4 * exp(x4), z5 * exp(x5)]]

        membersMatrix = [-(Ve + x2 - x1 - log1p(self.Ki(Q2, Q1, E1, self.deltaEi(z2, z1, G)))),
                         -(Ve + x3 - x2 - log1p(self.Ki(Q3, Q2, E2, self.deltaEi(z3, z2, G)))),
                         -(Ve + x4 - x3 - log1p(self.Ki(Q4, Q3, E3, self.deltaEi(z3, z2, G)))),
                         -(Ve + x5 - x4 - log1p(self.Ki(Q5, Q4, E4, self.deltaEi(z4, z3, G)))),
                         -(exp(Ve) + exp(x1) + exp(x2) + exp(x3) + exp(x4) + exp(x5) - alpha -
                           ((self._p * 7.242 * 10 **3)/self._T)),
                         -(exp(Ve) - z2 * exp(x2) + z3 * exp(x3) + z4 * exp(x4) + z5 * exp(x5))]

        return scalarMatrix, membersMatrix


    def findCoefs(self):
        '''Gauss'''

        a, b = self.findScalars()

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




    def increment(self):
        pass
