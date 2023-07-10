from time import perf_counter
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Empty(Exception):
    pass
class LinkedStack:
    #--- -Node class- ---
    class _Node:
        __slots__ = '_element', '_next' #faster memory access
        
        def __init__(self,element,next):
            self._element = element
            self._next = next
            
    #--- -Stack methods- ---
    def __init__(self): #empty stack
        self._head = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._head._element
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


S = LinkedStack()

def push_analyse(n):
    start = perf_counter()
    S.push(n)
    stop = perf_counter()
    return (stop-start)*1000, n

push_data = [push_analyse(i) for i in range(0,100)]
print(push_data)

x_push = []
y_push = []

for i in push_data:
    x_push.append(i[1])
    y_push.append(i[0])


print(x_push)
print(y_push)
plt.plot(x_push,y_push,'ro',label="Dane")
# plt.loglog(x1,y1,'ro',label="Dane")
plt.title("push_analyse")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x_push,a,b):
    return 0*x_push + 0.00025

popt, pcov = curve_fit(func,x_push,y_push)
x_ = np.arange(0,100)

plt.plot(x_push,y_push,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("push_analyse fit")
plt.legend()
plt.show()


print(S.__len__())
print(S.top())


def pop_analyse(n):
    iter = []
    time = []
    for n in range(0,n):
        start = perf_counter()
        S.pop()
        iter.append(n)
        stop = perf_counter()
        time.append((stop-start)*1000)
    return time, iter

pop_data = pop_analyse(100)
print(pop_data[0])

x_pop = pop_data[1]
y_pop = pop_data[0]
plt.plot(x_pop,y_pop,'ro',label="Dane")
# plt.loglog(x1,y1,'ro',label="Dane")
plt.title("pop_analyse")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.legend()
plt.show()


def func(x_pop,a,b):
    return 0*x_pop + 0.0005

popt, pcov = curve_fit(func,x_pop,y_pop)
x_ = np.arange(0,100)

plt.plot(x_pop,y_pop,'ro',label="Dane")
plt.plot(x_,func(x_,*popt),'b-',label="Model")
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas wykonania')
plt.title("pop_analyse fit")
plt.legend()
plt.show()
