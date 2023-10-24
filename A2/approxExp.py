import random
from graph import Graph
from graph import MVC
from approx import *

from matplotlib import pyplot as plt

def createRandomGraph(i, j):
    g = Graph(i)
    edge_count = 0

    while edge_count < j:
        node1 = random.randint(0, i-1)
        node2 = random.randint(0, i-1)

        if node1 != node2 and not g.are_connected(node1, node2):
            g.add_edge(node1, node2)
            edge_count += 1
    return g

def exp1(m):
    gList = []
    for i in range (100): 
        gList.append(createRandomGraph(8,m))
    gList2 = gList.copy()
    gList3 = gList.copy()
    gList4 = gList.copy()
    
    
    mvcList = []
    for i in range(len(gList)): mvcList.append(MVC(gList[i]))
    mvcSum = 0
    for i in range(len(mvcList)): mvcSum += len(mvcList[i])
        
    apx1 = 0
    apx2 = 0
    apx3 = 0
    
    for i in range(len(gList2)):
        apx1 += len(approx1(gList2[i]))
        apx2 += len(approx2(gList3[i]))
        apx3 += len(approx3(gList4[i]))
        
        
    return [apx1/mvcSum, apx2/mvcSum, apx3/mvcSum]

def graphAndRunExp1():
    results = []
    for i in range(1,25):
        results.append(exp1(i))
    
    approx1 = [a[0] for a in results]
    approx2 = [a[1] for a in results]
    approx3 = [a[2] for a in results]
    m = [a for a in range(1,25)]
    
    plt.plot(m, approx1, label = "approximation 1")
    plt.plot(m, approx2, label = "approximation 2")
    plt.plot(m, approx3, label = "approximation 3")
    plt.xlabel('Number of Edges')
    plt.ylabel('expected performance')
    plt.title('Expected Performance of Vertex Cover Approximations vs. Graph Complexity')
    plt.show()
    
    
def main():
    graphAndRunExp1()
    
main()
        
