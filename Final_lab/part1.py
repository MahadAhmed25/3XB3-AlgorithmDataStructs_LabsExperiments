import random
from matplotlib import pyplot as plt
import final_project_part1
#import min_heap2
from GraphLibrary.min_heap2 import * 




def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = MinHeap([])
    nodes = list(G.adj.keys())
    
    counter=[]
    num_nodes = len(nodes)
    total=0
    max_approx_iter=0

    for i in range(num_nodes):
        counter.append(0)


    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(Element(node, float("inf")))
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

graph_exp1()

def random_graphgenerator(num_graphs, size_ofgraph, max_weight): #this func takes in # of graphs, size of them and max weights  to return back random full cycle graphs in a list
    list_of_graphs=[]
    for i in range(num_graphs):
        list_of_graphs.append(final_project_part1.create_random_complete_graph(size_ofgraph, max_weight))
        
    return list_of_graphs

def shortest_path_cost(list_of_graphs): #finds shortest path given a list of graphs
    shortest_cost=[]
    maxiters =[]
    for i in range(len(list_of_graphs)):
        shortest_dist=final_project_part1.dijkstra(list_of_graphs[i], 0) #stores dictionary of shortest path from non-approx function
        maxiters.append(shortest_dist[1])
        shortest_cost.append(final_project_part1.total_dist(shortest_dist[0])) #finds total disatnce given above shortest path dictionary
    
    return shortest_cost, maxiters

def average_ratio_calc(table_array,row,column, shortest_object1):
    total =[]
    num_ofdec=[]

    for i in range(column+1):
        num_ofdec.append(0)


    for i in range(len(shortest_object1)):
        for j in range(shortest_object1[i]+1):
            num_ofdec[j]=num_ofdec[j] + 1
        

    #print(num_ofdec)


    for i in range(column):
        total.append(0.0)

    for i in range(column):
        for j in range(row):
            total[i] = total[i]+ table_array[j][i] 

    for x in range(len(total)):
        total[x] = total[x]/num_ofdec[x+1]
        
    return total



def k_increments_path(list_of_graphs,shortest_object): #this function takes a list of graphs, sends back the length of path 
    
    maxval= max(shortest_object[1])
    
    #print(shortest_object[1][6])
    #print(maxval)
    

    #each_ratio = [ [0]*maxval for i in range(maxval)]   
    each_ratio = arr = [[0 for i in range(maxval)] for j in range(len(list_of_graphs))] 

    for j in range(len(list_of_graphs)):
        for i in range(1, shortest_object[1][j]+1):
            short_distapprox, num_node_decapprox, total_dec_approx = dijkstra_approx(list_of_graphs[j], 0,i)
            total_curr_dist = final_project_part1.total_dist(short_distapprox)
            #print(each_ratio[j][i-1])
            each_ratio[j][i-1]= (total_curr_dist/ shortest_object[0][j])

    #print("New ratios: ", each_ratio)
    #print()

    ratio_lists=average_ratio_calc(each_ratio,len(list_of_graphs),maxval,shortest_object[1])


    return ratio_lists



def exp2():
    print("----- Exp2 Using Disjktra-----") 

    set1 = random_graphgenerator(10,10,50) #list of 10 random graphs, sized with  nodes 
    set2 = random_graphgenerator(10,25,50) #list of 10 random graphs, sized with  nodes
    set3 = random_graphgenerator(10,40,50) #list of 10 random graphs, sized with  nodes
    set4 = random_graphgenerator(10,55,50) #list of 10 random graphs, sized with  nodes
    set5 = random_graphgenerator(10,70,50) #list of 10 random graphs, sized with  nodes

    shortest_1=shortest_path_cost(set1)
    shortest_2=shortest_path_cost(set2)
    shortest_3=shortest_path_cost(set3)
    shortest_4=shortest_path_cost(set4)
    shortest_5=shortest_path_cost(set5)

    #print((shortest_1[1]))  
    #print((shortest_2[1]))
    #print((shortest_3[1])) 
    #print((shortest_4[1])) 
    #print((shortest_5[1])) 

    #print((shortest_3[0])) 

    ratio_list1 = k_increments_path(set1,shortest_1)
    ratio_list2 = k_increments_path(set2,shortest_2)
    ratio_list3 = k_increments_path(set3,shortest_3)
    ratio_list4 = k_increments_path(set4,shortest_4)
    ratio_list5 = k_increments_path(set5,shortest_5)

    print(ratio_list1)  
    print(ratio_list2) 
    print(ratio_list3) 
    print(ratio_list4) 
    print(ratio_list5) 


    maxdec= max(shortest_5[1])
    

    return ratio_list1, ratio_list2 ,ratio_list3 ,ratio_list4, ratio_list5, maxdec
    


def graph_exp2():
    y1,y2,y3,y4,y5,k =exp2()
    
    x1=[]
    x2=[]
    x3=[]
    x4=[]
    x5=[]

    for i in range(len(y1)):
        x1.append(i+1)
    for i in range(len(y2)):
        x2.append(i+1)
    for i in range(len(y3)):
        x3.append(i+1)
    for i in range(len(y4)):
        x4.append(i+1)
    for i in range(len(y5)):
        x5.append(i+1)


    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.plot(x4, y4)
    plt.plot(x5, y5)

    plt.legend(["Graph size 10 Nodes", "Graph size 25 Nodes","Graph size 40 Nodes","Graph size 55 Nodes","Graph size 70 Nodes" ])
    plt.xlabel('Number of decreases k')
    plt.ylabel('Ratio to shortest path')
    plt.title('Dijkstra Approx number of keys vs ratio')
    plt.show()

graph_exp2()


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

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