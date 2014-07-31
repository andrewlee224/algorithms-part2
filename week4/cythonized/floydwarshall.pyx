"""
Floyd-Warshall algorithm for computing All-Pairs Shortest Paths.
"""


def getGraph(fPath="g1.txt"):

    # edgeList = []
    edgeDict = {}

    with open(fPath) as f:
        lines = f.readlines()
        numNodes, numEdges = map(int, lines[0].split())
        maxEdgeCost = float('-inf') 

        for line in lines[1:]:
            node1, node2, edgeCost = [ int(el) for el in line.split() ]
            # edgeList.append((node1, node2, edgeCost))
            edgeDict[(node1, node2)] = edgeCost
            maxEdgeCost = edgeCost if edgeCost > maxEdgeCost else maxEdgeCost

    return edgeDict, numNodes, maxEdgeCost


def floydwarshall(edgeDict, numNodes, maxEdgeCost):
    subproblemArr = [[]]
    cdef int k, i, j
    cdef int cNumNodes = numNodes

    # nodes numbering is 1-based
    # set up initial values for smallest subproblems
    for i in range(cNumNodes):
        subproblemArr[0].append([])
        for j in range(cNumNodes):
            subproblemArr[0][i].append([])
            if i == j:
                subproblemArr[0][i][j] = 0
                continue
            subproblemArr[0][i][j] = edgeDict.get((i+1, j+1), maxEdgeCost+1)

    # iterate over subproblem sizes using 1..n
    # first nodes
    cdef int val1
    cdef int val2
    k = 1
    i = 0
    j = 0
    for k in range(1, cNumNodes):
        subproblemArr.append([])
        print("iteration {}".format(k))

        # iterate over possible source nodes
        for i in range(cNumNodes):
            subproblemArr[k].append([])

            # iterate over possible destination nodes
            for j in range(cNumNodes):
                subproblemArr[k][i].append([])
                val1 = subproblemArr[k-1][i][j]
                val2 = subproblemArr[k-1][i][k] + subproblemArr[k-1][k][j] 
                if val1 <= val2:
                    subproblemArr[k][i][j] = val1
                else:
                    subproblemArr[k][i][j] = val2

    return subproblemArr


def checkNegativeCycles(subproblemArr, numNodes):
    cdef int i, j
    cdef int cNumNodes = numNodes

    for i in range(cNumNodes):
        if subproblemArr[cNumNodes-1][i][i] < 0:
            return True

    return False


def shortestPath(subproblemArr, numNodes):
    cdef int i, j
    cdef int cNumNodes = numNodes
    shortestVal = float('+inf')

    for i in range(cNumNodes):
        for j in range(cNumNodes):
            arrVal = subproblemArr[cNumNodes-1][i][j]
            if arrVal < shortestVal:
                shortestVal = arrVal 

    return arrVal


def main(fPath):
    edgeDict, numNodes, maxEdgeCost = getGraph(fPath)
    subproblems = floydwarshall(edgeDict, numNodes, maxEdgeCost) 
    negativeCycles = checkNegativeCycles(subproblems, numNodes)
    print("Negative cycles: {}".format(negativeCycles))
    if negativeCycles:
        return

    shortestVal = shortestPath(subproblems, numNodes)
    print("Shortest of all-pairs shortest paths value: {}".format(shortestVal))


if __name__ == '__main__':
    main()   
