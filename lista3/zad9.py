from collections import deque

class Stack:
 
    def __init__(self):
        self._data1 = deque()
        self._data2 = deque()
    
    def is_empty(self):
        return len(self._data1)==0
 
    def push(self, e):
        self._data2.append(e)
        while self._data1:
            self._data2.append(self._data1.popleft())
        self._data1, self._data2 = self._data2, self._data1
 
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data1.popleft()
 
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data1[0]
 
    def __len__(self):
        return len(self._data1)
 
# złożoność push -> n, pop -> 1, top -> 1

s = Stack()
s.push(432)
s.push(64)
s.push(23)
s.push(3)
s.push(37)
s.push(332)
print(len(s))
print(s.top())
s.pop()
print(s.top())
print(len(s))
