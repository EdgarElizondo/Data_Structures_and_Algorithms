class node:
    def __init__(self,size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


class Heap:
    def __init__(self,size):
        self.root = node(size)

    def peek(self):
        return self.root.customList[1]

    def heapSize(self):
        return self.root.heapSize
    
    def traversal(self,traversalType = 'levelOrder'):
        if traversalType == 'levelOrder':
            self.__levelOrder__()

    def insert(self,value,heapType = 'Min'):
        if self.root.heapSize + 1 >= self.root.maxSize:
            return "The Binary heap is full"
        self.root.heapSize += 1
        self.root.customList[self.root.heapSize] =  value
        self.__insertHeap(self.root,self.root.heapSize,heapType)
    
    def extract(self,heapType = 'Min'):
        if self.heapSize == 0:
            return
        
        extract = self.root.customList[1]
        self.root.customList[1] = self.root.customList[self.root.heapSize]
        self.root.customList[self.root.heapSize] = None
        self.root.heapSize -= 1
        self.__extractHeap(self.root,1,heapType)

        return extract

    def clear(self):
        self.root = node(self.root.maxSize - 1)

    def delete(self):
        self.root = None


    #_____________________________________________________________
    def __levelOrder__(self):
        for i in range(1,self.root.heapSize + 1):
            print(self.root.customList[i])
    
    def __insertHeap(self,root,index,heapType):
        parent = int(index/2)
        if index <= 1:
            return
        if heapType == 'Min':
            if root.customList[index] < root.customList[parent]:
                temp = root.customList[index]
                root.customList[index] = root.customList[parent]
                root.customList[parent] = temp
            self.__insertHeap(root,parent,heapType)

        elif heapType == 'Max':
            print([root.customList[index] , root.customList[parent]])
            print('--',[index , parent])
        
            if root.customList[index] > root.customList[parent]:
                temp = root.customList[index]
                root.customList[index] = root.customList[parent]
                root.customList[parent] = temp
            self.__insertHeap(root,parent,heapType)

    def __extractHeap(self,root,index,heapType = 'Min'):
        pass

bHeap = Heap(5)

bHeap.insert(4,'Max')
bHeap.insert(5,'Max')
bHeap.insert(2,'Max')
bHeap.insert(1,'Max')
bHeap.insert(6,'Max')


bHeap.traversal()