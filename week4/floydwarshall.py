"""
Floyd-Warshall algorithm for computing All-Pairs Shortest Paths.
"""


def getGraph(fPath="g1.txt"):

    # edgeList = []
    edgeDict = {}

    with open(fPath) as f:
        lines = f.readlines()
        numNodes, numEdges = map(int, lines[0].split())
        for line in lines[1:]:
            node1, node2, edgeCost = [ int(el) for el in line.split() ]
            # edgeList.append((node1, node2, edgeCost))
            edgeDict[(node1, node2)] = edgeCost

    return edgeDict, numNodes


def floydwarshall(edgeDict, numNodes):
    subproblemDict = {}

    # nodes numbering is 1-based
    # set up initial values for smallest subproblems
    for i in range(1, numNodes+1):
        subproblemDict[(i, i, 0)] = 0
        for j in range(1, numNodes+1):
            subproblemDict[(i, j, 0)] = edgeDict.get((i, j), float('+inf'))

    # iterate over subproblem sizes using 1..n
    # first nodes
    for k in range(1, numNodes+1):
        print("iteration {}".format(k))
        
        # iterate over possible source nodes
        for i in range(1, numNodes+1):
            
            # iterate over possible destination nodes
            for j in range(1, numNodes+1):
                val1 = subproblemDict[(i, j, k-1)]
                val2 = subproblemDict[(i, k, k-1)] + subproblemDict[(k, j, k-1)]
                if val1 >= val2:
                    subproblemDict[(i, j, k)] = val1
                else:
                    subproblemDict[(i, j, k)] = val2

    return subproblemDict
