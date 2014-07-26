"""
Dynamic algorithm for solving the knapsack problem.
"""


def loadData(fPath="knapsack1.txt"):
    items = []

    with open(fPath, 'r') as fileObj:
        lines = fileObj.readlines()
        totalWeight, numItems = map(int, lines[0].split())
        for line in lines[1:]:
            value, weight = map(int, line.split())
            items.append((value, weight))

    return items, totalWeight, numItems


def optimalSubproblems(items, totalWeight):
    """
    Build a 2d array of values of optimal solutions to subproblems
    depending on considered number of items and knapsack size.
    """

    optArray = [[]]
    # fill row 0 of output array with starting values
    for w in range(totalWeight+1):
        if items[0][1] <= w:
            optArray[0].append(items[0][0])
        else:
            optArray[0].append(0)

    # row 0 of output array already filled, so continue
    # filling from row 1 onwards
    for i, item in enumerate(items[1:]):
        i = i + 1
        optArray.append([])
        curVal, curWeight = item

        for w in range(totalWeight+1):
            optArray[i].append(optArray[i-1][w])
            if curWeight > w:
                continue

            v1 = optArray[i-1][w - curWeight] + curVal
            v2 = optArray[i-1][w]

            if v1 >= v2:
                optArray[i][w] = v1

    return optArray


if __name__ == '__main__':
    itemList, totalWeight, numItems = loadData()
    optArray = optimalSubproblems(itemList, totalWeight)
    print("Optimal value for knapsack problem " + 
        "with {} items and {} available weight: {}".format(numItems,
        totalWeight, optArray[-1][-1]))
