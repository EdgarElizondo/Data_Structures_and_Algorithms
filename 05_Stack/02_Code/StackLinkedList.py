
class __node__:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class __ll__:
    def __init__(self):
        self.head = None
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next
        
class Stack:

    def __init__(self,limit = None):
        self.ll = __ll__()
        self.limit = limit

    def __str__(self):
        values = [str(x.value) for x in self.ll]
        return '\n'.join(values)

    def isEmpty(self):
        if self.ll.head is None:
            return True
        else:
            return False
    
    def isFull(self):
        return False

    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            newNode = __node__(value)
            newNode.next = self.ll.head
            self.ll.head = newNode

    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            popvalue = self.ll.head.value
            self.ll.head = self.ll.head.next
            return popvalue

    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.ll.head.value

    def delete(self):
        self.ll.head = None


