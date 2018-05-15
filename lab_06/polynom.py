class Polynomial:
    def __init__(self, n, k=None):
        self.degree = n
        if k is None:
            self.koef = [0 for i in range(n + 1)]
        else:
            if len(k) > n:
                k = k[:n + 1]
            self.koef = [x for x in k]

    def __imul__(self, other):
        for i in range(len(self.koef)):
            self.koef[i] *= other
        return self

    def __isub__(self, other):
        if self.degree < other.degree:
            return None
        else:
            i = other.degree
            j = self.degree
            while i != -1:
                self.koef[j] -= other.koef[i]
                i -= 1
                j -= 1
            return self

    def up_degree(self) :
        self.degree += 1
        self.koef.append(0)

    def get(self, x):
        res = 0
        for i in range(self.degree + 1):
            res += (self.koef[i] * (x ** (self.degree - i)))
        return res

    def __str__(self):
        i = self.degree
        prnt_str = ""
        for k in self.koef:

            if not i:
                prnt_str += " + {0}".format(k)
            else:
                if k:
                    if i != self.degree:
                        prnt_str += " + "
                    prnt_str += "{0}x^{1}".format(k, i)
            i -= 1
        return  prnt_str