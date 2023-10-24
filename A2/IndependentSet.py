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

#Experiment 1 with 8 nodes and m edges
def ISvsVCExp1(m, alg):
    sum = 0
    for i in range (100): 
        g = createRandomGraph(8, m)
        sum += len(alg(g))
        
    return sum/100

#Experiment 2 with m nodes and minimum number of edges (e=2)
def ISvsVCExp2(m, alg):
    sum = 0
    for i in range (100): 
        g = createRandomGraph(m, 2)
        sum += len(alg(g))
        
    return sum/100

#Experiment 3 with m nodes and maximum number of edges (complete graph)
def ISvsVCExp3(m, alg):
    sum = 0
    numEdges = (m*(m-1))/2
    for i in range (100): 
        g = createRandomGraph(m, numEdges)
        sum += len(alg(g))
        
    return sum/100
        

def graphexp1():
    results = []
    for i in range(1,26):
        x = []
        x.append(ISvsVCExp1(i, MIS))
        x.append(ISvsVCExp1(i, MVC))
        results.append(x)
         
    isResults = [a[0] for a in results]
    vcResults = [a[1] for a in results]
    x1 = [a for a in range(1,26)]
    
    plt.figure(1)
    plt.plot(x1, isResults, label = "MIS")
    plt.plot(x1, vcResults, label = "MVC")
    plt.xlabel('Number of Edges')
    plt.ylabel('avg set size')
    plt.title('MIS & MVC wrt #ofEdges vs avgSetSize')
    plt.legend()
    plt.show()
    
    
def graphexp2():
    results = []
    for i in range(3,11):
        x = []
        x.append(ISvsVCExp2(i, MIS))
        x.append(ISvsVCExp2(i, MVC))
        results.append(x)
    
    isResults2 = [a[0] for a in results]
    vcResults2 = [a[1] for a in results]
    x2 = [a for a in range(3,11)]
    
    plt.figure(2)
    plt.plot(x2, isResults2, label = "MIS")
    plt.plot(x2, vcResults2, label = "MVC")
    plt.xlabel('Number of Nodes')
    plt.ylabel('avg set size')
    plt.title('MIS & MVC wrt #ofNodes vs avgSetSize with min edges')
    plt.legend()
    plt.show()
    
def graphexp3():
    results = []
    for i in range(3,11):
        x = []
        x.append(ISvsVCExp3(i, MIS))
        x.append(ISvsVCExp3(i, MVC))
        results.append(x)
    
    isResults = [a[0] for a in results]
    vcResults = [a[1] for a in results]
    x2 = [a for a in range(3,11)]
    
    plt.figure(3)
    plt.plot(x2, isResults, label = "MIS")
    plt.plot(x2, vcResults, label = "MVC")
    plt.xlabel('Number of Nodes')
    plt.ylabel('avg set size')
    plt.title('MIS & MVC wrt #ofNodes vs avgSetSize with max edges')
    plt.legend()
    plt.show()
    
    
graphexp1()
graphexp2()
graphexp3()
        

