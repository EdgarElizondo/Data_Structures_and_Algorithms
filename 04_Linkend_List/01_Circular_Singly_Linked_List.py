
class node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
#
class CSLL:
    # Init method
    def __init__(self):
        self.head = None
        self.tail = None
        self.elem = 0
    # Iteration method
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            
    
    # Creation of a Circular Singly Linked List
    def create(self,nodeValue):
        newNode = node(nodeValue)
        newNode.next = newNode
        self.head = newNode
        self.tail = newNode
        self.elem = 1
        return "The CSLL has been created"
    
    # Insert method in any location
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
                self.head = newNode
                self.tail.next = newNode
            elif (location == -1)|(location == self.elem):
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0
                tempNode = self.head
                # Find the location
                while index < location - 1:
                    index += 1
                    tempNode = tempNode.next
                # Insert the element in te n-th location
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            self.elem += 1
        
    # Trasversal Method
    def traversal(self):
        if self.head is None:
            print("The CSLL is empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.head:
                    break
    # Search Method
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
                if tempNode == self.tail.next:
                    return "Value not found"
    # Delete Method
    def delete(self):
        pass
    # Clear Method
    def clear(self):
        if self.head is None:
            print("The CSLL is already empty")
        else:
            self.head = None
            self.tail = None
            return "CLSS clear"
    
circular_SLL = CSLL()
circular_SLL.insert(1)
circular_SLL.insert(7)
circular_SLL.insert(15,1)
circular_SLL.insert(5,-1)
circular_SLL.insert(8,2)
circular_SLL.insert(13,-1)
circular_SLL.insert(10,3)

print([node.value for node in circular_SLL])
print(circular_SLL.clear())
print([node.value for node in circular_SLL])

