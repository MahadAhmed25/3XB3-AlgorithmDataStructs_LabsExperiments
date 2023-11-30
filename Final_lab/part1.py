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
    
    print("alg2 total # of decreases: ", total)
    print("list of the number of decreases for each node: ", counter)
    return dist



def test_dijk():
    print("-----Approx Alg 1 Dijk -----") 
    graph2 = final_project_part1.DirectedWeightedGraph()
    for i in range(7):
        graph2.add_node(i)#

    graph2.add_edge(0, 1, 3)#
    graph2.add_edge(0,2, 1)
    graph2.add_edge(0, 6, 2)#
    graph2.add_edge(1,3, 1)
    graph2.add_edge(1,5, 1)
    graph2.add_edge(2,1, 4)
    graph2.add_edge(2,3,5)
    graph2.add_edge(3,4,1)
    graph2.add_edge(5,4,2)
    graph2.add_edge(6,4,1)

    G2 =final_project_part1.create_random_complete_graph(20,50)
    
  




    print(final_project_part1.dijkstra(G2, 0))    


def testDijkApprox():
    print("-----Approx Alg 2 Dijk-----") 
    graph1 = final_project_part1.DirectedWeightedGraph()
    for i in range(7):
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

    print(dijkstra_approx(graph1, 0,3))    

test_dijk()
testDijkApprox()


#-----------------------------------------------------------
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