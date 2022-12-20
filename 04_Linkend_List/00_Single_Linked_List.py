
class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class sl_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elem = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #
    def insert(self,value,location = 0):
        if location > self.elem:
            location = self.elem
            print("Location is adjusted to list bounderies")
        
        newNode  = node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if (location == 0):
                newNode.next = self.head
                self.head = newNode    
            elif (location == self.elem)|(location == -1):
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0
                tempNode = self.head
                while index != location - 1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
        self.elem += 1
    # Trasverse Singly Linked List
    def traverse(self):
        if self.head is None:
            print("The SLL is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    # Search index value
    def index(self,nodeValue):
        if self.head is None:
            print("The SLL is empty")
        else:
            ind = 0
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return ind
                ind += 1 
                node = node.next
            return "The value does not exist in this list"
    #
    def delete(self,location = 0):
        if self.head is None:
            print("The SLL is empty")
        else:
            if self.elem == self.tail:
                self.head = None
                self.tail = None
            else:
                if (location == 0):
                    self.head = self.head.next
                elif (location == self.elem)|(location == -1):
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
                else:
                    index = 0
                    tempNode = self.head
                    while index < location -1:
                        tempNode = tempNode.next
                        index +=1
                    nextNode = tempNode.next
                    tempNode.next = nextNode.next

    def remove(self,value):
        if self.head is None:
            print("The SLL is empty")
        else:
            pass
    def clear(self):
        if self.head is None:
            print("The SLL is empty")
        else:
            self.head = None
            self.tail = None
