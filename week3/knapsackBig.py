"""
Implementation of the dynamic programming knapsack algorithm for a very
large dataset. Standard iterative approach is unfeasible, utilising a 
recursive approach and caching subproblems solutions instead.
"""

import sys

cacheDict = {}

def loadData(fPath="knapsack_big.txt"):
    items = []

    with open(fPath, 'r') as fileObj:
        lines = fileObj.readlines()
        totalWeight, numItems = map(int, lines[0].split())
        for line in lines[1:]:
            value, weight = map(int, line.split())
            items.append((value, weight))

    return items, totalWeight, numItems


def solve(partialItems, totalWeight):
    if totalWeight <= 0:
        return 0

    lastItem = partialItems[-1]
    if len(partialItems) == 1:
        if lastItem[1] <= totalWeight:
            return lastItem[0]
        else:
            return 0

    key1 = (len(partialItems[:-1]), totalWeight)
    val1 = cacheDict.get(key1)     
    if val1 is None:        
        val1 = solve(partialItems[:-1], totalWeight)
        cacheDict[key1] = val1

    key2 = (len(partialItems[:-1]), totalWeight - lastItem[1])
    val2pre = cacheDict.get(key2)
    if val2pre is None:
        val2pre = solve(partialItems[:-1], totalWeight - lastItem[1])
        cacheDict[key2] = val2pre
    if lastItem[1] <= totalWeight:
        val2 = val2pre + lastItem[0]
    else:
        val2 = 0

    retVal = val1 if val1 >= val2 else val2
    return retVal


def main():
    print("Calculating the knapsack optimal solution value..")
    itemList, totalWeight, numItems = loadData("knapsack_big.txt")
    sys.setrecursionlimit(numItems+200)

    optVal = solve(itemList, totalWeight)
        
    print("Optimal value: {}".format(optVal))

if __name__ == '__main__':
    main()
