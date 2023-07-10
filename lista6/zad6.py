class Stack:
    def __init__(self):
        self._data = [] 
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self,e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        if self.__len__() >= 2:
            return self._data[-2], self._data[-1]
        else:
            return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()    

s = Stack()


def partition(array, start_index, end_index):
    pivot = array[end_index]
    pivot_index = start_index 
    
    for i in range(start_index, end_index):
        if array[i] <= pivot:
            array[pivot_index], array[i] = array[i], array[pivot_index]
            pivot_index += 1
 
    array[pivot_index], array[end_index] = array[end_index], array[pivot_index]

    return pivot_index

def quicksort(array, n):

    start_index = 0
    end_index = n - 1

    s.push(start_index)
    s.push(end_index)

    while s.__len__() != 0:

        if s.__len__() >= 2:
            start_index = s.top()[0]
            end_index = s.top()[1]
            s.pop()
        else: 
            start_index = s.top()
            s.pop()

        pivotindex = partition(array, start_index, end_index)

        if pivotindex - 1 > start_index:
            s.push(start_index)
            s.push(pivotindex - 1)

        if pivotindex + 1 < end_index:
            s.push(start_index + 1)
            s.push(end_index)
    
array = [9, -2, 4, 7, 2, 4, 0, -1, 23, 16, -5]
n = len(array)
sort = quicksort(array, n)
print(array)
