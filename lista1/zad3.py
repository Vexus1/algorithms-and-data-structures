from time import perf_counter
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from random import randint

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = 1000, 2000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 42500, 50000

def zad3(tab):
    start = perf_counter()
    x = sorted(tab)
    stop = perf_counter()
    return x, len(tab), (stop-start)*1000

data_zad3 = [zad3(i) for i in ([randint(0,50) for i in range(n1)], [randint(0,50) for i in range(n2)], [randint(0,50) for i in range(n3)],
[randint(0,50) for i in range(n4)], [randint(0,50) for i in range(n5)], [randint(0,50) for i in range(n6)], [randint(0,50) for i in range(n7)],
[randint(0,50) for i in range(n8)], [randint(0,50) for i in range(n9)], [randint(0,50) for i in range(n10)], [randint(0,50) for i in range(n11)])]


x5 = []
y5 = []
for i in data_zad3:
    x5.append(i[1])
    y5.append(i[2])


print(x5)
print(y5)
plt.plot(x5,y5,'ro',label="Dane")
# plt.loglog(x5,y5,'ro',label="Dane")
plt.title("zad 3")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x5,a,b):
    return a*x5*np.log(x5) + b

popt, pcov = curve_fit(func,x5,y5)

x_ = np.arange(1,n11)

plt.plot(x5,y5,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("zad 3 fit")
plt.legend()
plt.show()