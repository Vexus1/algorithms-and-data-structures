import os

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


dir_path = os.path.dirname(os.path.realpath(__file__))

def html_syntax(file):
    with open(file, 'r') as f:
        s = f.read()
        while(s.find("\n") != -1):
            s = s.replace("\n","")
        while(s.find("  ") != -1):
            s = s.replace("  ","")
    return s

def get_first_html_tag(html_string = ""):
    if len(html_string) == 0:
        return [None, html_string]
    index = html_string.find("<")
    endIndex = html_string.find(">")
    if index == -1 or endIndex == -1:
        return [None, html_string]
    tag = html_string[index+1:endIndex]
    html_string = html_string[endIndex+1:]
    return [tag.lower(), html_string]

def check_syntax(html_string = ""):
    s = Stack()
    tag = ""
    tag,html = get_first_html_tag(html_string)
    while tag != None:
        if tag[0] != "/":
            s.push(tag)
        else:
            tag = tag[1:]
            prevTag = s.pop()
            if(tag != prevTag):
                return False
        tag,html = get_first_html_tag(html)
    return True

html = html_syntax(f"{dir_path}\page.html")
print(check_syntax(html))


