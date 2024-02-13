from collections import defaultdict

class Graph:
    def __init__(self,gDict = defaultdict(list)):
        self.gDict = gDict

    def addEdge(self,vertex,edge):
        self.gDict[vertex].append(edge)

    def bfs(self,vertex = None):
        if vertex == None:
            vertex = list(self.gDict.keys())[0]
        
        queue = [vertex]
        visited = [vertex]

        while queue:
            deVertex  = queue.pop(0)
            print(deVertex)
            for adjVertex in self.gDict[deVertex]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    queue.append(adjVertex)
    
    def dfs(self,vertex = None):
        if vertex == None:
            vertex = list(self.gDict.keys())[0]
        
        stack = [vertex]
        visited = [vertex]

        while stack:
            pop = stack.pop()
            print(pop)
            for adjVertex in self.gDict[pop]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    stack.append(adjVertex)

def SSSP_bfs(graph,start,end):
    queue = [start]
    while queue:
        path  = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjVertex in graph.get(node,[]):
            new_path = list(path)
            new_path.append(adjVertex)
            queue.append(new_path)
            

gElem = {"a":["b","c"],
        "b":["d","g"],
        "c":["d","e"],
        "d":["f"],
        "e":["f"],
        "g":["f"]}

gDict = Graph(gElem)
print(SSSP_bfs(gElem,"a","e"))