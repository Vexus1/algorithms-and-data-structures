class Stack:
    def __init__(self):
        self._data = [] #nowy pusty stos
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self,e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()        
    

class Queue_with_two_stacks:

    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()

    def enqueue(self, e):
        self._stack1.push(e)

    def dequeue(self):
        if self._stack2.is_empty():
            while len(self._stack1) > 0:
                self._stack2.push(self._stack1.pop())
            x = self._stack2.pop()
            while len(self._stack2) > 0:
                self._stack1.push(self._stack2.pop())
            return x


q = Queue_with_two_stacks()

for i in range(8):
    q.enqueue(i)

for i in range(8):
    print(q.dequeue())
 