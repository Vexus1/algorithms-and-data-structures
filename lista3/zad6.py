class Deque:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]*Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._data[self._front]

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize_back(2*len(self._data))
        avail = (self._front + self._size)%len(self._data) # 3+2 % 6 = 5
        self._data[avail] = e
        self._size += 1
        return

    def add_first(self, e):
        if self._front == 0:
            self._resize_front(2*len(self._data))
        avail = self._front - 1
        self._data[avail] = e
        self._size += 1
        self._front -= 1
        return

    def delete_last(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        index = self._front + self._size - 1
        value = self._data[index]
        self._data[index] = None
        self._size -= 1
        return value

    def delete_first(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        return value
        
    def _resize_back(self,cap):
        # print("resize_back S ", self._data)
        old = self._data
        self._data = [None]*cap
        walk = self._front

        for k in range(self._size): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0    
        # print("resize_back E ", self._data)

    def _resize_front(self,cap):
        # print("resize_front S ", self._data)
        old = self._data
        added = cap - len(self._data)
        walk = self._front
        self._data = [None]*cap

        for k in range(added, cap): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = self._front + added
        # print("resize_front E ", self._data)


D = Deque()
for i in range(1,11):
    D.add_last(i)
print(len(D))

for i in range(1, 9):
    print(D.add_first(i*(-1)))

print(len(D))
print(D.delete_first())
print(len(D))
print(D.delete_last())
print(len(D))
print(D.delete_last())
print(len(D))
print(D.delete_last())
print(len(D))
