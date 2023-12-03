import random
from matplotlib import pyplot as plt
import final_project_part1
import min_heap2


def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap2.MinHeap([])
    nodes = list(G.adj.keys())
    
    counter=[]
    num_nodes = len(nodes)
    total=0
    max_approx_iter=0

    for i in range(num_nodes):
        counter.append(0)


    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap2.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)
    counter[source]=counter[source]+1
    total=total+1

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                if (counter[neighbour] <k):
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    
                    total=total+1
                    counter[neighbour]=counter[neighbour]+1
                    #print(counter)
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node
    
    return dist, counter, total

def exp1():
    print("----- Dijkstra -----") 

    G2 =final_project_part1.create_random_complete_graph(20,50)
    short_dist, max_iter, num_node_dec,total_dec =final_project_part1.dijkstra(G2, 0)

    shortest_dist =[] 
    decrease_num =[]

    print("Disjkstra regular alg Graph's attributes: ")
    print("Shortest distance from source to every other node: ", short_dist)
    print("Maximum number of decreases required on any node: ", max_iter )
    print("List of each node's number of times decreasing: ", num_node_dec)
    print("Total number of decreases (just to cross check): ", total_dec, "\n")
    dijkstra_dist = final_project_part1.total_dist(short_dist)
    print(dijkstra_dist)  

    decrease_num.append(max_iter)
    shortest_dist.append(dijkstra_dist) 

    total_dist =[] 
    num_decreases =[]

    for i in range(1, max_iter+1):
       short_distapprox, num_node_decapprox, total_dec_approx = dijkstra_approx(G2, 0,i)
       total_curr_dist = final_project_part1.total_dist(short_distapprox)

       num_decreases.append(i)
       total_dist.append(total_curr_dist)

    print(num_decreases)
    print(total_dist) 


    return decrease_num, shortest_dist, num_decreases, total_dist 


def graph_exp1():
    x1,y1,x2,y2 =exp1()

    plt.plot(x1, y1,color='r', marker='o')
    plt.plot(x2, y2, color='g')

    plt.legend(["Dijkstra", "Dijkstra Approx"])
    plt.xlabel('Number of decreases k')
    plt.ylabel('Shortest Path')
    plt.title('Dijkstra Approx number of keys vs shortest path')
    plt.show()

#graph_exp1()

def exp2():

    print("----- Exp2 using disjktra for this exp-----") 

    G2 =final_project_part1.create_random_complete_graph(20,50)
    short_dist, max_iter, num_node_dec,total_dec =final_project_part1.dijkstra(G2, 0)

    shortest_dist =[] 
    decrease_num =[]

    print("Disjkstra regular alg Graph's attributes: ")
    print("Shortest distance from source to every other node: ", short_dist)
    print("Maximum number of decreases required on any node: ", max_iter )
    print("List of each node's number of times decreasing: ", num_node_dec)
    print("Total number of decreases (just to cross check): ", total_dec, "\n")
    dijkstra_dist = final_project_part1.total_dist(short_dist)
    print(dijkstra_dist)  

    decrease_num.append(max_iter)
    shortest_dist.append(dijkstra_dist) 

    total_dist =[] 
    num_decreases =[]

    for i in range(1, max_iter+1):
       short_distapprox, num_node_decapprox, total_dec_approx = dijkstra_approx(G2, 0,i)
       total_curr_dist = final_project_part1.total_dist(short_distapprox)

       num_decreases.append(i)
       total_dist.append(total_curr_dist)

    print(num_decreases)
    print(total_dist) 


    return decrease_num, shortest_dist, num_decreases, total_dist 


def graph_exp2():
    x1,y1,x2,y2 =exp1()

    plt.plot(x1, y1,color='r', marker='o')
    plt.plot(x2, y2, color='g')

    plt.legend(["Dijkstra", "Dijkstra Approx"])
    plt.xlabel('Number of decreases k')
    plt.ylabel('Shortest Path')
    plt.title('Dijkstra Approx number of keys vs shortest path')
    plt.show()


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def create_random_complete_graph_negative(n,upper,lower):
    G = final_project_part1.DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(lower,upper))
    return G

def exp2():
    print("\nBellmanFord")
    G3 = create_random_complete_graph_negative(3,7,-3)
    print(G3.print_adjacencyList())

    print(final_project_part1.bellman_ford(G3, 0))



exp2()

def bellman_ford_approx(G, source,k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())
    
    counter2=[]
    num_nodes = len(nodes)
    total2=0

    for i in range(num_nodes):
        counter2.append(0)

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    counter2[source]=counter2[source]+1
    total2=total2+1

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour): #
                    if (counter2[neighbour] <k):
                        total2=total2+1
                        counter2[neighbour]=counter2[neighbour]+1

                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        pred[neighbour] = node
    print("alg2 total # of decreases: ", total2)
    return dist

def testBellmanApprox():
    print("-----Approx Alg 2 Bellman-----") 
    graph3 = final_project_part1.DirectedWeightedGraph()
    for i in range(5):
        graph3.add_node(i)#

    graph3.add_edge(0, 1, 10)#
    graph3.add_edge(0,2, 1)
    graph3.add_edge(1, 3, 1)#
    graph3.add_edge(2,1, 1)
    graph3.add_edge(2,3, 10)
    graph3.add_edge(3,4, 1)

    print(bellman_ford_approx(graph3, 0,1))

def testBellman():
    print("-----Approx Alg 2 Bellman-----") 
    graph4 = final_project_part1.DirectedWeightedGraph()
    for i in range(5):
        graph4.add_node(i)#

    graph4.add_edge(0, 1, 10)#
    graph4.add_edge(0,2, 1)
    graph4.add_edge(1, 3, 1)#
    graph4.add_edge(2,1, 1)
    graph4.add_edge(2,3, 10)
    graph4.add_edge(3,4, 1)

    print(final_project_part1.bellman_ford(graph4, 0))

#testBellman()

#testBellmanApprox()