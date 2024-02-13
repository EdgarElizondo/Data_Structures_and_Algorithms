
class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elem = 0
    # Iteration Method
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next
    # Creation Method
    def create(self,nodeValue):
        newNode = node(nodeValue)
        node.prev = None
        node.next = None
        self.head = newNode
        self.tail = newNode
        self.elem = 1
        return "The DLL has been created"
    # Insert Method
    def insert(self,nodeValue,location = 0):
        if location > self.elem:
            location = self.elem
            print("Location out of list bounderies adjusted")
        
        if self.head is None:
            return self.create(nodeValue)
        else:
            newNode = node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif (location == -1)|(location == self.elem):
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0
                tempNode = self.head
                while index < location - 1:
                    index += 1
                    tempNode = tempNode.next
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
            self.elem += 1
    
    # Traversal Method
    def traversal(self,reverse = False):
        if self.head is None:
            print("The DLL is empty")
        else:
            if reverse == True:
                tempNode = self.tail
                while tempNode:
                    print(tempNode.value)
                    tempNode = tempNode.prev
            else:
                tempNode = self.head
                while tempNode:
                    print(tempNode.value)
                    tempNode = tempNode.next
    # Search Index Method
    def index(self,nodeValue):
        if self.head is None:
            print("The CSLL is empty")
        else:
            ind = 0
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return ind
                ind += 1
                tempNode = tempNode.next
            return "Value not found"
    
    # Deletion Method
    def delete(self,location = 0):
        if self.head is None:
            print("The DLL is empty")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.elem = 0
            else:
                if location == 0:
                    self.head = self.head.next
                    self.head.prev = None
                elif (location == -1)|(location == self.elem):
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    index = 0
                    tempNode = self.head
                    while index < location - 1:
                        index += 1
                        tempNode = tempNode.next
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode
                self.elem -= 1
    
    # Clear Method
    def clear(self):
        if self.head is None:
            print("The DLL is already empty")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            self.elem = 0
            return "CLSS clear"