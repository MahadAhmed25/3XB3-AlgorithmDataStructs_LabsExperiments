import random
from graph import Graph
from graph import MVC
from approxExp import createRandomGraph

from matplotlib import pyplot as plt

def MIS(G):
    MIS = set()
    if G.number_of_nodes() == 0:
        return MIS
    if G.number_of_nodes() == 1:
        MIS.add(0)
        return MIS
    
    for node in G.adj:
        IS = find_IS(G, node)
        if len(IS) > len(MIS):
            MIS = IS
    return MIS

def find_IS(G, v):
    IS = set()
    curV = v
    IS.add(curV)

    for nieghbor in G.adj:
        if nieghbor != curV and nieghbor not in G.adj[curV]: 
            count = 0
            for nieghbor2 in IS.copy(): 
                if nieghbor not in G.adj[nieghbor2]:
                    count += 1
            
            if count == len(IS):
                IS.add(nieghbor)
                curV = nieghbor

    return IS

def ISvsVCExp1(m):
    gList = []
    for i in range (100): 
        gList.append(createRandomGraph(8,m))
        
    avgSumIS = 0
    avgSumVC = 0
    
    for i in range (len(gList)):
        avgSumIS += len(MIS(gList[i]))
        avgSumVC += len(MVC(gList[i]))
        
    return [avgSumIS/100, avgSumVC/100]

def graphAndRunExperiment():
    results = []
    for i in range(1,26):
        results.append(ISvsVCExp1(i))
        
    isResults = [a[0] for a in results]
    vcResults = [a[1] for a in results]
    x = [a for a in range(1,26)]
    
    plt.plot(x, isResults, label = "MIS")
    plt.plot(x, vcResults, label = "MVC")
    plt.xlabel('Number of Edges')
    plt.ylabel('avg set size')
    plt.legend()
    plt.show()
    
graphAndRunExperiment()
        

