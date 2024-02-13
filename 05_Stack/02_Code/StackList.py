

class Stack:

    def __init__(self,limit = None):
        self.list = []
        self.limit = limit
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.limit:
            return True
        else:
            return False

    # Push method
    def push(self,value):
        if self.isFull():
            return "There stack is full"
        else:
            self.list.append(value)

    # Pop method
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            self.list.pop()

    # Peek method
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None