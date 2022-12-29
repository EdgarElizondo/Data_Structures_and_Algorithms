

class Queue:
    def __init__(self,limit = None):
        self.items = []
        self.limit = limit

    def __str__(self):
        values = [str(x) for x in self.items]
        return "["+','.join(values)+"]"

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return "The Queue is full"
        self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "The Queue is empty"
        self.items = self.items[1:]

    def peek(self):
        if self.isEmpty():
            return "The Queue is empty"
        return self.items[0]

    def delete(self):
        self.items = []



