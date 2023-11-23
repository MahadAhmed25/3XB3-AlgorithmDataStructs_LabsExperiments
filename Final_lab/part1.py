import final_project_part1
import min_heap2


def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap2.MinHeap([])
    nodes = list(G.adj.keys())
    

    max_dec=k+1

    num_nodes = len(nodes)

    counter=[]

    for i in range(num_nodes):
        counter.append(0)


    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap2.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)
    counter[source]=counter[source]+1
    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                if (counter[neighbour] <max_dec):
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    counter[neighbour]=counter[neighbour]+1
                    #print("decrease ", neighbour)
                    #print("check ", counter[neighbour])
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist

def test_dijk():
    print("-----Approx Alg 1 -----") 
    graph2 = final_project_part1.DirectedWeightedGraph()
    for i in range(5):
        graph2.add_node(i)#

    graph2.add_edge(0, 1, 10)#
    graph2.add_edge(0,2, 1)
    graph2.add_edge(1, 3, 1)#
    graph2.add_edge(2,1, 1)
    graph2.add_edge(2,3, 10)
    graph2.add_edge(3,4, 1)


    print(final_project_part1.dijkstra(graph2, 0))    
test_dijk()


def test2():
    print("-----Approx Alg 2 -----") 
    graph1 = final_project_part1.DirectedWeightedGraph()
    for i in range(5):
        graph1.add_node(i)#

    graph1.add_edge(0, 1, 10)#
    graph1.add_edge(0,2, 1)
    graph1.add_edge(1, 3, 1)#
    graph1.add_edge(2,1, 1)
    graph1.add_edge(2,3, 10)
    graph1.add_edge(3,4, 1)

    print(dijkstra_approx(graph1, 0,0))    


test2()