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
    optArray = [[]]
    for w in range(totalWeight):
        if items[0][1] <= w:
            optArray[0].append(items[0][0])
        else:
            optArray[0].append(0)

    for i, item in enumerate(items[1:]):
        i = i + 1
        optArray.append([])
        curVal, curWeight = item

        for w in range(totalWeight):
            optArray[i].append(0)
            if curWeight > w:
                continue

            v1 = optArray[i-1][w - curWeight] + curVal
            v2 = optArray[i-1][w]

            if v1 >= v2:
                optArray[i][w] = v1
            else:
                optArray[i][w] = v2

    return optArray
