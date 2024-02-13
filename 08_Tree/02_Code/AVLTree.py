import queue as Q

class node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
class Tree:
    def __init__(self,value):
        self.root = node(value)
        
    def traversal(self,ntype = 1):
        """
        ntype{
            0: Pre-Order Traversal
            1: In-Order Traversal
            2: Post-Order Traversal
            3: Level Traversal
            Default: 1
            }
        """
        if ntype == 0:
            self.__preOrderTraversal(self.root)
        elif ntype == 1:
            self.__inOrderTraversal(self.root)
        elif ntype == 2:
            self.__postOrderTraversal(self.root)
        elif ntype == 3:
            self.__levelTraversal(self.root)

    def search(self,value):
        return self.__search(value,self.root)
    
    def height(self):
        return self.__height(self.root)
    
    def balance(self):
        return self.__balance(self.root)
    
    def add(self,value):
        self.root = self.__add(value,self.root)
    
    def minVal(self):
        return self.__minVal(self.root)

    def delete(self,value):
        return self.__delete(value,self.root)

    def clear(self):
        self.root = node()
    # __________________________________________________________________________________________________________
    # Private (called) functions
    # __________________________________________________________________________________________________________
    #Traversal algorithms
    def __preOrderTraversal(self,nodeValue):
        if not nodeValue:
            return
        print(nodeValue.data)
        self.__preOrderTraversal(nodeValue.left)
        self.__preOrderTraversal(nodeValue.right)
    
    def __inOrderTraversal(self,nodeValue):
        if not nodeValue:
            return
        self.__inOrderTraversal(nodeValue.left)
        print(nodeValue.data)
        self.__inOrderTraversal(nodeValue.right)
    
    def __postOrderTraversal(self,nodeValue):
        if not nodeValue:
            return
        self.__postOrderTraversal(nodeValue.left)
        self.__postOrderTraversal(nodeValue.right)
        print(nodeValue.data)
        
    def __levelTraversal(self,nodeValue):
        if not nodeValue:
            return
        else:
            tempQ = Q.Queue()
            tempQ.put(nodeValue)
            while not tempQ.empty():
                root = tempQ.get()
                print(root.data)
                if root.left is not None:
                    tempQ.put(root.left)
                if root.right is not None:
                    tempQ.put(root.right)
    
    def __search(self,value,node):
        if not node:
            return False
        if value == node.data:
            return True
        elif value < node.data: 
            return self.__search(value,node.left)
        else:
            return self.__search(value,node.right)

    def __height(self,root):
        if not root:
            return 0
        return root.height
    
    # Rotations
    def __rightRotation(self,disbalanceNode):
        newRoot = disbalanceNode.left
        disbalanceNode.left = disbalanceNode.left.right
        newRoot.right = disbalanceNode
        disbalanceNode.height = 1 + max(self.__height(disbalanceNode.left),self.__height(disbalanceNode.right))
        newRoot.height = 1 + max(self.__height(newRoot.left),self.__height(newRoot.right))
        return newRoot
    def __leftRotation(self,disbalanceNode):
        newRoot = disbalanceNode.right
        disbalanceNode.right = disbalanceNode.right.left
        newRoot.left = disbalanceNode
        disbalanceNode.height = 1 + max(self.__height(disbalanceNode.left),self.__height(disbalanceNode.right))
        newRoot.height = 1 + max(self.__height(newRoot.left),self.__height(newRoot.right))
        return newRoot
    
    def __balance(self,root):
        if not root:
            return 0
        return self.__height(root.left) - self.__height(root.right)        

    def __add(self,value,root):
        if not root:
            return node(value)
        # Else condition
        if value <= root.data:
            root.left = self.__add(value,root.left)
        else:
            root.right = self.__add(value,root.right)
        # Update height
        root.height = 1 + max(self.__height(root.left),self.__height(root.right))
        balance = self.__balance(root)
        # Rotation conditions
        if (balance > 1):
            #print('--',value)
            if (value <= root.left.data):
                root = self.__rightRotation(root)
            else:
                root.left = self.__leftRotation(root.left)
                root = self.__rightRotation(root)
        if (balance < -1):
            if (value > root.right.data):
                root = self.__leftRotation(root)
            else:
                root.right = self.__rightRotation(root.right)
                root = self.__leftRotation(root)
        return root

    def __minVal(self,node):
        if not node:
            return node
        return self.__minVal(node.left)
    
    def __delete(self,value,root):
        if not root:
            return root
        # Else condition
        if value < root.data:
            root.left = self.__delete(value,root.left)
        elif value > root.data:
            root.right = self.__delete(value,root.right)
        else:
            if root.left is None:
                tempNode = root.right
                root = None
                return tempNode 
            elif root.right is None:
                tempNode = root.right
                root = None
                return tempNode
            # In case the node has its two children
            tempNode = self.__minVal(root.right)
            root.data = tempNode.data
            root.right = self.__delete(tempNode.data,root.right)
        # Check for unbalance (Rotation)
        root.height = 1 + max(self.__height(root.left),self.__height(root.right))
        balance = self.__balance(root)
        # Rotation conditions
        if (balance > 1):
            if self.__balance(root.left) >= 0:
                root = self.__rightRotation(root)
            else:
                root.left = self.__leftRotation(root.left)
                root = self.__rightRotation(root)
        if (balance < -1):
            if self.__balance(root.right) <= 0:
                root = self.__leftRotation(root)
            else:
                root.right = self.__rightRotation(root.right)
                root = self.__leftRotation(root)
        return root
