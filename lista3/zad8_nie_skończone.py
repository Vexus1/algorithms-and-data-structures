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

def permutations(n):
    s = Stack()
    numbers = (i for i  in range(1, n+1, -1))
    # print(type(numbers))
    for i in numbers:
        print(i)
        s.push(([i], numbers - set([i])))
    while not s.is_empty():
        tab1, left = s.pop()
        if len(left) == 0:
            print(tab1)
        else:
            for i in left:
                tab2 = tab1[:]
                tab2.append(i)
                s.push((tab2, numbers - set(tab2)))

print(permutations(4)) 
