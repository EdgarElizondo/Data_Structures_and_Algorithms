
from collections import defaultdict

class uGraph:

    def __init__(self,nVertices):
        self.graph = defaultdict(list)
        self.nVertices = nVertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self,v,visited,stack):

        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)
    
    def topologicalSort(self):
        
        stack = []
        visited  = []

        for i in list(self.graph):
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
        print(stack)



graph = uGraph(8)
graph.addEdge("A","C")
graph.addEdge("C","E")
graph.addEdge("E","H")
graph.addEdge("E","F")
graph.addEdge("F","G")
graph.addEdge("B","D")
graph.addEdge("B","C")
graph.addEdge("D","F")


graph.topologicalSort()

