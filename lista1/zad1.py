from time import perf_counter
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from random import randint


p = [9,5,2,5,6,7,4,3,2]

def wielomian_On2(p,x):
    """Algorytm klasy O(n^2) obliczenia wartości wielomianu w punkcie"""
    wynik = 0
    for i in range(0, len(p)):
        suma = p[i]
        for j in range(0, len(p)-1-i):
            suma *= x
        wynik += suma
    return wynik

print(wielomian_On2(p,1))




def wielomian_Onlogn(p,x):
    """Algorytm klasy O(nlogn) obliczenia wartości wielomianu w punkcie"""
    z = [0]*len(p)
    w = x
    for i in range(0,len(p)):
        z[i] = w
        w *= x

    return wielomian_Onlogn_oblicz(z,p,x)

def wielomian_Onlogn_oblicz(z,p,x):

    if len(p) == 1:
        return p[0]
    k = len(p) // 2
    a = wielomian_Onlogn_oblicz(z,p[:k],x)
    b = wielomian_Onlogn_oblicz(z,p[k:],x)
    return a+b*z[len(p[k:])]

print(wielomian_Onlogn(p,1))




n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = 1000, 2000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 42500, 50000

def schemat_hornera1(p,x):

    wynik = 0
    start = perf_counter()
    for i in range(0, len(p)):
        a = p[i]
        wynik += a*x**i
    stop = perf_counter()
    return wynik, len(p), (stop-start)*1000


print(schemat_hornera1(p,1))


data = [schemat_hornera1(i, 1) for i in ([randint(0,50) for i in range(n1)], [randint(0,50) for i in range(n2)], [randint(0,50) for i in range(n3)],
[randint(0,50) for i in range(n4)], [randint(0,50) for i in range(n5)], [randint(0,50) for i in range(n6)], [randint(0,50) for i in range(n7)],
[randint(0,50) for i in range(n8)], [randint(0,50) for i in range(n9)], [randint(0,50) for i in range(n10)], [randint(0,50) for i in range(n11)])]
print(data)
    
x = []
y = []
for i in data:
    # print(i)
    x.append(i[1])
    y.append(i[2])

print(x)
print(y)
plt.plot(x,y,'ro',label="Dane")
# plt.loglog(x1,y1,'ro',label="Dane")
plt.title("horner")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x,a,b):
    return a*x + b

popt, pcov = curve_fit(func,x,y)

x_ = np.arange(1,n11)

plt.plot(x,y,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("horner fit")
plt.legend()
plt.show()