"""
Module for clustering a graph with implicit edge lengths. Graph
nodes are labeled by n-bit sequences, and the distances between
nodes are defined as the number of differing bits between the
nodes labels.
"""

from itertools import izip

def getGraph(fPath="clustering_big.txt"):

    with open(fPath) as f:
        lines = f.readlines()
        numNodes, labelBits = map(int, lines[0].split())
        nodeList = []

        for line in lines[1:]:
            # trim '\n' by omitting last 2 characters
            node = "".join([ el for el in line if el is not " "])[:-1]
            nodeList.append(node)

    return nodeList


def hammingDistance(node1, node2):
    assert len(node1) == len(node2)

    return sum(c1 != c2 for c1, c2 in izip(node1, node2))


