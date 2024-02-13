
class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elem = 0

    # Len Method
    def __len__(self):
        return self.elem
    
    # Iteration Method
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                break

    # Creation Method
    def create(self,nodeValue):
        newNode = node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        self.elem = 1
        return "The DLL has been created"

    # Insert element Method
    def insert(self,nodeValue,location = 0):
        if location > self.elem:
            location = self.elem
            print("Location out of list bounderies adjusted")
        
        if self.head is None:
            return self.create(nodeValue)
        else:
            newNode = node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
            elif (location == -1)|(location == self.elem):
                newNode.next = self.head
                newNode.next = self.head
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
            else:
                index = 0 
                tempNode = self.head
                while index < location - 1:
                    index += 1
                    tempNode = tempNode.next
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                newNode.prev.next = newNode
            self.elem += 1
                
    # Trasversal Method
    def trasversal(self,reverse = False):
        if self.head is None:
            print("The CDLL is empty")
        else:
            if reverse:
                tempNode = self.tail
                while tempNode:
                    print(tempNode.value)
                    tempNode = tempNode.prev
                    if tempNode == self.head.prev:
                        break
            else:
                tempNode = self.head
                while tempNode:
                    print(tempNode.value)
                    tempNode = tempNode.next
                    if tempNode == self.tail.next:
                        break
                
    # Search index value
    def index(self,nodeValue):
        if self.head is None:
            print("The CDLL is empty")
        else:
            ind = 0
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return ind
                if tempNode == self.tail:
                    return "Value not found"
                ind += 1
                tempNode = tempNode.next
                
    # Deletion Method
    def delete(self,location = 0):
        if self.head is None:
            print("The CDLL is empty")
        else:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                if location == 0:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
                elif (location == -1)|(location == self.elem):
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    index = 0
                    tempNode = self.head
                    while index < location - 1:
                        index += 1
                        tempNode = tempNode.next
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode
                self.elem -= 1

    # Clear all linked list method
    def clear(self):
        if self.head is None:
            print("The CDLL is already empty")
        else:
            tempNode = self.head
            self.tail.next = None
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            self.elem = 0
