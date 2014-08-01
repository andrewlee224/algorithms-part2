"""
Floyd-Warshall algorithm for computing All-Pairs Shortest Paths.
Implementation with Cython and NumPy arrays, much faster than regular Python.
Space-optimized, using only the recent 2 biggest classes of subproblems.
"""

import numpy as np
cimport numpy as np


def getGraph(fPath="g1.txt"):

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
    cdef np.ndarray[np.float_t, ndim=2] oldArr = np.zeros((numNodes, numNodes), dtype='float')
    cdef np.ndarray[np.float_t, ndim=2] newArr = np.zeros((numNodes, numNodes), dtype='float')

    cdef int k, i, j
    cdef int cNumNodes = numNodes

    # set up initial values for smallest subproblems
    for i in range(cNumNodes):
        for j in range(cNumNodes):
            if i == j:
                oldArr[i, j] = 0
                continue
            oldArr[i, j] = edgeDict.get((i+1, j+1), float('+inf'))

    cdef float val1
    cdef float val2
    k = 1
    i = 0
    j = 0
    # iterate over subproblem sizes using 1..n
    # first nodes
    for k in range(1, cNumNodes):
        print("iteration {}".format(k))

        # iterate over possible source nodes
        for i in range(cNumNodes):

            # iterate over possible destination nodes
            for j in range(cNumNodes):
                val1 = oldArr[i, j]
                val2 = oldArr[i, k] + oldArr[k, j] 
                if val1 <= val2:
                    newArr[i, j] = val1
                else:
                    newArr[i, j] = val2
        oldArr = newArr

    return newArr


def checkNegativeCycles(subproblemArr, numNodes):
    cdef int i
    cdef int cNumNodes = numNodes

    for i in range(cNumNodes):
        if subproblemArr[i][i] < 0:
            return True

    return False


def shortestPath(subproblemArr, numNodes):
    cdef int i, j
    cdef int cNumNodes = numNodes
    cdef float arrVal
    shortestVal = float('+inf')

    for i in range(cNumNodes):
        for j in range(cNumNodes):
            if i == j:
                continue
            arrVal = subproblemArr[i][j]
            if arrVal < shortestVal:
                shortestVal = arrVal 

    return shortestVal


def main(fPath):
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
