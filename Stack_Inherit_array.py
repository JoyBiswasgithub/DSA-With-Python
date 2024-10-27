class Stack(list):
    def push(self, item):
        self.append(item)
        
    def is_empty(self):
        return len(self)==0
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('Empty')
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Empty')
        
    def insert(self, index, data):
        raise AttributeError("Attribute not Found")