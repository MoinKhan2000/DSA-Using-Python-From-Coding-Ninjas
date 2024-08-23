""" 
Code : Get Path - BFS
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
Find the path using BFS and print the shortest path available.
Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
4. Save the input graph in Adjacency Matrix.
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
The following line contain two integers, that denote the value of v1 and v2.
Output Format :
Print the path from v1 to v2 in reverse order.
Constraints :
2 <= V <= 1000
1 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
0 <= v1 <= 2^31 - 1
0 <= v2 <= 2^31 - 1
Time Limit: 1 second
Sample Input 1 :
4 4
0 1
0 3
1 2
2 3
1 3
Sample Output 1 :
3 0 1
Sample Input 2 :
6 3
5 3
0 1
3 4
0 3
Sample Output 2 :
"""
import queue
import sys


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

    def __hasPathHelper(self, v1, v2):
        if self.adMatrix[v1][v2] == 1:
            return True
        for i in range(self.V):
            if self.adMatrix[v1][i]:
                return self.__hasPathHelper(i, v2)
        return False

    def hasPath(self, v1, v2):
        return self.__hasPathHelper(v1, v2)

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

    def getBFSPath(self, v1, v2):
        visited = [False] * self.V
        mapping = {}
        q = queue.Queue()
        q.put(v1)
        visited[v1] = True
        mapping[v1] = -1

        while not q.empty():
            node = q.get()

            for i in range(self.V):
                if self.adMatrix[node][i] > 0 and not visited[i]:
                    q.put(i)
                    visited[i] = True
                    mapping[i] = node

                    if i == v2:
                        # Reconstruct the path from v1 to v2
                        path = []
                        temp_node = v2
                        while temp_node != -1:
                            path.insert(0, temp_node)
                            temp_node = mapping[temp_node]
                        return path[::-1]

        return []


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
    res = graph.getBFSPath(v1, v2)
    for el in res:
        print(el, end=" ")

except ValueError as e:
    sys.exit()
