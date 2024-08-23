""" 
Code : Is Connected ?
Send Feedback
Given an undirected graph G(V,E), check if the graph G is connected graph or not.
Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
Output Format :
The first and only line of output contains "true" if the given graph is connected or "false", otherwise.
Constraints :
0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
Time Limit: 1 second
Sample Input 1:
4 4
0 1
0 3
1 2
2 3
Sample Output 1:
true
Sample Input 2:
4 3
0 1
1 3 
0 3
Sample Output 2:
false 
Sample Output 2 Explanation
The graph is not connected, even though vertices 0,1 and 3 are connected to each other but there isn’t any path from vertices 0,1,3 to vertex 2. 

"""

# Write your code here
import queue
import sys


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
        self.__dfsHelper(visited, 0)
        print()

    def DFS2(self, visited):
        self.__dfsHelper(visited, 0)
        print()

    def BFS(self):
        visited = [False] * self.V
        q = queue.Queue()
        q.put(0)
        if self.V > 0:
            visited[0] = True
        else:
            return
        while q.empty() is False:
            node = q.get()
            print(node, end=" ")
            for i in range(self.V):
                if self.adMatrix[node][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
        for i in range(self.V):
            if visited[i] == False:
                print(i, end=" ")

    def __hasPathHelper(self, v1, v2, visited):
        if v1 == v2:
            return True
        # cheking in the below neighbours nodes if there exists a path to v2 using dfs
        visited[v1] = True
        for i in range(self.V):
            if self.adMatrix[v1][i] == 1 and visited[i] == False:
                visited[i] = True
                if self.__hasPathHelper(i, v2, visited):
                    return True
        return False

    def hasPath(self, v1, v2):
        visited = [False] * self.V
        if self.__hasPathHelper(v1, v2, visited):
            print("true")
        else:
            print("false")

    def isConnected(self, v1, v2):
        visited = [False] * self.V
        self.DFS2(visited)
        if False in visited:
            return False
        return True


# Rest of the class remains the same
try:
    v, e = map(int, input().split())
    if v < 0 or e < 0 or e > (v * (v - 1)) / 2:
        raise ValueError("Invalid input")

    # Creating a graph
    graph = Graph(v)

    # Adding edges to the graph
    for _ in range(e - 1):
        v1, v2 = map(int, input().split())
        if 0 <= v1 < v and 0 <= v2 < v:
            graph.addEdge(v1, v2)
        else:
            sys.exit()

    # Perform BFS traversal
    if v > 0 and e > 0:
        v1, v2 = map(int, input().split())
        print("true") if graph.isConnected(v1, v2) else print("false")
    else:
        print("true")


except ValueError as e:
    sys.exit()
