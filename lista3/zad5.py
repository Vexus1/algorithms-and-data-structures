class Queue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]

    def _clear_memory(self):
        new_data = []
        for i in range(0, len(self._data)):
            if self._data[i] != None:
                new_data.append(self._data[i])
        self._data = new_data
        self._front = 0
        return 

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        if self._size <= 2:
            self._clear_memory()
        return value
    
    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def _resize(self,cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front

        for k in range(self._size): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0    
    

Q = Queue()
for i in range(1,11):
    print(Q.enqueue(i))

Q.enqueue(3)
print(len(Q))

for i in range(1, 9):
    print(Q.dequeue())
print(len(Q))

for i in range(1,11):
    Q.enqueue(i)

print(len(Q))
for i in range(1, 11):
    print(Q.dequeue())

print(len(Q))
Q.enqueue(1)
print(len(Q))
