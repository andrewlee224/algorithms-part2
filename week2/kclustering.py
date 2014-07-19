"""
K-clustering algorithm using the Union-Find data structure.
Proceeds similar to Kruskal's MST algorithm, differs in stopping 
when there are k components of a graph, instead of a connected
graph.
"""

import unionfind as uf
from collections import deque

def getGraph(fPath="clustering1.txt"):

    edgeList = []
    with open(fPath) as f:
        lines = f.readlines()
        numNodes = int(lines[0])
        for line in lines[1:]:
            node1, node2, edgeCost = [ int(el) for el in line.split() ]
            edgeList.append((node1, node2, edgeCost))

    return edgeList, numNodes

def kclustering(k, edgeList, numNodes):
    
    # sort edges by their weights ascending, then select in this
    # order
    edgeList.sort(key=lambda tup: tup[2])
    edgeDeque = deque(edgeList)
    ufStruct = uf.UnionFind(list(range(1, numNodes+1))) # for 1-based

    while (ufStruct.totalComponents > k):
        # select cheapest edge that does not create cycles
        candidate = edgeDeque.popleft()
        ufStruct.union(candidate[0], candidate[1])

    # max spacing is the smallest unused edge
    while edgeDeque:
        maxSpacingEdge = edgeDeque.popleft()
        if ufStruct.find(maxSpacingEdge[0]) != \
                                    ufStruct.find(maxSpacingEdge[1]):
            break

    return maxSpacingEdge


if __name__ == '__main__':
    edgeList, numNodes = getGraph("clustering1.txt")
    k = 4
    maxSpacingEdge = kclustering(k, edgeList, numNodes)
    
    print("{}-clustering max spacing: {}".format(k, maxSpacingEdge[2]))
