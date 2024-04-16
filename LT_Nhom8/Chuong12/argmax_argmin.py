import numpy as np
import matplotlib.pyplot as plt

N = 100
L = 1

def f(i,n):
    x = i * L/N
    lam = 2 * L/ (n+1)
    return  x * (L-x) * np.sin(2 * np.pi*x/lam)

a = np.fromfunction(f,(N+1,5))
min_i = a.argmin(axis = 0)
max_i = a.argmin(axis =0)
print(plt.plot(a, c = 'k'))
print(plt.plot(min_i,a[min_i, np.arange(5)],'v', c = 'k', markersize = 10))
print(plt.plot(max_i,a[max_i, np.arange(5)],'^', c = 'k', markersize = 10))
print(plt.xlabel(r'$x$'))
print(plt.ylabel(r'$f(x,n)$'))
print(plt.show())
