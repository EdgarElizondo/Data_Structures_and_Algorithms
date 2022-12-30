

class BinaryTree:
    def __init__(self,size):
        self.list = [None] * (size + 1)
        self.lastIndex = 0
        self.size = size

    def add(self,value):
        if self.lastIndex == self.size:
            return "The Binary Tree is full"
        else:
            self.list[self.lastIndex + 1] = value
            self.lastIndex += 1
    def search(self,value):
        for val in self.list:
            if val == value:
                return True
        return False
    
    # Traversal algorithms
    def __preOrderTraversal(self,n = 1):
        if self.list[n] == None:
            return
        else:
            # Current Node
            print(self.list[n])
            # Left Child
            self.__preOrderTraversal(2*n)
            # Right Child
            self.__preOrderTraversal(2*n + 1)
    
    def __inOrderTraversal(self,n = 1):
        if self.list[n] == None:
            return
        else:
            # Left Child
            self.__inOrderTraversal(2*n)
            # Current Node
            print(self.list[n])
            # Right Child
            self.__inOrderTraversal(2*n + 1)

    def __postOrderTraversal(self,n = 1):
        if self.list[n] == None:
            return
        else:
            # Left Child
            self.__postOrderTraversal(2*n)
            # Right Child
            self.__postOrderTraversal(2*n + 1)
            # Current Node
            print(self.list[n])
            
    def __levelTraversal(self):
        if self.list[1] == None:
            return
        else:
            for i in range(1,self.lastIndex + 1):
                print(self.list[i])
                
    def traversal(self,ntype = 3):
        """
        ntype{
            0: Pre-Order Traversal
            1: In-Order Traversal
            2: Post-Order Traversal
            3: Level Traversal
            }
        """
        if ntype == 0:
            self.__preOrderTraversal()
        elif ntype == 1:
            self.__inOrderTraversal()
        elif ntype == 2:
            self.__postOrderTraversal()
        elif ntype == 3:
            self.__levelTraversal()
    
    def delete(self,value):
        if self.list[1] == None:
            return "The Binary Tree is empty"
        else:
            for i in range(1,self.lastIndex + 1):
                if self.list[i] == value:
                    self.list[i] = self.list[self.lastIndex]
                    self.list[self.lastIndex] = None
                    self.lastIndex -= 1
                    return
            return 'Element not found'

    def clear(self):
        if self.list[1] == None:
            return "The Binary Tree is empty"
        self.list = [None] * (self.size + 1)
        self.lastIndex = 0
