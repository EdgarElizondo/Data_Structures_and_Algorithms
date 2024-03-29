
from random import randint

class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next
    
    def __str__(self):
        values =  [str(x.value) for x in self]
        return '->'.join(values)

    def __len__(self):
        result = 0
        tempNode = self.head
        while tempNode:
            result += 1
            tempNode = tempNode.next
        return result

    def add(self, value):
        if self.head is None:
            newNode = node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self,n,min_value,max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return    






