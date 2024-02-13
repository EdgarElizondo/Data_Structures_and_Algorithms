import queue as Q

class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    #Traversal algorithms
    def __preOrderTraversal(self,node):
        if not node:
            return
        print(node.data)
        self.__preOrderTraversal(node.left)
        self.__preOrderTraversal(node.right)
    
    def __inOrderTraversal(self,node):
        if not node:
            return
        self.__inOrderTraversal(node.left)
        print(node.data)
        self.__inOrderTraversal(node.right)
    
    def __postOrderTraversal(self,node):
        if not node:
            return
        self.__postOrderTraversal(node.left)
        self.__postOrderTraversal(node.right)
        print(node.data)
        
    def __levelTraversal(self,node):
        if not node:
            return
        else:
            tempQ = Q.Queue()
            tempQ.put(node)
            while not tempQ.empty():
                root = tempQ.get()
                print(root.data)
                if root.left is not None:
                    tempQ.put(root.left)
                if root.right is not None:
                    tempQ.put(root.right)
                    
            #while not root.
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
            self.__preOrderTraversal(self)
        elif ntype == 1:
            self.__inOrderTraversal(self)
        elif ntype == 2:
            self.__postOrderTraversal(self)
        elif ntype == 3:
            self.__levelTraversal(self)
    
    def search(self,value):
        if not self:
            return "The Tree is empty"
        else:
            tempQ = Q.Queue()
            tempQ.put(self)
            while not tempQ.empty():
                root = tempQ.get()
                if root.data == value:
                    return True
                if root.left is not None:
                    tempQ.put(root.left)
                if root.right is not None:
                    tempQ.put(root.right)
            return False

    def add(self,node):
        if not self.data:
            self.data = node
        else:
            tempQ = Q.Queue()
            tempQ.put(self)
            while not tempQ.empty():
                root = tempQ.get()
                if root.left is not None:
                    tempQ.put(root.left)
                else:
                    root.left  = node
                    return
                if root.right is not None:
                    tempQ.put(root.right)
                else:
                    root.right = node
                    return
        
    def deepestNode(self):
        if not self:
            return
        else:
            tempNode = Q.Queue()
            tempNode.put(self)
            while not tempNode.empty():
                root = tempNode.get()
                if root.left is not None:
                    tempNode.put(root.left)
                if root.right is not None:
                    tempNode.put(root.right)
            return root.data

    def deleteNode(self,dNode):
        if not self:
            return
        else:
            tempNode = Q.Queue()
            tempNode.put(self)
            while not tempNode.empty():
                root = tempNode.get()
                if root.data is dNode:
                    root.data = None
                    return
                if root.left:
                    if root.left.data is dNode:
                        root.left = None
                        return
                    else:
                        tempNode.put(root.left)
                if root.right:
                    if root.right.data is dNode:
                        root.right = None
                        return
                    else:
                        tempNode.put(root.right)
            
    def delete(self,Node):
        if not self.data:
            return "The binary tree is empty"
        else:
            tempNode = Q.Queue()
            tempNode.put(self)
            while not tempNode.empty():
                root = tempNode.get()
                if root.data == Node:
                    dNode = self.deepestNode()
                    self.deleteNode(dNode)
                    root.data = dNode
                    return
                if root.left is not None:
                    tempNode.put(root.left)
                if root.right is not None:
                    tempNode.put(root.right)
            return 'Element not found'

    def clear(self):
        if not self.data:
            return "The binary tree is empty"
        else:
            self.data = None
            self.left = None
            self.right = None

tree = Tree('Drinks')
hot = Tree('Hot')
cold = Tree('Cold')
tea = Tree('Tea')
coffee= Tree('Coffee')
cola = Tree('Cola')

 
tree.add(hot)
tree.add(cold)
tree.add(tea)
tree.add(coffee)
tree.add(cola)
tree.traversal()

print('________________')
tree.clear()
tree.traversal()





