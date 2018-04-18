from math import *

class nolin_eq:

    def __init__(self, p, T):
        self._p = p
        self._T = T
        self._k = 1.38 * 10**(-23)
        self._Ei = [12.08,0,0,0,0]
        self._Zi = [0,1,2,3,4]
        self._Qi = [1,4.30,5.98]
        self._Values = [0]*7

    def Ki(self, Qi1, Qi, Ei, deltaEi):
        '''Ki'''
        return (2 * 2.415 * 10**(-3) * Qi1/Qi * self._T**(3/2)*exp(-(Ei - deltaEi)*11603/self._T))

    def deltaEi(self, Zi1, Zi, G):
        '''deltaEi'''
        return (8.61 * 10**(-5) * self._T * log(((1+Zi1**2 * G/2)*(1+G/2))/(1 + Zi**2 * G/2)))

    def initial_value(self):
        '''Находит начальные приближения'''
        deltaEi = self.deltaEi(self._Zi[1], self._Zi[0], 0)
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
        self._Values[6] = 0

        print(self._Values)



create = nolin_eq(15, 8000)

create.initial_value()