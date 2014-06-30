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
