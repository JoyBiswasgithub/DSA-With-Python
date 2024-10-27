class StackLinkList:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def push(self, item):
        new_node = StackLinkList(item)
        if self.n == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.n += 1
    
    def pop(self):
        if self.n == 0:
            return "Empty"
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.n -= 1
    
    def __len__(self):
        return self.n
        
    def peek(self):
        if self.n == 0:
            return "Empty"
        else:
            return self.head.data
        