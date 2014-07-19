"""
Module for clustering a graph with implicit edge lengths. Graph
nodes are labeled by n-bit sequences, and the distances between
nodes are defined as the number of differing bits between the
nodes labels.
"""

import unionfind as uf
from itertools import izip, combinations

def getGraph(fPath="clustering_big.txt"):

    with open(fPath) as f:
        lines = f.readlines()
        numNodes, labelBits = map(int, lines[0].split())
        nodeList = []

        for line in lines[1:]:
            # trim '\n' by omitting last 2 characters
            node = "".join([ el for el in line if el is not " "])[:-1]
            nodeList.append(node)

    return nodeList, labelBits


def hammingDistance(node1, node2):
    assert len(node1) == len(node2)

    return sum(c1 != c2 for c1, c2 in izip(node1, node2))

def calculateMasks(bitsLabel=24):
    """
    Create swap masks in the form tuples with numbers
    indicating which bits to swap.
    """

    swapMasks1 = [ (el, ) for el in range(bitsLabel) ]
    swapMasks2 = [ c for c in combinations(range(bitsLabel), 2) ]

    return swapMasks1 + swapMasks2

def swapByMask(label, mask):
    """Swap bits in label according to a mask"""

    modLabel = [ c for c in label ]

    for bitNum in mask:
        if modLabel[bitNum] == '0':
            modLabel[bitNum] = '1'
        elif modLabel[bitNum] == '1':
            modLabel[bitNum] = '0'

    return "".join(modLabel)

def createLabelDict(nodeList):
    d = {}

    for i, node in enumerate(nodeList):
        if node not in d:
            d[node] = [i]
        else:
            d[node].append(i)

    return d

def implicitClustering(nodeList, maxDist=3, bitsLabel=24):
    
    numNodes = len(nodeList)
    ufstruct = uf.UnionFind(list(range(len(nodeList))))
    
    swapMasks = calculateMasks(bitsLabel)
    labelDict = createLabelDict(nodeList)

    numClusterings = 0
    for i, node1 in enumerate(nodeList):
        print("Node {} of {}".format(i, numNodes-1))
        for sameLabelIndex in labelDict[node1]:
            if sameLabelIndex != i:
                ufstruct.union(i, sameLabelIndex)

        for mask in swapMasks:
            modLabel = swapByMask(node1, mask)
            if modLabel in labelDict:
                for index in labelDict[modLabel]:
                    ufstruct.union(i, index)

    k = ufstruct.totalComponents #len(nodeList) - numClusterings
    return k


if __name__ == '__main__':
    print("Loading graph..")
    nodeList, labelBits = getGraph()
    print("Calculating clusters..")
    maxDist = 3
    k = implicitClustering(nodeList, maxDist, labelBits)
    print("Minimum number of clusters to ensure that members " + 
        "differ at most with 3 bits: {}".format(k))
