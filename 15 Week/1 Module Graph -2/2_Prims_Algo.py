import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.adMatrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def addEdge(self, v1, v2, wt):
        self.adMatrix[v1][v2] = wt
        self.adMatrix[v2][v1] = wt

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
        print(sv)
        visited[sv] = True
        for neighbor in range(self.V):
            if self.adMatrix[sv][neighbor] > 0 and not visited[neighbor]:
                self.__dfsHelper(visited, neighbor)

    def DFS(self):
        visited = [False for _ in range(self.V)]
        self.__dfsHelper(visited, 0)

    def getMinVertex(self, visited, weight):
        # Use camel case
        minVertex = -1
        for i in range(self.V):
            if visited[i] is False and (
                minVertex == -1 or weight[minVertex] > weight[i]
            ):
                minVertex = i
        return minVertex

    def prims(self):
        visited = [False for i in range(self.V)]
        parent = [-1 for i in range(self.V)]
        weight = [sys.maxsize for i in range(self.V)]
        weight[0] = 0

        for i in range(self.V - 1):
            minVertex = self.getMinVertex(visited, weight)
            visited[minVertex] = True

            # Explore the neighbours of minVertex which is not visited and update the weight correspondint that if required.;

            for j in range(self.V):
                if self.adMatrix[minVertex][j] > 0 and visited[j] is False:
                    if self.adMatrix[minVertex][j] < weight[j]:
                        weight[j] = self.adMatrix[minVertex][j]
                        parent[j] = minVertex
        for i in range(1, self.V):
            if i < parent[i]:
                print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))
            else:
                print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))


li = [int(x) for x in input().split()]
n = li[0]
nEdge = li[1]
g = Graph(nEdge)
for i in range(nEdge):
    currInput = [int(ele) for ele in input().split()]
    g.addEdge(currInput[0], currInput[1], currInput[2])

# Calling the func
g.prims()
