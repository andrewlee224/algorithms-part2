"""
Greedy algorithm for minimizing the weighted sum of completion times.
Implemented versions with two scoring functions: 
    w_i - l_i (suboptimal) and 
    w_i/l_i (optimal)
"""

def score1(w, l):
    return w - l

def score2(w, l):
    return w/float(l)

def loadData(fName):
    with open(fName, 'r') as fileObj:
        lines = fileObj.readlines()
        numJobs = int(lines[0].strip())    # first line contains number of jobs
        jobList = [ (int(line.split()[0]), int(line.split()[1])) for line in lines[1:] ] 

    return jobList

def sortJobs(jobList, scoreFunc):
    scoreJobList = [ (w, l, scoreFunc(w, l)) for w, l in jobList ]
    scoreJobList.sort(key=lambda tup: tup[0], reverse=True)   # sort by weight first to resolve ties
    scoreJobList.sort(key=lambda tup: tup[2], reverse=True)   # sort by score function

    return scoreJobList

def sumCompletionTimes(sortedJobList):
    weightedSum = 0
    lengthSum = 0

    for job in sortedJobList:
        lengthSum += job[1]
        weightedSum += job[0] * lengthSum

    return weightedSum, lengthSum

def main(fName, scoreFunc):
    print("Loading data")
    jobList = loadData(fName)
    print("Computing scores for jobs and sorting")
    scoreJobList = sortJobs(jobList, scoreFunc)
    print("Computing weighted sum of completion times")
    weightedSum, lengthSum = sumCompletionTimes(scoreJobList)
    print("Weighted sum: {0}\nLength sum: {1}".format(weightedSum, lengthSum))

if __name__ == '__main__':
    main('jobs.txt', score1)
