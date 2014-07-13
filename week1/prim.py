"""
Prim's Minimum Spanning Tree algorithm. Straightforward
implementation without utilising heap.
"""


def getGraph(fPath="edges.txt"):

    edgeList = []
    with open(fPath) as f:
        lines = f.readlines()
        numNodes, numEdges = [ int(el) for el in lines[0].split() ]
        for line in lines[1:]:
            node1, node2, edgeCost = [ int(el) for el in line.split() ]
            edgeList.append((node1, node2, edgeCost))

    return edgeList, numNodes, numEdges


def prim(edgeList, numNodes):
    """
    Run Prim's MST on graph in the form of edge list
    """

    X = set()  # set of explored nodes
    V = set(range(1, numNodes+1))   # set of unexplored nodes
    E = set()   # set of edges of MST
    totalCost = 0   # total sum of the edge costs of the MST

    start = 1
    X.add(start)
    V.remove(start)

    while len(V) is not 0:
        # look at all edges crossing the X and V sets
        lowestCost = float('inf')
        foundNodeX = None
        foundNodeV = None

        for edge in edgeList:
            if edge[0] in X and edge[1] in V:
                if edge[2] < lowestCost:
                    foundNodeX = edge[0]
                    foundNodeV = edge[1]
                    lowestCost = edge[2]
            elif edge[1] in X and edge[0] in V:
                if edge[2] < lowestCost:
                    foundNodeX = edge[1]
                    foundNodeV = edge[0]
                    lowestCost = edge[2]

        print("foundNodeX: {0}, foundNodeV: {1}".format(foundNodeX, foundNodeV))

        X.add(foundNodeV)
        V.remove(foundNodeV)
        E.add((foundNodeX, foundNodeV, lowestCost))
        totalCost += lowestCost

    return E, totalCost

if __name__ == '__main__':
    print("Computing MST...")
    edgeList, numNodes, numEdges = getGraph()
    E, totalCost = prim(edgeList, numNodes)

    print("Total cost: {}".format(totalCost))
