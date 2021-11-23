from numpy import *
import matplotlib.pyplot as plt
import pylab

x = linspace(-5,5)
y = 1/x*sin(5*x)

plt.plot(x, y, 'r-', label = '1/x*sin(5*x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('My graph')
plt.legend(['1/x*sin(5*x)'],
        loc='upper left')

pylab.savefig('Graph 1.png',dpi=200)
plt.show()