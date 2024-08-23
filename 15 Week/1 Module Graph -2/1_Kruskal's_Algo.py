class Edge:
    def __init__(self, src, dst, wt):
        self.src = src
        self.dst = dst
        self.wt = wt


def getParent(v, parent):
    if v == parent[v]:
        return v
    return getParent(parent[v], parent)


def krusKal(edges, nVertices):
    parent = [i for i in range(nVertices)]
    print(parent)
    edges = sorted(edges, key=lambda edge: edge.wt)
    """ sorting the edges array on the basis of edge.wt """
    # for el in edges:
    #     print(el.src, el.dst, el.wt)
    output = []
    count = 0
    i = 0
    while count < nVertices - 1:
        currentEdge = edges[i]
        srcParent = getParent(currentEdge.src, parent)
        dstParent = getParent(currentEdge.dst, parent)
        if srcParent != dstParent:
            output.append(currentEdge)
            count += 1
            parent[srcParent] = dstParent
        i += 1

    return output


li = [int(ele) for ele in input().split()]
n = li[0]
e = li[1]

edges = []

for i in range(e):
    currInput = [int(ele) for ele in input().split()]
    src = currInput[0]
    dst = currInput[1]
    wt = currInput[2]
    edge = Edge(src, dst, wt)
    edges.append(edge)

output = krusKal(edges, n)
for edge in output:
    if edge.src < edge.dst:
        print("{0} {1} {2}".format(edge.src, edge.dst, edge.wt))
    else:
        print("{0} {1} {2}".format(edge.dst, edge.src, edge.wt))
