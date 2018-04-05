from pylab import *

class Priblizhenie:

    def __init__(self, data, n):
        self._data = data
        self._n = n
        self._N = len(data)

    def bazis_function(self, x, k):
        return x**k

    def scalar_phi(self, k, m):
        '''(Phi_k, Phi_m) =
        sum(data[i][2] * bazis_function(data[i][0], k+m))from i = 1 to N'''

        sum = 0

        for i in range(0,self._N,1):
           sum += self._data[i][2] * self.bazis_function(self._data[i][0], (k + m))

        return sum


    def scalar_y(self, k):
        '''(y, Phi_k) =
        sum(data[i][2] * data[i][1]*bazis_function(data[i][0], k))from i = 1 to N'''

        sum = 0

        for i in range(0, self._N,1):
            sum += self._data[i][2] * self._data[i][1] * self.bazis_function(self._data[i][0], k)

        return sum


    def find_scalars(self):
        '''am * (x^k,x^m) + am*(x^k,x^m) + ... = (y,x^m)'''

        scalars_array = []
        free_members_array = []

        for k in range(self._n + 1):
            scalars_array.append([])
            free_members_array.append(self.scalar_y(k))
            for m in range(self._n + 1):
                scalars_array[k].append(self.scalar_phi(k,m))

        return scalars_array, free_members_array


    def find_coeffs(self):
        '''Find coefficents of polynom'''

        a, b = self.find_scalars()

        x = [0] * (self._n+1)

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



array = [[0.75, 2.5, 1], [1.5, 1.2, 1], [2.25, 1.12, 1], [3, 2.25, 1], [3.75, 4.28, 1]]
x = [0.75, 1.50, 2.25, 3.00, 3.75]
y = [2.50, 1.20, 1.12, 2.25, 4.28]


utochnenie = Priblizhenie(array, 2)

coeffs = utochnenie.find_coeffs()

x1 = np.arange(0.75,5,0.5)
y1 = coeffs[0] + coeffs[1]*x1 + coeffs[2]*x1**2

plot(x,y, '*r')
plot(x1,y1)

show()





