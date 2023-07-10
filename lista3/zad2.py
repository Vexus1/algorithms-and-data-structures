from time import perf_counter
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def pop_method(tab):
    """Przeprowadza analizę eksperymentalną dla metody pop."""
    start = perf_counter()
    for i in range(200):
        j = randint(0,1000)
        tab.pop(j)
    stop = perf_counter()
    return len(tab), (stop - start)*1000


r = 20000
n = 100000

data = [pop_method(i) for i in ([randint(-r,r) for i in range(n)],  [randint(-r,r) for i in range(n*2)], [randint(-r,r) for i in range(n*3)], 
[randint(-r,r) for i in range(n*4)], [randint(-r,r) for i in range(n*5)], [randint(-r,r) for i in range(n*6)], [randint(-r,r) for i in range(n*7)],
[randint(-r,r) for i in range(n*8)], [randint(-r,r) for i in range(n*9)], [randint(-r,r) for i in range(n*10)], [randint(-r,r) for i in range(n*11)], 
[randint(-r,r) for i in range(n*12)], [randint(-r,r) for i in range(n*13)], [randint(-r,r) for i in range(n*14)], [randint(-r,r) for i in range(n*15)], 
[randint(-r,r) for i in range(n*16)], [randint(-r,r) for i in range(n*17)], [randint(-r,r) for i in range(n*18)], [randint(-r,r) for i in range(n*19)],
[randint(-r,r) for i in range(n*20)], [randint(-r,r) for i in range(n*21)], [randint(-r,r) for i in range(n*22)], [randint(-r,r) for i in range(n*23)])]
    
x = []
y = []
for i in data:
    x.append(i[0])
    y.append(i[1])

print(y)
plt.plot(x,y,'ro',label="Dane")
# plt.loglog(x1,y1,'ro',label="Dane")
plt.title("pop")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x,a,b):
    return a*x + b

popt, pcov = curve_fit(func,x,y)
x_ = np.arange(1,n*23)

plt.plot(x,y,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("pop fit")
plt.legend()
plt.show()
