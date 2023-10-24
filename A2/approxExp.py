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

#Experiment with e edges and 8 nodes
def exp1(e, alg):
    sum = 0
    for i in range(100):
        graph = createRandomGraph(8, e)
        if len(MVC(graph)) == len(alg(graph)):
            sum+=1
    return sum/100

#Experiment with n nodes and minimum edges (edges = 3)
def exp2(n, alg):
    sum = 0
    for i in range(100):
        graph = createRandomGraph(n, 3)
        if len(MVC(graph)) == len(alg(graph)):
            sum+=1
    return sum/100

#Experiment with n nodes and maximum # of edges n(n-1)/2
def exp3(n, alg):
    sum = 0
    numEdges = (n*(n-1))/2
    for i in range(100):
        graph = createRandomGraph(n, numEdges)
        if len(MVC(graph)) == len(alg(graph)):
            sum+=1
    return sum/100

def graphexp1():
    results = []
    for i in range (1,26):
        x = []
        x.append(exp1(i,approx1))
        x.append(exp1(i,approx2))
        x.append(exp1(i,approx3))
        results.append(x)
        
    app1 = [a[0] for a in results]
    app2 = [a[1] for a in results]
    app3 = [a[2] for a in results]
    x = [a for a in range(1,26)]
    
    plt.plot(x, app1, label = "approximation 1")
    plt.plot(x, app2, label = "approximation 2")
    plt.plot(x, app3, label = "approximation 3")
    plt.xlabel('Number of Edges')
    plt.ylabel('expected performance')
    plt.title('Expected Performance of Vertex Cover Approximations vs. Graph Complexity')
    plt.legend()
    plt.show()
    
def graphexp2():
    results = []
    for i in range (3,11):
        x = []
        x.append(exp2(i,approx1))
        x.append(exp2(i,approx2))
        x.append(exp2(i,approx3))
        results.append(x)
        
    app1 = [a[0] for a in results]
    app2 = [a[1] for a in results]
    app3 = [a[2] for a in results]
    x = [a for a in range(3,11)]
    
    plt.plot(x, app1, label = "approximation 1")
    plt.plot(x, app2, label = "approximation 2")
    plt.plot(x, app3, label = "approximation 3")
    plt.xlabel('Number of Nodes')
    plt.ylabel('expected performance')
    plt.title('Expected Performance of Vertex Cover Approximations vs. Graph Complexity')
    plt.legend()
    plt.show()
    
def graphexp3():
    results = []
    for i in range (3,11):
        x = []
        x.append(exp3(i,approx1))
        x.append(exp3(i,approx2))
        x.append(exp3(i,approx3))
        results.append(x)
        
    app1 = [a[0] for a in results]
    app2 = [a[1] for a in results]
    app3 = [a[2] for a in results]
    x = [a for a in range(3,11)]
    
    plt.plot(x, app1, label = "approximation 1")
    plt.plot(x, app2, label = "approximation 2")
    plt.plot(x, app3, label = "approximation 3")
    plt.xlabel('Number of Nodes')
    plt.ylabel('expected performance')
    plt.title('Expected Performance of Vertex Cover Approximations vs. Graph Complexity')
    plt.legend()
    plt.show()
    
# graphexp1()
# graphexp2()
# graphexp3()
    

    

        
        
