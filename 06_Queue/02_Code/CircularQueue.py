

class Queue:
    def __init__(self,size):
        self.items = [None] * size
        self.size = size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return "["+",".join(values)+"]"

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        if(self.start == 0)&(self.top + 1 == self.size):
            return True
        return False
    
    def enqueue(self,value):
        if self.isFull():
            return "The Queue is full"
        else:
            if self.top + 1 == self.size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            
    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            value = self.items[self.start]
            self.items[self.start] = None
            if self.star == self.top:
                self.start = -1
                self.top = -1
            if self.start + 1 ==  self.size:
                self.start = 0
            else:
                self.start += 1
            return value

    def peek(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = [None] * self.size
        self.start = -1
        self.top = -1

