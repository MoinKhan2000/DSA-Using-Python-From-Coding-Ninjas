import queue


class Graph:
    def __init__(self, vertices):
        self.V = vertices
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
        self.__dfsHelper(visited, 0)
        print()

    def BFS(self):
        visited = [False for _ in range(self.V)]
        q = queue.Queue()
        q.put(0)
        visited[0] = True
        while not q.empty():
            node = q.get()
            print(node, end=" ")
            visited[node] = True
            for i in range(self.V):
                if self.adMatrix[node][i] > 0 and visited[i] == False:
                    q.put(i)
        print()

    def BFS2(self):
        visited = [False] * self.V
        q = queue.Queue()
        q.put(0)
        visited[0] = True
        while q.empty() is False:
            node = q.get()
            print(node, end=" ")
            for i in range(self.V):
                if self.adMatrix[node][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
        for ind, mark in enumerate(visited):
            if mark == False:
                print(ind, end=" ")
        print()

    def __hashPathHelper(self, v1, v2):
        if self.adMatrix[v1][v2] == 1:
            return True
        for i in range(self.V):
            if self.adMatrix[v1][i]:
                return self.__hashPathHelper(i, v2)
        return False

    def hasPath(self, v1, v2):
        return self.__hashPathHelper(v1, v2)

    def __getDFSPathHelper(self, v1, v2, pathList, visited):
        if v1 == v2:
            pathList.append(v1)
            return pathList
        visited[v1] = True
        for i in range(self.V):
            if self.adMatrix[v1][i] == 1 and not visited[i]:
                result = self.__getDFSPathHelper(i, v2, pathList.copy(), visited)
                if result is not None:
                    pathList = result + [v1]
                    return pathList
        return None

    def getDFSPath(self, v1, v2):
        pathList = []
        visited = [False for _ in range(self.V)]
        result = self.__getDFSPathHelper(v1, v2, pathList, visited)
        if result:
            return result
        else:
            return []


# Testing the Graph
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.printGraph()
print("DFS order -> ", end=" ")
g.DFS()
print("BFS order -> ", end=" ")
g.BFS()
print("BFS ordr2 -> ", end=" ")
g.BFS2()
print(g.hasPath(1, 3))

print(g.getDFSPath(0, 2))
