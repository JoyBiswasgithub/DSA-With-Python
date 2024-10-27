class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0
    def __len__(self):
        return self.n
    
    def __str__(self):
        res = ''
        temp = self.head
        while (temp != None):
            res = res + str(temp.data) + '->'
            temp = temp.next
        return res[:-2]
    
    
    ##### Item Addition #############
    # If Empty Link List
    def empty(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node 
        self.n = self.n + 1   
        
    
    def add(self, item):
        if self.head == None:
            self.empty(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
            self.n = self.n +1
        
    def append(self, data):
        if self.head == None:
            self.empty(data)
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.n = self.n + 1

        
    def insert(self, pos, data):
        if pos <= 0 or pos > self.n + 1:
            return "Error - Out of Range"
        elif pos == 1:
            self.add(data)
        elif pos == self.n + 1:
            self.append(data)
        else:
            new_node = Node(data)
            temp = self.head
            i = 1
            while (i<pos-1):
                temp = temp.next
                i += 1
            new_node.next = temp.next
            temp.next = new_node
            self.n = self.n + 1
            
            
            
    ############ Item Deletion ###########
    def pop(self):
        if self.head == None:
            print("Empty Link List")
        else:
            self.head = self.head.next
            self.n -= 1
    def delete(self):
        if self.head == None:
            print("Empty Link List")
        elif (self.n == 1):
            self.pop()
        else:
            temp = self.head
            while(temp.next != self.tail):
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.n -= 1
        
    def delpos(self, pos):
        if pos <= 0 or pos > self.n:
            return "Error - Out of Range"
        if pos == 1:
            self.pop()
        elif pos == self.n:
            self.delete()
        else:
            temp = self.head
            i = 1
            while i < pos - 1:
                temp = temp.next
                i += 1
            if temp.next:
                temp.next = temp.next.next
            self.n -= 1
            
            
    ############ Search ###########3
    def search(self, item):
        temp = self.head
        flag = 0
        pos = 1
        while temp != None:
            if temp.data == item:
                flag = 1
                return pos
            temp = temp.next
            pos += 1
        if flag == 0:
            return "Item Not Found"
    
    def __getitem__(self, pos):
        if pos > self.n or pos<1:
            return "Error - Out of range"
        else:
            index = 1
            temp = self.head 
            while temp != None:
                if pos == index:
                    return temp.data
                temp = temp.next
                index += 1