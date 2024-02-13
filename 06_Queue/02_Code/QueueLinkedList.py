

class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode  = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.queue]
        return "["+",".join(values)+"]"

    def isEmpty(self):
        if self.queue.head is None:
            return True
        return False
            
    def enqueue(self,value):
        newNode = node(value)
        if self.isEmpty():
            self.queue.head = newNode
            self.queue.tail = newNode
        else:
            self.queue.tail.next = newNode
            self.queue.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            tempNode = self.queue.head
            if self.queue.head == self.queue.tail:
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.queue.head
    
    def delete(self):
        if self.isEmpty():
            return "The queue is already empty"
        else:
            self.queue.head = None
            self.queue.tail = None
