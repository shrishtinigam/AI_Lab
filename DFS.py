from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, target): 
        visited.add(v)
        print(v, end=' ')
        if(v == target):
            print(f"Found")
            exit(0)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, target)

    def DFS(self, v, target):
        print(f"Starting from {v}, to reach target {target}.")
        visited = set()
        self.DFSUtil(v, visited, target)



g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
g.addEdge(3, 7)
g.addEdge(3, 8)
g.addEdge(4, 9)
g.addEdge(4, 10)
g.addEdge(5, 11)
g.addEdge(5, 12)
g.addEdge(6, 13)
g.addEdge(7, 14)
g.addEdge(8, 15)
g.addEdge(9, 16)
g.addEdge(9, 17)
g.addEdge(10, 18)
g.addEdge(11, 19)
g.addEdge(12, 20)
g.addEdge(16, 21)


print("Following is Depth First Traversal")
g.DFS(1, 14)