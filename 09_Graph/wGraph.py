import heapq

# Class for edges
class Edge:
    def __init__(self,weight,start,target):
        self.weight = weight
        self.start = start
        self.target = target

class Node:
    def __init__(self,name):
        self.name =  name
        self.isVisited = False
        # previous node that comes before current node
        self.predecessor = None
        self.neighbors = []
        self.minDistance = float("inf")
    
    def __lt__(self,otherNode):
        return self.minDistance < otherNode.minDistance
    
    def addEdge(self,weight,destination):
        edge = Edge(weight,self,destination)
        self.neighbors.append(edge)

# Dijkstra Algorithm
class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self,start):
        start.minDistance = 0
        heapq.heappush(self.heap,start)
        while self.heap:
            # pop elements with the lowest distance
            currentVertex = heapq.heappop(self.heap)
            if currentVertex.isVisited:
                continue
            # consider neighbors
            for edge in currentVertex.neighbors:
                start = edge.start
                target = edge.target
                newDistance = start.minDistance + edge.weight
                if newDistance < target.minDistance:
                    target.minDistance = newDistance
                    target.predecessor = start
                    #update Heap
                    heapq.heappush(self.heap,target)
            currentVertex.isVisited = True

    def getShortestPath(self,vertex):
        print(f"The shortest path to the vertex is {vertex.minDistance}")
        currentVertex = vertex
        while currentVertex is not None:
            print(currentVertex.name, end=" ")
            currentVertex = currentVertex.predecessor

# Step 1: Create nodes
nodeA =  Node("A")
nodeB =  Node("B")
nodeC =  Node("C")
nodeD =  Node("D")
nodeE =  Node("E")
nodeF =  Node("F")
nodeG =  Node("G")
nodeH =  Node("H")

# Step 2: Create edges
nodeA.addEdge(6,nodeB)
nodeA.addEdge(10,nodeC)
nodeA.addEdge(9,nodeD)

nodeB.addEdge(5,nodeD)
nodeB.addEdge(16,nodeE)
nodeB.addEdge(13,nodeF)

nodeC.addEdge(6,nodeD)
nodeC.addEdge(21,nodeG)
nodeC.addEdge(5,nodeH)

nodeD.addEdge(8,nodeF)
nodeD.addEdge(7,nodeH)

nodeE.addEdge(10,nodeG)

nodeF.addEdge(4,nodeE)
nodeF.addEdge(12,nodeG)

nodeH.addEdge(2,nodeF)
nodeH.addEdge(14,nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.getShortestPath(nodeG)

