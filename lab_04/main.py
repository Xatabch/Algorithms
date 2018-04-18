from pylab import *
import least_square

array = [[0.75, 2.5, 1], [1.5, 1.2, 1], [2.25, 1.12, 1], [3, 2.25, 1], [3.75, 4.28, 1]]
x = [0.75, 1.50, 2.25, 3.00, 3.75]
y = [2.50, 1.20, 1.12, 2.25, 4.28]


utochnenie = least_square.Priblizhenie(array, 3)

coeffs = utochnenie.find_coeffs()

print(coeffs)

x1 = np.arange(0.75,1.5,0.5)
#print(len(x1))
#y1 = (coeffs[0],9,0)
y1 = coeffs[0] + coeffs[1]*x1 + coeffs[2]*x1**2
#y1 = [coeffs[0] for i in range(len(x1))]

plot(x,y, '*r')
plot(x1,y1)

show()





