"""
Implementation of the dynamic programming knapsack algorithm for a very
large dataset. Standard iterative approach is unfeasible, utilising a recursive approach and caching subproblems solutions instead.
"""


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
    print("="*50)
    if totalWeight <= 0:
        print("Total weight < 0, return 0")
        return 0

    lastItem = partialItems[-1]
    if len(partialItems) == 1:
        print("Last item, return "),
        if lastItem[1] <= totalWeight:
            print(lastItem[0])
            return lastItem[0]
        else:
            print("0")
            return 0

    print("Enter first case {}".format(len(partialItems)))
    val1 = solve(partialItems[:-1], totalWeight)
    print("Enter second case {}".format(len(partialItems)))
    val2 = solve(partialItems[:-1], totalWeight - lastItem[1]) + lastItem[0]

    retVal = val1 if val1 >= val2 else val2
    print(partialItems, totalWeight)
    print(totalWeight, val1, val2, retVal)
    return retVal
