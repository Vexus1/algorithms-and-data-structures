from time import perf_counter
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def extend_performance(tab2):
    """Analiza wydajności metody extend"""
    tab1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
    start = perf_counter()
    tab1.extend(tab2)
    stop = perf_counter()
    return len(tab1), (stop-start)*1000



def append_performance(tab2):
    """Analiza wydajności metody append"""
    tab1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
    start = perf_counter()
    for i in tab2:
        tab1.append(i)
    stop = perf_counter()
    return len(tab1), (stop-start)*1000



tab2a = [i for i in range(0,1000)]
tab2b = [i for i in range(0,10000)]
tab2c = [i for i in range(0,1000000)]
tab2d = [i for i in range(0,5000000)]
tab2e = [i for i in range(0,10000000)]
tab2f = [i for i in range(0,20000000)]
tab2g = [i for i in range(0,40000000)]


# print(f"extend: {extend_performance(tab2a)}")
# print(f"append: {append_performance(tab2a)}")
# print(f"extend: {extend_performance(tab2b)}")
# print(f"append: {append_performance(tab2b)}")
# print(f"extend: {extend_performance(tab2c)}")
# print(f"append: {append_performance(tab2c)}")
# print(f"extend: {extend_performance(tab2d)}")
# print(f"append: {append_performance(tab2d)}")
# print(f"extend: {extend_performance(tab2e)}")
# print(f"append: {append_performance(tab2e)}")
# print(f"extend: {extend_performance(tab2f)}")
# print(f"append: {append_performance(tab2f)}")
# print(f"extend: {extend_performance(tab2g)}")
# print(f"append: {append_performance(tab2g)}")


data_extend = [extend_performance(i) for i in (tab2a,tab2b,tab2c,tab2d,tab2e,tab2f,tab2g)]
x_extend = []
y_extend = []

for i in data_extend:
    x_extend.append(i[0])
    y_extend.append(i[1])


data_append = [append_performance(i) for i in (tab2a,tab2b,tab2c,tab2d,tab2e,tab2f,tab2g)]
    
x_append = []
y_append = []

for i in data_append:
    x_append.append(i[0])
    y_append.append(i[1])


plt.plot(x_extend,y_extend,'ro', label="extend")
plt.plot(x_append,y_append,'go', label="append")
plt.title("append vs extend")
plt.xlabel('array length')
plt.ylabel('execution time')
plt.legend()
plt.show()


def func_extend(x_extend,a,b):
    return a*x_extend + b

popt_extend, pcov_extend = curve_fit(func_extend,x_extend,y_extend)

def func_append(x_append,a,b):
    return a*x_append + b

popt_append, pcov_append = curve_fit(func_append,x_append,y_append)
x_ = np.arange(1,40000010)

plt.plot(x_extend,y_extend,'ro',label="extend_data")
plt.plot(x_,func_extend(x_,*popt_extend),'b-',label="extend_model")
plt.plot(x_append,y_append,'go',label="append_Dane")
plt.plot(x_,func_append(x_,*popt_append),'y-',label="append_Model")
plt.xlabel('array length')
plt.ylabel('execution time')
plt.title("extend vs append fit")
plt.legend()
plt.show()