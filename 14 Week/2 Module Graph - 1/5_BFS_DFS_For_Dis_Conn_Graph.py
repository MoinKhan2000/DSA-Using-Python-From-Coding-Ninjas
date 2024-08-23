import queue


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.adMatrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def addEdge(self, v1, v2):
        self.adMatrix[v1][v2] = 1
        self.adMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adMatrix[v1][v2] = 0
        self.adMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if (self.adMatrix[v1][v2] > 0) else False

    def printGraph(self):
        for i in range(self.V):
            for j in range(self.V):
                print("{0}".format(self.adMatrix[i][j]), end=" ")
            print()

    def __dfsHelper(self, visited, sv):
        print(sv, end=" ")
        visited[sv] = True
        for neighbor in range(self.V):
            if self.adMatrix[sv][neighbor] > 0 and not visited[neighbor]:
                self.__dfsHelper(visited, neighbor)

    def DFS(self):
        visited = [False for _ in range(self.V)]
        for i in range(len(visited)):
            if visited[i] is False:
                self.__dfsHelper(visited, i)
        print()

    def __bfsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while not q.empty():
            node = q.get()
            print(node, end=" ")
            visited[node] = True
            for i in range(self.V):
                if self.adMatrix[node][i] > 0 and visited[i] == False:
                    q.put(i)
                    visited[i] = True

    def BFS(self):
        visited = [False for _ in range(self.V)]
        for i in range(self.V):
            if visited[i] == False:
                self.__bfsHelper(i, visited)

    def __hashPathHelper(self, v1, v2):
        if self.adMatrix[v1][v2] == 1:
            return True
        # cheking in the below neighbours nodes if there exists a path to v2 using dfs
        for i in range(self.V):
            if self.adMatrix[v1][i]:
                return self.__hashPathHelper(i, v2)
                # return True
        return False

    def hasPath(self, v1, v2):
        return self.__hashPathHelper(v1, v2)


# Testing the Graph
g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.printGraph()
print("DFS order -> ", end=" ")
g.DFS()
print("BFS order -> ", end=" ")
g.BFS()

# make a function which add 2 number
