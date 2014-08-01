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
    subproblemArr = [[]]

    # nodes numbering is 1-based
    # set up initial values for smallest subproblems
    for i in range(numNodes):
        subproblemArr[0].append([])
        for j in range(numNodes):
            subproblemArr[0][i].append([])
            if i == j:
                subproblemArr[0][i][j] = 0
                continue
            subproblemArr[0][i][j] = edgeDict.get((i+1, j+1), float('+inf'))

    # iterate over subproblem sizes using 1..n
    # first nodes
    for k in range(1, numNodes):
        subproblemArr.append([])
        print("iteration {}".format(k))
        # iterate over possible source nodes
        for i in range(numNodes):
            subproblemArr[k].append([])
            # print("iteration {}, {}".format(k, i))

            # iterate over possible destination nodes
            for j in range(numNodes):
                subproblemArr[k][i].append([])
                val1 = subproblemArr[k-1][i][j]
                val2 = subproblemArr[k-1][i][k] + subproblemArr[k-1][k][j] 
                if val1 <= val2:
                    subproblemArr[k][i][j] = val1
                else:
                    subproblemArr[k][i][j] = val2

    return subproblemArr


def checkNegativeCycles(subproblemArr, numNodes):
    for i in range(numNodes):
        if subproblemArr[numNodes-1][i][i] < 0:
            return True

    return False


def shortestPath(subproblemArr, numNodes):
    shortestVal = float('+inf')

    for i in range(numNodes):
        for j in range(numNodes):
            arrVal = subproblemArr[numNodes-1][i][j]
            if arrVal < shortestVal:
                shortestVal = arrVal 

    return shortestVal


def main(fPath="g1.txt"):
    edgeDict, numNodes = getGraph(fPath)
    subproblems = floydwarshall(edgeDict, numNodes) 
    negativeCycles = checkNegativeCycles(subproblems, numNodes)
    print("Negative cycles: {}".format(negativeCycles))
    if negativeCycles:
        return

    shortestVal = shortestPath(subproblems, numNodes)
    print("Shortest of all-pairs shortest paths value: {}".format(shortestVal))


if __name__ == '__main__':
    main()   
