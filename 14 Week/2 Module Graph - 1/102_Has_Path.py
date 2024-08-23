""" 
Code : BFS Traversal
Send Feedback
Given an undirected and disconnected graph G(V, E), print its BFS traversal.
Note:
1. Here you need to consider that you need to print BFS path starting from vertex 0 only. 
2. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
3. E is the number of edges present in graph G.
4. Take graph input in the adjacency matrix.
5. Handle for Disconnected Graphs as well
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains space separated two integers, that denote that there exists an edge between vertex a and b.
Output Format :
Print the BFS Traversal, as described in the task.
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
0 1 3 2
"""

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

    def __hashPathHelper(self, v1, v2, visited):
        if self.adMatrix[v1][v2] == 1:
            return True
        # cheking in the below neighbours nodes if there exists a path to v2 using dfs
        for i in range(self.V):
            if self.adMatrix[v1][i] == 1 and visited[i] == False:
                visited[i] = True
                return self.__hashPathHelper(i, v2, visited)
                # return True
        return False

    def hasPath(self, v1, v2):
        visited = [False] * self.V
        return self.__hashPathHelper(v1, v2, visited)


# Rest of the class remains the same
try:
    v, e = map(int, input().split())
    if v < 0 or e < 0 or e > (v * (v - 1)) / 2:
        raise ValueError("Invalid input")

    # Creating a graph
    graph = Graph(v)

    # Adding edges to the graph
    for _ in range(e):
        v1, v2 = map(int, input().split())
        if 0 <= v1 < v and 0 <= v2 < v:
            graph.addEdge(v1, v2)
        else:
            sys.exit()

    # Perform BFS traversal
    v1, v2 = map(int, input().split())
    print("true") if graph.hasPath(v1, v2) else print("false")


except ValueError as e:
    sys.exit()
