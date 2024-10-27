class Stack:
    def __init__(self):
        self.A = []
        
    def __len__(self):
        return len(self.A)
    
    def is_empty(self):
        return len(self.A)==0
    
    def push(self, item):
        return self.A.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.A.pop()
        else:
            raise IndexError('Empty')
    def peek(self):
        if not self.is_empty():
            return self.A[-1]
        else:
            raise IndexError("Empty")
        