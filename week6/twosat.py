"""
Algorithm for solving the 2-SAT problem.
Reduces to counting strongly connected components, here solved by using
Kosaraju algorithm
"""

import sys

import kosaraju as kr


def createGraph(fName="2sat1.txt"):
    """
    Create an implication graph
    """

    edgeList = []

    with open(fName) as fObj:
        lines = fObj.readlines()
        numVars = numClauses = int(lines[0].strip())
        for line in lines[1:]:
            val1, val2 = [ int(el) for el in line.split() ]
            edgeList.append((-val1, val2))
            edgeList.append((-val2, val1))

    return edgeList, numVars, numClauses


def twosat(edgeList, numVars):
    adjDict, revAdjDict, vertexSet = kr.createAdjDict(edgeList)
    print("Computing strong connected components..")
    leaders, ftimes = kr.kosaraju(adjDict, revAdjDict, vertexSet)
    print("Computing original leader vertices..")
    origLeaders = kr.origLeaders(leaders, kr.invFtimes)

    print("Checking for contradicting vertices in connected components..")
    for vertex in range(1, numVars+1):
        if vertex in origLeaders and -vertex in origLeaders:
            if origLeaders[vertex] == origLeaders[-vertex]:
                return False

    return True


def main():
    fName = sys.argv[1]
    edgeList, numVars, numClauses = createGraph(fName)
    success = twosat(edgeList, numVars)

    if success is True:
        print("Specified 2-SAT instance is satisfiable")
    else:
        print("Specified 2-SAT instance is unsatisfiable")


if __name__ == '__main__':
    main()
