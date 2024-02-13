import queue as Q

class node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self,data = None):
        self.root = node(data)        
            
    def add(self,value):
        if self.root.data == None:
            self.root.data = value
        else:
            tempNode = self.root
            while tempNode:
                if value <= tempNode.data:
                    if tempNode.left is None:
                        tempNode.left = node(value)
                        return
                    else:
                        tempNode = tempNode.left
                else:
                    if tempNode.right is None:
                        tempNode.right = node(value)
                        return
                    else:
                        tempNode = tempNode.right
    
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
                    
            #while not root.
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
    
    def __search(self,value,node):
        if not node:
            return False
        if value == node.data:
            return True
        elif value < node.data: 
            return self.__search(value,node.left)
        else:
            return self.__search(value,node.right)

    def search(self,value):
        return self.__search(value,self.root)

    def minVal(self,node = None):
        if not node:
            tempNode = self.root
        else:
            tempNode = node
        while tempNode.left:
            tempNode = tempNode.left
        return tempNode

    def delete(self,value):
        self.__delete(value,self.root)

    def __delete(self,value,node):
        if not node:
            return
        # Find the element
        if value == node.data:
            if node.left is None:
                tempNode = node.right
                node = None
                return tempNode 
            if node.right is None:
                tempNode = node.right
                node = None
                return tempNode
            # In case the node has its two children
            tempNode = self.minVal(node.right)
            node.data = tempNode.data
            node.right = self.__delete(tempNode.data,node.right)

        elif value < node.data: 
            node.left = self.__delete(value,node.left)
        else:
            node.right = self.__delete(value,node.right)
        return node

    def clear(self):
        self.root = node()

tree = BST(70)
tree.add(50)
tree.add(90)
tree.add(30)
tree.add(60)
tree.add(80)
tree.add(100)
tree.add(20)
tree.add(40)
tree.traversal(3)
print('_______________________')
tree.clear()
tree.traversal(3)






