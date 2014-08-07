"""
Dynamic programming algorithm for solving the Traveling Salesman Problem
"""

import numpy as np


def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def getPoints(fPath="tsp.txt"):
    with open(fPath, 'r') as fObj:
        lines = fObj.readlines()
        numPoints = int(lines[0].strip())
        points = []
        for line in lines[1:]:
            points.append(tuple(map(float, line.split())))

        return points, numPoints


def computeDistances(points):
    distArr = np.zeros((len(points), len(points)), dtype='float')

    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i, len(points)):
            x2, y2 = points[j]
            distArr[i, j] = distArr[j, i] = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    return distArr


def computeSets(maxCardinality):
    """
    Compute sets (combinations) of elements up to specified cardinality.
    Outputs a dictionary with keys specifying list of sets of a given
    cardinality.
    """

    sets = {}

    for num in range(maxCardinality + 1):
        sets[num] = []

    for num in xrange(2**maxCardinality):
        sets[bin(num).count('1')].append(num)

    return sets


def onesIndices(num):
    """Returns 1-based indices of set bits"""

    onesIndices = []
    bl = num.bit_length()
    for i in range(bl+1):
        if num & 0b1 == 1:
            onesIndices.append(i)
        num = num >> 1
    return onesIndices


def tsp(points, sets, distances):
    subproblemArr = np.ones((2**(len(points)), len(points)),
                                dtype='float')
    subproblemArr = subproblemArr * float('inf')
   
    # initialize base cases
    for i in range(2**(len(points))):
        subproblemArr[i, 0] = float('inf')
    subproblemArr[1, 0] = 0

    #for routeSet in sets[1]:
    #    j = [ i for i, j in enumerate(bin(routeSet)) if j == '1' ][0]
    #    subproblemArr[routeSet, j] = distances[0, j]

    for m in range(2, len(points)+1):
        for routeSet in sets[m]:
            # make sure that first vertex is in the route
            if routeSet & 0b1 != 0b1:
                continue

            # binary numbers are represented as strings, e.g. '0b10101'
            jCandidates = onesIndices(routeSet) # [ i-2 for i, j in enumerate(bin(routeSet)) if j == '1' ]
            #print("jCandidates: {}".format(jCandidates))
            for j in jCandidates:
                if jCandidates == 0:
                    continue

                xorMask = 2**j # bin('0b' + '0' * j + '1')
                previousSet = routeSet ^ xorMask
                #print(bin(routeSet))
                #print(bin(previousSet))
                #print('='*50)
                bestVal = float('inf')
                
                for k in jCandidates:
                    if k == j:
                        continue
                    val = subproblemArr[previousSet, k] + distances[k, j]
                    bestVal = val if val < bestVal else bestVal
                subproblemArr[routeSet, j] = bestVal

    # choose last hop in the route
    shortestRoute = float('inf')
    for j in range(1, len(points)):
        val = subproblemArr[2**len(points)-1, j] + distances[j, 0]
        shortestRoute = val if val < shortestRoute else shortestRoute

    return subproblemArr, shortestRoute
