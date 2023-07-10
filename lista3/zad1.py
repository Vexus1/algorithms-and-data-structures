import ctypes #tablice niskopoziomowe

class DynamicArray:
    
    def __init__(self):
        self._n = 0 #liczba elementów
        self._capacity = 1 #rozmiar tablicy
        self._A = self._make_array(self._capacity) #właściwa tablica
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
        
    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def insert(self,k,value):

        if k < 0 or k > self._n:
            raise IndexError("invalid index")
        
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        
        for i in range(self._n-1, k-1, -1):
            self._A[i+1] = self._A[i]

        self._A[k] = value
        self._n += 1


    def remove(self,value):
        if self._n == 0:
            raise ValueError("Array is empty")
        else:
            for i in range(self._n):
                if self._A[i] == value:
                    self._A[i] = None
        return

    def expand(self, *seq):
        for el in seq:
            self.append(el)
        
    def __str__(self):
        nums = ""
        for i in range(self._n):
            nums += str(self._A[i])+", "
        nums = nums[:-2]
        return "["+nums+"]"
        
    def _make_array(self,c):
        return (c*ctypes.py_object)()

d = DynamicArray()
d.append(2)
d.append(1)
d.append(3)
d.append(7)
d.insert(3,2137)
d.remove(2137)
d.expand(2,1,3,7,1337)
print(len(d))
print(str(d))
