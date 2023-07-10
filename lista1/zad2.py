from time import perf_counter
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from random import randint

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = 1000, 2000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 42500, 50000

def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    start = perf_counter()
    for j in range(n):
        total += S[j]
    stop = perf_counter()
    return total, (stop-start)*1000, n


data1 = [example1(i) for i in ([randint(0,50) for i in range(n1)], [randint(0,50) for i in range(n2)], [randint(0,50) for i in range(n3)],
[randint(0,50) for i in range(n4)], [randint(0,50) for i in range(n5)], [randint(0,50) for i in range(n6)], [randint(0,50) for i in range(n7)],
[randint(0,50) for i in range(n8)], [randint(0,50) for i in range(n9)], [randint(0,50) for i in range(n10)], [randint(0,50) for i in range(n11)])]
print(data1)
    
x1 = []
y1 = []
for i in data1:
    x1.append(i[2])
    y1.append(i[1])

print(x1)
print(y1)
plt.plot(x1,y1,'ro',label="Dane")
# plt.loglog(x1,y1,'ro',label="Dane")
plt.title("example1")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x1,a,b):
    return a*x1 + b

popt, pcov = curve_fit(func,x1,y1)
x_ = np.arange(1,n11)

plt.plot(x1,y1,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("example1 fit")
plt.legend()
plt.show()

def example2(S):
    """Return the sum of the elements with even index in sequence S.
    """
    n = len(S)
    total = 0
    start = perf_counter()
    for j in range(0, n, 2):
        total += S[j]
    stop = perf_counter()
    return total, (stop-start)*1000, n


data2 = [example1(i) for i in ([randint(0,50) for i in range(n1)], [randint(0,50) for i in range(n2)], [randint(0,50) for i in range(n3)],
[randint(0,50) for i in range(n4)], [randint(0,50) for i in range(n5)], [randint(0,50) for i in range(n6)], [randint(0,50) for i in range(n7)],
[randint(0,50) for i in range(n8)], [randint(0,50) for i in range(n9)], [randint(0,50) for i in range(n10)], [randint(0,50) for i in range(n11)])]
print(data2)
    
x2 = []
y2 = []
for i in data2:
    x2.append(i[2])
    y2.append(i[1])

print(x2)
print(y2)
plt.plot(x2,y2,'ro',label="Dane")
# plt.loglog(x2,y2,'ro',label="Dane")
plt.title("example2")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x2,a,b):
    return a*x2 + b

popt, pcov = curve_fit(func,x2,y2)

x_ = np.arange(1,n11)

plt.plot(x2,y2,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("example2 fit")
plt.legend()
plt.show()


def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    start = perf_counter()
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    stop = perf_counter()
    return total, (stop-start)*1000, n


data3 = [example3(i) for i in ([randint(0,50) for i in range(int(n1/10))], [randint(0,50) for i in range(int(n2/10))], [randint(0,50) for i in range(int(n3/10))],
[randint(0,50) for i in range(int(n4/10))], [randint(0,50) for i in range(int(n5/10))], [randint(0,50) for i in range(int(n6/10))], [randint(0,50) for i in range(int(n7/10))],
[randint(0,50) for i in range(int(n8/10))], [randint(0,50) for i in range(int(n9/10))], [randint(0,50) for i in range(int(n10/10))], [randint(0,50) for i in range(int(n11/10))])]
print(data3)


x3 = []
y3 = []
for i in data3:
    # print(i)
    x3.append(i[2])
    y3.append(i[1])

print(x3)
print(y3)
plt.plot(x3,y3,'ro',label="Dane")
# plt.loglog(x3,y3,'ro',label="Dane")
plt.title("example3")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x3,a,b):
    return a*x3**2 + b

popt, pcov = curve_fit(func,x3,y3)
x_ = np.arange(1,int(n11/10))

plt.plot(x3,y3,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("example3 fit")
plt.legend()
plt.show()


def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex
    sums in A."""
    n = len(A)
    count = 0
    start = perf_counter()
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1
    stop = perf_counter()
    return total, (stop-start)*1000, n


data4_0 = [
    [
    [randint(0,50) for i in range(int(n1/100))], [randint(0,50) for i in range(int(n2/100))], [randint(0,50) for i in range(int(n3/100))], [randint(0,50) for i in range(int(n4/100))],
    [randint(0,50) for i in range(int(n5/100))], [randint(0,50) for i in range(int(n6/100))], [randint(0,50) for i in range(int(n7/100))], [randint(0,50) for i in range(int(n8/100))],
    [randint(0,50) for i in range(int(n9/100))], [randint(0,50) for i in range(int(n10/100))], [randint(0,50) for i in range(int(n11/100))]
    ],
    [
    [randint(0,50) for i in range(int(n1/100))], [randint(0,50) for i in range(int(n2/100))], [randint(0,50) for i in range(int(n3/100))],[randint(0,50) for i in range(int(n4/100))],
    [randint(0,50) for i in range(int(n5/100))], [randint(0,50) for i in range(int(n6/100))], [randint(0,50) for i in range(int(n7/100))], [randint(0,50) for i in range(int(n8/100))],
    [randint(0,50) for i in range(int(n9/100))], [randint(0,50) for i in range(int(n10/100))], [randint(0,50) for i in range(int(n11/100))]
    ]
]
data4_1 = data4_0[0]
data4_2 = data4_0[1]

data4 = []
for i in range(0,len(data4_1)):
    data = [example4(data4_1[i],data4_2[i])]
    # print(data)
    data4+=data
    
    
x4 = []
y4 = []
for i in data4:
    print(i)
    x4.append(i[2])
    y4.append(i[1])

print(x4)
print(y4)
plt.plot(x4,y4,'ro',label="Dane")
# plt.loglog(x4,y4,'ro',label="Dane")
plt.title("example4")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x4,a,b):
    return a*x4**3 + b

popt, pcov = curve_fit(func,x4,y4)
x_ = np.arange(1,int(n11/100))

plt.plot(x4,y4,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("example4 fit")
plt.legend()
plt.show()