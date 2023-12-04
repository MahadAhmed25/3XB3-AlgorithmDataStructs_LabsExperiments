import time

from matplotlib import pyplot as plt
from GraphLibrary.min_heap2 import *
import random

class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)
    
    def print_adjacencyList(self):
        for node, neighbors, in self.adj.items():
            print(f"{node}: {', '.join([f'{neighbor}({self.w(node, neighbor)})' for neighbor in neighbors])}")


def dijkstra(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = MinHeap([])
    nodes = list(G.adj.keys())
    sum=0
    max_iterations=0

    counter2=[]
    for i in range(len(nodes)):
        counter2.append(0)

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)
    sum=sum+1
    counter2[source]=counter2[source]+1

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                sum=sum+1
                counter2[neighbour]=counter2[neighbour]+1
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    
    for i in range(len(counter2)): #returns back the maximum number of decreases requried on any node
        if counter2[i]> max_iterations:
            max_iterations = counter2[i]


    #print("alg1 total # of decreases: ", sum)
    #print("Maximum number of decreases for any node: ", max_iterations)
    #print("list of the number of decreases for each node: ", counter2 )
    
    return dist, max_iterations, counter2, sum

def dijkstraSP(G, source, destination):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    Q = MinHeap([])
    nodes = list(G.adj.keys())
    sum = 0

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)
    sum += 1

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        if current_node == destination:
            # Reached the destination, construct and return the path
            path = []
            current_node = destination
            while current_node in pred:
                path.insert(0, current_node)
                current_node = pred[current_node]
            # Include the source node in the path
            path.insert(0, source)
            return path

        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                sum += 1
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
                
    # If destination is not reached, return an empty path
    return []


def bellman_ford(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    num_dec =0 
    

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0
    num_dec=num_dec+1

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour): #
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
                    num_dec=num_dec+1
    print("alg1 total # of decreases: ", num_dec)
    return dist


def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G


#Assumes G represents its nodes as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G):
    n = G.number_of_nodes()
    d = [[float("inf") for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i, j):
                d[i][j] = G.w(i, j)
        d[i][i] = 0
    return d

def test():
    print("-----Approx Alg 2 Dijk-----") 
    graph1 = DirectedWeightedGraph()
    for i in range(8):
        graph1.add_node(i)#

    graph1.add_edge(0, 1, 3)#
    graph1.add_edge(0,2, 1)
    graph1.add_edge(0, 6, 2)#
    graph1.add_edge(1,3, 1)
    graph1.add_edge(1,5, 1)
    graph1.add_edge(2,1, 4)
    graph1.add_edge(2,3,5)
    graph1.add_edge(3,4,1)
    graph1.add_edge(5,4,2)
    graph1.add_edge(6,4,1)
    
    print(mystery(graph1)) 

#test()

def graph_and_run_experimentMystery(max_edge):
    num_itemsrec=[]
    run_timerec =[]

    for current_items in range(10, 100, 1):
        G2 = create_random_complete_graph(current_items,max_edge)
        start=0; end=0
        start = time.time()
        mystery(G2)
        end = time.time()
        num_itemsrec.append(current_items)
        run_timerec.append(end-start)
        

    plt.plot(num_itemsrec, run_timerec,color='r')

    plt.legend(["Mystery Algorithm Complexity"])
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time in seconds')
    plt.title('Runtime vs Number of Nodes')
    plt.show()

graph_and_run_experimentMystery(30)

G = DirectedWeightedGraph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_edge(0,1,1)
G.add_edge(1,2,1)
#G.print_adjacencyList()

#print(dijkstraSP(G, 0, 2))